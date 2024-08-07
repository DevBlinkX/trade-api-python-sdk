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


class ExitOrderRequest(object):
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
        'symbol': 'str',
        'exc': 'str',
        'prd_type': 'str',
        'bo_ord_status': 'str',
        'ord_id': 'str',
        'par_ord_id': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'exc': 'exc',
        'prd_type': 'prdType',
        'bo_ord_status': 'boOrdStatus',
        'ord_id': 'ordId',
        'par_ord_id': 'parOrdId'
    }

    def __init__(self, symbol=None, exc=None, prd_type=None, bo_ord_status=None, ord_id=None,
                 par_ord_id=None):  # noqa: E501
        """ExitOrderRequest - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._exc = None
        self._prd_type = None
        self._bo_ord_status = None
        self._ord_id = None
        self._par_ord_id = None
        self.discriminator = None
        self.symbol = symbol
        self.exc = exc
        self.prd_type = prd_type
        self.bo_ord_status = bo_ord_status
        self.ord_id = ord_id
        self.par_ord_id = par_ord_id

    @property
    def symbol(self):
        """Gets the symbol of this ExitOrderRequest.  # noqa: E501


        :return: The symbol of this ExitOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this ExitOrderRequest.


        :param symbol: The symbol of this ExitOrderRequest.  # noqa: E501
        :type: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def exc(self):
        """Gets the exc of this ExitOrderRequest.  # noqa: E501


        :return: The exc of this ExitOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._exc

    @exc.setter
    def exc(self, exc):
        """Sets the exc of this ExitOrderRequest.


        :param exc: The exc of this ExitOrderRequest.  # noqa: E501
        :type: str
        """
        if exc is None:
            raise ValueError("Invalid value for `exc`, must not be `None`")  # noqa: E501
        allowed_values = ["NSE", "BSE", "NFO", "BFO", "CDS", "BCD", "MCXSX", "MCX", "NCO", "BCO", "ICEX"]  # noqa: E501
        if exc not in allowed_values:
            raise ValueError(
                "Invalid value for `exc` ({0}), must be one of {1}"  # noqa: E501
                .format(exc, allowed_values)
            )

        self._exc = exc

    @property
    def prd_type(self):
        """Gets the prd_type of this ExitOrderRequest.  # noqa: E501


        :return: The prd_type of this ExitOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._prd_type

    @prd_type.setter
    def prd_type(self, prd_type):
        """Sets the prd_type of this ExitOrderRequest.


        :param prd_type: The prd_type of this ExitOrderRequest.  # noqa: E501
        :type: str
        """
        if prd_type is None:
            raise ValueError("Invalid value for `prd_type`, must not be `None`")  # noqa: E501
        allowed_values = ["CASH", "MTF", "INTRADAY", "MARGIN", "SHORTSELL", "COVER_ORDER", "BRACKET_ORDER", "NRML",
                          "TNC", "DELIVERY", "NONE"]  # noqa: E501
        if prd_type not in allowed_values:
            raise ValueError(
                "Invalid value for `prd_type` ({0}), must be one of {1}"  # noqa: E501
                .format(prd_type, allowed_values)
            )

        self._prd_type = prd_type

    @property
    def bo_ord_status(self):
        """Gets the bo_ord_status of this ExitOrderRequest.  # noqa: E501


        :return: The bo_ord_status of this ExitOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._bo_ord_status

    @bo_ord_status.setter
    def bo_ord_status(self, bo_ord_status):
        """Sets the bo_ord_status of this ExitOrderRequest.


        :param bo_ord_status: The bo_ord_status of this ExitOrderRequest.  # noqa: E501
        :type: str
        """
        if bo_ord_status is None:
            raise ValueError("Invalid value for `bo_ord_status`, must not be `None`")  # noqa: E501

        self._bo_ord_status = bo_ord_status

    @property
    def ord_id(self):
        """Gets the ord_id of this ExitOrderRequest.  # noqa: E501


        :return: The ord_id of this ExitOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._ord_id

    @ord_id.setter
    def ord_id(self, ord_id):
        """Sets the ord_id of this ExitOrderRequest.


        :param ord_id: The ord_id of this ExitOrderRequest.  # noqa: E501
        :type: str
        """
        if ord_id is None:
            raise ValueError("Invalid value for `ord_id`, must not be `None`")  # noqa: E501

        self._ord_id = ord_id

    @property
    def par_ord_id(self):
        """Gets the par_ord_id of this ExitOrderRequest.  # noqa: E501


        :return: The par_ord_id of this ExitOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._par_ord_id

    @par_ord_id.setter
    def par_ord_id(self, par_ord_id):
        """Sets the par_ord_id of this ExitOrderRequest.


        :param par_ord_id: The par_ord_id of this ExitOrderRequest.  # noqa: E501
        :type: str
        """
        if par_ord_id is None:
            raise ValueError("Invalid value for `par_ord_id`, must not be `None`")  # noqa: E501

        self._par_ord_id = par_ord_id

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
        if issubclass(ExitOrderRequest, dict):
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
        if not isinstance(other, ExitOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
