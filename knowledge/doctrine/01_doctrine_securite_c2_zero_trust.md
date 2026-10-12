# DOCTRINE D'ENTREPRISE : SÉCURITÉ ZERO-TRUST & CLASSIFICATION C2

**Référence :** DOC-SEC-C2-001  
**Standard :** NIST SP 800-207 Zero-Trust Architecture  
**Champ d'application :** Tout projet manipulant des données sensibles, financières ou de facturation  

---

## 1. Paliers de Classification des Données
* **C0 (Public) :** Données en accès libre sur Internet sans impact en cas de divulgation.
* **C1 (Interne) :** Données réservées aux collaborateurs de l'entreprise (notes de service, documentations non sensibles).
* **C2 (Confidentiel) :** Données dont la compromission entraîne un préjudice financier, juridique ou réputationnel modéré.
* **C2 MASSIF (Hautement Critique) :** Données financières, factures, comptes bancaires, grands livres comptables ou données personnelles volumineuses ($> 100 000$ enregistrements).

---

## 2. Exigences Impératives pour le Niveau C2 MASSIF
1. **Zéro IP Publique (Zero-Trust Network) :**
   - Interdiction formelle de tout point de terminaison exposé sur Internet (`publicNetworkAccess = Disabled`).
   - Tout flux vers les services Cloud (PaaS, SaaS) doit impérativement transiter via des **Azure Private Endpoints (Private Link)**.
   - Liaisons hybrides On-Premise ➔ Cloud acheminées par **ExpressRoute dédié avec chiffrement matériel MACsec**.

2. **Chiffrement de Bout en Bout avec Clé Client (CMK) :**
   - Toutes les données au repos (Data at Rest) doivent être chiffrées par une clé maîtresse gérée par le client (**Customer-Managed Key - CMK**).
   - La clé CMK doit résider dans un composant matériel HSM certifié au minimum **FIPS 140-2 Niveau 3** (Azure Key Vault Premium ou Managed HSM).
   - Procédure d'urgence de révocation de clé (**Kill-Switch**) automatisée et testée : neutralisation des données en moins de **15 minutes**.

3. **Protection des Données Personnelles & RGPD :**
   - Pseudonymisation irréversible (hachage **SHA-256 avec sel dynamique**) sur tous les identifiants clients et comptes bancaires exposés dans les modèles décisionnels.
   - Sécurité dynamique à la ligne (**Row-Level Security - RLS**) et à la colonne (**Column-Level Security - CLS**).
   - Purge automatique des données expirées selon la politique légale de conservation.

4. **Auditabilité & Traçabilité Immuable (SOX) :**
   - 100% des logs d'accès, de requêtage et de modification de schéma doivent être streamés vers le SIEM d'entreprise.
   - Rétention immuable **WORM (Write Once, Read Many)** verrouillée sur 365 jours minimum.
