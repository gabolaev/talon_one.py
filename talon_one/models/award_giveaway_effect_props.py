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


class AwardGiveawayEffectProps(object):
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
        'pool_id': 'int',
        'pool_name': 'str',
        'recipient_integration_id': 'str',
        'giveaway_id': 'int',
        'code': 'str'
    }

    attribute_map = {
        'pool_id': 'poolId',
        'pool_name': 'poolName',
        'recipient_integration_id': 'recipientIntegrationId',
        'giveaway_id': 'giveawayId',
        'code': 'code'
    }

    def __init__(self, pool_id=None, pool_name=None, recipient_integration_id=None, giveaway_id=None, code=None, local_vars_configuration=None):  # noqa: E501
        """AwardGiveawayEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pool_id = None
        self._pool_name = None
        self._recipient_integration_id = None
        self._giveaway_id = None
        self._code = None
        self.discriminator = None

        self.pool_id = pool_id
        self.pool_name = pool_name
        self.recipient_integration_id = recipient_integration_id
        self.giveaway_id = giveaway_id
        self.code = code

    @property
    def pool_id(self):
        """Gets the pool_id of this AwardGiveawayEffectProps.  # noqa: E501

        The ID of the giveaways pool the code was taken from.  # noqa: E501

        :return: The pool_id of this AwardGiveawayEffectProps.  # noqa: E501
        :rtype: int
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this AwardGiveawayEffectProps.

        The ID of the giveaways pool the code was taken from.  # noqa: E501

        :param pool_id: The pool_id of this AwardGiveawayEffectProps.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and pool_id is None:  # noqa: E501
            raise ValueError("Invalid value for `pool_id`, must not be `None`")  # noqa: E501

        self._pool_id = pool_id

    @property
    def pool_name(self):
        """Gets the pool_name of this AwardGiveawayEffectProps.  # noqa: E501

        The name of the giveaways pool the code was taken from.  # noqa: E501

        :return: The pool_name of this AwardGiveawayEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        """Sets the pool_name of this AwardGiveawayEffectProps.

        The name of the giveaways pool the code was taken from.  # noqa: E501

        :param pool_name: The pool_name of this AwardGiveawayEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pool_name is None:  # noqa: E501
            raise ValueError("Invalid value for `pool_name`, must not be `None`")  # noqa: E501

        self._pool_name = pool_name

    @property
    def recipient_integration_id(self):
        """Gets the recipient_integration_id of this AwardGiveawayEffectProps.  # noqa: E501

        The integration ID of the profile that was awarded the giveaway.  # noqa: E501

        :return: The recipient_integration_id of this AwardGiveawayEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._recipient_integration_id

    @recipient_integration_id.setter
    def recipient_integration_id(self, recipient_integration_id):
        """Sets the recipient_integration_id of this AwardGiveawayEffectProps.

        The integration ID of the profile that was awarded the giveaway.  # noqa: E501

        :param recipient_integration_id: The recipient_integration_id of this AwardGiveawayEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and recipient_integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `recipient_integration_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                recipient_integration_id is not None and len(recipient_integration_id) > 1000):
            raise ValueError("Invalid value for `recipient_integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._recipient_integration_id = recipient_integration_id

    @property
    def giveaway_id(self):
        """Gets the giveaway_id of this AwardGiveawayEffectProps.  # noqa: E501

        The internal ID for the giveaway that was awarded.  # noqa: E501

        :return: The giveaway_id of this AwardGiveawayEffectProps.  # noqa: E501
        :rtype: int
        """
        return self._giveaway_id

    @giveaway_id.setter
    def giveaway_id(self, giveaway_id):
        """Sets the giveaway_id of this AwardGiveawayEffectProps.

        The internal ID for the giveaway that was awarded.  # noqa: E501

        :param giveaway_id: The giveaway_id of this AwardGiveawayEffectProps.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and giveaway_id is None:  # noqa: E501
            raise ValueError("Invalid value for `giveaway_id`, must not be `None`")  # noqa: E501

        self._giveaway_id = giveaway_id

    @property
    def code(self):
        """Gets the code of this AwardGiveawayEffectProps.  # noqa: E501

        The giveaway code that was awarded.  # noqa: E501

        :return: The code of this AwardGiveawayEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AwardGiveawayEffectProps.

        The giveaway code that was awarded.  # noqa: E501

        :param code: The code of this AwardGiveawayEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, AwardGiveawayEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwardGiveawayEffectProps):
            return True

        return self.to_dict() != other.to_dict()
