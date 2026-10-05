def test_create_task_returns_201_and_todo_status(client):
    response = client.post("/tasks", json={"title": "Préparer la démo"})

    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1
    assert body["status"] == "todo"
    assert body["assignee"] is None


def test_create_task_rejects_empty_title(client):
    response = client.post("/tasks", json={"title": ""})

    assert response.status_code == 422


def test_list_tasks_filters_by_status(client, make_task):
    make_task("A")
    done = make_task("B")
    client.patch(f"/tasks/{done['id']}", json={"status": "done"})

    response = client.get("/tasks", params={"status": "done"})

    assert response.status_code == 200
    assert [t["title"] for t in response.json()] == ["B"]


def test_get_unknown_task_uses_project_error_format(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {
        "error": {"code": "not_found", "message": "Tâche 999 introuvable"},
    }


def test_update_task_changes_only_given_fields(client, make_task):
    task = make_task("Relire", assignee="Nadia")

    response = client.patch(f"/tasks/{task['id']}", json={"status": "in_progress"})

    assert response.status_code == 200
    assert response.json()["status"] == "in_progress"
    assert response.json()["assignee"] == "Nadia"
