from flask import Flask,request
import requests

import crud

REST = Flask(__name__)




@REST.route('/',methods=['POST','GET','PUT','DELETE'])
def entry():
    req = {}
    if request.method == 'POST':
        req = request.json
        crud.create(req["message"])
        return req
    if request.method == 'GET':
        req = request.json
        retrive = crud.retrive(req["message"])
        return retrive
    if request.method == 'PUT':
        req = request.json
        update = crud.update(req["_id"],req["message"])
        return update
    if request.method == 'DELETE':
        req = request.json
        crud.delete(req["message"])
        return req
    return req



if __name__ == '__main__':
  REST.run()