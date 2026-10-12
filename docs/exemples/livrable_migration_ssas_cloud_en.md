# SAFe Agile Implementation Backlog: NovaAnalytics Modernization Engine

---

## 1. Enabler Epic Portfolio Card

```
+---------------------------------------------------------------------------------------------------------------------+
| ENABLER EPIC: ENB-EPIC-01                                                                                           |
| Title: NovaAnalytics Zero-Trust Cloud Modernization & C2 MASSIF Architectural Transformation                        |
| Portfolio: Financial Decision Support Systems                                                                       |
| Epic Owner: System Architect & Agile Delivery Enabler                                                               |
+---------------------------------------------------------------------------------------------------------------------+
```

### 1.1 Epic Statement & Objective
* **Epic Name:** `ENB-EPIC-01: NovaAnalytics Zero-Trust Cloud Modernization & C2 MASSIF Architectural Transformation`
* **Epic Owner:** System Architect & Lead Enterprise Delivery Enabler
* **Start Date / Target PI:** PI-01 to PI-04

**Description:**  
Modernize the core legacy financial analytical infrastructure (`BillingCube`, `RecoveryCube`, and `LedgerCube`) by deprecating on-premises SSAS monolithic servers and establishing a hardened, cloud-native Azure Landing Zone. The target implementation leverages a decoupled lakehouse storage foundation (Delta Lake on ADLS Gen2/OneLake), isolated Power BI Premium/Fabric Capacities, Hexagonal domain ingestion services, and automated Tabular Model Definition Language (TMDL) DevSecOps deployment pipelines—complying strictly with NIST SP 800-207 Zero-Trust and C2 MASSIF classification standards.

### 1.2 Business & Enabler Outcome Hypothesis
* **Scalability & Cost Optimization:** Decoupling compute from storage eliminates over-provisioned bare-metal capacity, mitigating month-end ledger closing query contention and auto-scaling to support over 1,500 concurrent financial consumers.
* **Security & Regulatory Compliance:** Fulfills all CISO Audit reservations (DCA Gateways 1 through 5) by enforcing 100% network isolation via Azure Private Link, Customer-Managed Keys (CMK) backed by Azure Key Vault Premium HSM, Purview Information Protection, and granular Row-Level / Object-Level Security (RLS/OLS).
* **Delivery Agility (ALM):** Transitioning from opaque monolithic `.bim` files to modular TMDL Git schemas managed through automated XMLA CI/CD pipelines reduces deployment cycle time from weeks to hours with zero manual administrative interventions.
* **Domain Integrity:** Isolating statutory balance verification inside a framework-independent Hexagonal Core prevents data corruption prior to analytical ingestion.

### 1.3 Leading Indicators & Success Metrics
1. **Zero-Trust Network Verification:** 0 public IP addresses provisioned across all cloud components (`publicNetworkAccess = Disabled`).
2. **Direct Lake Stability:** 0 silent fallbacks to DirectQuery on `BillingCube` under high-concurrency loads.
3. **Financial Data Parity:** 0.000% calculation variance between AS-IS SSAS cubes and TO-BE models across the past 3 fiscal closing years (36 closed accounting months).
4. **Code Quality & Craftsmanship:** 100% deterministic test execution (< 3 seconds total run time) on core domain logic with > 90% branch coverage; 0 Tabular Best Practice Analyzer (BPA) error violations.
5. **Recovery Objectives:** Recovery Point Objective (RPO) = 0 for ingested Delta records (RPO < 24h disaster scenario); Recovery Time Objective (RTO) < 4 hours via Infrastructure-as-Code (Terraform) automated deployment.

### 1.4 Non-Functional Requirements (NFR) Envelope
* **NFR-SEC-01 (Perimeter):** Strict private routing via Azure Private Endpoints (RFC 1918) across ExpressRoute with MACsec IEEE 802.1AE encryption.
* **NFR-SEC-02 (Crypto):** Data-at-rest encrypted via CMK using Azure Key Vault Premium (FIPS 140-2/3 Level 3 HSM) with Soft-Delete (90 days) and Purge Protection. TLS 1.3 mandated for all transit.
* **NFR-SEC-03 (Isolation):** Dedicated Fabric Capacity SKU allocated strictly for statutory `LedgerCube` workloads to prevent noisy-neighbor risks during monthly closings.
* **NFR-PERF-01 (Latency):** Sub-second visual rendering for 95% of standard financial queries in Power BI.
* **NFR-AUD-01 (Auditability):** 100% immutable audit event forwarding to Microsoft Sentinel with a 365-day retention policy.

### 1.5 Scope Boundaries

```
+-----------------------------------------------------+----------------------------------------------------+
| IN-SCOPE                                            | OUT-OF-SCOPE                                       |
+-----------------------------------------------------+----------------------------------------------------+
| • Dual ExpressRoute & Private Endpoint landing zone | • Direct internet-facing access or public endpoints|
| • Azure Key Vault Premium HSM CMK configuration     | • Generic multi-cloud abstraction frameworks       |
| • Hexagonal Core domain entities & Aggregates (DDD) | • Direct Lake on LedgerCube & RecoveryCube (OLS/RLS|
| • TMDL conversion for Billing, Recovery, and Ledger |   limitations mandate Import Mode per CISO)        |
| • Direct Lake deployment for BillingCube only       | • Continuous streaming Kafka topologies (KISS:     |
| • Large Model Import Mode for Recovery & Ledger     |   micro-batch deterministic watermarks enforced)   |
| • Automated CI/CD via Azure DevOps / XMLA pipelines | • Dedicated Managed HSM pool deployment (demoted   |
| • Microsoft Sentinel 365-day audit integration      |   to AKV Premium HSM per CISO directive)           |
+-----------------------------------------------------+----------------------------------------------------+
```

---

## 2. Prioritized Enabler Features Backlog & WSJF Matrix

