# Agent LangGraph - Projet boutique

Prototype Python autour des règles d'une boutique : indexation d'un PDF avec
Google Gemini Embeddings et ChromaDB, ainsi que des outils SQLite.

## Prérequis

- Python 3.12 ou plus récent
- [uv](https://docs.astral.sh/uv/)
- Une clé API Google AI Studio pour créer les embeddings

## Installation

```powershell
uv sync
```

Créez un fichier `.env` à la racine du projet et ajoutez-y votre clé :

```dotenv
GOOGLE_API_KEY=votre_cle_api
```

Le fichier `.env` et les données locales de ChromaDB ne sont pas suivis par Git.
Le document `politique_boutique.pdf` doit être présent à la racine.

## Indexation du document

```powershell
uv run indexer.py
```

L'index est créé dans `chroma_db/`. Le script utilise par défaut le modèle
`gemini-embedding-001`; les variables `FICHIER_PDF`, `EMBEDDINGS`, `CHROMA_DIR`
et `COLLECTION` permettent de modifier ces valeurs.

Le module `outils_base.py` contient la base SQLite de démonstration et ses
outils. Le point d'entrée de paquet `projet-boutique` est encore un exemple
minimal.