# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import os
import subprocess
from typing import Any, Text, Dict, List
import requests
import re
import datetime
from rasa_sdk.events import ReminderScheduled
from rasa_sdk.events import ReminderCancelled
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

channel = "D010ZGDGNBU"
API_ENDPOINT = "https://slack.com/api/chat.postMessage"
count = 0
class aggregate(Action):

    def name(self) -> Text:
        return "action_Aggregate1"

    async def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        model = tracker.get_slot("mongo_type"):quit
        time = tracker.get_slot("mongo_time")
        print(model)
        print(time)
       """  if schema != None:
            schema = schema.lower()
        if schema == "cr":
            result = subprocess.run(['qliksense','config','view'] , stdout=subprocess.PIPE)
            message = result.stdout.decode("unicode_escape")
            dispatcher.utter_message(message)
            return [SlotSet("cluster_element", None)]   
        elif schema == "crd":
            result = subprocess.run(['qliksense','operator','crd'] , stdout=subprocess.PIPE)
            message = result.stdout.decode("unicode_escape")
            dispatcher.utter_message(message)
            return [SlotSet("cluster_element", None)]
        elif schema=="all":
            result = subprocess.run(['qliksense','config','list-contexts'] , stdout=subprocess.PIPE)
            message = result.stdout.decode("unicode_escape")
        else:
            message = "Sorry I could not understand what you mean"
            dispatcher.utter_message(message)
            return [SlotSet("cluster_element", None)]
        
       

        result = decode(message)
        print(result)

        text = """[
                    {{
                        "type": "section",
                        "text": {{
                            "type": "mrkdwn",
                            "text": "```{}```"
                        }}
                    }}
                ]
            """.format(result)
        print(type(message))
        # data to be sent to api 
        data = {
                "token": API_KEY,
                "channel": channel,
                "text": "Error",
                "blocks": text
               } 
  
        # sending post request and saving response as response object 
        r = requests.post(url = API_ENDPOINT, data = data)
        
        # extracting response text  
        pastebin_url = r.text 
        print("The pastebin URL is:%s"%pastebin_url)  

        return [SlotSet("cluster_element", None)] """

        return [SlotSet("cluster_element", None)]


class ActionCheckRestaurants(Action):
   def name(self) -> Text:
      return "action_Aggregate"

   def run(self,
           dispatcher: CollectingDispatcher,
           tracker: Tracker,
           domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

      

      return []