The backlog is prioritized using SAFe **Weighted Shortest Job First (WSJF)**:
$$\text{WSJF} = \frac{\text{Cost of Delay (CoD)}}{\text{Job Size}} = \frac{\text{User-Business Value (UBV)} + \text{Time Criticality (TC)} + \text{Risk Reduction / Opportunity Enablement (RR/OE)}}{\text{Job Size (JS)}}$$

Scale for values: 1 to 20 (Fibonacci-like scale).

```
+-------------+----------------------------------------------------+-----+----+-------+-----+----+-------+
| Feature ID  | Feature Name                                       | UBV | TC | RR/OE | CoD | JS | WSJF  |
+-------------+----------------------------------------------------+-----+----+-------+-----+----+-------+
| ENB-FEAT-01 | Zero-Trust Network Foundations & Private Link ALZ  | 13  | 13 |  20   | 46  | 5  |  9.20 |
| ENB-FEAT-02 | FIPS Cryptographic Layer & CMK Key Management       |  8  |  8 |  20   | 36  | 5  |  7.20 |
| ENB-FEAT-03 | Hexagonal Domain Ingestion Core (Tactical DDD)     | 13  |  8 |  13   | 34  | 5  |  6.80 |
| ENB-FEAT-04 | Declarative TMDL Engine & ALM DevSecOps Pipeline    | 13  | 13 |  13   | 39  | 8  |  4.88 |
| ENB-FEAT-05 | Ingestion Adapters & Deterministic Watermarking    | 13  |  8 |   8   | 29  | 8  |  3.63 |
| ENB-FEAT-06 | BillingCube Lakehouse Ingestion & Direct Lake Mode | 20  | 13 |   8   | 41  | 13 |  3.15 |
| ENB-FEAT-07 | Statutory LedgerCube Semantic Engine (Import Mode)  | 20  | 20 |  13   | 53  | 13 |  4.08 |
| ENB-FEAT-08 | RecoveryCube Delinquency Lifecycle (Import & RLS)   | 13  |  8 |   8   | 29  | 8  |  3.63 |
| ENB-FEAT-09 | Audit Immutability, Sentinel Logs & DCA Gates      |  8  | 13 |  20   | 41  | 5  |  8.20 |
+-------------+----------------------------------------------------+-----+----+-------+-----+----+-------+
```

### Execution Sequencing:
1. **Wave 1 (PI-01 Sprint 1-2):** `ENB-FEAT-01` (Network Foundations) & `ENB-FEAT-02` (Crypto/CMK)
2. **Wave 2 (PI-01 Sprint 3-5):** `ENB-FEAT-09` (Audit Foundations), `ENB-FEAT-03` (Hexagonal Domain Core), `ENB-FEAT-04` (TMDL DevSecOps ALM)
3. **Wave 3 (PI-02 Sprint 1-3):** `ENB-FEAT-05` (Ingestion Adapters) & `ENB-FEAT-07` (LedgerCube Statutory Import Engine)
4. **Wave 4 (PI-02 Sprint 4-5):** `ENB-FEAT-06` (BillingCube Direct Lake) & `ENB-FEAT-08` (RecoveryCube Import Engine)

---

## 3. Detailed Technical User Stories Backlog

```
=====================================================================================================================
FEATURE: ENB-FEAT-01 — Zero-Trust Network Foundations & Private Link ALZ
Parent Epic: ENB-EPIC-01 | Target PI: PI-01 | WSJF: 9.20
Description: Establish an Azure Enterprise Landing Zone (ALZ) perimeter adhering to NIST SP 800-207. 
Eliminate public ingress/egress, configure MACsec hybrid routing, and deploy private DNS resolution.
=====================================================================================================================
```

#### User Story: `NOVA-NET-101`
* **Title:** ExpressRoute Dual Circuit Provisioning with MACsec Hardware Encryption & BGP Peering
* **Story Format:**  
  *As an* Infrastructure Architect,  
  *I want* to configure active-active Dual 10 Gbps ExpressRoute circuits between on-premises datacenters and Azure Hub VNet with IEEE 802.1AE MACsec hardware encryption,  
  *So that* all hybrid cross-premises network traffic is encrypted at Layer 2 without crossing the public internet, satisfying C2 MASSIF baseline constraints.
* **Story Points:** 5
* **Technical Tasks:**
  * Define Terraform modules for Azure ExpressRoute Gateway with active-active zone-redundant SKU (`ErGw3AZ`).
  * Implement point-to-point MACsec encryption profiles utilizing pre-shared keys registered in key vaults.
  * Establish BGP route filters advertising strictly private corporate CIDR subnets (RFC 1918) with BFD (Bidirectional Forwarding Detection) enabled.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Hardware-level MACsec encryption verification**
    * **Given** an active BGP peering link established between on-premises core routers and the Azure ExpressRoute gateway,
    * **When** packets traverse the primary or secondary 10 Gbps physical circuit,
    * **Then** 802.1AE MACsec line-rate encryption must be actively asserted with zero plaintext fallbacks observed in physical port telemetry.
  * **Scenario 2: Primary circuit failover tolerance**
    * **Given** high-volume active data traffic flowing across primary ExpressRoute Circuit A,
    * **When** Circuit A experiences a link failure or administrative down state,
    * **Then** traffic must failover automatically to secondary Circuit B via BGP within < 500 ms without TCP connection reset or data transmission drops.

---

#### User Story: `NOVA-NET-102`
* **Title:** Azure Private Endpoints & Hub-Spoke Private DNS Resolver Configuration
* **Story Format:**  
  *As a* Cloud Security Engineer,  
  *I want* to implement Azure Private Endpoints and private DNS resolution zones across all landing zone spokes with public network access strictly disabled,  
  *So that* computational runtimes and analytical engines resolve storage and PaaS resources exclusively via non-routable private IP addresses.
