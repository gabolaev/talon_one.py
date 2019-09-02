# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from talon_one.models.cart_item_adjustment import CartItemAdjustment  # noqa: F401,E501


class CartItem(object):
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
        'name': 'str',
        'sku': 'str',
        'quantity': 'int',
        'price': 'float',
        'category': 'str',
        'weight': 'float',
        'height': 'float',
        'width': 'float',
        'length': 'float',
        'position': 'float',
        'attributes': 'object',
        'adjustment': 'CartItemAdjustment'
    }

    attribute_map = {
        'name': 'name',
        'sku': 'sku',
        'quantity': 'quantity',
        'price': 'price',
        'category': 'category',
        'weight': 'weight',
        'height': 'height',
        'width': 'width',
        'length': 'length',
        'position': 'position',
        'attributes': 'attributes',
        'adjustment': 'adjustment'
    }

    def __init__(self, name=None, sku=None, quantity=None, price=None, category=None, weight=None, height=None, width=None, length=None, position=None, attributes=None, adjustment=None):  # noqa: E501
        """CartItem - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._sku = None
        self._quantity = None
        self._price = None
        self._category = None
        self._weight = None
        self._height = None
        self._width = None
        self._length = None
        self._position = None
        self._attributes = None
        self._adjustment = None
        self.discriminator = None

        self.name = name
        self.sku = sku
        self.quantity = quantity
        self.price = price
        if category is not None:
            self.category = category
        if weight is not None:
            self.weight = weight
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if length is not None:
            self.length = length
        if position is not None:
            self.position = position
        if attributes is not None:
            self.attributes = attributes
        if adjustment is not None:
            self.adjustment = adjustment

    @property
    def name(self):
        """Gets the name of this CartItem.  # noqa: E501


        :return: The name of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CartItem.


        :param name: The name of this CartItem.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def sku(self):
        """Gets the sku of this CartItem.  # noqa: E501


        :return: The sku of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this CartItem.


        :param sku: The sku of this CartItem.  # noqa: E501
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501
        if sku is not None and len(sku) < 1:
            raise ValueError("Invalid value for `sku`, length must be greater than or equal to `1`")  # noqa: E501

        self._sku = sku

    @property
    def quantity(self):
        """Gets the quantity of this CartItem.  # noqa: E501


        :return: The quantity of this CartItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CartItem.


        :param quantity: The quantity of this CartItem.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501
        if quantity is not None and quantity < 1:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `1`")  # noqa: E501

        self._quantity = quantity

    @property
    def price(self):
        """Gets the price of this CartItem.  # noqa: E501


        :return: The price of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this CartItem.


        :param price: The price of this CartItem.  # noqa: E501
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def category(self):
        """Gets the category of this CartItem.  # noqa: E501


        :return: The category of this CartItem.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this CartItem.


        :param category: The category of this CartItem.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def weight(self):
        """Gets the weight of this CartItem.  # noqa: E501

        Weight of item in mm  # noqa: E501

        :return: The weight of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CartItem.

        Weight of item in mm  # noqa: E501

        :param weight: The weight of this CartItem.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def height(self):
        """Gets the height of this CartItem.  # noqa: E501

        Height of item in mm  # noqa: E501

        :return: The height of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CartItem.

        Height of item in mm  # noqa: E501

        :param height: The height of this CartItem.  # noqa: E501
        :type: float
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this CartItem.  # noqa: E501

        Width of item in mm  # noqa: E501

        :return: The width of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CartItem.

        Width of item in mm  # noqa: E501

        :param width: The width of this CartItem.  # noqa: E501
        :type: float
        """

        self._width = width

    @property
    def length(self):
        """Gets the length of this CartItem.  # noqa: E501

        Length of item in mm  # noqa: E501

        :return: The length of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CartItem.

        Length of item in mm  # noqa: E501

        :param length: The length of this CartItem.  # noqa: E501
        :type: float
        """

        self._length = length

    @property
    def position(self):
        """Gets the position of this CartItem.  # noqa: E501

        Position of the Cart Item in the Cart (calculated internally)  # noqa: E501

        :return: The position of this CartItem.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CartItem.

        Position of the Cart Item in the Cart (calculated internally)  # noqa: E501

        :param position: The position of this CartItem.  # noqa: E501
        :type: float
        """

        self._position = position

    @property
    def attributes(self):
        """Gets the attributes of this CartItem.  # noqa: E501

        Arbitrary properties associated with this item  # noqa: E501

        :return: The attributes of this CartItem.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CartItem.

        Arbitrary properties associated with this item  # noqa: E501

        :param attributes: The attributes of this CartItem.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def adjustment(self):
        """Gets the adjustment of this CartItem.  # noqa: E501


        :return: The adjustment of this CartItem.  # noqa: E501
        :rtype: CartItemAdjustment
        """
        return self._adjustment

    @adjustment.setter
    def adjustment(self, adjustment):
        """Sets the adjustment of this CartItem.


        :param adjustment: The adjustment of this CartItem.  # noqa: E501
        :type: CartItemAdjustment
        """

        self._adjustment = adjustment

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
        if issubclass(CartItem, dict):
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
        if not isinstance(other, CartItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other