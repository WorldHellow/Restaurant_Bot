from rasa_core.actions import Action
from rasa_core.events import SlotSet
import csv 
import pandas as pd
print("Hello there")
class ActionCheckRestaurants(Action):
   def name(self):
      # type: () -> Text
      return "action_check_restaurants"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]

      #cuisine = tracker.get_slot('cusine')
      #food = tracker.get_slot('food')
      #location = tracker.get_slot('location')
      dispatcher.utter_message("This is a message")
      
      #df = pd.read_csv("restarunts.csv")
      #result = df.loc[(df['categories'].str.contains(cusine))]      
      #dispatcher.utter_template("there is no such restarunt")
      #dispatcher.utter_template({result})

      return []