* **Story Points:** 5
* **Technical Tasks:**
  * Deploy Azure Private DNS Zones (`privatelink.blob.core.windows.net`, `privatelink.dfs.core.windows.net`, `privatelink.vaultcore.azure.net`, `privatelink.analysis.windows.net`).
  * Provision Azure Private Endpoints for storage accounts, Key Vault, and Fabric Workspaces.
  * Configure User-Defined Routes (UDR) routing `0.0.0.0/0` outbound traffic to Azure Firewall Premium with deep packet inspection.
  * Set `publicNetworkAccess = "Disabled"` flag across all landing zone PaaS resources via Azure Policy.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: DNS name resolution isolation**
    * **Given** an ingestion engine instance residing within Spoke VNet subnet,
    * **When** it queries the fully qualified domain name of ADLS Gen2 or Azure Key Vault,
    * **Then** the returned IP address must belong to the provisioned private endpoint subnet range (RFC 1918) and never return a public routable IP.
  * **Scenario 2: Public boundary penetration probe**
    * **Given** a client workstation external to the corporate network without VPN or ExpressRoute peering,
    * **When** it attempts an HTTP/HTTPS handshake or connection to any storage, vault, or Fabric resource,
    * **Then** the request must immediately return `HTTP 403 Forbidden` or name resolution failure (`NXDOMAIN`).

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-02 — FIPS Cryptographic Layer & CMK Key Management
Parent Epic: ENB-EPIC-01 | Target PI: PI-01 | WSJF: 7.20
Description: Deploy Azure Key Vault Premium (FIPS 140-2/3 Level 3 HSM) to enforce Customer-Managed Keys (CMK)
across ADLS Gen2, OneLake, and Fabric Capacities, incorporating automated lifecycle rotation and soft-delete guards.
=====================================================================================================================
```

#### User Story: `NOVA-SEC-201`
* **Title:** Azure Key Vault Premium HSM Provisioning with Purge Protection & Soft-Delete Guards
* **Story Format:**  
  *As a* Security Architect,  
  *I want* to deploy Azure Key Vault Premium backed by hardware security modules with Purge Protection and a 90-day Soft-Delete retention lock,  
  *So that* encryption keys cannot be permanently destroyed or purged maliciously, preventing unrecoverable cryptographic operational lockout.
* **Story Points:** 3
* **Technical Tasks:**
  * Provision Azure Key Vault Premium tier in paired primary and secondary recovery regions using Terraform.
  * Apply resource locks (`CanNotDelete`) and configure flags: `enable_purge_protection = true`, `soft_delete_retention_days = 90`.
  * Establish Entra ID Key Vault Access Policies utilizing Azure RBAC (`Key Vault Crypto Service Encryption User`).
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Key Vault deletion guard assertion**
    * **Given** a provisioned Key Vault Premium instance containing CMK root keys,
    * **When** an administrative account attempts to execute a purge or immediate deletion API call,
    * **Then** the operation must fail with an access policy error, retaining keys in soft-delete state for the enforced 90 days.
  * **Scenario 2: FIPS HSM boundary attestation**
    * **Given** root cryptographic key creation commands initiated via automation,
    * **When** keys are generated within the vault,
    * **Then** the key specification must be configured as `RSA-HSM` or `EC-HSM` meeting FIPS 140-2/3 Level 3 verification.

---

#### User Story: `NOVA-SEC-202`
* **Title:** Storage at Rest Customer-Managed Key (CMK) Double Encryption & Automated 365-Day Rotation
* **Story Format:**  
  *As a* SecOps Engineer,  
  *I want* to bind storage accounts and semantic capacity compute to Azure Key Vault CMK keys and configure Azure Event Grid automated key rotation,  
  *So that* all static storage is double-encrypted and cryptographic root keys rotate yearly without service degradation.
* **Story Points:** 5
* **Technical Tasks:**
  * Configure User-Assigned Managed Identity (UAMI) for ADLS Gen2 and Power BI Fabric Capacity.
  * Grant UAMI permissions `Wrap Key` / `Unwrap Key` on target Key Vault CMK.
  * Configure double encryption (`encryption_at_rest_with_platform_and_customer_managed_keys = true`).
  * Deploy Azure Event Grid subscription listening to `Microsoft.KeyVault.KeyNearExpiry` events, triggering automated key version roll via Azure Automation runbook.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Storage encryption validation**
    * **Given** ADLS Gen2 storage accounts provisioned for the Lakehouse,
    * **When** parquet files are written to the data lake,
    * **Then** the files must be written with storage-layer double encryption validated via ARM properties (`keySource = Microsoft.Keyvault`).
  * **Scenario 2: Automated key rotation execution**
    * **Given** a CMK approaching expiration (30 days remaining),
    * **When** the Event Grid notification fires,
    * **Then** a new key version must be generated automatically in AKV Premium, and downstream storage must retain read-access to legacy-encrypted blocks while re-wrapping new writes.

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-03 — Hexagonal Domain Ingestion Core (Tactical DDD)
Parent Epic: ENB-EPIC-01 | Target PI: PI-01 | WSJF: 6.80
Description: Implement the framework-independent Domain Core for Ledger, Recovery, and Billing contexts 
following Hexagonal Architecture (Ports & Adapters) with 100% deterministic test isolation.
=====================================================================================================================
```

#### User Story: `NOVA-DOM-301`
* **Title:** Statutory Ledger Aggregate Root & Invariant Verification Engine
* **Story Format:**  
  *As a* Lead Software Engineer,  
  *I want* to implement the `LedgerPartition` aggregate root and immutable value objects (`Money`, `FiscalPeriod`, `ChartOfAccountCode`, `JournalEntry`) in pure C#,  
  *So that* double-entry balancing rules and watermark progression are enforced with mathematical determinism prior to persistence.
