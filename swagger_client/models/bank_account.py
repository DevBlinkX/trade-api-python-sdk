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


class BankAccount(object):
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
        'default_bank': 'bool',
        'acc_no': 'str',
        'cheque_name': 'str',
        'bank_name': 'str',
        'acc_type': 'str',
        'micr_code': 'str',
        'ifsc_code': 'str'
    }

    attribute_map = {
        'default_bank': 'defaultBank',
        'acc_no': 'accNo',
        'cheque_name': 'chequeName',
        'bank_name': 'bankName',
        'acc_type': 'accType',
        'micr_code': 'micrCode',
        'ifsc_code': 'ifscCode'
    }

    def __init__(self, default_bank=None, acc_no=None, cheque_name=None, bank_name=None, acc_type=None, micr_code=None,
                 ifsc_code=None):  # noqa: E501
        """BankAccount - a model defined in Swagger"""  # noqa: E501
        self._default_bank = None
        self._acc_no = None
        self._cheque_name = None
        self._bank_name = None
        self._acc_type = None
        self._micr_code = None
        self._ifsc_code = None
        self.discriminator = None
        if default_bank is not None:
            self.default_bank = default_bank
        if acc_no is not None:
            self.acc_no = acc_no
        if cheque_name is not None:
            self.cheque_name = cheque_name
        if bank_name is not None:
            self.bank_name = bank_name
        if acc_type is not None:
            self.acc_type = acc_type
        if micr_code is not None:
            self.micr_code = micr_code
        if ifsc_code is not None:
            self.ifsc_code = ifsc_code

    @property
    def default_bank(self):
        """Gets the default_bank of this BankAccount.  # noqa: E501


        :return: The default_bank of this BankAccount.  # noqa: E501
        :rtype: bool
        """
        return self._default_bank

    @default_bank.setter
    def default_bank(self, default_bank):
        """Sets the default_bank of this BankAccount.


        :param default_bank: The default_bank of this BankAccount.  # noqa: E501
        :type: bool
        """

        self._default_bank = default_bank

    @property
    def acc_no(self):
        """Gets the acc_no of this BankAccount.  # noqa: E501


        :return: The acc_no of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._acc_no

    @acc_no.setter
    def acc_no(self, acc_no):
        """Sets the acc_no of this BankAccount.


        :param acc_no: The acc_no of this BankAccount.  # noqa: E501
        :type: str
        """

        self._acc_no = acc_no

    @property
    def cheque_name(self):
        """Gets the cheque_name of this BankAccount.  # noqa: E501


        :return: The cheque_name of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._cheque_name

    @cheque_name.setter
    def cheque_name(self, cheque_name):
        """Sets the cheque_name of this BankAccount.


        :param cheque_name: The cheque_name of this BankAccount.  # noqa: E501
        :type: str
        """

        self._cheque_name = cheque_name

    @property
    def bank_name(self):
        """Gets the bank_name of this BankAccount.  # noqa: E501


        :return: The bank_name of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        """Sets the bank_name of this BankAccount.


        :param bank_name: The bank_name of this BankAccount.  # noqa: E501
        :type: str
        """

        self._bank_name = bank_name

    @property
    def acc_type(self):
        """Gets the acc_type of this BankAccount.  # noqa: E501


        :return: The acc_type of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._acc_type

    @acc_type.setter
    def acc_type(self, acc_type):
        """Sets the acc_type of this BankAccount.


        :param acc_type: The acc_type of this BankAccount.  # noqa: E501
        :type: str
        """

        self._acc_type = acc_type

    @property
    def micr_code(self):
        """Gets the micr_code of this BankAccount.  # noqa: E501


        :return: The micr_code of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._micr_code

    @micr_code.setter
    def micr_code(self, micr_code):
        """Sets the micr_code of this BankAccount.


        :param micr_code: The micr_code of this BankAccount.  # noqa: E501
        :type: str
        """

        self._micr_code = micr_code

    @property
    def ifsc_code(self):
        """Gets the ifsc_code of this BankAccount.  # noqa: E501


        :return: The ifsc_code of this BankAccount.  # noqa: E501
        :rtype: str
        """
        return self._ifsc_code

    @ifsc_code.setter
    def ifsc_code(self, ifsc_code):
        """Sets the ifsc_code of this BankAccount.


        :param ifsc_code: The ifsc_code of this BankAccount.  # noqa: E501
        :type: str
        """

        self._ifsc_code = ifsc_code

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
        if issubclass(BankAccount, dict):
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
        if not isinstance(other, BankAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
