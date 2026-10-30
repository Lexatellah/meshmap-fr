# MeshMap FR

**Live demo: https://meshmap-fr.onrender.com**

Carte communautaire des rÃ©seaux mesh, associatifs et alternatifs en France.

**Objectif :** rendre visibles les initiatives lÃ©gales qui rÃ©duisent le coÃ»t d'accÃ¨s Ã  Internet et la dÃ©pendance aux gros FAI.

![AperÃ§u de la carte](docs/screenshot.png)

## Pourquoi ce projet

- Le prix et la couverture Internet restent trÃ¨s inÃ©gaux en France.
- Beaucoup de rÃ©seaux communautaires existent mais sont invisibles.
- Partager une connexion entre voisins est **lÃ©gal** ; revendre Ã  grande Ã©chelle sans statut d'opÃ©rateur ne l'est pas.
- Ce projet est **informatif** et ne remplace pas un conseil juridique.

## FonctionnalitÃ©s

- Carte interactive (Leaflet + OpenStreetMap)
- Ajout de rÃ©seau via un formulaire avec sÃ©lection sur la carte
- API REST : `GET /api/networks`, `POST /api/networks`
- Base SQLite locale, aucune dÃ©pendance Ã  un service tiers
- Interface en franÃ§ais, code et commentaires en anglais

## Stack

- Python 3.10+ / Flask 3
- SQLite
- Leaflet 1.9 (CDN)
- Aucune clÃ© API requise

## Installation locale

```powershell
git clone https://github.com/Lexatellah/meshmap-fr.git
cd meshmap-fr
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py


Puis ouvrir http://127.0.0.1:5000

Sur Linux/macOS :
git clone https://github.com/Lexatellah/meshmap-fr.git
cd meshmap-fr
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py