* **Story Points:** 5
* **Technical Tasks:**
  * Create `NovaAnalytics.Domain` project with zero external dependencies (no Azure SDKs, EF Core, or frameworks).
  * Implement Value Objects with strict encapsulation and fail-fast invariants (`Money`, `FiscalPeriod`, `TenantId`, `ChartOfAccountCode`).
  * Build `JournalEntry` verifying debit/credit summation matching (`debit.Amount == credit.Amount`).
  * Implement `LedgerPartition` aggregate root guarding operations `AppendJournalEntry()` and `SealPartition()`.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Double-entry balance invariant enforcement**
    * **Given** an active `LedgerPartition`,
    * **When** an application attempts to append a `JournalEntry` where total debits do not equal total credits,
    * **Then** the aggregate must immediately throw a `DomainInvariantViolationException` and reject state modification.
  * **Scenario 2: Partition sealing modification block**
    * **Given** a `LedgerPartition` that has been explicitly sealed (`IsSealed == true`),
    * **When** any new journal entry is appended,
    * **Then** the domain must throw a `DomainInvariantViolationException` indicating the partition is locked.
  * **Scenario 3: Sequence watermark progression**
    * **Given** an aggregate with current watermark sequence $N$,
    * **When** an entry arrives with sequence number $\le N$,
    * **Then** the aggregate must throw a `DomainInvariantViolationException` to prevent out-of-order state mutations.

---

#### User Story: `NOVA-DOM-302`
* **Title:** Inbound & Outbound Port Contract Definition & Application Orchestration Services
* **Story Format:**  
  *As a* Software Craftsman,  
  *I want* to establish driver and driven interfaces (`ISynchronizeLedgerPartitionUseCase`, `ILedgerPartitionRepository`, `ISecurityAuditSinkPort`) and application use-case coordinators,  
  *So that* core business workflows are fully decoupled from concrete database and network infrastructure.
