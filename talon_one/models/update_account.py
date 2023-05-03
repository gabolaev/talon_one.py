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


class UpdateAccount(object):
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
        'attributes': 'object',
        'company_name': 'str',
        'billing_email': 'str',
        'state': 'str',
        'plan_expires': 'datetime'
    }

    attribute_map = {
        'attributes': 'attributes',
        'company_name': 'companyName',
        'billing_email': 'billingEmail',
        'state': 'state',
        'plan_expires': 'planExpires'
    }

    def __init__(self, attributes=None, company_name=None, billing_email=None, state=None, plan_expires=None, local_vars_configuration=None):  # noqa: E501
        """UpdateAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._company_name = None
        self._billing_email = None
        self._state = None
        self._plan_expires = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        self.company_name = company_name
        self.billing_email = billing_email
        if state is not None:
            self.state = state
        if plan_expires is not None:
            self.plan_expires = plan_expires

    @property
    def attributes(self):
        """Gets the attributes of this UpdateAccount.  # noqa: E501

        Arbitrary properties associated with this campaign.  # noqa: E501

        :return: The attributes of this UpdateAccount.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UpdateAccount.

        Arbitrary properties associated with this campaign.  # noqa: E501

        :param attributes: The attributes of this UpdateAccount.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def company_name(self):
        """Gets the company_name of this UpdateAccount.  # noqa: E501

        Name of your company.  # noqa: E501

        :return: The company_name of this UpdateAccount.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this UpdateAccount.

        Name of your company.  # noqa: E501

        :param company_name: The company_name of this UpdateAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and company_name is None:  # noqa: E501
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                company_name is not None and len(company_name) < 1):
            raise ValueError("Invalid value for `company_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._company_name = company_name

    @property
    def billing_email(self):
        """Gets the billing_email of this UpdateAccount.  # noqa: E501

        The billing email address associated with your company account.  # noqa: E501

        :return: The billing_email of this UpdateAccount.  # noqa: E501
        :rtype: str
        """
        return self._billing_email

    @billing_email.setter
    def billing_email(self, billing_email):
        """Sets the billing_email of this UpdateAccount.

        The billing email address associated with your company account.  # noqa: E501

        :param billing_email: The billing_email of this UpdateAccount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and billing_email is None:  # noqa: E501
            raise ValueError("Invalid value for `billing_email`, must not be `None`")  # noqa: E501

        self._billing_email = billing_email

    @property
    def state(self):
        """Gets the state of this UpdateAccount.  # noqa: E501

        State of the account (active, deactivated).  # noqa: E501

        :return: The state of this UpdateAccount.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateAccount.

        State of the account (active, deactivated).  # noqa: E501

        :param state: The state of this UpdateAccount.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "deactivated"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def plan_expires(self):
        """Gets the plan_expires of this UpdateAccount.  # noqa: E501

        The point in time at which your current plan expires.  # noqa: E501

        :return: The plan_expires of this UpdateAccount.  # noqa: E501
        :rtype: datetime
        """
        return self._plan_expires

    @plan_expires.setter
    def plan_expires(self, plan_expires):
        """Sets the plan_expires of this UpdateAccount.

        The point in time at which your current plan expires.  # noqa: E501

        :param plan_expires: The plan_expires of this UpdateAccount.  # noqa: E501
        :type: datetime
        """

        self._plan_expires = plan_expires

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
        if not isinstance(other, UpdateAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateAccount):
            return True

        return self.to_dict() != other.to_dict()
