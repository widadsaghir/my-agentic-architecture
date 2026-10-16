Date : Jeudi 15 octobre 2026

# Modèle de Discours Oral : L'Architecte Augmenté

**Durée totale de parole :** 15 minutes (hors vidéo de démo et session de questions)  
**Tonalité :** Confraternelle, directe, professionnelle, passionnée et pragmatique.  
**Objectif :** Embarquer l'auditoire par le vécu commun, démontrer la rigueur de l'approche et donner envie de voir la démo.

---

## Slide 1 : Titre & Accroche (Minute 00:00 - 01:30)

Bonjour à toutes et à tous.

Je suis particulièrement heureux de vous retrouver aujourd'hui pour cet échange entre pairs. 

Pour démarrer, j'aimerais vous poser une question très directe : combien de jours, ou de semaines, vous a demandé la rédaction de votre tout dernier dossier d'architecture ? Et surtout, sur ces dizaines d'heures passées devant votre clavier, quelle proportion était réellement consacrée à de la réflexion pure, à de l'analyse d'impact et à des arbitrages de conception ?

Si votre quotidien ressemble au mien, la réponse est souvent un peu amère. Nous avons choisi ce métier pour résoudre des équations complexes, concevoir des systèmes résilients et guider les choix stratégiques de l'entreprise. Pourtant, une part écrasante de notre temps s'évapore dans la mise en forme de documents, la déclinaison manuelle d'exigences et la mise à jour de schémas.

L'objet de notre session d'aujourd'hui n'est pas de vous parler d'un énième gadget d'intelligence artificielle qui écrit des textes génériques. Je viens vous partager un retour d'expérience très concret sur la mise en place d'une brigade multi-agents spécialisée, pensée par et pour des architectes, capable de nous décharger de la corvée documentaire tout en renforçant notre exigence méthodologique.

---

## Slide 2 : Le Paradoxe Quotidien de l'Architecte (Minute 01:30 - 03:30)

Regardons la réalité en face. Aujourd'hui, près de soixante-dix pour cent de notre temps utile est capté par la logistique documentaire. 

Nous passons des journées entières à :
- Rédiger des dossiers d'architecture technique de quarante ou cinquante pages, où de nombreux chapitres sont des réécritures de contextes connus.
- Traduire à la main nos intentions d'architecture en dizaines d'Epics et d'Enabler Stories sous Jira pour que les équipes agiles puissent démarrer leurs sprints.
- Remplir manuellement des grilles de conformité sécurité, des formulaires d'homologation et des matrices d'analyse des risques.
- Redessiner les mêmes flux sous plusieurs formats pour plaire à différents comités : en Draw.io pour les uns, en PlantUML pour les développeurs, en Mermaid pour la documentation dans Git.

Pendant que nous faisons ce travail de scribe, nous ne sommes pas sur le terrain avec les équipes de développement. Nous manquons de temps pour challenger en profondeur les choix d'infrastructure. Et surtout, nous souffrons d'un manque criant de contradictoire au quotidien. Dans la plupart de nos projets, nous sommes seuls face à notre copie jusqu'au jour du passage en comité officiel d'architecture.

---

## Slide 3 : Le Mirage du Simple Chatbot IA (Minute 03:30 - 05:30)

Lorsque les modèles d'IA générative sont arrivés, beaucoup d'entre nous ont fait le test : ouvrir ChatGPT ou Gemini, copier-coller un besoin et lui demander d'écrire une architecture.

Et nous avons tous constaté la même impasse. 

Un chatbot classique est un interlocuteur poli et complaisant. Vous lui proposez une solution complexe avec un bus d'événements et trois microservices pour un besoin qui mériterait un simple batch monolithique ? Il vous répondra que c'est une excellente idée et vous écrira la configuration sans sourciller. 

Il présente trois défauts majeurs pour notre métier :
- Il n'a aucun esprit contradictoire. Il ne traque ni les points uniques de défaillance, ni la sur-ingénierie, ni les coûts cachés dans le cloud.
- Il ignore notre doctrine d'entreprise. Il ne connaît pas nos exigences strictes de sécurité Zero-Trust, notre règle de chiffrement des données de niveau deux ou notre standard d'architecture hexagonale.
- Il ne dispose d'aucun outil technique déterministe. Il invente du texte, mais il est incapable de produire un fichier Draw.io exploitable ou un export CSV propre et directement importable dans Jira.

Bref, un simple LLM ne peut pas jouer le rôle d'architecte. En revanche, si on l'organise en un collectif d'agents spécialisés, soumis à des rôles stricts et dotés d'outils rigoureux, le résultat change du tout au tout.

---

## Slide 4 : Le Concept de la Brigade Multi-Agents (Minute 05:30 - 08:30)

C'est exactement la genèse de notre plateforme : la Multi-Agent Architecture Platform.

Plutôt qu'un assistant fourre-tout, nous avons modélisé une véritable brigade de spécialistes virtuels qui travaillent ensemble autour d'une table d'architecture.

Voici comment ils se répartissent les rôles :
- Le Lead Architecture Manager orchestre le travail global et rédige la synthèse exécutive selon les huit phases de la méthode TOGAF.
- Le Solution Architect traite la macro-architecture, les patrons de résilience cloud et la communication asynchrone.
- Le Challenger, ou Red Team. C'est l'agent le plus précieux du collectif. Son unique mission consiste à attaquer le travail du Solution Architect. Il cherche les SPOF, applique impitoyablement les principes KISS et YAGNI, et met le doigt sur chaque complexité inutile.
- Le CISO & Data Protection Architect audite chaque choix sous l'angle du Zero-Trust NIST, classe les flux en niveaux de sensibilité et vérifie les mécanismes de chiffrement.
- Le Software Crafter descend au niveau du code : il garantit le découpage en architecture hexagonale, les agrégats DDD et la testabilité unitaire.
- Le SAFe Delivery Enabler prend la conception validée et la découpe immédiatement en User Stories prêtes pour le backlog.
- Enfin, l'agent FinOps chiffre le modèle économique comparatif entre l'hébergement historique et la cible cloud.

