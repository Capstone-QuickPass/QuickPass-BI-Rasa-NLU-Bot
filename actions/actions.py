# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pymongo import MongoClient
import pprint
import datetime
import time
from datetime import datetime, timedelta 
import requests
import textdistance

client = MongoClient("mongodb+srv://QuickPassBoys:bigchungus123@cluster0.jsf18.mongodb.net/QuickPass?retryWrites=true&w=majority")
db = client.QuickPass

class aggregate(Action):

    def name(self) -> Text:
        return "action_Aggregate"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        model = tracker.get_slot("mongo_type")
        time1 = tracker.get_slot("mongo_time")
        print(model)
        print(time1)
        current_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        t0 = datetime.now()
        t = datetime.now() - timedelta(hours=float(time1))
        prev_time = t.strftime("%m/%d/%Y, %H:%M:%S")
        print(prev_time, t)
        
        if model == "people":
            
            people = db.people
            pprint.pprint(people.find())
            n = []
            ct = 0
            for person in people.find({"datetime": {"$gte": prev_time, "$lt": current_time}}):
                n.append(person)
                ct+=1
                dispatcher.utter_message("Individual "+str(ct)+": "+str(person['datetime']))
            pprint.pprint(len(n))
            message = str(len(n)) + " person(s) have entered the building in the last " + time1+ " hour(s)"
            dispatcher.utter_message(message)
        if model == "alerts":
            
            alerts = db.alerts
            ct = 0
            n = []
            for alert in alerts.find({"time": {"$gte": prev_time, "$lt": current_time}}):
                ct+=1
                n.append(alert)
                dispatcher.utter_message("Alert "+str(ct)+": "+" \n Time -> "+str(alert["time"])+", \n Type -> "+str(alert["type"]))
            pprint.pprint(len(n))
            message = str(len(n)) + " alert(s) have occured in the last " + time1+ " hour(s)"
            dispatcher.utter_message(message)
        
        dispatcher.utter_message()
        return [SlotSet("mongo_type", None)]

class action_Pop(Action):

    def name(self) -> Text:
        return "action_Pop"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        pop = tracker.get_slot("pop_type")
    
        print(pop)
        fac_info = requests.get('http://quickpass-backend.azurewebsites.net/facility/by/602ea8d423a00b4812b77ee6')
        fac = fac_info.json()
        isCapacitySet = fac['isCapacitySet']
        capacity = fac['capacity']
        print(capacity)
        currentCapacity = fac['currentCapacity']
        
        if pop == "max" or pop == "maximum" or textdistance.hamming(pop, "maximum")<2:
            dispatcher.utter_message("The maximum capacity set for this facility is: "+str(capacity)+" individuals")
        elif pop == "current" or pop=="currently" or textdistance.hamming(pop, "current")<2:
            dispatcher.utter_message("The current load of the facility is "+str(currentCapacity)+" individuals")
        
        dispatcher.utter_message()
        return [SlotSet("mongo_type", None)]