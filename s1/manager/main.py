from manager import Manager
from manager import Model
from list_models_command import ListModelsCommand
from add_model_command import AddModelCommand
from edit_model_command import EditModelCommand
from remove_model_command import RemoveModelCommand
from upload_model_command import UploadModelCommand
import sys

manager = Manager()

manager.add(Model(name = "my model", version = "0.1"))

print(manager.models)

def run():
  manager = Manager()

  manager.models.append(Model("ModelA", "1.4"))
  manager.models.append(Model("ModelB", "1.0"))

  while True:
    print("Please enter command (list, add, edit, remove, upload):")
    command = sys.stdin.readline().strip().lower()
    if not command:
      break
    elif command == "list": 
      ListModelsCommand(manager).run()
    elif command == "add": 
      AddModelCommand(manager).run()
    elif command == "edit":
      EditModelCommand(manager).run()
    elif command == "remove":
      RemoveModelCommand(manager).run()
    elif command == "upload":
      UploadModelCommand(manager).run()
      
run()