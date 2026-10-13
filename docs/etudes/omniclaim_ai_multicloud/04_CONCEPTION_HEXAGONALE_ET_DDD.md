# GUIDE DE CONCEPTION LOGICIELLE — PLATEFORME OMNICLAIM AI
**Niveau d'Exigence :** Software Craftsmanship / Clean Architecture / DDD / TDD 100%  
**Conforme aux arbitrages :** Mono-Cloud unifié (AWS natif / Amazon Bedrock), Politique de Sécurité CISO (Zero-Trust NIST SP 800-207, C2 MASSIF) & Revue Red Team (KISS / YAGNI / Suppression du Multi-Cloud Hybride).

---

## 1. SPÉCIFICATION DE L'ARCHITECTURE HEXAGONALE (PORTS & ADAPTERS)

L'architecture découple strictement le **Cœur de Domaine Métier** (pur, sans dépendance externe, frameworks ou SDK) des **Adaptateurs d'Infrastructure et d'Interface** (API, S3, Base de données, AWS Bedrock, MSK/SQS).

### Schéma Textuel de la Topologie Hexagonale

```text
       [ Adaptateurs Entrants (Drivers / Inbound) ]
       │
       ├─► REST API Adapter (Spring Boot / FastAPI Controllers)
       └─► Async Worker Adapter (AWS SQS / MSK Consumer)
             │
             ▼  (Appel des Ports Entrants)
       ┌────────────────────────────────────────────────────────┐
       │                   PORTS ENTRANTS                       │
       │           (Use Case Interfaces / Command In)           │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                                  ▼
       ┌────────────────────────────────────────────────────────┐
       │                 CŒUR DE DOMAINE MÉTIER                 │
       │              (Architecture Hexagonale Pure)            │
       │                                                        │
       │  [ Aggregates ] ◄──► [ Entities ] ◄──► [ Value Objects ] │
       │         ▲                                      ▲       │
       │         └───────────[ Domain Services ]────────┘       │
       └──────────────────────────┬─────────────────────────────┘
                                  │
                                  ▼  (Implémentation des Ports Sortants)
       ┌────────────────────────────────────────────────────────┐
       │                    PORTS SORTANTS                      │
       │              (Driven Ports / SPI Interfaces)           │
       └──────────────────────────┬─────────────────────────────┘
             │                    │                     │
             ▼                    ▼                     ▼
       [ Persistence Adapter ]  [ Storage Adapter ]  [ AI Cognitive Adapter ]
       (PostgreSQL / DynamoDB)   (AWS S3 Data Lake)   (Amazon Bedrock / Guardrails)
             │                    │                     │
             └────────────────────┴─────────────────────┘
                    [ Adaptateurs Sortants (Driven / Outbound) ]
```

### Définition formelle des Ports et Adaptateurs

1. **Ports Entrants (Inbound / Drivers) :**
   * `SubmitClaimUseCase` (Interface définissant la méthode `submit(command: SubmitClaimCommand): ClaimId`)
   * `EvaluateClaimUseCase` (Interface définissant la méthode `evaluate(claimId: ClaimId): EvaluationResult`)
