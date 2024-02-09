from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("https://www.google.com")
        self.client.get("https://www.google.com")