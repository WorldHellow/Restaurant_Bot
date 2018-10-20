from __future__ import unicode_literals
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.actions import Action
from rasa_core.events import SlotSet

def train_nlu(data, config1, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(config1))
	trainer.train(training_data)
	model_directory = trainer.persist(model_dir)

def run_nlu():
	interpreter = Interpreter.load('./models/default/restaruntnlu')
	x = interpreter.parse("show me chines restaurants in the south")
	print(x)

class ActionCheckRestaurants(Action):
   def name(self):
      # type: () -> Text
      return "action_check_restaurants"

   def run(self, dispatcher, tracker, domain):

      dispatcher.utter_message("Fuck off")
      return []


def run(serve_forever=True):
    interpreter = RasaNLUInterpreter("models/default/restaruntnlu")
    agent = Agent.load("models/current/dialogue", interpreter=interpreter)

    if serve_forever:
        agent.handle_channel(ConsoleInputChannel())
    return agent


if __name__ == '__main__':
	#train_nlu('./data/data.json', 'config_spacy.yml', './models')
	#run_nlu()
        run()


 
