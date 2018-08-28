# -*- coding: utf-8 -*-
"""OpenAPI core operations models module"""
from openapi_core.schema.responses.exceptions import InvalidResponse


class Operation(object):
    """Represents an OpenAPI Operation."""

    def __init__(
            self, http_method, path_name, responses, parameters,
            request_body=None, deprecated=False, operation_id=None, security=None):
        self.http_method = http_method
        self.path_name = path_name
        self.responses = dict(responses)
        self.parameters = dict(parameters)
        self.request_body = request_body
        self.deprecated = deprecated
        self.operation_id = operation_id
        self.security = security

    def __getitem__(self, name):
        return self.parameters[name]

    def get_response(self, http_status='default'):
        # @todo: move to Responses object
        try:
            return self.responses[http_status]
        except KeyError:
            # try range
            http_status_range = '{0}XX'.format(http_status[0])
            if http_status_range in self.responses:
                return self.responses[http_status_range]

            if 'default' not in self.responses:
                raise InvalidResponse(
                    "Unknown response http status {0}".format(http_status))

            return self.responses['default']
