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


class EffectEntity(object):
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
        'campaign_id': 'int',
        'ruleset_id': 'int',
        'rule_index': 'int',
        'rule_name': 'str',
        'effect_type': 'str',
        'triggered_by_coupon': 'int',
        'triggered_for_catalog_item': 'int'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'ruleset_id': 'rulesetId',
        'rule_index': 'ruleIndex',
        'rule_name': 'ruleName',
        'effect_type': 'effectType',
        'triggered_by_coupon': 'triggeredByCoupon',
        'triggered_for_catalog_item': 'triggeredForCatalogItem'
    }

    def __init__(self, campaign_id=None, ruleset_id=None, rule_index=None, rule_name=None, effect_type=None, triggered_by_coupon=None, triggered_for_catalog_item=None, local_vars_configuration=None):  # noqa: E501
        """EffectEntity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._campaign_id = None
        self._ruleset_id = None
        self._rule_index = None
        self._rule_name = None
        self._effect_type = None
        self._triggered_by_coupon = None
        self._triggered_for_catalog_item = None
        self.discriminator = None

        self.campaign_id = campaign_id
        self.ruleset_id = ruleset_id
        self.rule_index = rule_index
        self.rule_name = rule_name
        self.effect_type = effect_type
        if triggered_by_coupon is not None:
            self.triggered_by_coupon = triggered_by_coupon
        if triggered_for_catalog_item is not None:
            self.triggered_for_catalog_item = triggered_for_catalog_item

    @property
    def campaign_id(self):
        """Gets the campaign_id of this EffectEntity.  # noqa: E501

        The ID of the campaign that triggered this effect.  # noqa: E501

        :return: The campaign_id of this EffectEntity.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this EffectEntity.

        The ID of the campaign that triggered this effect.  # noqa: E501

        :param campaign_id: The campaign_id of this EffectEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def ruleset_id(self):
        """Gets the ruleset_id of this EffectEntity.  # noqa: E501

        The ID of the ruleset that was active in the campaign when this effect was triggered.  # noqa: E501

        :return: The ruleset_id of this EffectEntity.  # noqa: E501
        :rtype: int
        """
        return self._ruleset_id

    @ruleset_id.setter
    def ruleset_id(self, ruleset_id):
        """Sets the ruleset_id of this EffectEntity.

        The ID of the ruleset that was active in the campaign when this effect was triggered.  # noqa: E501

        :param ruleset_id: The ruleset_id of this EffectEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ruleset_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ruleset_id`, must not be `None`")  # noqa: E501

        self._ruleset_id = ruleset_id

    @property
    def rule_index(self):
        """Gets the rule_index of this EffectEntity.  # noqa: E501

        The position of the rule that triggered this effect within the ruleset.  # noqa: E501

        :return: The rule_index of this EffectEntity.  # noqa: E501
        :rtype: int
        """
        return self._rule_index

    @rule_index.setter
    def rule_index(self, rule_index):
        """Sets the rule_index of this EffectEntity.

        The position of the rule that triggered this effect within the ruleset.  # noqa: E501

        :param rule_index: The rule_index of this EffectEntity.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and rule_index is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_index`, must not be `None`")  # noqa: E501

        self._rule_index = rule_index

    @property
    def rule_name(self):
        """Gets the rule_name of this EffectEntity.  # noqa: E501

        The name of the rule that triggered this effect.  # noqa: E501

        :return: The rule_name of this EffectEntity.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this EffectEntity.

        The name of the rule that triggered this effect.  # noqa: E501

        :param rule_name: The rule_name of this EffectEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_name is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def effect_type(self):
        """Gets the effect_type of this EffectEntity.  # noqa: E501

        The type of effect that was triggered. See [API effects](https://docs.talon.one/docs/dev/integration-api/api-effects).  # noqa: E501

        :return: The effect_type of this EffectEntity.  # noqa: E501
        :rtype: str
        """
        return self._effect_type

    @effect_type.setter
    def effect_type(self, effect_type):
        """Sets the effect_type of this EffectEntity.

        The type of effect that was triggered. See [API effects](https://docs.talon.one/docs/dev/integration-api/api-effects).  # noqa: E501

        :param effect_type: The effect_type of this EffectEntity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and effect_type is None:  # noqa: E501
            raise ValueError("Invalid value for `effect_type`, must not be `None`")  # noqa: E501

        self._effect_type = effect_type

    @property
    def triggered_by_coupon(self):
        """Gets the triggered_by_coupon of this EffectEntity.  # noqa: E501

        The ID of the coupon that was being evaluated when this effect was triggered.  # noqa: E501

        :return: The triggered_by_coupon of this EffectEntity.  # noqa: E501
        :rtype: int
        """
        return self._triggered_by_coupon

    @triggered_by_coupon.setter
    def triggered_by_coupon(self, triggered_by_coupon):
        """Sets the triggered_by_coupon of this EffectEntity.

        The ID of the coupon that was being evaluated when this effect was triggered.  # noqa: E501

        :param triggered_by_coupon: The triggered_by_coupon of this EffectEntity.  # noqa: E501
        :type: int
        """

        self._triggered_by_coupon = triggered_by_coupon

    @property
    def triggered_for_catalog_item(self):
        """Gets the triggered_for_catalog_item of this EffectEntity.  # noqa: E501

        The ID of the catalog item that was being evaluated when this effect was triggered.  # noqa: E501

        :return: The triggered_for_catalog_item of this EffectEntity.  # noqa: E501
        :rtype: int
        """
        return self._triggered_for_catalog_item

    @triggered_for_catalog_item.setter
    def triggered_for_catalog_item(self, triggered_for_catalog_item):
        """Sets the triggered_for_catalog_item of this EffectEntity.

        The ID of the catalog item that was being evaluated when this effect was triggered.  # noqa: E501

        :param triggered_for_catalog_item: The triggered_for_catalog_item of this EffectEntity.  # noqa: E501
        :type: int
        """

        self._triggered_for_catalog_item = triggered_for_catalog_item

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
        if not isinstance(other, EffectEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EffectEntity):
            return True

        return self.to_dict() != other.to_dict()
