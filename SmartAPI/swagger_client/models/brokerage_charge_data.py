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

class BrokerageChargeData(object):
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
        'brokerage': 'BrokerageCharge'
    }

    attribute_map = {
        'brokerage': 'brokerage'
    }

    def __init__(self, brokerage=None):  # noqa: E501
        """BrokerageChargeData - a model defined in Swagger"""  # noqa: E501
        self._brokerage = None
        self.discriminator = None
        if brokerage is not None:
            self.brokerage = brokerage

    @property
    def brokerage(self):
        """Gets the brokerage of this BrokerageChargeData.  # noqa: E501


        :return: The brokerage of this BrokerageChargeData.  # noqa: E501
        :rtype: BrokerageCharge
        """
        return self._brokerage

    @brokerage.setter
    def brokerage(self, brokerage):
        """Sets the brokerage of this BrokerageChargeData.


        :param brokerage: The brokerage of this BrokerageChargeData.  # noqa: E501
        :type: BrokerageCharge
        """

        self._brokerage = brokerage

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
        if issubclass(BrokerageChargeData, dict):
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
        if not isinstance(other, BrokerageChargeData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other