# TaskFlow — référence API

Toute évolution de l'API doit être reportée ici (règle du projet).

## Format des erreurs

Toutes les erreurs métier renvoient :

```json
{ "error": { "code": "not_found", "message": "Tâche 42 introuvable" } }
```

Les erreurs de validation (422) gardent le format FastAPI par défaut.

## Endpoints

| Méthode | Route | Description | Codes |
|---|---|---|---|
| GET | `/tasks` | Liste les tâches, filtre optionnel `?status=todo\|in_progress\|done` | 200 |
| POST | `/tasks` | Crée une tâche (`title` obligatoire, `assignee` optionnel) | 201, 422 |
| GET | `/tasks/{id}` | Détail d'une tâche | 200, 404 |
| PATCH | `/tasks/{id}` | Modifie `title`, `assignee` et/ou `status` | 200, 404, 422 |
