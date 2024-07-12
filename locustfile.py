from locust import HttpUser, task


class StatusUser(HttpUser):
    @task
    def get_status(self):
        self.client.get("/status")
