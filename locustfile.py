from locust import HttpUser, task, between
import time

class APIUser(HttpUser):
    wait_time = between(1, 2)

    # Defining the post task using the JSON test data
    @task()
    def predict_endpoint(self):
        payload = {"type": "Local"}

        self.client.get('/', json = payload)
        print('Sucesso')
