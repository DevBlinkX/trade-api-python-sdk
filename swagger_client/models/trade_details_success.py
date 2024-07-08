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

class TradeDetailsSuccess(object):
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
        'infoid': 'str',
        'data': 'list[TradeDetailsData]',
        'infomsg': 'str',
        'timestamp': 'float'
    }

    attribute_map = {
        'infoid': 'infoid',
        'data': 'data',
        'infomsg': 'infomsg',
        'timestamp': 'timestamp'
    }

    def __init__(self, infoid=None, data=None, infomsg=None, timestamp=None):  # noqa: E501
        """TradeDetailsSuccess - a model defined in Swagger"""  # noqa: E501
        self._infoid = None
        self._data = None
        self._infomsg = None
        self._timestamp = None
        self.discriminator = None
        if infoid is not None:
            self.infoid = infoid
        self.data = data
        self.infomsg = infomsg
        self.timestamp = timestamp

    @property
    def infoid(self):
        """Gets the infoid of this TradeDetailsSuccess.  # noqa: E501


        :return: The infoid of this TradeDetailsSuccess.  # noqa: E501
        :rtype: str
        """
        return self._infoid

    @infoid.setter
    def infoid(self, infoid):
        """Sets the infoid of this TradeDetailsSuccess.


        :param infoid: The infoid of this TradeDetailsSuccess.  # noqa: E501
        :type: str
        """

        self._infoid = infoid

    @property
    def data(self):
        """Gets the data of this TradeDetailsSuccess.  # noqa: E501


        :return: The data of this TradeDetailsSuccess.  # noqa: E501
        :rtype: list[TradeDetailsData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TradeDetailsSuccess.


        :param data: The data of this TradeDetailsSuccess.  # noqa: E501
        :type: list[TradeDetailsData]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def infomsg(self):
        """Gets the infomsg of this TradeDetailsSuccess.  # noqa: E501


        :return: The infomsg of this TradeDetailsSuccess.  # noqa: E501
        :rtype: str
        """
        return self._infomsg

    @infomsg.setter
    def infomsg(self, infomsg):
        """Sets the infomsg of this TradeDetailsSuccess.


        :param infomsg: The infomsg of this TradeDetailsSuccess.  # noqa: E501
        :type: str
        """
        if infomsg is None:
            raise ValueError("Invalid value for `infomsg`, must not be `None`")  # noqa: E501

        self._infomsg = infomsg

    @property
    def timestamp(self):
        """Gets the timestamp of this TradeDetailsSuccess.  # noqa: E501


        :return: The timestamp of this TradeDetailsSuccess.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this TradeDetailsSuccess.


        :param timestamp: The timestamp of this TradeDetailsSuccess.  # noqa: E501
        :type: float
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

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
        if issubclass(TradeDetailsSuccess, dict):
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
        if not isinstance(other, TradeDetailsSuccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other