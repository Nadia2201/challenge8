from datetime import datetime
from dateutil.relativedata 

class ManageBirthdays():

    def __init__(self):
        self.friends = {}

    def add_friend(self, name, birthday):
        self.friends[name] = birthday 

    def update_record(self, name, new_date):
        if name in self.friends:
            self.friends[name] = new_date 
        else:
            print("Unable to find friend")      

    def update_name(self, old_name, new_name):
        if old_name in self.friends:
            self.friends[new_name] = self.friends.pop(old_name)
        else:
            print("Unable to find friend")    

    def remind_birthday(self, days=14):
        pass    