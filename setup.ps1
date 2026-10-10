<#
.SYNOPSIS
Script d'installation automatisée pour Multi-Agent Architecture Platform (AAP) sous Windows PowerShell.

.DESCRIPTION
Ce script vérifie la présence de Python, crée l'environnement virtuel (.venv),
installe les dépendances requises et prépare le fichier de configuration .env.
#>

$ErrorActionPreference = "Stop"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Initialisation de Multi-Agent Architecture Platform    " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan

# 1. Vérification de Python
Write-Host "`n[1/5] Vérification de l'installation de Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python détecté : $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Erreur : Python n'est pas détecté dans votre PATH." -ForegroundColor Red
    Write-Host "Veuillez installer Python 3.10 ou 3.11 depuis python.org." -ForegroundColor Red
    exit 1
}

# 2. Création de l'environnement virtuel (.venv)
Write-Host "`n[2/5] Gestion de l'environnement virtuel (.venv)..." -ForegroundColor Yellow
if (-not (Test-Path ".venv")) {
    Write-Host "Création du dossier .venv en cours..." -ForegroundColor Gray
    python -m venv .venv
    Write-Host "✓ Environnement virtuel créé avec succès." -ForegroundColor Green
} else {
    Write-Host "✓ L'environnement virtuel (.venv) existe déjà." -ForegroundColor Green
}

# 3. Activation de l'environnement virtuel
Write-Host "`n[3/5] Activation de l'environnement virtuel..." -ForegroundColor Yellow
$activateScript = ".\.venv\Scripts\Activate.ps1"

if (Test-Path $activateScript) {
    & $activateScript
    Write-Host "✓ Environnement virtuel activé." -ForegroundColor Green
} else {
    Write-Host "✗ Script d'activation introuvable dans $activateScript." -ForegroundColor Red
    exit 1
}

# 4. Installation des dépendances
Write-Host "`n[4/5] Installation des dépendances Python..." -ForegroundColor Yellow
.\.venv\Scripts\python.exe -m pip install --upgrade pip --quiet
.\.venv\Scripts\pip.exe install -r requirements.txt

Write-Host "✓ Dépendances installées avec succès." -ForegroundColor Green

# 5. Préparation du fichier .env
Write-Host "`n[5/5] Vérification de la configuration d'environnement (.env)..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    Copy-Item ".env.example" ".env"
    Write-Host "✓ Fichier .env créé à partir de .env.example." -ForegroundColor Green
    Write-Host "⚠ IMPORTANT : Ouvrez le fichier .env et renseignez votre clé GEMINI_API_KEY." -ForegroundColor Magenta
} else {
    Write-Host "✓ Le fichier .env est déjà présent." -ForegroundColor Green
}

Write-Host "`n==========================================================" -ForegroundColor Cyan
Write-Host "  Installation terminée avec succès !                    " -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "`nPour activer votre environnement manuellement :" -ForegroundColor White
Write-Host "  .\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "`nPour lancer la plateforme :" -ForegroundColor White
Write-Host '  python src\main.py --language "French" --input "Mon étude d''architecture"' -ForegroundColor Yellow
Write-Host ""
