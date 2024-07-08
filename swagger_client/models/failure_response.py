# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FailureResponse(object):
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
        'info_id': 'str',
        'data': 'object',
        'info_msg': 'str',
        'timpstamp': 'float'
    }

    attribute_map = {
        'info_id': 'infoId',
        'data': 'data',
        'info_msg': 'infoMsg',
        'timpstamp': 'timpstamp'
    }

    def __init__(self, info_id=None, data=None, info_msg=None, timpstamp=None):  # noqa: E501
        """FailureResponse - a model defined in Swagger"""  # noqa: E501
        self._info_id = None
        self._data = None
        self._info_msg = None
        self._timpstamp = None
        self.discriminator = None
        self.info_id = info_id
        self.data = data
        self.info_msg = info_msg
        if timpstamp is not None:
            self.timpstamp = timpstamp

    @property
    def info_id(self):
        """Gets the info_id of this FailureResponse.  # noqa: E501


        :return: The info_id of this FailureResponse.  # noqa: E501
        :rtype: str
        """
        return self._info_id

    @info_id.setter
    def info_id(self, info_id):
        """Sets the info_id of this FailureResponse.


        :param info_id: The info_id of this FailureResponse.  # noqa: E501
        :type: str
        """
        if info_id is None:
            raise ValueError("Invalid value for `info_id`, must not be `None`")  # noqa: E501

        self._info_id = info_id

    @property
    def data(self):
        """Gets the data of this FailureResponse.  # noqa: E501


        :return: The data of this FailureResponse.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this FailureResponse.


        :param data: The data of this FailureResponse.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def info_msg(self):
        """Gets the info_msg of this FailureResponse.  # noqa: E501


        :return: The info_msg of this FailureResponse.  # noqa: E501
        :rtype: str
        """
        return self._info_msg

    @info_msg.setter
    def info_msg(self, info_msg):
        """Sets the info_msg of this FailureResponse.


        :param info_msg: The info_msg of this FailureResponse.  # noqa: E501
        :type: str
        """
        if info_msg is None:
            raise ValueError("Invalid value for `info_msg`, must not be `None`")  # noqa: E501

        self._info_msg = info_msg

    @property
    def timpstamp(self):
        """Gets the timpstamp of this FailureResponse.  # noqa: E501


        :return: The timpstamp of this FailureResponse.  # noqa: E501
        :rtype: float
        """
        return self._timpstamp

    @timpstamp.setter
    def timpstamp(self, timpstamp):
        """Sets the timpstamp of this FailureResponse.


        :param timpstamp: The timpstamp of this FailureResponse.  # noqa: E501
        :type: float
        """

        self._timpstamp = timpstamp

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
        if issubclass(FailureResponse, dict):
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
        if not isinstance(other, FailureResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other