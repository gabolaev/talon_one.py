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


class CouponRejectionReason(object):
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
        'coupon_id': 'int',
        'reason': 'str'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'coupon_id': 'couponId',
        'reason': 'reason'
    }

    def __init__(self, campaign_id=None, coupon_id=None, reason=None, local_vars_configuration=None):  # noqa: E501
        """CouponRejectionReason - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._campaign_id = None
        self._coupon_id = None
        self._reason = None
        self.discriminator = None

        self.campaign_id = campaign_id
        self.coupon_id = coupon_id
        self.reason = reason

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CouponRejectionReason.  # noqa: E501


        :return: The campaign_id of this CouponRejectionReason.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CouponRejectionReason.


        :param campaign_id: The campaign_id of this CouponRejectionReason.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and campaign_id is None:  # noqa: E501
            raise ValueError("Invalid value for `campaign_id`, must not be `None`")  # noqa: E501

        self._campaign_id = campaign_id

    @property
    def coupon_id(self):
        """Gets the coupon_id of this CouponRejectionReason.  # noqa: E501


        :return: The coupon_id of this CouponRejectionReason.  # noqa: E501
        :rtype: int
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this CouponRejectionReason.


        :param coupon_id: The coupon_id of this CouponRejectionReason.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and coupon_id is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_id`, must not be `None`")  # noqa: E501

        self._coupon_id = coupon_id

    @property
    def reason(self):
        """Gets the reason of this CouponRejectionReason.  # noqa: E501


        :return: The reason of this CouponRejectionReason.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this CouponRejectionReason.


        :param reason: The reason of this CouponRejectionReason.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reason is None:  # noqa: E501
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501
        allowed_values = ["CouponNotFound", "CouponPartOfNotRunningCampaign", "CampaignLimitReached", "ProfileLimitReached", "CouponRecipientDoesNotMatch", "CouponExpired", "CouponStartDateInFuture", "CouponRejectedByCondition", "EffectCouldNotBeApplied", "CouponPartOfNotTriggeredCampaign", "CouponReservationRequired", "ProfileRequired"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and reason not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

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
        if not isinstance(other, CouponRejectionReason):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CouponRejectionReason):
            return True

        return self.to_dict() != other.to_dict()
