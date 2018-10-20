from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import logging
import warnings
import csv 
import pandas as pd
import unicodedata

from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core import utils
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.events import SlotSet
from rasa_core.featurizers import (
    MaxHistoryTrackerFeaturizer,
    BinarySingleStateFeaturizer)
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_nlu.model import Metadata, Interpreter

logger = logging.getLogger(__name__)


class RestaurantAPI(object):
    def search(self, info):
        return "papi's pizza place"


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("looking for restaurants")
        restaurant_api = RestaurantAPI()
        restaurants = restaurant_api.search(tracker.get_slot("cuisine"))
        return [SlotSet("matches", restaurants)]

class ActionCheckRestaurants(Action):
    def name(self):
        return 'action_check_restaurants'

    def run(self, dispatcher, tracker, domain):
	dispatcher.utter_message("here's what I found:")
	cuisine1 = tracker.get_slot("cuisine")
	food = tracker.get_slot("food")
	location = tracker.get_slot("location")
	print(type(cuisine1))
	dispatcher.utter_message("here's what I found:")
	#unicodedata.normalize('NFKD', cuisine1).encode('ascii','ignore')
	cuisine1.encode('ascii','ignore')
	
	print(type(cuisine1))
	df = pd.read_csv("yelp_business.csv")
	#result = df.loc[(df['categories'].str.contains(cuisine1, case = False).head(n=1))]
	dispatcher.utter_message("here's what I found:")
	return []


def train_dialogue(domain_file="restaurant_domain.yml",
                   model_path="models/dialogue",
                   training_data_file="data/babi_stories.md"):
    agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy()])

    #training_data = agent.load_data(training_data_file)
    agent.train(
            training_data_file,
            epochs=400,
            batch_size=100,
            validation_split=0.2
    )

    agent.persist(model_path)
    return agent

def train_nlu():
    from rasa_nlu.training_data import load_data
    from rasa_nlu import config
    from rasa_nlu.model import Trainer

    training_data = load_data('data/franken_data.json')
    trainer = Trainer(config.load("nlu_model_config.yml"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/',
                                      fixed_model_name="current")

    return model_directory


def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/current')
	x = interpreter.parse("show me some chines restaurants")
	print(x)


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/nlu/default/current")
    agent = Agent.load("models/dialogue", interpreter=Interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent



if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")

    parser = argparse.ArgumentParser(
            description='starts the bot')

    parser.add_argument(
            'task',
            choices=["train-nlu", "train-dialogue", "run","run-nlu"],
            help="what the bot should do - e.g. run or train?")
    task = parser.parse_args().task

    # decide what to do based on first parameter of the script
    if task == "train-nlu":
        train_nlu()
    elif task == "train-dialogue":
        train_dialogue()
    elif task == "run":
        run()
    elif task == "run-nlu":
	run_nlu()