* **Story Points:** 3
* **Technical Tasks:**
  * Define Inbound Ports (`ISynchronizeLedgerPartitionUseCase`, `IIngestBillingBatchUseCase`).
  * Define Outbound Ports (`ILedgerPartitionRepository`, `IBillingRecordRepository`, `ISecurityAuditSinkPort`, `ICryptographicVerificationPort`).
  * Implement `SynchronizeLedgerPartitionService` coordinating domain aggregates and driven ports.
  * Write unit test suites using in-memory mockless stubs/fakes achieving 100% deterministic assertion.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Complete port isolation assertion**
    * **Given** the `NovaAnalytics.Domain` compiled assembly,
    * **When** static reflection or dependency analysis scans assembly references,
    * **Then** it must contain zero references to Microsoft Azure, Fabric, ADLS, or storage libraries.
  * **Scenario 2: Orchestration workflow execution**
    * **Given** a valid `IngestLedgerPartitionCommand`,
    * **When** `SynchronizeLedgerPartitionService.ExecuteAsync()` is invoked against fake in-memory repositories,
    * **Then** the partition must be loaded, modified, saved, and an audit event emitted with `Success == true`.

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-04 — Declarative TMDL Engine & ALM DevSecOps Pipeline
Parent Epic: ENB-EPIC-01 | Target PI: PI-01 | WSJF: 4.88
Description: Establish Tabular Model Definition Language (TMDL) multi-folder Git structures with automated
CI/CD release pipelines via XMLA endpoints, including automated Tabular Best Practice Analyzer (BPA) checks.
=====================================================================================================================
```

#### User Story: `NOVA-ALM-401`
* **Title:** Multi-Folder TMDL Serialization & Git Branching Structure Implementation
* **Story Format:**  
  *As an* Analytics Engineer,  
  *I want* to convert monolithic `.bim` model definitions into multi-folder Tabular Model Definition Language (TMDL) format within Git,  
  *So that* measures, calculation groups, partitions, and roles can be code-reviewed, merged, and versioned without merge conflicts.
* **Story Points:** 3
* **Technical Tasks:**
  * Configure Tabular Editor 3 CLI scripts to extract existing SSAS model metadata and serialize to TMDL.
  * Structure source code directories into folders: `tables/`, `roles/`, `relationships/`, `cultures/`, `expressions/`.
  * Establish Git branch protection rules requiring peer review and automated validation pipeline passing prior to PR merge.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: TMDL multi-folder commit verification**
    * **Given** a model refactoring task changing a DAX measure formula,
    * **When** the developer stages and commits changes,
    * **Then** the Git diff must isolate changes strictly to the single modified table/measure `.tmdl` file, leaving all other structural files untouched.
  * **Scenario 2: Bidirectional compilation validation**
    * **Given** a serialized TMDL repository structure,
    * **When** the Tabular Editor 3 compiler executes `decompile` and `compile`,
    * **Then** the output Tabular Object Model (TOM) must preserve structural parity with 0 metadata truncation errors.

---

#### User Story: `NOVA-ALM-402`
* **Title:** Automated ALM CI/CD Pipeline with Tabular Best Practice Analyzer (BPA) Gating
* **Story Format:**  
  *As a* DevSecOps Engineer,  
  *I want* to implement an Azure DevOps / GitLab CI pipeline that executes Tabular Best Practice Analyzer rules and deploys via XMLA endpoints using Workload Identity Federation,  
  *So that* unoptimized, insecure, or hardcoded models are automatically blocked from deployment.
* **Story Points:** 5
* **Technical Tasks:**
  * Author CI YAML pipeline steps executing Tabular Editor CLI with standardized enterprise BPA rulesets.
  * Implement gating: pipeline fails if any BPA rule with Severity = "Error" is violated (e.g., missing descriptions on measures, invalid DAX syntax, unindexed relationship foreign keys).
  * Configure continuous deployment CD step authenticating via Entra ID Workload Identity to deployment target XMLA read/write endpoints (`powerbi://api.powerbi.com/v1.0/myorg/...`).
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Pipeline gate blocking BPA violations**
    * **Given** a pull request containing unformatted DAX measures or unindexed relationship keys flagged as severity "Error",
    * **When** the continuous integration validation job runs,
    * **Then** the build pipeline must fail immediately, comment on the pull request with violation details, and block merge.
  * **Scenario 2: Zero-credential deployment via XMLA**
    * **Given** a merged commit on the release branch,
    * **When** the deployment step runs,
    * **Then** it must authenticate to the target Fabric/Power BI Premium workspace XMLA endpoint using Workload Identity Federation with zero plaintext secrets stored in pipeline variables.

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-05 — Ingestion Adapters & Deterministic Watermarking
Parent Epic: ENB-EPIC-01 | Target PI: PI-02 | WSJF: 3.63
Description: Implement driven infrastructure adapters for Delta Lake storage and on-premises ingestion
via High-Availability Self-Hosted Integration Runtime (SHIR) VM clusters using incremental watermarks.
=====================================================================================================================
```

#### User Story: `NOVA-ING-501`
* **Title:** High-Availability Self-Hosted Integration Runtime (SHIR) Cluster Deployment
* **Story Format:**  
  *As an* Infrastructure Engineer,  
  *I want* to deploy a dedicated 4-node Self-Hosted Integration Runtime (SHIR) cluster on hardened private virtual machines within the ingress spoke,  
  *So that* extraction of on-premises transactional data executes with high availability and without inbound firewall openings.
* **Story Points:** 5
* **Technical Tasks:**
  * Provision 4 dedicated Windows Server VMs across separate availability zones in the Ingestion spoke VNet.
  * Install Azure Data Factory SHIR software and link nodes into a single resilient HA Gateway cluster.
  * Configure outbound-only proxy rules allowing communication solely to Azure Service Bus Relay FQDNs on TCP port 443; eliminate all inbound rules.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Cluster node outage failover**
    * **Given** an ongoing scheduled ingestion pipeline processing ledger batches,
    * **When** one SHIR virtual machine is abruptly powered off or terminated,
    * **Then** remaining cluster nodes must re-balance and continue the data pipeline execution without pipeline job failure.
  * **Scenario 2: Outbound network egress restriction**
    * **Given** network inspection active on the ingestion spoke firewall,
    * **When** SHIR VMs communicate outward,
    * **Then** packet logs must show connections exclusively targeting designated Service Bus endpoints on port 443 with zero arbitrary internet destinations allowed.

---

#### User Story: `NOVA-ING-502`
* **Title:** Incremental Watermark Delta Lake Storage Adapter
* **Story Format:**  
  *As a* Data Engineer,  
  *I want* to implement driven port adapters that write validated domain records into Delta Parquet lakehouse storage using sequential watermark checkpoints,  
  *So that* data ingestion is idempotent, prevents record duplication, and adheres to ACID transaction semantics.
* **Story Points:** 5
* **Technical Tasks:**
  * Implement `ILedgerPartitionRepository` concrete adapter using Azure Data Lake Storage Gen2 SDK / Delta Kernel.
  * Implement watermark tracking tables recording `LastProcessedSequenceNumber` and `TimestampUtc`.
  * Ensure writing utilizes atomic Delta commits (`MERGE` statements conditioned on primary business keys and sequence progression).
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Idempotent replay execution**
    * **Given** a historical batch of billing records previously committed at Watermark $X$,
    * **When** the ingestion adapter is invoked again with the identical batch payload,
    * **Then** the adapter must detect the existing watermark, perform an idempotent upsert, and avoid creating duplicate records in underlying Delta Parquet files.
  * **Scenario 2: Atomic ACID rollback on transaction failure**
    * **Given** an active multi-part Delta commit write operation,
    * **When** a storage or network failure interrupts the write midway through,
    * **Then** the transaction must abort cleanly, leaving the Delta log in its prior valid state with zero partial uncommitted parquet files visible to consumers.

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-06 — BillingCube Lakehouse Ingestion & Direct Lake Mode
Parent Epic: ENB-EPIC-01 | Target PI: PI-02 | WSJF: 3.15
Description: Migrate BillingCube transactional datasets to Delta Parquet and deploy the semantic layer in
Direct Lake mode, adhering strictly to CISO directives (no OLS, scalar RLS predicates, fallback guards).
=====================================================================================================================
```

#### User Story: `NOVA-MOD-601`
* **Title:** BillingCube Star-Schema Modernization & Delta Lake Ingestion
* **Story Format:**  
  *As an* Analytics Engineer,  
  *I want* to transform legacy SSAS BillingCube tables into a clean Delta Lake star schema (Fact Invoicing, Dim Customer, Dim Billing Cycle, Dim Date),  
  *So that* analytical queries query optimized Delta Parquet files directly without ETL transformation overhead.
* **Story Points:** 8
* **Technical Tasks:**
  * Design Delta Lake schema: `fact_billing_transactions`, `dim_customer`, `dim_billing_cycle`, `dim_date`.
  * Execute historical backfill using date-partitioned micro-batches to prevent ExpressRoute bandwidth saturation.
  * Optimize Delta tables with V-Order indexing and Z-Ordering on `CustomerID` and `TransactionDate`.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Data parity verification against legacy SSAS**
    * **Given** 3 years of historical billing data ingested into Delta Parquet tables,
    * **When** aggregation queries calculate total billing amounts, tax figures, and invoice counts,
    * **Then** results must show a 0.000% numerical variance compared to the AS-IS on-premises SSAS BillingCube.
  * **Scenario 2: Delta storage optimization assertions**
    * **Given** Delta storage tables loaded with historical partitions,
    * **When** table metadata is inspected via Fabric utilities,
    * **Then** tables must demonstrate active V-Order encoding and compaction to eliminate small file overhead.

