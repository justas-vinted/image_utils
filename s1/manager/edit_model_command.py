from manager import Manager
from manager import Model
from pick_model_command import PickModelCommand
from add_model_command import UpdateModelCommand
import sys

class EditModelCommand:

  def __init__(self, manager: Manager):
    self.manager = manager
  
  def run(self):
    selectedModel = PickModelCommand(self.manager).run()
    if selectedModel:
      UpdateModelCommand(selectedModel).run()