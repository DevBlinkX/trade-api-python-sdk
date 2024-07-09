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


class ModifyOrderData(object):
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
        'ord_status': 'str',
        'rej_reason': 'str'
    }

    attribute_map = {
        'ord_id': 'ordId',
        'ord_status': 'ordStatus',
        'rej_reason': 'rejReason'
    }

    def __init__(self, ord_id=None, ord_status=None, rej_reason=None):  # noqa: E501
        """ModifyOrderData - a model defined in Swagger"""  # noqa: E501
        self._ord_id = None
        self._ord_status = None
        self._rej_reason = None
        self.discriminator = None
        if ord_id is not None:
            self.ord_id = ord_id
        if ord_status is not None:
            self.ord_status = ord_status
        if rej_reason is not None:
            self.rej_reason = rej_reason

    @property
    def ord_id(self):
        """Gets the ord_id of this ModifyOrderData.  # noqa: E501


        :return: The ord_id of this ModifyOrderData.  # noqa: E501
        :rtype: str
        """
        return self._ord_id

    @ord_id.setter
    def ord_id(self, ord_id):
        """Sets the ord_id of this ModifyOrderData.


        :param ord_id: The ord_id of this ModifyOrderData.  # noqa: E501
        :type: str
        """

        self._ord_id = ord_id

    @property
    def ord_status(self):
        """Gets the ord_status of this ModifyOrderData.  # noqa: E501


        :return: The ord_status of this ModifyOrderData.  # noqa: E501
        :rtype: str
        """
        return self._ord_status

    @ord_status.setter
    def ord_status(self, ord_status):
        """Sets the ord_status of this ModifyOrderData.


        :param ord_status: The ord_status of this ModifyOrderData.  # noqa: E501
        :type: str
        """
        allowed_values = ["Executed", "Pending", "Cancelled", "Transit", "Rejected", "Requested", "None"]  # noqa: E501
        if ord_status not in allowed_values:
            raise ValueError(
                "Invalid value for `ord_status` ({0}), must be one of {1}"  # noqa: E501
                .format(ord_status, allowed_values)
            )

        self._ord_status = ord_status

    @property
    def rej_reason(self):
        """Gets the rej_reason of this ModifyOrderData.  # noqa: E501


        :return: The rej_reason of this ModifyOrderData.  # noqa: E501
        :rtype: str
        """
        return self._rej_reason

    @rej_reason.setter
    def rej_reason(self, rej_reason):
        """Sets the rej_reason of this ModifyOrderData.


        :param rej_reason: The rej_reason of this ModifyOrderData.  # noqa: E501
        :type: str
        """

        self._rej_reason = rej_reason

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
        if issubclass(ModifyOrderData, dict):
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
        if not isinstance(other, ModifyOrderData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
