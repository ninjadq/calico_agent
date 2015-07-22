#!/usr/bin/env python
# encoding: utf-8

from flask_restful import reqparse, abort, Resource
from calico_agent.common.util import calicoctl

put_parser = reqparse.RequestParser()
put_parser.add_argument(
    'ip',
    help='ip address of this host'
)
put_parser.add_argument(
    'node-image',
    dest='node_image',
    help='specific node image'
)
put_parser.add_argument(
    'ip6',
    help='ip6 address'
)
put_parser.add_argument(
    'as',
    dest='autonomous_system',
    help='automous system number'
)


class Node(Resource):
    def put(self):
        args = put_parser.parse_args()
        ip = args.ip
        node_image = args.node_image
        ip6 = args.ip6
        autonomous_system = args.autonomous_system
        command_args = ['node']

        if ip:
            command_args.append('--ip={}'.format(ip))
        elif ip6:
            command_args.append('--ip6')
            command_args.append(ip6)
        else:
            abort(404, message="Your must specify an ip address")

        if node_image:
            command_args.append('--node-image')
            command_args.append(node_image)

        if autonomous_system:
            command_args.append('--as')
            command_args.append(autonomous_system)

        result = calicoctl(*command_args)

        return {'message': result}, 201
