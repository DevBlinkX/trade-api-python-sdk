# coding: utf-8

"""
    Authentication API

    API for user authentication  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class LoginResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'str',
        'message': 'str',
        'data': 'object',
        'timestamp': 'int'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'data': 'data',
        'timestamp': 'timestamp'
    }

    def __init__(self, code=None, message=None, data=None, timestamp=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._message = None
        self._data = None
        self._timestamp = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if data is not None:
            self.data = data
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def code(self):
        """Gets the code of this InlineResponse200.  # noqa: E501


        :return: The code of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this InlineResponse200.


        :param code: The code of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this InlineResponse200.  # noqa: E501


        :return: The message of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InlineResponse200.


        :param message: The message of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def data(self):
        """Gets the data of this InlineResponse200.  # noqa: E501


        :return: The data of this InlineResponse200.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse200.


        :param data: The data of this InlineResponse200.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def timestamp(self):
        """Gets the timestamp of this InlineResponse200.  # noqa: E501


        :return: The timestamp of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this InlineResponse200.


        :param timestamp: The timestamp of this InlineResponse200.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LoginResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other