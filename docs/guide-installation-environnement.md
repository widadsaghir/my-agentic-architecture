# Guide d'Installation et Configuration de l'Environnement

Ce guide détaille la mise en place complète de l'environnement d'exécution pour la **Multi-Agent Architecture Platform (AAP)** sur un poste de travail Windows.

---

## 1. Prérequis Système

* **Système d'exploitation :** Windows 10 / 11 avec PowerShell.
* **Python :** Version **3.10** ou **3.11** recommandée (vérifier avec `python --version`).
* **Accès API :** Une clé d'API Google Gemini valide (obtenable gratuitement sur [Google AI Studio](https://aistudio.google.com/)).
* **Outils complémentaires (pour les livrables futurs) :**
  * *Java (JDK 17+) :* Présent sur votre poste (pour la compilation PlantUML).
  * *Node.js / npm :* Présent sur votre poste (pour la génération des présentations Marp/PPT).

---

## 2. Méthode 1 : Installation Automatisée (Recommandée)

Un script PowerShell automatisé est fourni à la racine du projet : `setup.ps1`.

### Étapes d'exécution :
1. Ouvrez un terminal PowerShell dans le dossier du projet :
   ```powershell
   cd "C:\Users\ws48e6bl\OneDrive - EDF\Architecure\my-agentic-architecture"
   ```
2. Lancez le script d'initialisation :
   ```powershell
   .\setup.ps1
   ```
   *(Si PowerShell bloque l'exécution des scripts non signés, débloquez temporairement la session avec : `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`).*

3. Le script effectue automatiquement :
   * La vérification de Python.
   * La création du dossier d'environnement virtuel `.venv`.
   * L'activation du `.venv`.
   * La mise à jour de `pip` et l'installation de `requirements.txt`.
   * La création du fichier `.env` depuis le modèle `.env.example`.

4. Éditez ensuite le fichier `.env` pour renseigner votre clé :
   ```ini
   GEMINI_API_KEY=AIzaSy...votre_cle_ici
   ```

---

## 3. Méthode 2 : Installation Manuelle (Pas à pas)

Si vous préférez exécuter chaque commande manuellement ou diagnostiquer un blocage :

### Étape 1 : Créer l'environnement virtuel isolé
```powershell
cd "C:\Users\ws48e6bl\OneDrive - EDF\Architecure\my-agentic-architecture"
python -m venv .venv
```

### Étape 2 : Activer l'environnement virtuel
```powershell
.\.venv\Scripts\Activate.ps1
```
*(Vous devez voir `(.venv)` s'afficher au début de votre invite de commande).*

### Étape 3 : Installer les dépendances
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Étape 4 : Configurer le fichier de variables d'environnement
Copiez le modèle et renseignez votre clé :
```powershell
Copy-Item .env.example .env
notepad .env
```

---

## 4. Prise en compte du Proxy d'Entreprise (Si applicable)

Si vous installez les paquets derrière un proxy d'entreprise restreint, ajoutez temporairement vos variables de proxy avant de lancer `pip` :

```powershell
$env:HTTP_PROXY="http://votre-proxy:port"
$env:HTTPS_PROXY="http://votre-proxy:port"
pip install -r requirements.txt
```

Dans le fichier `.env`, vous pouvez également décommenter les lignes `HTTP_PROXY` et `HTTPS_PROXY` pour que les requêtes des agents vers l'API Gemini transitent par ce même proxy.

---

## 5. Test de Validation (Smoke Test)

Une fois l'installation terminée et la clé configurée dans `.env`, testez la plateforme avec une consigne simple :

```powershell
.\.venv\Scripts\Activate.ps1
python src\main.py --language "French" --input "Cadrage initial de migration Cloud"
```

---

## 6. Dépannage Courant (Troubleshooting)

| Problème rencontré | Cause probable | Solution |
| :--- | :--- | :--- |
| **`Activate.ps1 cannot be loaded because running scripts is disabled`** | Restriction PowerShell Windows par défaut. | Exécutez : `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, puis relancez `.\.venv\Scripts\Activate.ps1`. |
| **`No module named 'crewai'` lors du lancement** | Le script s'exécute sur le Python global au lieu du `.venv`. | Assurez-vous d'avoir activé `.venv` ou lancez directement : `.\.venv\Scripts\python.exe src\main.py ...`. |
| **`AuthenticationError: OpenAI API key not found`** | L'agent CrewAI n'a pas reçu l'objet LLM Gemini explicitement. | Sera résolu lors du déploiement de la Brique 1 dans le code source. |
