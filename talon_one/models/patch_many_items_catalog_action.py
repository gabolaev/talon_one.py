# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class PatchManyItemsCatalogAction(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'price': 'float',
        'filters': 'list[CatalogActionFilter]',
        'attributes': 'object'
    }

    attribute_map = {
        'price': 'price',
        'filters': 'filters',
        'attributes': 'attributes'
    }

    def __init__(self, price=None, filters=None, attributes=None, local_vars_configuration=None):  # noqa: E501
        """PatchManyItemsCatalogAction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._price = None
        self._filters = None
        self._attributes = None
        self.discriminator = None

        if price is not None:
            self.price = price
        if filters is not None:
            self.filters = filters
        if attributes is not None:
            self.attributes = attributes

    @property
    def price(self):
        """Gets the price of this PatchManyItemsCatalogAction.  # noqa: E501

        Price of the item.  # noqa: E501

        :return: The price of this PatchManyItemsCatalogAction.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PatchManyItemsCatalogAction.

        Price of the item.  # noqa: E501

        :param price: The price of this PatchManyItemsCatalogAction.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def filters(self):
        """Gets the filters of this PatchManyItemsCatalogAction.  # noqa: E501

        The list of filters used to select the items to patch, joined by `AND`.  **Note:** Every item in the catalog will be modified if there are no filters.   # noqa: E501

        :return: The filters of this PatchManyItemsCatalogAction.  # noqa: E501
        :rtype: list[CatalogActionFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this PatchManyItemsCatalogAction.

        The list of filters used to select the items to patch, joined by `AND`.  **Note:** Every item in the catalog will be modified if there are no filters.   # noqa: E501

        :param filters: The filters of this PatchManyItemsCatalogAction.  # noqa: E501
        :type: list[CatalogActionFilter]
        """

        self._filters = filters

    @property
    def attributes(self):
        """Gets the attributes of this PatchManyItemsCatalogAction.  # noqa: E501

        The attributes of the items to patch.  # noqa: E501

        :return: The attributes of this PatchManyItemsCatalogAction.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this PatchManyItemsCatalogAction.

        The attributes of the items to patch.  # noqa: E501

        :param attributes: The attributes of this PatchManyItemsCatalogAction.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchManyItemsCatalogAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchManyItemsCatalogAction):
            return True

        return self.to_dict() != other.to_dict()
