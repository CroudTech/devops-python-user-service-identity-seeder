import json
import urllib.request
import random
import string
import requests

class Seeder:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.seedIdentityServer()

    def seedIdentityServer(self):
        for user in self.getData():
            payload = {
                "id": "{system_id}:croudie-network:croudies:{user_id}".format(system_id=user["systemId"], user_id=user["id"]),
                "password": self.randomString() + "A1$",
                "email": user["emailAddress"],
                "userName": user["emailAddress"],
            }
            print(json.dumps(payload))
            #result = requests.delete(url=self.dest + "/" + payload["id"])
            result = requests.post(url=self.dest, json=payload)
            print(result)

    def getData(self):
        data = []
        result = json.load(urllib.request.urlopen(self.source))
        data = data + result["results"]
        while result["next"] != None:
            result = json.load(urllib.request.urlopen(result["next"]))
            data = data + result["results"]

        self.users = data
        return self.users

    def randomString(self, stringLength=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))