import boto3
import uuid
from random import choice
from string import ascii_uppercase

class Model:

  def __init__(self, name = "", version = "0"):
    self.name = name
    self.version = version
    self.identifier = ''.join(choice(ascii_uppercase) for i in range(16))

  def __repr__(self):
    return f"The model name is {self.name}. The version of model is {self.version}"

class Manager:

  def __init__(self):
    self.models = []

  def add(self, model: Model):
    self.models.append(model)

# def create_bucket_name(bucket_prefix):
#     # The generated bucket name must be between 3 and 63 chars long
#     return ''.join([bucket_prefix, str(uuid.uuid4())])

# def create_bucket(bucket_prefix, s3_connection):
#     session = boto3.session.Session()
#     current_region = session.region_name
#     bucket_name = create_bucket_name(bucket_prefix)
#     bucket_response = s3_connection.create_bucket(
#         Bucket=bucket_name,
#         CreateBucketConfiguration={
#         'LocationConstraint': current_region})
#     print(bucket_name, current_region)
#     return bucket_name, bucket_response


# s3 = boto3.resource('s3')

# # first_bucket_name, first_response = create_bucket(bucket_prefix='myapp-',  s3_connection=s3.meta.client)

# # print(first_bucket_name, first_response)

# print(s3.buckets.filter(Prefix="myapp-"))

# for bucket in s3.buckets.filter(Prefix="myapp-"):
#   for obj in bucket.objects.filter(Prefix='/photos'):
#     print('{0}:{1}'.format(bucket.name, obj.key))