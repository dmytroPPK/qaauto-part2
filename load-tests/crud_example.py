from locust import HttpUser, SequentialTaskSet, constant_pacing, task
from random import randint


class TestCRUD(SequentialTaskSet):

    @task
    def create_user(self):
        user_data = {
            "name": f"name-{randint(1, 50)}",
            "job": f"job-{randint(51, 100)}"
        }
        res = self.client.post("/api/users", user_data, name="create user")
        self.user_id = res.json().get('id')

    @task
    def update_user(self):
        user_data = {
            "name": f"name-{randint(1, 50)}",
            "job": f"job-{randint(51, 100)}"
        }
        self.client.put(f"/api/users/{self.user_id}", user_data, name="update user")

    @task
    def get_users_by_page(self):

        self.client.get(f"/api/users?page=1", name="get users")

    @task
    def delete_user(self):

        self.client.delete(f"/api/users/{self.user_id}", name="delete user")


class Start(HttpUser):
    tasks = [TestCRUD]
    wait_time = constant_pacing(3)