2. **Ports Sortants (Outbound / Driven / SPI) :**
   * `ClaimRepositoryPort` (Interface pour la persistance et l'hydratation de l'agrégat `Claim`)
   * `DocumentStoragePort` (Interface pour l'interaction sécurisée avec le Data Lake S3)
   * `ClaimAnalyzerPort` (Interface pour l'analyse cognitive isolée via Amazon Bedrock)
   * `EventPublisherPort` (Interface pour la publication des événements de domaine asynchrones)
3. **Adaptateurs (Adapters) :**
   * *Entrants :* `RestClaimController` (expose les endpoints HTTP), `SqsClaimConsumer` (consomme les files d'attente d'ingestion).
   * *Sortants :* `PostgresClaimRepository` (implémente `ClaimRepositoryPort` via JPA/jOOQ), `S3DocumentStorageAdapter` (gère les flux binaires vers S3), `BedrockClaimAnalyzerAdapter` (encapsule les appels aux LLM AWS Bedrock avec filtres de modération et PII).

---

## 2. MODÉLISATION DOMAIN-DRIVEN DESIGN (DDD)

### Bounded Context
* **Nom du Contexte :** `ClaimAdjudicationContext`
* **Rôle :** Gestion, analyse de risque, calcul d'indemnisation et application des règles Human-in-the-Loop (HITL) pour les sinistres assurantiels.

### Agrégat Racine, Entités et Value Objects Immuables

```text
[ Claim (Agrégat Racine) ]
 ├── claimId : ClaimId (Value Object)
 ├── policyId : PolicyId (Value Object)
 ├── claimant : Claimant (Entité interne)
 ├── financialAmount : ClaimAmount (Value Object immuable)
 ├── status : ClaimStatus (Value Object / Enum)
 ├── fraudScore : FraudScore (Value Object immuable)
 └── documents : List<SupportingDocument> (Entités internes)
```

#### Code Source Cœur (Clean Code / SOLID / Immuabilité)

```python
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional
from uuid import UUID

# --- VALUE OBJECTS ---

@dataclass(frozen=True)
class ClaimId:
    value: UUID

@dataclass(frozen=True)
class PolicyId:
    value: str

@dataclass(frozen=True)
class ClaimAmount:
    cents: int
    currency: str = "EUR"

    def __post_init__(self):
        if self.cents < 0:
            raise ValueError("Le montant du sinistre ne peut pas être négatif.")

@dataclass(frozen=True)
class FraudScore:
    value: float

    def __post_init__(self):
        if not (0.0 <= self.value <= 1.0):
            raise FraudScoreError("Le score de fraude doit être compris entre 0.0 et 1.0.")

class ClaimStatus(Enum):
    SUBMITTED = "SUBMITTED"
    ANALYZING = "ANALYZING"
    AUTO_APPROVED = "AUTO_APPROVED"
    PENDING_HITL = "PENDING_HITL"
    REJECTED = "REJECTED"

# --- ENTITÉS INTERNES & AGRÉGAT RACINE ---

@dataclass(frozen=True)
class SupportingDocument:
    document_id: str
    s3_key: str
    hash_sha256: str

class Claim:
    """Agrégat Racine du Bounded Context ClaimAdjudicationContext"""
    def __init__(self, claim_id: ClaimId, policy_id: PolicyId, amount: ClaimAmount, documents: List[SupportingDocument]):
        self._claim_id = claim_id
        self._policy_id = policy_id
        self._amount = amount
        self._documents = list(documents)
        self._status = ClaimStatus.SUBMITTED
        self._fraud_score: Optional[FraudScore] = None
        self._domain_events: List = []

    @property
    def claim_id(self) -> ClaimId: return self._claim_id
    @property
    def status(self) -> ClaimStatus: return self._status
    @property
    def amount(self) -> ClaimAmount: return self._amount
    @property
    def fraud_score(self) -> Optional[FraudScore]: return self._fraud_score

    def evaluate_risk(self, fraud_score: FraudScore) -> None:
        """Applique les règles métier de gouvernance HITL (Règle < 2000€ et score < 0.15)"""
        self._fraud_score = fraud_score
        self._status = ClaimStatus.ANALYZING

        # Règle Métier HITL stricte
        threshold_amount_cents = 2000_00
        fraud_limit = 0.15

        if self._amount.cents < threshold_amount_cents and self._fraud_score.value < fraud_limit:
            self._status = ClaimStatus.AUTO_APPROVED
        else:
            self._status = ClaimStatus.PENDING_HITL
```

---

## 3. STRATÉGIE DE TESTABILITÉ UNITAIRE (TDD 100%)

### Pyramide des tests et isolation absolue
* **Tests Unitaires du Domaine (100% TDD) :** 0 dépendance d'infrastructure, 0 base de données, 0 appel réseau/LLM. Utilisation exclusive de mocks/stubs des ports sortants. Exécution en mémoire (< 1 seconde pour des milliers de tests).
* **Tests d'Intégration des Adaptateurs :** Validation des adaptateurs techniques (PostgreSQL, S3, Bedrock) via des conteneurs éphémères (Testcontainers).
* **Tests End-to-End (E2E) :** Scénarios nominaux et dégradés limités aux parcours critiques.

#### Exemple de Test Unitaire Pur du Domaine (TDD)

```python
import pytest
from uuid import uuid4
from domain.model import Claim, ClaimId, PolicyId, ClaimAmount, FraudScore, ClaimStatus, SupportingDocument

def test_given_low_amount_and_low_fraud_when_evaluate_then_auto_approved():
    # Arrange (Given)
    claim = Claim(
        claim_id=ClaimId(uuid4()),
        policy_id=PolicyId("POL-998877"),
        amount=ClaimAmount(cents=1500_00), # 1500 € (< 2000 €)
        documents=[SupportingDocument("doc-1", "s3://bucket/invoice.pdf", "sha256...")]
    )
    low_fraud = FraudScore(value=0.10) # < 0.15

    # Act (When)
    claim.evaluate_risk(low_fraud)

    # Assert (Then)
    assert claim.status == ClaimStatus.AUTO_APPROVED
    assert claim.fraud_score == low_fraud

def test_given_high_amount_when_evaluate_then_pending_hitl():
    # Arrange (Given)
    claim = Claim(
        claim_id=ClaimId(uuid4()),
        policy_id=PolicyId("POL-998877"),
        amount=ClaimAmount(cents=2500_00), # 2500 € (>= 2000 €)
        documents=[SupportingDocument("doc-1", "s3://bucket/invoice.pdf", "sha256...")]
    )
    low_fraud = FraudScore(value=0.05)

    # Act (When)
    claim.evaluate_risk(low_fraud)

    # Assert (Then) - Forcé vers le gestionnaire humain (HITL)
    assert claim.status == ClaimStatus.PENDING_HITL
```

---

## 4. DIRECTIVES CLEAN CODE & SOLID POUR LES ÉQUIPES DE BUILD

Les équipes de développement doivent respecter strictement les directives ci-dessous sous peine de rejet en revue de code (Pull Request Gate) :

1. **Principe de Responsabilité Unique (SRP - SOLID) :**
   * Une classe, un agrégat ou un service ne doit avoir qu'une seule raison de changer. Les règles de calcul métier ne doivent jamais être mélangées avec le code d'infrastructure (ex: requêtes SQL dans les entités).
2. **Principe Ouvert/Fermé (OCP - SOLID) :**
   * Le domaine métier doit être ouvert à l'extension mais fermé à la modification. L'ajout d'un nouveau fournisseur d'IA ou d'un nouveau canal d'ingestion se fait par création d'un nouvel adaptateur implémentant le port existant, sans modifier une seule ligne du Cœur de Domaine.
3. **Principe de Substitution de Liskov (LSP - SOLID) & Inversion de Dépendance (DIP - SOLID) :**
   * Le domaine dépend exclusivement d'abstractions (Ports). L'injection de dépendances par constructeur est obligatoire. Aucune instanciation par `new` d'un service d'infrastructure n'est tolérée dans le domaine.
4. **Clean Code & KISS / YAGNI :**
   * **Immuabilité par défaut :** Tous les Value Objects doivent être immuables (`frozen=True` en Python, `final` / records en Java/C#).
   * **Pas de Primitive Obsession :** Interdiction d'utiliser des types primitifs (`str`, `int`) pour manipuler des identifiants métiers ou des montants financiers (utilisation systématique de Value Objects typés).
   * **Gestion rigoureuse des erreurs :** Le domaine lève des exceptions métiers explicites (`DomainException`). Les erreurs techniques d'infrastructure sont capturées au niveau des adaptateurs sortants et converties.
   * **Sécurité & Zero-Trust de code :** Interdiction absolue de logger des PII (données personnelles) ou des tokens d'authentification. Utilisation d'outils automatisés de SAST et SCA (SonarQube, GitGuardian) bloquant tout commit non conforme.