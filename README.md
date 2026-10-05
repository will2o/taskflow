# TaskFlow — projet fil rouge

API de gestion de tâches d'équipe (FastAPI + pytest). Ce dépôt sert de terrain de jeu pendant les deux jours de formation Claude Code : chaque module le fait évoluer.

| Module | Ce que vous ferez sur ce dépôt |
|---|---|
| 1 | Lancer Claude Code dessus, écrire son `CLAUDE.md` |
| 2 | Ajouter des endpoints par prompts, refactorer `scripts/legacy/report.py`, générer des tests |
| 3 | Créer une skill qui applique les conventions du projet |
| 4 | Hooks de formatage et de sécurité, pull request automatisée |
| 5 | Brancher PostgreSQL via MCP, packager la config en plugin |
| 6 | Subagents de test et de revue, guidelines de sécurité |

## Installation

Python 3.10 ou plus récent.

```bash
python -m venv .venv
# macOS / Linux / WSL
source .venv/bin/activate
# Windows PowerShell
.venv\Scripts\Activate.ps1

pip install -e ".[dev]"
```

## Commandes

```bash
pytest                      # tests (doivent être verts avant tout commit)
ruff check . && ruff format .   # lint + formatage
uvicorn app.main:app --reload   # serveur sur http://localhost:8000 (doc : /docs)
```

## Structure

```
app/
  main.py          # application FastAPI + handler d'erreurs global
  errors.py        # ApiError, NotFoundError, ConflictError
  schemas.py       # modèles Pydantic (TaskCreate, TaskUpdate, TaskOut, TaskStatus)
  repository.py    # stockage en mémoire
  routers/tasks.py # endpoints /tasks
tests/
  conftest.py      # fixtures : client, make_task
  test_tasks.py
docs/api.md        # référence des endpoints, à tenir à jour
scripts/legacy/    # code historique, ne pas toucher avant le Module 2
```

Il n'y a volontairement **pas** de `CLAUDE.md` : c'est l'objet du TP 1.2.
