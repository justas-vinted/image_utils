from manager import Manager
from manager import Model

class ListModelsCommand:

  def __init__(self, manager: Manager):
    self.manager = manager
  
  def run(self):
    models_count = len(self.manager.models)
    if models_count == 0:
      print("You have no models.")

    for index, model in enumerate(self.manager.models):
      print(f"{index}. {model}")
