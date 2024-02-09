from datetime import datetime, timedelta
import math


class ManageBirthdays:

    def __init__(self):
        self.friends = {}
        self.mark_card_done= {}

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
        remind_list = []
        for friend in self.friends:
            birthday = datetime.strptime(self.friends[friend], '%Y-%m-%d').date()
            today = datetime.now().date()
            next_birthday = datetime(today.year, birthday.month, birthday.day).date()
            days_difference = (next_birthday - today).days
            print(friend)
            print(days_difference)
            if days_difference <= days:
                remind_list.append(friend)
        print(remind_list)        
        return remind_list
# Tests
# manager = ManageBirthdays()
# manager.add_friend("Phil", "1976-5-15")        
# manager.add_friend("Nadia", "1986-2-15")
# manager.add_friend("James", "1996-3-11")
# manager.add_friend("John", "1988-2-20")
# manager.remind_birthday(days=14)

    def calculate_age(self, friend_list):
        age_dict = {}
        for friend in friend_list:
            birthday = datetime.strptime(self.friends[friend], '%Y-%m-%d').date()
            today = datetime.now().date()
            year = datetime(birthday.year, today.month, today.day).date()
            age = (today - year).days
            age_dict[friend] = math.floor(age/365)
        return age_dict   
# TO DO
    def birthday_card_done(self,friend_name):
        for friend in self.friends:
            self.mark_card_done[friend] = ""
        expiration = datetime.now().date() + timedelta(days=365)
        print(expiration)
        for friend in self.mark_card_done:
            if friend == friend_name:
                self.mark_card_done[friend] = 'done',{'expiration_time': expiration}
            
        #return self.mark_card_done[friend]

manager = ManageBirthdays()
manager.add_friend("Phil", "1976-5-15")        
manager.add_friend("Nadia", "1986-2-15")
manager.add_friend("James", "1996-3-11")
manager.add_friend("John", "1988-2-20")
manager.birthday_card_done("Nadia")