from models.event import *



event1 = Event("27/11/2021", "The Offspring", "30000", "Hydro", "live music event")
event2 = Event("15/02/2022", "Birthday party", "10", "Escape Room", "Harry's birthday party")
event3 = Event("30/01/2022", "Hiking Sunday", "6", "The Cobbler", "The Cobbler hike: 8am")
events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)


