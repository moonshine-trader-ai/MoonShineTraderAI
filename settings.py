import json

class Settings:

    def __init__(self):

        with open("settings.json", "r") as file:
            self.data = json.load(file)

    def get(self, key):
        return self.data[key]