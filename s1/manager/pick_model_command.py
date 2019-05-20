from manager import Manager
from manager import Model

import sys

class PickModelCommand:

  def __init__(self, manager: Manager):
    self.manager = manager
  
  def run(self) -> Model:
    models_count = len(self.manager.models)
    if models_count == 0:
      print("You have no models.")
      return None
    
    for index, model in enumerate(self.manager.models):
      print(f"{index}. {model}")
    print("Enter position of the model:")
    position = int(sys.stdin.readline().lstrip().rstrip())

    if not position in (0, models_count):
      print(f"There is no model at {position}")
      return None
    return self.manager.models[position]