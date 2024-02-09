from lib.manager import*

def test_adding_a_friend():
    manager = ManageBirthdays()
    manager.add_friend("Phil", "1976-5-15")
    assert manager.friends["Phil"] == ("1976-5-15")

def test_updating_birthday():
    manager = ManageBirthdays()
    manager.add_friend("Phil", "1976-5-15")
    manager.update_record("Phil", "1996-5-15")
    assert manager.friends["Phil"] == ("1996-5-15")    

def test_updating_name():
    manager = ManageBirthdays()
    manager.add_friend("Phil", "1976-5-15")
    manager.update_name("Phil", "Nadia")
    assert manager.friends["Nadia"] == ("1976-5-15")  

def test_remind_birthdays_coming_soon():  
    manager = ManageBirthdays()
    manager.add_friend("Phil", "1976-5-15")        
    manager.add_friend("Nadia", "1986-2-15")
    manager.add_friend("James", "1996-3-11")
    # upcoming_dates = remind_birthday(days=14)
    # assert len(upcoming_dates) == 1
    # assert "Nadia" in upcoming_dates
    actual = manager.remind_birthday()
    expected = ["Nadia"]
    assert actual == expected

def test_return_the_age_of_friends_whose_birthday_is_coming_soon():
    manager = ManageBirthdays()
    manager.add_friend("Phil", "1976-5-15")        
    manager.add_friend("Nadia", "1986-2-15")
    manager.add_friend("James", "1996-3-11")    
    manager.add_friend("John", "1988-2-20")
    friends_list = manager.remind_birthday()
    upcoming_ages = manager.calculate_age(friends_list)
    assert upcoming_ages == {'John': 36, 'Nadia': 38}
    
def test_mark_a_birthday_card_as_done():
    manager = ManageBirthdays()
    manager.add_friend("Phil", "1976-5-15")        
    manager.add_friend("Nadia", "1986-2-15")
    manager.add_friend("James", "1996-3-11") 
    manager.birthday_card_done("Nadia")
    assert manager.mark_card_done["Nadia"] == ('done', {'expiration_time': datetime.date(2025, 2, 6)})