from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.repository import repository


@pytest.fixture
def client() -> Iterator[TestClient]:
    """Client HTTP sur un dépôt vide. Chaque test repart de zéro."""
    repository.clear()
    with TestClient(app) as c:
        yield c
    repository.clear()


@pytest.fixture
def make_task(client: TestClient):
    """Fabrique : make_task("titre") crée une tâche via l'API et renvoie le JSON."""

    def _make(title: str = "Écrire les tests", assignee: str | None = None) -> dict:
        response = client.post("/tasks", json={"title": title, "assignee": assignee})
        assert response.status_code == 201
        return response.json()

    return _make
