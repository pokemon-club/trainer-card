from falcon import HTTPUnauthorized
from jwt import decode
from os import environ


def authorize_as(header, needs_to_be):
  levels = ['player', 'developer']
  try:
    jwt_auth = header.split(' ')
    if jwt_auth[0] != 'Bearer':
      raise HTTPUnauthorized('unautharized', 'unautharized')
    data = decode(jwt_auth[1], environ['JWT_KEY'], algorithm='HS256')
    user_is = levels.index(data['level'])
    must_be = levels.index(needs_to_be)
    return user_is >= must_be

  except:
    raise HTTPUnauthorized('unautharized', 'unautharized')