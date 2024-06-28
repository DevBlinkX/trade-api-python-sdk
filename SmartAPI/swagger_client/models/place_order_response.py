# coding: utf-8

"""
    order-services Api Doc

    Rest APIs  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: sales@marketsimplified.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PlaceOrderResponse(object):
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
        'info_msg': 'str',
        'timestamp': 'int',
        'data': 'PlaceOrderData'
    }

    attribute_map = {
        'info_id': 'infoID',
        'info_msg': 'infoMsg',
        'timestamp': 'timestamp',
        'data': 'data'
    }

    def __init__(self, info_id=None, info_msg=None, timestamp=None, data=None):  # noqa: E501
        """PlaceOrderResponse - a model defined in Swagger"""  # noqa: E501
        self._info_id = None
        self._info_msg = None
        self._timestamp = None
        self._data = None
        self.discriminator = None
        if info_id is not None:
            self.info_id = info_id
        if info_msg is not None:
            self.info_msg = info_msg
        if timestamp is not None:
            self.timestamp = timestamp
        if data is not None:
            self.data = data

    @property
    def info_id(self):
        """Gets the info_id of this PlaceOrderResponse.  # noqa: E501


        :return: The info_id of this PlaceOrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._info_id

    @info_id.setter
    def info_id(self, info_id):
        """Sets the info_id of this PlaceOrderResponse.


        :param info_id: The info_id of this PlaceOrderResponse.  # noqa: E501
        :type: str
        """

        self._info_id = info_id

    @property
    def info_msg(self):
        """Gets the info_msg of this PlaceOrderResponse.  # noqa: E501


        :return: The info_msg of this PlaceOrderResponse.  # noqa: E501
        :rtype: str
        """
        return self._info_msg

    @info_msg.setter
    def info_msg(self, info_msg):
        """Sets the info_msg of this PlaceOrderResponse.


        :param info_msg: The info_msg of this PlaceOrderResponse.  # noqa: E501
        :type: str
        """

        self._info_msg = info_msg

    @property
    def timestamp(self):
        """Gets the timestamp of this PlaceOrderResponse.  # noqa: E501


        :return: The timestamp of this PlaceOrderResponse.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this PlaceOrderResponse.


        :param timestamp: The timestamp of this PlaceOrderResponse.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def data(self):
        """Gets the data of this PlaceOrderResponse.  # noqa: E501


        :return: The data of this PlaceOrderResponse.  # noqa: E501
        :rtype: PlaceOrderData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PlaceOrderResponse.


        :param data: The data of this PlaceOrderResponse.  # noqa: E501
        :type: PlaceOrderData
        """

        self._data = data

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
        if issubclass(PlaceOrderResponse, dict):
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
        if not isinstance(other, PlaceOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
