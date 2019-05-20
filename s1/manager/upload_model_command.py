from manager import Manager
from manager import Model
from pick_model_command import PickModelCommand

import sys
import boto3

class UploadModelCommand:

  def __init__(self, manager: Manager):
    self.manager = manager
    self.s3 = boto3.resource('s3')
  
  def run(self):
    selectedModel = PickModelCommand(self.manager).run()
    if not selectedModel:
      return
    print(self.__create_bucket(selectedModel))

  def __create_bucket(self, model: Model):
    session = boto3.session.Session()
    current_region = session.region_name
    return self.s3.meta.client.create_bucket(
      Bucket=model.identifier, 
      CreateBucketConfiguration={'LocationConstraint': current_region}
    )