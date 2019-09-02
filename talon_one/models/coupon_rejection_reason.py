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


class CouponRejectionReason(object):
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
        'campaign_id': 'int',
        'coupon_id': 'int',
        'reason': 'str'
    }

    attribute_map = {
        'campaign_id': 'campaignId',
        'coupon_id': 'couponId',
        'reason': 'reason'
    }

    def __init__(self, campaign_id=None, coupon_id=None, reason=None):  # noqa: E501
        """CouponRejectionReason - a model defined in Swagger"""  # noqa: E501

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
        if campaign_id is None:
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
        if coupon_id is None:
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
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501
        allowed_values = ["CouponNotFound", "CouponPartOfNotRunningCampaign", "CouponLimitReached", "CampaignLimitReached", "ProfileLimitReached", "CouponRecipientDoesNotMatch", "CouponExpired", "CouponStartDateInFuture", "CouponRejectedByCondition"]  # noqa: E501
        if reason not in allowed_values:
            raise ValueError(
                "Invalid value for `reason` ({0}), must be one of {1}"  # noqa: E501
                .format(reason, allowed_values)
            )

        self._reason = reason

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
        if issubclass(CouponRejectionReason, dict):
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
        if not isinstance(other, CouponRejectionReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other