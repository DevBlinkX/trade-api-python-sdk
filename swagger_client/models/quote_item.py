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

class QuoteItem(object):
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
        'exchange_instrument_id': 'str',
        'ltp': 'float',
        'exchange': 'str'
    }

    attribute_map = {
        'exchange_instrument_id': 'exchangeInstrumentID',
        'ltp': 'ltp',
        'exchange': 'exchange'
    }

    def __init__(self, exchange_instrument_id=None, ltp=None, exchange=None):  # noqa: E501
        """QuoteItem - a model defined in Swagger"""  # noqa: E501
        self._exchange_instrument_id = None
        self._ltp = None
        self._exchange = None
        self.discriminator = None
        if exchange_instrument_id is not None:
            self.exchange_instrument_id = exchange_instrument_id
        if ltp is not None:
            self.ltp = ltp
        if exchange is not None:
            self.exchange = exchange

    @property
    def exchange_instrument_id(self):
        """Gets the exchange_instrument_id of this QuoteItem.  # noqa: E501


        :return: The exchange_instrument_id of this QuoteItem.  # noqa: E501
        :rtype: str
        """
        return self._exchange_instrument_id

    @exchange_instrument_id.setter
    def exchange_instrument_id(self, exchange_instrument_id):
        """Sets the exchange_instrument_id of this QuoteItem.


        :param exchange_instrument_id: The exchange_instrument_id of this QuoteItem.  # noqa: E501
        :type: str
        """

        self._exchange_instrument_id = exchange_instrument_id

    @property
    def ltp(self):
        """Gets the ltp of this QuoteItem.  # noqa: E501


        :return: The ltp of this QuoteItem.  # noqa: E501
        :rtype: float
        """
        return self._ltp

    @ltp.setter
    def ltp(self, ltp):
        """Sets the ltp of this QuoteItem.


        :param ltp: The ltp of this QuoteItem.  # noqa: E501
        :type: float
        """

        self._ltp = ltp

    @property
    def exchange(self):
        """Gets the exchange of this QuoteItem.  # noqa: E501


        :return: The exchange of this QuoteItem.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this QuoteItem.


        :param exchange: The exchange of this QuoteItem.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

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
        if issubclass(QuoteItem, dict):
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
        if not isinstance(other, QuoteItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other