---

#### User Story: `NOVA-MOD-602`
* **Title:** BillingCube Direct Lake Semantic Model Deployment & Fallback Guard Telemetry
* **Story Format:**  
  *As a* Semantic Model Architect,  
  *I want* to configure the modernized BillingCube Power BI semantic model in Direct Lake mode with scalar RLS and fallback monitoring alerts,  
  *So that* consumers experience sub-second report query rendering without silent drops into DirectQuery mode.
* **Story Points:** 5
* **Technical Tasks:**
  * Create TMDL definition pointing the semantic model directly to OneLake Delta tables in Direct Lake mode.
  * Implement simple scalar Row-Level Security (RLS) predicates using `[TenantId] = USERNAME()`.
  * Verify zero Object-Level Security (OLS) rules are defined on the model (per CISO mandate).
  * Configure telemetry alerts via Azure Log Analytics tracking event `DirectQuery fallback occurred`.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Direct Lake operational rendering**
    * **Given** the BillingCube semantic model deployed in workspace capacity,
    * **When** concurrent Power BI reporting queries execute against the model,
    * **Then** 100% of queries must resolve via Direct Lake mode, achieving sub-second response times for 95% of queries.
  * **Scenario 2: Automated fallback alerting**
    * **Given** semantic model telemetry streaming to Log Analytics,
    * **When** any query triggers an unsupported function causing a fallback to DirectQuery,
    * **Then** an alert must be logged immediately with high severity, notifying SecOps and Engineering within 60 seconds.

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-07 — Statutory LedgerCube Semantic Engine (Import Mode)
Parent Epic: ENB-EPIC-01 | Target PI: PI-02 | WSJF: 4.08
Description: Deploy the statutory LedgerCube into Power BI Premium Large Model Import Mode on a dedicated
isolated Capacity SKU, enforcing statutory Object-Level Security (OLS) and dynamic Row-Level Security (RLS).
=====================================================================================================================
```

#### User Story: `NOVA-MOD-701`
* **Title:** Dedicated Capacity SKU Provisioning for Statutory Ledger Workloads
* **Story Format:**  
  *As an* Enterprise Solution Architect,  
  *I want* to provision a dedicated Fabric/Power BI Premium Capacity SKU isolated strictly for the statutory `LedgerCube`,  
  *So that* intensive month-end financial closing computations cannot experience noisy-neighbor resource throttling from other corporate workloads.
* **Story Points:** 5
* **Technical Tasks:**
  * Provision dedicated Power BI Premium Capacity SKU (`P1`/`F64` or higher) isolated from the general analytical pool.
  * Configure workspace bindings routing `LedgerCube` exclusively to this dedicated capacity.
  * Enforce resource governances and alerts tracking CPU and memory saturation thresholds.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Compute isolation verification**
    * **Given** concurrent reporting executions and batch loads executing across Billing and Recovery domains,
    * **When** peak month-end general ledger closing queries execute on the Ledger workspace,
    * **Then** Ledger compute utilization must remain completely isolated on its dedicated capacity without shared memory throttling.
  * **Scenario 2: Large dataset storage format enablement**
    * **Given** the target Ledger workspace,
    * **When** workspace properties are configured via automation,
    * **Then** `Large Dataset Storage Format` must be set to `Enabled` and bound to the capacity.

---

#### User Story: `NOVA-MOD-702`
* **Title:** Statutory Ledger Dynamic RLS & Object-Level Security (OLS) Configuration
* **Story Format:**  
  *As an* Analytics Security Engineer,  
  *I want* to implement dynamic Row-Level Security and Object-Level Security masking sensitive accounts and journal dimensions in the LedgerCube TMDL model,  
  *So that* unreleased financial closings and confidential statutory accounts are masked from unauthorized internal personas.
* **Story Points:** 8
* **Technical Tasks:**
  * Define Object-Level Security (OLS) rules in TMDL metadata setting `tablePermission = none` on sensitive accounts (`Executive_Compensation`, `M&A_Provisions`) for standard user roles.
  * Implement dynamic RLS filtering journal records by `UserPrincipalName()` mapped to statutory organizational entities.
  * Deploy automated DAX unit tests asserting security filtering across multiple mock user identities.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Object-Level Security masking assertion**
    * **Given** a business analyst user belonging to the general financial reporting group,
    * **When** they query the LedgerCube via Power BI Desktop or Service,
    * **Then** the masked statutory tables and measures must not appear in field lists, and explicit DAX queries targeting them must return an authorization failure.
  * **Scenario 2: Dynamic Row-Level Security isolation**
    * **Given** an accounting manager assigned strictly to Entity `FR-PARIS`,
    * **When** they generate general ledger balance reports,
    * **Then** returned journal entries must contain exclusively `TenantId == "FR-PARIS"`, with zero records accessible from other operating units.

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-08 — RecoveryCube Delinquency Lifecycle Modernization (Import & RLS)
Parent Epic: ENB-EPIC-01 | Target PI: PI-02 | WSJF: 3.63
Description: Modernize RecoveryCube into Large Model Import Mode, modeling debt collection lifecycles,
dunning stages, and dynamic RLS protecting sensitive customer solvency and default records.
=====================================================================================================================
```

#### User Story: `NOVA-MOD-801`
* **Title:** RecoveryCube Delinquency State Machine Modeling & TMDL Implementation
* **Story Format:**  
  *As an* Analytics Engineer,  
  *I want* to codify the RecoveryCube delinquency lifecycle and dunning bucket state machine into TMDL using Large Model Import Mode,  
  *So that* operational debt recovery metrics, aging brackets, and legal dunning workflows are modeled accurately.
