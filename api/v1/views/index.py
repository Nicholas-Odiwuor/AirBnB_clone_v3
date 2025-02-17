#!/usr/bin/python3
"""
Module for the Status route
"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """ Returns the status of the API """
    return jsonify({"status": "OK"})

