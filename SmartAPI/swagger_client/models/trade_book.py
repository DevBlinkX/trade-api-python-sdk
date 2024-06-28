# coding: utf-8

"""
    portfolio-services Api Doc

    Rest APIs  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: sales@marketsimplified.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TradeBook(object):
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
        'symbol': 'SymbolDto',
        'ord_id': 'str',
        'exch_trd_id': 'str',
        'exch_ord_id': 'str',
        'prd_type': 'str',
        'ord_action': 'str',
        'ord_type': 'str',
        'traded_price': 'float',
        'trade_time': 'str',
        'traded_qty': 'int',
        'remain_qty': 'int',
        'qty': 'int',
        'ord_validity': 'str',
        'und_asset': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'ord_id': 'ordId',
        'exch_trd_id': 'exchTrdId',
        'exch_ord_id': 'exchOrdId',
        'prd_type': 'prdType',
        'ord_action': 'ordAction',
        'ord_type': 'ordType',
        'traded_price': 'tradedPrice',
        'trade_time': 'tradeTime',
        'traded_qty': 'tradedQty',
        'remain_qty': 'remainQty',
        'qty': 'qty',
        'ord_validity': 'ordValidity',
        'und_asset': 'undAsset'
    }

    def __init__(self, symbol=None, ord_id=None, exch_trd_id=None, exch_ord_id=None, prd_type=None, ord_action=None, ord_type=None, traded_price=None, trade_time=None, traded_qty=None, remain_qty=None, qty=None, ord_validity=None, und_asset=None):  # noqa: E501
        """TradeBook - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._ord_id = None
        self._exch_trd_id = None
        self._exch_ord_id = None
        self._prd_type = None
        self._ord_action = None
        self._ord_type = None
        self._traded_price = None
        self._trade_time = None
        self._traded_qty = None
        self._remain_qty = None
        self._qty = None
        self._ord_validity = None
        self._und_asset = None
        self.discriminator = None
        if symbol is not None:
            self.symbol = symbol
        if ord_id is not None:
            self.ord_id = ord_id
        if exch_trd_id is not None:
            self.exch_trd_id = exch_trd_id
        if exch_ord_id is not None:
            self.exch_ord_id = exch_ord_id
        if prd_type is not None:
            self.prd_type = prd_type
        if ord_action is not None:
            self.ord_action = ord_action
        if ord_type is not None:
            self.ord_type = ord_type
        if traded_price is not None:
            self.traded_price = traded_price
        if trade_time is not None:
            self.trade_time = trade_time
        if traded_qty is not None:
            self.traded_qty = traded_qty
        if remain_qty is not None:
            self.remain_qty = remain_qty
        if qty is not None:
            self.qty = qty
        if ord_validity is not None:
            self.ord_validity = ord_validity
        if und_asset is not None:
            self.und_asset = und_asset

    @property
    def symbol(self):
        """Gets the symbol of this TradeBook.  # noqa: E501


        :return: The symbol of this TradeBook.  # noqa: E501
        :rtype: SymbolDto
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this TradeBook.


        :param symbol: The symbol of this TradeBook.  # noqa: E501
        :type: SymbolDto
        """

        self._symbol = symbol

    @property
    def ord_id(self):
        """Gets the ord_id of this TradeBook.  # noqa: E501


        :return: The ord_id of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._ord_id

    @ord_id.setter
    def ord_id(self, ord_id):
        """Sets the ord_id of this TradeBook.


        :param ord_id: The ord_id of this TradeBook.  # noqa: E501
        :type: str
        """

        self._ord_id = ord_id

    @property
    def exch_trd_id(self):
        """Gets the exch_trd_id of this TradeBook.  # noqa: E501


        :return: The exch_trd_id of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._exch_trd_id

    @exch_trd_id.setter
    def exch_trd_id(self, exch_trd_id):
        """Sets the exch_trd_id of this TradeBook.


        :param exch_trd_id: The exch_trd_id of this TradeBook.  # noqa: E501
        :type: str
        """

        self._exch_trd_id = exch_trd_id

    @property
    def exch_ord_id(self):
        """Gets the exch_ord_id of this TradeBook.  # noqa: E501


        :return: The exch_ord_id of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._exch_ord_id

    @exch_ord_id.setter
    def exch_ord_id(self, exch_ord_id):
        """Sets the exch_ord_id of this TradeBook.


        :param exch_ord_id: The exch_ord_id of this TradeBook.  # noqa: E501
        :type: str
        """

        self._exch_ord_id = exch_ord_id

    @property
    def prd_type(self):
        """Gets the prd_type of this TradeBook.  # noqa: E501


        :return: The prd_type of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._prd_type

    @prd_type.setter
    def prd_type(self, prd_type):
        """Sets the prd_type of this TradeBook.


        :param prd_type: The prd_type of this TradeBook.  # noqa: E501
        :type: str
        """
        allowed_values = ["CASH", "MTF", "INTRADAY", "MARGIN", "SHORTSELL", "COVER_ORDER", "BRACKET_ORDER", "NRML", "TNC", "DELIVERY", "NONE"]  # noqa: E501
        if prd_type not in allowed_values:
            raise ValueError(
                "Invalid value for `prd_type` ({0}), must be one of {1}"  # noqa: E501
                .format(prd_type, allowed_values)
            )

        self._prd_type = prd_type

    @property
    def ord_action(self):
        """Gets the ord_action of this TradeBook.  # noqa: E501


        :return: The ord_action of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._ord_action

    @ord_action.setter
    def ord_action(self, ord_action):
        """Sets the ord_action of this TradeBook.


        :param ord_action: The ord_action of this TradeBook.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUY", "SELL", "SHORT", "NONE"]  # noqa: E501
        if ord_action not in allowed_values:
            raise ValueError(
                "Invalid value for `ord_action` ({0}), must be one of {1}"  # noqa: E501
                .format(ord_action, allowed_values)
            )

        self._ord_action = ord_action

    @property
    def ord_type(self):
        """Gets the ord_type of this TradeBook.  # noqa: E501


        :return: The ord_type of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._ord_type

    @ord_type.setter
    def ord_type(self, ord_type):
        """Sets the ord_type of this TradeBook.


        :param ord_type: The ord_type of this TradeBook.  # noqa: E501
        :type: str
        """
        allowed_values = ["Market", "Limit", "Stop", "Stop-loss", "SL-M", "SL", "None"]  # noqa: E501
        if ord_type not in allowed_values:
            raise ValueError(
                "Invalid value for `ord_type` ({0}), must be one of {1}"  # noqa: E501
                .format(ord_type, allowed_values)
            )

        self._ord_type = ord_type

    @property
    def traded_price(self):
        """Gets the traded_price of this TradeBook.  # noqa: E501


        :return: The traded_price of this TradeBook.  # noqa: E501
        :rtype: float
        """
        return self._traded_price

    @traded_price.setter
    def traded_price(self, traded_price):
        """Sets the traded_price of this TradeBook.


        :param traded_price: The traded_price of this TradeBook.  # noqa: E501
        :type: float
        """

        self._traded_price = traded_price

    @property
    def trade_time(self):
        """Gets the trade_time of this TradeBook.  # noqa: E501


        :return: The trade_time of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        """Sets the trade_time of this TradeBook.


        :param trade_time: The trade_time of this TradeBook.  # noqa: E501
        :type: str
        """

        self._trade_time = trade_time

    @property
    def traded_qty(self):
        """Gets the traded_qty of this TradeBook.  # noqa: E501


        :return: The traded_qty of this TradeBook.  # noqa: E501
        :rtype: int
        """
        return self._traded_qty

    @traded_qty.setter
    def traded_qty(self, traded_qty):
        """Sets the traded_qty of this TradeBook.


        :param traded_qty: The traded_qty of this TradeBook.  # noqa: E501
        :type: int
        """

        self._traded_qty = traded_qty

    @property
    def remain_qty(self):
        """Gets the remain_qty of this TradeBook.  # noqa: E501


        :return: The remain_qty of this TradeBook.  # noqa: E501
        :rtype: int
        """
        return self._remain_qty

    @remain_qty.setter
    def remain_qty(self, remain_qty):
        """Sets the remain_qty of this TradeBook.


        :param remain_qty: The remain_qty of this TradeBook.  # noqa: E501
        :type: int
        """

        self._remain_qty = remain_qty

    @property
    def qty(self):
        """Gets the qty of this TradeBook.  # noqa: E501


        :return: The qty of this TradeBook.  # noqa: E501
        :rtype: int
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """Sets the qty of this TradeBook.


        :param qty: The qty of this TradeBook.  # noqa: E501
        :type: int
        """

        self._qty = qty

    @property
    def ord_validity(self):
        """Gets the ord_validity of this TradeBook.  # noqa: E501


        :return: The ord_validity of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._ord_validity

    @ord_validity.setter
    def ord_validity(self, ord_validity):
        """Sets the ord_validity of this TradeBook.


        :param ord_validity: The ord_validity of this TradeBook.  # noqa: E501
        :type: str
        """
        allowed_values = ["DAY", "IOC", "GMT", "GTC", "AMO", "GTD", "NONE"]  # noqa: E501
        if ord_validity not in allowed_values:
            raise ValueError(
                "Invalid value for `ord_validity` ({0}), must be one of {1}"  # noqa: E501
                .format(ord_validity, allowed_values)
            )

        self._ord_validity = ord_validity

    @property
    def und_asset(self):
        """Gets the und_asset of this TradeBook.  # noqa: E501


        :return: The und_asset of this TradeBook.  # noqa: E501
        :rtype: str
        """
        return self._und_asset

    @und_asset.setter
    def und_asset(self, und_asset):
        """Sets the und_asset of this TradeBook.


        :param und_asset: The und_asset of this TradeBook.  # noqa: E501
        :type: str
        """

        self._und_asset = und_asset

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
        if issubclass(TradeBook, dict):
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
        if not isinstance(other, TradeBook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
