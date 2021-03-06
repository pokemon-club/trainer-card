from bson.objectid import ObjectId
from util.insert import insert_object


class ClientError:
  def __init__(self, database):
    self.collection = database['client_error']
    self.create_keys = ['user_id', 'app', 'message', 'browser', 'line']
    self.update_keys = ['issue', 'resolved']

  def all(self):
    return self.collection.find()

  def find(self, error_id):
    if(isinstance(error_id, str)):
      error_id = ObjectId(error_id)
    return self.collection.find_one({'_id': error_id})

  def create(self, content):
    insert = insert_object(self.create_keys, content, True)
    created = self.collection.insert_one(insert)
    return created

  def update(self, content, error_id):
    keys = list(set(self.create_keys) | set(self.update_keys))
    insert = insert_object(keys, content)
    resource = self.collection.update_one({'_id': ObjectId(error_id)},
                                          {'$set': insert})
    return resource
