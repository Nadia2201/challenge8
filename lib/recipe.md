# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class ManageBirthdays():
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.friends = {}
        # Parameters:
        #  
        # Side effects:
        #   instantiate an empty dictionary
        pass # No code here yet

    def add_friend(self, friend, birthday)
        # Parameters:
        #   friend: string representing a name
        #   birthday: date in the format YYYY-MM-DD
        # Returns:
        #   
        # Side-effects
        #   add a key value pai to the friend dictionary
        pass # No code here yet

    def update_record(self, friend, new_date):
        # Parameters:
        #   friend: string representing a name
        #   new_date: date in the format YYYY-MM-DD
        # Returns:
        #   
        # Side-effects
        #   updates the birthday fro a friend already in the dictionary 
        pass # No code here yet

    def update_name(self, friend, new_name):
        # Parameters:
        #   friend: string representing a name
        #   new_name: string of the friend's new name
        #Returns:
        #   
        # Side-effects:
        #   updates the new name in the dictionary
        pass # No code here yet
``
    def remind_birthday(self):
        # Parameters:
        
        #Returns:
        #   Friends' birthdays coming soon - 14days
        # Side-effects:
        #   
        pass # No code here yet

    def calculate_age(self, friend):
        # Parameters:
        #   friends : list of friends
        #Returns:
        #   age : integer
        # Side-effects:
        #   
        pass # No code here yet 

    def mark_card_done(self, name, year):
        # Parameters:
        #   name : string
        #   year:
        #Returns:
        #   a card as done
        # Side-effects:
        #   
        pass # No code here yet      

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a friend with a birthday, we want the name and birthday added to the dictionary friend
"""
def test_adding_a_friend():
    manager = ManageBirthdays()
    manager.friends("Phil", (1976-05-15))
    assert ManageBirthdays["Phil"] == (1976-05-15)

    # friend= ManageBirthdays()
    # add_friend(("Phil", (1976-05-15)))
    # friend.friends 
"""
Given a friend with a wrong birthday date, I want to update the date
"""
def test_updating_birthday():
    manager = ManageBirthdays()
    manager.friends("Phil", (1976-05-15))
    manager.upate_record("Phil", (1996-05-15)
    assert manager.friends["Phil"] == ("1996-5-15")

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
