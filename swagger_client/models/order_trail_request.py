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

class OrderTrailRequest(object):
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
        'ord_id': 'str',
        'instrument': 'str'
    }

    attribute_map = {
        'ord_id': 'ordId',
        'instrument': 'instrument'
    }

    def __init__(self, ord_id=None, instrument=None):  # noqa: E501
        """OrderTrailRequest - a model defined in Swagger"""  # noqa: E501
        self._ord_id = None
        self._instrument = None
        self.discriminator = None
        self.ord_id = ord_id
        if instrument is not None:
            self.instrument = instrument

    @property
    def ord_id(self):
        """Gets the ord_id of this OrderTrailRequest.  # noqa: E501


        :return: The ord_id of this OrderTrailRequest.  # noqa: E501
        :rtype: str
        """
        return self._ord_id

    @ord_id.setter
    def ord_id(self, ord_id):
        """Sets the ord_id of this OrderTrailRequest.


        :param ord_id: The ord_id of this OrderTrailRequest.  # noqa: E501
        :type: str
        """
        if ord_id is None:
            raise ValueError("Invalid value for `ord_id`, must not be `None`")  # noqa: E501

        self._ord_id = ord_id

    @property
    def instrument(self):
        """Gets the instrument of this OrderTrailRequest.  # noqa: E501


        :return: The instrument of this OrderTrailRequest.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this OrderTrailRequest.


        :param instrument: The instrument of this OrderTrailRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["STK", "ETF", "IDX", "COM", "UNDCUR", "CUR", "FUTIVX", "FUTSTK", "FUTIDX", "FUTCUR", "FUTIRD", "FUTIRC", "FUTIRT", "FUTIRF", "FUTCOM", "FUTBLN", "FUTENR", "FUTMET", "FUTAGR", "OPTIDX", "OPTSTK", "OPTCOM", "OPTBLN", "OPTENR", "OPTAGR", "OPTCUR", "OPTIRC", "OPTIRD", "UNDCOM", "AUCSO", "FUTIDXSPR", "FUTSTKSPR", "FUTCURSPR", "FUTIRTSPR", "FUTIRCSPR", "FUTIRDSPR", "OPTCURSPR", "OPTIRCSPR", "FUTCOMSPR", "OPTCOMSPR", "UNDIRC", "UNDIRD", "UNDIRT", "NONE"]  # noqa: E501
        if instrument not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument, allowed_values)
            )

        self._instrument = instrument

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
        if issubclass(OrderTrailRequest, dict):
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
        if not isinstance(other, OrderTrailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other