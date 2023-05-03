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


class AudienceCustomer(object):
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
        'id': 'int',
        'created': 'datetime',
        'integration_id': 'str',
        'attributes': 'object',
        'account_id': 'int',
        'closed_sessions': 'int',
        'total_sales': 'float',
        'loyalty_memberships': 'list[LoyaltyMembership]',
        'audience_memberships': 'list[AudienceMembership]',
        'last_activity': 'datetime',
        'sandbox': 'bool',
        'connected_applications_ids': 'list[int]',
        'connected_audiences': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'integration_id': 'integrationId',
        'attributes': 'attributes',
        'account_id': 'accountId',
        'closed_sessions': 'closedSessions',
        'total_sales': 'totalSales',
        'loyalty_memberships': 'loyaltyMemberships',
        'audience_memberships': 'audienceMemberships',
        'last_activity': 'lastActivity',
        'sandbox': 'sandbox',
        'connected_applications_ids': 'connectedApplicationsIds',
        'connected_audiences': 'connectedAudiences'
    }

    def __init__(self, id=None, created=None, integration_id=None, attributes=None, account_id=None, closed_sessions=None, total_sales=None, loyalty_memberships=None, audience_memberships=None, last_activity=None, sandbox=None, connected_applications_ids=None, connected_audiences=None, local_vars_configuration=None):  # noqa: E501
        """AudienceCustomer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._integration_id = None
        self._attributes = None
        self._account_id = None
        self._closed_sessions = None
        self._total_sales = None
        self._loyalty_memberships = None
        self._audience_memberships = None
        self._last_activity = None
        self._sandbox = None
        self._connected_applications_ids = None
        self._connected_audiences = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.integration_id = integration_id
        self.attributes = attributes
        self.account_id = account_id
        self.closed_sessions = closed_sessions
        self.total_sales = total_sales
        if loyalty_memberships is not None:
            self.loyalty_memberships = loyalty_memberships
        if audience_memberships is not None:
            self.audience_memberships = audience_memberships
        self.last_activity = last_activity
        if sandbox is not None:
            self.sandbox = sandbox
        if connected_applications_ids is not None:
            self.connected_applications_ids = connected_applications_ids
        if connected_audiences is not None:
            self.connected_audiences = connected_audiences

    @property
    def id(self):
        """Gets the id of this AudienceCustomer.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this AudienceCustomer.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AudienceCustomer.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this AudienceCustomer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this AudienceCustomer.  # noqa: E501

        The time this entity was created. The time this entity was created.  # noqa: E501

        :return: The created of this AudienceCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this AudienceCustomer.

        The time this entity was created. The time this entity was created.  # noqa: E501

        :param created: The created of this AudienceCustomer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def integration_id(self):
        """Gets the integration_id of this AudienceCustomer.  # noqa: E501

        The integration ID set by your integration layer.  # noqa: E501

        :return: The integration_id of this AudienceCustomer.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this AudienceCustomer.

        The integration ID set by your integration layer.  # noqa: E501

        :param integration_id: The integration_id of this AudienceCustomer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                integration_id is not None and len(integration_id) > 1000):
            raise ValueError("Invalid value for `integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._integration_id = integration_id

    @property
    def attributes(self):
        """Gets the attributes of this AudienceCustomer.  # noqa: E501

        Arbitrary properties associated with this item.  # noqa: E501

        :return: The attributes of this AudienceCustomer.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AudienceCustomer.

        Arbitrary properties associated with this item.  # noqa: E501

        :param attributes: The attributes of this AudienceCustomer.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def account_id(self):
        """Gets the account_id of this AudienceCustomer.  # noqa: E501

        The ID of the Talon.One account that owns this profile.  # noqa: E501

        :return: The account_id of this AudienceCustomer.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AudienceCustomer.

        The ID of the Talon.One account that owns this profile.  # noqa: E501

        :param account_id: The account_id of this AudienceCustomer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def closed_sessions(self):
        """Gets the closed_sessions of this AudienceCustomer.  # noqa: E501

        The total amount of closed sessions by a customer. A closed session is a successful purchase.  # noqa: E501

        :return: The closed_sessions of this AudienceCustomer.  # noqa: E501
        :rtype: int
        """
        return self._closed_sessions

    @closed_sessions.setter
    def closed_sessions(self, closed_sessions):
        """Sets the closed_sessions of this AudienceCustomer.

        The total amount of closed sessions by a customer. A closed session is a successful purchase.  # noqa: E501

        :param closed_sessions: The closed_sessions of this AudienceCustomer.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and closed_sessions is None:  # noqa: E501
            raise ValueError("Invalid value for `closed_sessions`, must not be `None`")  # noqa: E501

        self._closed_sessions = closed_sessions

    @property
    def total_sales(self):
        """Gets the total_sales of this AudienceCustomer.  # noqa: E501

        The total amount of money spent by the customer **before** discounts are applied.  The total sales amount excludes the following: - Cancelled or reopened sessions. - Returned items.   # noqa: E501

        :return: The total_sales of this AudienceCustomer.  # noqa: E501
        :rtype: float
        """
        return self._total_sales

    @total_sales.setter
    def total_sales(self, total_sales):
        """Sets the total_sales of this AudienceCustomer.

        The total amount of money spent by the customer **before** discounts are applied.  The total sales amount excludes the following: - Cancelled or reopened sessions. - Returned items.   # noqa: E501

        :param total_sales: The total_sales of this AudienceCustomer.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_sales is None:  # noqa: E501
            raise ValueError("Invalid value for `total_sales`, must not be `None`")  # noqa: E501

        self._total_sales = total_sales

    @property
    def loyalty_memberships(self):
        """Gets the loyalty_memberships of this AudienceCustomer.  # noqa: E501

        **DEPRECATED** A list of loyalty programs joined by the customer.   # noqa: E501

        :return: The loyalty_memberships of this AudienceCustomer.  # noqa: E501
        :rtype: list[LoyaltyMembership]
        """
        return self._loyalty_memberships

    @loyalty_memberships.setter
    def loyalty_memberships(self, loyalty_memberships):
        """Sets the loyalty_memberships of this AudienceCustomer.

        **DEPRECATED** A list of loyalty programs joined by the customer.   # noqa: E501

        :param loyalty_memberships: The loyalty_memberships of this AudienceCustomer.  # noqa: E501
        :type: list[LoyaltyMembership]
        """

        self._loyalty_memberships = loyalty_memberships

    @property
    def audience_memberships(self):
        """Gets the audience_memberships of this AudienceCustomer.  # noqa: E501

        The audiences the customer belongs to.  # noqa: E501

        :return: The audience_memberships of this AudienceCustomer.  # noqa: E501
        :rtype: list[AudienceMembership]
        """
        return self._audience_memberships

    @audience_memberships.setter
    def audience_memberships(self, audience_memberships):
        """Sets the audience_memberships of this AudienceCustomer.

        The audiences the customer belongs to.  # noqa: E501

        :param audience_memberships: The audience_memberships of this AudienceCustomer.  # noqa: E501
        :type: list[AudienceMembership]
        """

        self._audience_memberships = audience_memberships

    @property
    def last_activity(self):
        """Gets the last_activity of this AudienceCustomer.  # noqa: E501

        Timestamp of the most recent event received from this customer. This field is updated on calls that trigger the rule-engine and that are not [dry requests](https://docs.talon.one/docs/dev/integration-api/dry-requests/#overlay).  For example, [reserving a coupon](https://docs.talon.one/integration-api#operation/createCouponReservation) for a customer doesn't impact this field.   # noqa: E501

        :return: The last_activity of this AudienceCustomer.  # noqa: E501
        :rtype: datetime
        """
        return self._last_activity

    @last_activity.setter
    def last_activity(self, last_activity):
        """Sets the last_activity of this AudienceCustomer.

        Timestamp of the most recent event received from this customer. This field is updated on calls that trigger the rule-engine and that are not [dry requests](https://docs.talon.one/docs/dev/integration-api/dry-requests/#overlay).  For example, [reserving a coupon](https://docs.talon.one/integration-api#operation/createCouponReservation) for a customer doesn't impact this field.   # noqa: E501

        :param last_activity: The last_activity of this AudienceCustomer.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_activity is None:  # noqa: E501
            raise ValueError("Invalid value for `last_activity`, must not be `None`")  # noqa: E501

        self._last_activity = last_activity

    @property
    def sandbox(self):
        """Gets the sandbox of this AudienceCustomer.  # noqa: E501

        Shows whether the customer is part of a sandbox or live Application. See the [docs](https://docs.talon.one/docs/product/applications/overview#application-environments).   # noqa: E501

        :return: The sandbox of this AudienceCustomer.  # noqa: E501
        :rtype: bool
        """
        return self._sandbox

    @sandbox.setter
    def sandbox(self, sandbox):
        """Sets the sandbox of this AudienceCustomer.

        Shows whether the customer is part of a sandbox or live Application. See the [docs](https://docs.talon.one/docs/product/applications/overview#application-environments).   # noqa: E501

        :param sandbox: The sandbox of this AudienceCustomer.  # noqa: E501
        :type: bool
        """

        self._sandbox = sandbox

    @property
    def connected_applications_ids(self):
        """Gets the connected_applications_ids of this AudienceCustomer.  # noqa: E501

        A list of the IDs of the Applications that are connected to this customer profile.  # noqa: E501

        :return: The connected_applications_ids of this AudienceCustomer.  # noqa: E501
        :rtype: list[int]
        """
        return self._connected_applications_ids

    @connected_applications_ids.setter
    def connected_applications_ids(self, connected_applications_ids):
        """Sets the connected_applications_ids of this AudienceCustomer.

        A list of the IDs of the Applications that are connected to this customer profile.  # noqa: E501

        :param connected_applications_ids: The connected_applications_ids of this AudienceCustomer.  # noqa: E501
        :type: list[int]
        """

        self._connected_applications_ids = connected_applications_ids

    @property
    def connected_audiences(self):
        """Gets the connected_audiences of this AudienceCustomer.  # noqa: E501

        A list of the IDs of the audiences that are connected to this customer profile.  # noqa: E501

        :return: The connected_audiences of this AudienceCustomer.  # noqa: E501
        :rtype: list[int]
        """
        return self._connected_audiences

    @connected_audiences.setter
    def connected_audiences(self, connected_audiences):
        """Sets the connected_audiences of this AudienceCustomer.

        A list of the IDs of the audiences that are connected to this customer profile.  # noqa: E501

        :param connected_audiences: The connected_audiences of this AudienceCustomer.  # noqa: E501
        :type: list[int]
        """

        self._connected_audiences = connected_audiences

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
        if not isinstance(other, AudienceCustomer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AudienceCustomer):
            return True

        return self.to_dict() != other.to_dict()