* **Story Points:** 5
* **Technical Tasks:**
  * Model fact and dimension structures: `fact_recovery_actions`, `dim_delinquency_bucket`, `dim_dunning_stage`.
  * Implement DAX calculation groups handling aging rollups (30/60/90/180+ days past due).
  * Configure automated incremental refresh partitions in TMDL using date range parameters (`RangeStart`, `RangeEnd`).
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Incremental partition refresh validation**
    * **Given** the RecoveryCube deployed in Import Mode with historical data archived,
    * **When** an incremental refresh pipeline executes via XMLA,
    * **Then** only active modified partitions (last 30 days) must refresh in memory, preserving historical closed partitions unchanged.
  * **Scenario 2: Calculation group accuracy**
    * **Given** customer accounts in various dunning phases,
    * **When** financial controllers apply the Delinquency Aging calculation group,
    * **Then** recovery exposure totals must reconcile with 0 variance against operational debt management registers.

---

#### User Story: `NOVA-MOD-802`
* **Title:** Sensitive Default Data Row-Level Security & PII Protection
* **Story Format:**  
  *As a* Data Privacy Officer,  
  *I want* to implement dynamic RLS and data masking on RecoveryCube customer identification and banking attributes,  
  *So that* collection agents view only their assigned recovery portfolios and GDPR Article 9/10 sensitive data is safeguarded.
* **Story Points:** 5
* **Technical Tasks:**
  * Define dynamic RLS rules in TMDL binding `CollectorID` to Azure Entra ID user claims.
  * Apply data masking and redaction on sensitive banking attributes (IBAN, Tax Reference numbers).
  * Validate that downstream queries executed by unassigned collectors yield null results.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Collector portfolio isolation**
    * **Given** Collector User A assigned to Portfolio `DEFAULT-COMMERCIAL`,
    * **When** they browse the RecoveryCube semantic model,
    * **Then** they must only see records where `Portfolio == "DEFAULT-COMMERCIAL"`, with default accounts belonging to other teams masked.
  * **Scenario 2: Data export protection**
    * **Given** an authorized user reviewing recovery dashboards,
    * **When** they attempt to export raw underlying records to Excel/CSV,
    * **Then** Purview DLP policies must prevent export of masked customer PII data elements.

---

```
=====================================================================================================================
FEATURE: ENB-FEAT-09 — Audit Immutability, Sentinel Logs & DCA Gates
Parent Epic: ENB-EPIC-01 | Target PI: PI-01 | WSJF: 8.20
Description: Fulfill CISO Audit Mandates by routing 100% of audit logs to Microsoft Sentinel with a 365-day
immutable retention policy, binding Purview sensitivity labels, and satisfying DCA Homologation Gates.
=====================================================================================================================
```

#### User Story: `NOVA-AUD-901`
* **Title:** Immutable Audit Streaming to Microsoft Sentinel with 365-Day Retention
* **Story Format:**  
  *As a* SecOps Lead,  
  *I want* to stream all control-plane and data-plane diagnostic logs (AKV, ADLS, Power BI Activity, Azure Firewall) to a dedicated Log Analytics / Sentinel workspace with a 365-day immutable retention policy,  
  *So that* all access attempts and administrative events satisfy non-repudiation and auditability requirements.
* **Story Points:** 3
* **Technical Tasks:**
  * Configure diagnostic settings on all Landing Zone resources pointing to centralized Log Analytics.
  * Configure Sentinel workspace retention policy: `retentionInDays = 365`.
  * Enable Immutable Storage policies (WORM compliant) on underlying audit log storage sinks.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Administrative action audit logging**
    * **Given** an authorized administrator updating an XMLA model partition or changing a Key Vault policy,
    * **When** the operation completes,
    * **Then** a structured security audit record must appear in Microsoft Sentinel tables within < 5 minutes.
  * **Scenario 2: Immutability assertion**
    * **Given** historical security audit logs stored in the workspace,
    * **When** an administrator attempts to delete, truncate, or reduce retention periods on historical logs,
    * **Then** the Azure control plane must reject the request via immutable policy locks.

---

#### User Story: `NOVA-AUD-902`
* **Title:** Microsoft Purview Information Protection Sensitivity Label Binding
* **Story Format:**  
  *As a* Data Protection Officer,  
  *I want* to bind Microsoft Purview `RESTRICTED - FINANCIAL / C2 MASSIF` sensitivity labels programmatically to all three semantic models,  
  *So that* encryption, downstream DLP, and export protections are inherited automatically across all Power BI artifacts.
* **Story Points:** 3
* **Technical Tasks:**
  * Define sensitivity label GUIDs within Microsoft Purview Information Protection.
  * Integrate label assignment into the automated TMDL deployment pipeline via XMLA metadata injection.
  * Configure Conditional Access Policies enforcing managed-device compliance for accessing labeled models.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Mandatory sensitivity label inheritance**
    * **Given** a successful automated deployment of `LedgerCube` or `BillingCube`,
    * **When** users open the report in Power BI Service or connect via Excel,
    * **Then** the banner must display `RESTRICTED - FINANCIAL / C2 MASSIF` and apply corporate encryption policies.
  * **Scenario 2: Unauthorized exfiltration blockage**
    * **Given** an unmanaged personal device attempting to access a labeled model,
    * **When** authentication evaluates Conditional Access policies,
    * **Then** access must be blocked immediately, logging a security alert in Sentinel.

---

#### User Story: `NOVA-AUD-903`
* **Title:** DCA Homologation Gate Execution & Automated DR Failover Drill
* **Story Format:**  
  *As the* System Architect & Delivery Enabler,  
  *I want* to execute an automated disaster recovery deployment drill via Terraform in a secondary paired region and document DCA Homologation Gates 1 through 5,  
  *So that* the formal CISO approval gate is cleared for production cutover.
