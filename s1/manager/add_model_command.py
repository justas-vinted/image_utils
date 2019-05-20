from manager import Manager
from manager import Model
import sys

class AddModelCommand:

  def __init__(self, manager: Manager):
    self.manager = manager
    self.model = Model()
  
  def run(self):
    UpdateModelCommand(self.model).run()
    self.manager.add(self.model)

class UpdateModelCommand:

  def __init__(self, model: Model):
    self.model = model
  
  def run(self):
    self.setName()
    self.setVersion()

  def setName(self):
    print("Enter name of the model:")
    self.model.name = sys.stdin.readline().lstrip().rstrip()

  def setVersion(self):
    print("Enter version of the model:")
    self.model.version = sys.stdin.readline().lstrip().rstrip()
  