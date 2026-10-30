# MeshMap FR

Carte communautaire des réseaux mesh, associatifs et alternatifs en France.

**Objectif :** rendre visibles les initiatives légales qui réduisent le coût d'accès à Internet et la dépendance aux gros FAI.

![Aperçu de la carte](docs/screenshot.png)

## Pourquoi ce projet

- Le prix et la couverture Internet restent très inégaux en France.
- Beaucoup de réseaux communautaires existent mais sont invisibles.
- Partager une connexion entre voisins est **légal** ; revendre à grande échelle sans statut d'opérateur ne l'est pas.
- Ce projet est **informatif** et ne remplace pas un conseil juridique.

## Fonctionnalités

- Carte interactive (Leaflet + OpenStreetMap)
- Ajout de réseau via un formulaire avec sélection sur la carte
- API REST : `GET /api/networks`, `POST /api/networks`
- Base SQLite locale, aucune dépendance à un service tiers
- Interface en français, code et commentaires en anglais

## Stack

- Python 3.10+ / Flask 3
- SQLite
- Leaflet 1.9 (CDN)
- Aucune clé API requise

## Installation locale

```powershell
git clone https://github.com/<ton-pseudo>/meshmap-fr.git
cd meshmap-fr
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py


Puis ouvrir http://127.0.0.1:5000

Sur Linux/macOS :
git clone https://github.com/<ton-pseudo>/meshmap-fr.git
cd meshmap-fr
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
