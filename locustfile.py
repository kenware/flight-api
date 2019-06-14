from locust import HttpLocust, TaskSet, task
import json
from locustMock import user_data, headers, flight_data

class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.createUser()

    def createUser(self):
        self.client.post('api/v1/users/', data=json.dumps(user_data),\
            headers={'content-type': 'application/json'})

    def login(self):
        user = self.client.post('api/v1/login/', data=json.dumps(user_data),\
            headers={'content-type': 'application/json'})
        return user.json()

    @task(1)
    def getUser(self):
        user = self.login()
        self.client.get(f'api/v1/users/{user["id"]}/', headers=headers(user["token"]))

    @task(2)
    def updateUser(self):
        user = self.login()
        user_data['country'] ='Nigeria'
        self.client.put(f'api/v1/users/{user["id"]}/', data=json.dumps(user_data),\
            headers=headers(user["token"]))
    
    @task(3)
    def getAllUser(self):
        user = self.login()
        self.client.get('api/v1/users/', headers=headers(user["token"]))
    
    @task(3)
    def getFlights(self):
        user = self.login()
        self.client.get(f'api/v1/flight/', headers=headers(user["token"]))

    @task(4)
    def createFlight(self):
        user = self.login()
        flight = self.client.post('api/v1/flight/', headers=headers(user["token"]), data=flight_data)
        return flight.json(), user
      
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000