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

class MarginUnPledgeRequest(object):
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
        'unpledge_list': 'list[Pledge]'
    }

    attribute_map = {
        'unpledge_list': 'unpledgeList'
    }

    def __init__(self, unpledge_list=None):  # noqa: E501
        """MarginUnPledgeRequest - a model defined in Swagger"""  # noqa: E501
        self._unpledge_list = None
        self.discriminator = None
        if unpledge_list is not None:
            self.unpledge_list = unpledge_list

    @property
    def unpledge_list(self):
        """Gets the unpledge_list of this MarginUnPledgeRequest.  # noqa: E501


        :return: The unpledge_list of this MarginUnPledgeRequest.  # noqa: E501
        :rtype: list[Pledge]
        """
        return self._unpledge_list

    @unpledge_list.setter
    def unpledge_list(self, unpledge_list):
        """Sets the unpledge_list of this MarginUnPledgeRequest.


        :param unpledge_list: The unpledge_list of this MarginUnPledgeRequest.  # noqa: E501
        :type: list[Pledge]
        """

        self._unpledge_list = unpledge_list

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
        if issubclass(MarginUnPledgeRequest, dict):
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
        if not isinstance(other, MarginUnPledgeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other