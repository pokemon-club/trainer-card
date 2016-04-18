from bson.json_util import dumps
from falcon import HTTP_204, HTTP_404, HTTPUnauthorized
from model import Report
from json import loads
from util.authorize import authorize_as


class Single:
  def __init__(self, database):
    self.model = Report(database)

  def on_get(self, req, resp, report_id):
    if authorize_as(req.auth, 'developer'):
      resource = self.model.find(report_id)
      if resource != None:
        resp.body = dumps(resource)
      else:
        resp.status = HTTP_404
    else:
      raise HTTPUnauhtorized('unauthorized', 'unauthorized')

  def on_put(self, req, resp, report_id):
    if authorize_as(req.auth, 'developer'):
      body = loads(req.stream.read().decode('utf-8'))
      resource = self.model.update(body, report_id)
      if resource.modified_count == 1:
        resp.status = HTTP_204
    else:
      raise HTTPUnauthorized('unauthorized', 'unauthorized')