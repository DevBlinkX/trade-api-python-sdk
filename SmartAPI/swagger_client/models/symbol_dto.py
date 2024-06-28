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

class SymbolDto(object):
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
        'disp_sym': 'str',
        'instrument': 'str',
        'base_sym': 'str',
        'company_name': 'str',
        'isin': 'str',
        'exc': 'str',
        'exc_tkn': 'int',
        'series': 'str',
        'lot_size': 'int',
        'tick_size': 'str',
        'expiry_date': 'date',
        'option_type': 'str',
        'strike_price': 'float',
        'stream_sym': 'str',
        'segment': 'str',
        'fno': 'bool',
        'mtf': 'bool',
        'multiplier': 'str',
        'freeze_qty': 'str'
    }

    attribute_map = {
        'symbol': 'symbol',
        'disp_sym': 'dispSym',
        'instrument': 'instrument',
        'base_sym': 'baseSym',
        'company_name': 'companyName',
        'isin': 'isin',
        'exc': 'exc',
        'exc_tkn': 'excTkn',
        'series': 'series',
        'lot_size': 'lotSize',
        'tick_size': 'tickSize',
        'expiry_date': 'expiryDate',
        'option_type': 'optionType',
        'strike_price': 'strikePrice',
        'stream_sym': 'streamSym',
        'segment': 'segment',
        'fno': 'fno',
        'mtf': 'mtf',
        'multiplier': 'multiplier',
        'freeze_qty': 'freezeQty'
    }

    def __init__(self, symbol=None, disp_sym=None, instrument=None, base_sym=None, company_name=None, isin=None, exc=None, exc_tkn=None, series=None, lot_size=None, tick_size=None, expiry_date=None, option_type=None, strike_price=None, stream_sym=None, segment=None, fno=None, mtf=None, multiplier=None, freeze_qty=None):  # noqa: E501
        """SymbolDto - a model defined in Swagger"""  # noqa: E501
        self._symbol = None
        self._disp_sym = None
        self._instrument = None
        self._base_sym = None
        self._company_name = None
        self._isin = None
        self._exc = None
        self._exc_tkn = None
        self._series = None
        self._lot_size = None
        self._tick_size = None
        self._expiry_date = None
        self._option_type = None
        self._strike_price = None
        self._stream_sym = None
        self._segment = None
        self._fno = None
        self._mtf = None
        self._multiplier = None
        self._freeze_qty = None
        self.discriminator = None
        if symbol is not None:
            self.symbol = symbol
        if disp_sym is not None:
            self.disp_sym = disp_sym
        if instrument is not None:
            self.instrument = instrument
        if base_sym is not None:
            self.base_sym = base_sym
        if company_name is not None:
            self.company_name = company_name
        if isin is not None:
            self.isin = isin
        if exc is not None:
            self.exc = exc
        if exc_tkn is not None:
            self.exc_tkn = exc_tkn
        if series is not None:
            self.series = series
        if lot_size is not None:
            self.lot_size = lot_size
        if tick_size is not None:
            self.tick_size = tick_size
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if option_type is not None:
            self.option_type = option_type
        if strike_price is not None:
            self.strike_price = strike_price
        if stream_sym is not None:
            self.stream_sym = stream_sym
        if segment is not None:
            self.segment = segment
        if fno is not None:
            self.fno = fno
        if mtf is not None:
            self.mtf = mtf
        if multiplier is not None:
            self.multiplier = multiplier
        if freeze_qty is not None:
            self.freeze_qty = freeze_qty

    @property
    def symbol(self):
        """Gets the symbol of this SymbolDto.  # noqa: E501


        :return: The symbol of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this SymbolDto.


        :param symbol: The symbol of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def disp_sym(self):
        """Gets the disp_sym of this SymbolDto.  # noqa: E501


        :return: The disp_sym of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._disp_sym

    @disp_sym.setter
    def disp_sym(self, disp_sym):
        """Sets the disp_sym of this SymbolDto.


        :param disp_sym: The disp_sym of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._disp_sym = disp_sym

    @property
    def instrument(self):
        """Gets the instrument of this SymbolDto.  # noqa: E501


        :return: The instrument of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this SymbolDto.


        :param instrument: The instrument of this SymbolDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["STK", "ETF", "IDX", "COM", "UNDCUR", "CUR", "FUTIVX", "FUTSTK", "FUTIDX", "FUTCUR", "FUTIRD", "FUTIRC", "FUTIRT", "FUTIRF", "FUTCOM", "FUTBLN", "FUTENR", "FUTMET", "FUTAGR", "OPTIDX", "OPTSTK", "OPTCOM", "OPTBLN", "OPTENR", "OPTAGR", "OPTCUR", "OPTIRC", "OPTIRD", "UNDCOM", "AUCSO", "FUTIDXSPR", "FUTSTKSPR", "FUTCURSPR", "FUTIRTSPR", "FUTIRCSPR", "FUTIRDSPR", "OPTCURSPR", "OPTIRCSPR", "FUTCOMSPR", "OPTCOMSPR", "UNDIRC", "UNDIRD", "UNDIRT", "NONE"]  # noqa: E501
        if instrument not in allowed_values:
            raise ValueError(
                "Invalid value for `instrument` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument, allowed_values)
            )

        self._instrument = instrument

    @property
    def base_sym(self):
        """Gets the base_sym of this SymbolDto.  # noqa: E501


        :return: The base_sym of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._base_sym

    @base_sym.setter
    def base_sym(self, base_sym):
        """Sets the base_sym of this SymbolDto.


        :param base_sym: The base_sym of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._base_sym = base_sym

    @property
    def company_name(self):
        """Gets the company_name of this SymbolDto.  # noqa: E501


        :return: The company_name of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this SymbolDto.


        :param company_name: The company_name of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def isin(self):
        """Gets the isin of this SymbolDto.  # noqa: E501


        :return: The isin of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this SymbolDto.


        :param isin: The isin of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def exc(self):
        """Gets the exc of this SymbolDto.  # noqa: E501


        :return: The exc of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._exc

    @exc.setter
    def exc(self, exc):
        """Sets the exc of this SymbolDto.


        :param exc: The exc of this SymbolDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["NSE", "BSE", "NFO", "BFO", "CDS", "BCD", "MCXSX", "MCX", "NCO", "BCO", "ICEX"]  # noqa: E501
        if exc not in allowed_values:
            raise ValueError(
                "Invalid value for `exc` ({0}), must be one of {1}"  # noqa: E501
                .format(exc, allowed_values)
            )

        self._exc = exc

    @property
    def exc_tkn(self):
        """Gets the exc_tkn of this SymbolDto.  # noqa: E501


        :return: The exc_tkn of this SymbolDto.  # noqa: E501
        :rtype: int
        """
        return self._exc_tkn

    @exc_tkn.setter
    def exc_tkn(self, exc_tkn):
        """Sets the exc_tkn of this SymbolDto.


        :param exc_tkn: The exc_tkn of this SymbolDto.  # noqa: E501
        :type: int
        """

        self._exc_tkn = exc_tkn

    @property
    def series(self):
        """Gets the series of this SymbolDto.  # noqa: E501


        :return: The series of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this SymbolDto.


        :param series: The series of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._series = series

    @property
    def lot_size(self):
        """Gets the lot_size of this SymbolDto.  # noqa: E501


        :return: The lot_size of this SymbolDto.  # noqa: E501
        :rtype: int
        """
        return self._lot_size

    @lot_size.setter
    def lot_size(self, lot_size):
        """Sets the lot_size of this SymbolDto.


        :param lot_size: The lot_size of this SymbolDto.  # noqa: E501
        :type: int
        """

        self._lot_size = lot_size

    @property
    def tick_size(self):
        """Gets the tick_size of this SymbolDto.  # noqa: E501


        :return: The tick_size of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._tick_size

    @tick_size.setter
    def tick_size(self, tick_size):
        """Sets the tick_size of this SymbolDto.


        :param tick_size: The tick_size of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._tick_size = tick_size

    @property
    def expiry_date(self):
        """Gets the expiry_date of this SymbolDto.  # noqa: E501


        :return: The expiry_date of this SymbolDto.  # noqa: E501
        :rtype: date
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this SymbolDto.


        :param expiry_date: The expiry_date of this SymbolDto.  # noqa: E501
        :type: date
        """

        self._expiry_date = expiry_date

    @property
    def option_type(self):
        """Gets the option_type of this SymbolDto.  # noqa: E501


        :return: The option_type of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this SymbolDto.


        :param option_type: The option_type of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._option_type = option_type

    @property
    def strike_price(self):
        """Gets the strike_price of this SymbolDto.  # noqa: E501


        :return: The strike_price of this SymbolDto.  # noqa: E501
        :rtype: float
        """
        return self._strike_price

    @strike_price.setter
    def strike_price(self, strike_price):
        """Sets the strike_price of this SymbolDto.


        :param strike_price: The strike_price of this SymbolDto.  # noqa: E501
        :type: float
        """

        self._strike_price = strike_price

    @property
    def stream_sym(self):
        """Gets the stream_sym of this SymbolDto.  # noqa: E501


        :return: The stream_sym of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._stream_sym

    @stream_sym.setter
    def stream_sym(self, stream_sym):
        """Sets the stream_sym of this SymbolDto.


        :param stream_sym: The stream_sym of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._stream_sym = stream_sym

    @property
    def segment(self):
        """Gets the segment of this SymbolDto.  # noqa: E501


        :return: The segment of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this SymbolDto.


        :param segment: The segment of this SymbolDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["equity", "derivative", "derivative", "index", "commodity", "currency", "spread", "derivative", "none"]  # noqa: E501
        if segment not in allowed_values:
            raise ValueError(
                "Invalid value for `segment` ({0}), must be one of {1}"  # noqa: E501
                .format(segment, allowed_values)
            )

        self._segment = segment

    @property
    def fno(self):
        """Gets the fno of this SymbolDto.  # noqa: E501


        :return: The fno of this SymbolDto.  # noqa: E501
        :rtype: bool
        """
        return self._fno

    @fno.setter
    def fno(self, fno):
        """Sets the fno of this SymbolDto.


        :param fno: The fno of this SymbolDto.  # noqa: E501
        :type: bool
        """

        self._fno = fno

    @property
    def mtf(self):
        """Gets the mtf of this SymbolDto.  # noqa: E501


        :return: The mtf of this SymbolDto.  # noqa: E501
        :rtype: bool
        """
        return self._mtf

    @mtf.setter
    def mtf(self, mtf):
        """Sets the mtf of this SymbolDto.


        :param mtf: The mtf of this SymbolDto.  # noqa: E501
        :type: bool
        """

        self._mtf = mtf

    @property
    def multiplier(self):
        """Gets the multiplier of this SymbolDto.  # noqa: E501


        :return: The multiplier of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this SymbolDto.


        :param multiplier: The multiplier of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._multiplier = multiplier

    @property
    def freeze_qty(self):
        """Gets the freeze_qty of this SymbolDto.  # noqa: E501


        :return: The freeze_qty of this SymbolDto.  # noqa: E501
        :rtype: str
        """
        return self._freeze_qty

    @freeze_qty.setter
    def freeze_qty(self, freeze_qty):
        """Sets the freeze_qty of this SymbolDto.


        :param freeze_qty: The freeze_qty of this SymbolDto.  # noqa: E501
        :type: str
        """

        self._freeze_qty = freeze_qty

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
        if issubclass(SymbolDto, dict):
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
        if not isinstance(other, SymbolDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
