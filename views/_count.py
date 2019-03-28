from flask import Blueprint, request, jsonify, Response, abort
import requests
#from models import Acts
from models import Categories,Acts
from app import db

requestCounter = [0]

_count = Blueprint('_count',__name__,url_prefix='/_count')

@_count.route('',methods=['GET','DELETE'])
def listOrReset():
	if(request.method == 'GET'):
		response = jsonify(requestCounter)
		return response
	if(request.method == 'DELETE'):
		requestCounter[0] = 0
		return Response(status=200)