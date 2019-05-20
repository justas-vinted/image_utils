from manager import Manager
from manager import Model
from pick_model_command import PickModelCommand

import sys

class RemoveModelCommand:

  def __init__(self, manager: Manager):
    self.manager = manager
  
  def run(self):
    selectedModel = PickModelCommand(self.manager).run()
    if selectedModel:
      self.manager.models.remove(selectedModel)

    