Chaque agent dispose d'une fiche de poste précise, d'un périmètre d'action borné et d'un mandat clair.

---

## Slide 5 : L'Ingénierie Sous le Capot (Minute 08:30 - 11:30)

En tant qu'architectes, la façon dont un outil est construit nous importe autant que ses promesses. Ce système a été développé selon nos standards les plus stricts de Software Craftsmanship.

Trois choix techniques fondamentaux méritent d'être soulignés :

Premièrement, une architecture hexagonale pure. Le cœur métier de l'orchestration est totalement isolé des bibliothèques d'agents ou des fournisseurs de modèles.

Deuxièmement, une mémoire doctrinale locale. Grâce à une base vectorielle ChromaDB embarquée en local, nous injectons directement nos référentiels internes de sécurité, nos patrons cloud et nos règles de clean code. Les agents ne parlent pas dans le vide, ils s'appuient sur notre doctrine réelle.

Troisièmement, des adaptateurs déterministes à zéro token. Pour tout ce qui touche à la production de fichiers, nous n'utilisons aucun modèle probabiliste. Nos générateurs de schémas fabriquent nativement le XML compressé pour Draw.io, le PlantUML et le Mermaid. Notre exportateur Jira produit un fichier CSV délimité par des points-virgules pour s'ouvrir sans le moindre défaut dans les versions françaises d'Excel.

Enfin, nous avons intégré un sas de sécurité humain obligatoire : l'outil GitPublisher effectue un scan anti-fuite de secrets et demande systématiquement une validation formelle avant d'enregistrer quoi que ce soit dans Git.

Pour couronner le tout, quarante-huit tests d'architecture automatisés s'exécutent en moins de deux secondes pour vérifier qu'aucune dérive de conception n'apparaît dans le code de la plateforme.

---

## Slide 6 : Le Workflow Opérationnel (Minute 10:30 - 12:00)

Regardons comment s'enchaîne le travail au sein de la brigade, de la prise en compte du besoin jusqu'à la publication formelle.

Le pipeline suit cinq étapes rigoureuses :
- Première étape : l'architecte injecte le cadrage initial dans un simple fichier Markdown avec ses contraintes de volumétrie, de RPO/RTO et de sécurité. La doctrine d'entreprise est automatiquement injectée depuis notre base vectorielle locale ChromaDB.
- Deuxième étape : le Solution Architect propose une première cible macro (services, bus de données, base de données).
- Troisième étape : c'est le clou du système, le choc contradictoire. Le Challenger / Red Team attaque sans complaisance pour traquer la sur-ingénierie et les SPOF, tandis que le CISO impose les contraintes de chiffrement CMK et de zonage C2.
- Quatrième étape : le Crafter décline la cible en architecture hexagonale et le profil SAFe découpe le backlog en User Stories techniques avec leur Definition of Done.
- Cinquième étape : nos adaptateurs purs à zéro token produisent les schémas et le fichier Jira, et l'outil GitPublisher attend notre validation humaine explicite avant tout enregistrement.

---

## Slide 7 : Les Études Concrètes Menées sur le Terrain (Minute 12:00 - 14:00)

Cette brigade n'est pas un concept théorique de laboratoire. Nous l'avons directement éprouvée sur nos problématiques d'architecture et de production les plus exigeantes.

Voici quatre cas d'usage emblématiques où elle a fait ses preuves :

Premièrement, sur la modernisation et la migration décisionnelle Cloud NovaAnalytics. C'est le cas complet qui a généré notre pack de dix livrables. Le Challenger y a refusé un cluster Kafka surdimensionné au profit d'un pipeline serverless, permettant de démontrer une réduction de coût de trente-trois pour cent et de produire douze User Stories prêtes pour Jira.

Deuxièmement, sur Félix et les flux GESMA sur le port 9096. Sur un périmètre qui traite quatre-vingts mille factures chaque nuit, la brigade a permis de cartographier avec précision les échanges asynchrones entre PERF et RISPI/INT, d'analyser le comportement des flux et de verrouiller l'isolation réseau sans perturber le train SAFe.

Troisièmement, sur l'étude de migration de PostgreSQL vers DBaaS. La problématique n'était pas un simple sujet technique, mais une lourde charge opérationnelle liée à la maintenance manuelle de machines virtuelles via Ansible. La brigade a instruit l'opportunité DBaaS managée pour les deux cas d'usage clés : GOC pour l'audit des messages asynchrones Kafka et JMS, et Wispr pour le référentiel de configuration applicative.

Quatrièmement, sur Far&Co et l'ESIP. La brigade a instruit les ouvertures de flux pour les serveurs batchs ODI, en générant immédiatement les schémas d'architecture et le dossier de sécurité DCA.

Dans chacun de ces cas, la brigade a apporté un gain de temps massif et une traçabilité d'arbitrage irréprochable.

---

## Slide 8 : Transition vers la Démo Vidéo (Minute 14:00 - 15:00)

Rien ne remplace la démonstration concrète. 

Pour vous faire gagner du temps et vous épargner les temps de latence réseau ou de calcul d'API, j'ai enregistré une séquence vidéo de huit minutes.

Nous allons voir la brigade à l'œuvre en direct : observez bien la phase où le Challenger critique la proposition du Solution Architect, l'ouverture des schémas sous Draw.io et la restitution du fichier Jira sous Excel.

C'est parti pour la vidéo.