* **Story Points:** 5
* **Technical Tasks:**
  * Author end-to-end Terraform automation executing full platform redeployment in Azure secondary paired region.
  * Execute drill measuring Recovery Time Objective (RTO < 4 hours) and Recovery Point Objective (RPO < 24 hours).
  * Compile formal DCA compliance artifact package verifying Gates 1 to 5 for CISO review.
* **Acceptance Criteria (Given / When / Then):**
  * **Scenario 1: Disaster recovery redeployment execution**
    * **Given** primary region outage simulated during an operational drill,
    * **When** the disaster recovery Terraform pipeline is triggered targeting the paired region,
    * **Then** all landing zone networks, vaults, storage, and semantic models must be fully provisioned and verified in < 4 hours.
  * **Scenario 2: Homologation sign-off readiness**
    * **Given** completed execution of test matrices across Gates 1 (Network), 2 (Crypto), 3 (RLS/OLS), 4 (DevSecOps), and 5 (Audit/DR),
    * **When** audit logs and compliance evidences are aggregated,
    * **Then** 100% of verification criteria must pass with zero critical or high reservations remaining.

---

## 4. Standardized Definition of Done (DoD)

To ensure operational excellence, technical craftsmanship, and C2 MASSIF security compliance across every iteration, all User Stories delivered by the Agile Release Train must satisfy the following **Definition of Done (DoD)** before being marked as **Accepted**:

```
+---------------------------------------------------------------------------------------------------------------------+
|                                          STANDARDIZED DEFINITION OF DONE (DoD)                                      |
|                                       NovaAnalytics Platform — C2 MASSIF Baseline                                   |
+---------------------------------------------------------------------------------------------------------------------+
```

### 1. Hexagonal & Domain Purity (Craftsmanship Standard)
* [ ] The Domain Core layer (`NovaAnalytics.Domain`) contains **zero dependencies** on external frameworks, Azure SDKs, Delta Spark drivers, database connectors, or presentation components.
* [ ] All business invariants, calculations, and rules are encapsulated strictly within **Aggregates, Entities, and immutable Value Objects**.
* [ ] Domain state modifications fail-fast: invalid business states cannot be instantiated (throwing explicit domain validation exceptions).
* [ ] Boundary interactions execute exclusively through strongly-typed **Inbound (Driver) and Outbound (Driven) Ports**.

### 2. Testing, Test-Driven Development (TDD) & Quality Gates
* [ ] **100% Deterministic Domain Unit Testing:** Pure domain unit tests execute entirely in-memory with **0 external dependencies** (no network, no file I/O, no database).
* [ ] Test execution speed: the entire domain test suite completes in **< 3 seconds**.
* [ ] **Code Coverage:** Domain Core achieves **$\ge$ 90% branch coverage** and **100% aggregate invariant coverage**.
* [ ] Application Use Cases are thoroughly validated using fast in-memory test doubles (stubs/fakes); zero mocking of domain models.
* [ ] Numerical parity validation confirms **0.000% variance** between TO-BE and AS-IS financial results across targeted historical test partitions.

### 3. C2 MASSIF & Zero-Trust Security Baseline
* [ ] **Network Isolation:** Public network access is disabled (`publicNetworkAccess = Disabled`). All resource communications resolve strictly via **Azure Private Endpoints (RFC 1918)**.
* [ ] **Cryptographic Assurance:** Data at rest is encrypted via **Customer-Managed Keys (CMK)** backed by **Azure Key Vault Premium (FIPS 140-2/3 Level 3 HSM)** with Purge Protection and Soft-Delete active. Data in transit mandates **TLS 1.3**.
* [ ] **Identity & Least Privilege:** Zero credentials, keys, or SAS tokens exist in source code or Git. Authentication is enforced strictly via **Entra ID Managed Identities** or **Workload Identity Federation**.
* [ ] **Security Scans:** Static Application Security Testing (SAST) and secret detection scans (e.g., Gitleaks, Trivy, SonarQube) return **0 high or medium vulnerabilities**.
* [ ] **Purview Governance:** Relevant sensitivity labels (`RESTRICTED - FINANCIAL / C2 MASSIF`) are applied.

### 4. Semantic Engine & Tabular Model Standards
* [ ] The data model is serialized in modular **TMDL format** and committed to Git (no monolithic `.bim` files permitted).
* [ ] The model passes the automated **Tabular Best Practice Analyzer (BPA)** with **0 errors and 0 critical warnings**.
* [ ] Models targeting **Direct Lake Mode** (`BillingCube`) contain **zero Object-Level Security (OLS)** rules and utilize only supported scalar RLS predicates.
* [ ] Models requiring OLS and complex dynamic RLS (`LedgerCube`, `RecoveryCube`) are deployed exclusively in **Power BI Premium Large Model Import Mode** on dedicated capacity.
* [ ] DAX expressions avoid unoptimized iterators and contain descriptive metadata comments.

### 5. Infrastructure-as-Code (IaC) & DevSecOps ALM
* [ ] 100% of infrastructure provisioning is codified in **Terraform**, formatted, validated, and documented in accordance with the Azure Well-Architected Framework.
* [ ] Deployments to workspaces execute fully automated via **XMLA Read/Write endpoints** triggered from the CI/CD pipeline using Service Principals/Workload Identities; zero manual portal updates.
* [ ] Configuration changes are peer-reviewed through pull requests requiring at least **two independent senior approvals** (including one System Architect/Security Lead).
* [ ] Rollback strategy and disaster recovery procedures are fully documented and validated via automated scripts.

### 6. Auditability & Observability
* [ ] Diagnostic telemetry for all control-plane and data-plane operations is verified streaming to the central **Azure Log Analytics / Microsoft Sentinel** workspace.
* [ ] Audit events conform to non-repudiation requirements and satisfy the **365-day immutable retention policy**.
* [ ] Operational performance and fallback alerts (e.g., Direct Lake to DirectQuery fallback, capacity memory pressure) are active and routed to on-call engineering dashboards.