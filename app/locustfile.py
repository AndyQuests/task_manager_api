from locust import HttpUser, task, between

class TaskManagerUser(HttpUser):
    wait_time = between(1,2)

    @task
    def get_tasks(self):
        self.client.get("/tasks")
    
    @task
    def create_task(self):
        self.client.post("tasks", json={
            "title": "locust-test",
            "description": "cheking concurrency"
        })