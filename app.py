#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask_restful import Api
from calico_agent.resources.node import Node

app = Flask(__name__)
api = Api(app)

api.add_resource(Node, '/node')


if __name__ == '__main__':
    app.run(debug=True)
