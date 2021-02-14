# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class CustomerSession(object):
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
        'integration_id': 'str',
        'created': 'datetime',
        'application_id': 'int',
        'profile_id': 'str',
        'coupon': 'str',
        'referral': 'str',
        'state': 'str',
        'cart_items': 'list[CartItem]',
        'identifiers': 'list[str]',
        'total': 'float',
        'attributes': 'object',
        'first_session': 'bool',
        'discounts': 'dict(str, float)'
    }

    attribute_map = {
        'integration_id': 'integrationId',
        'created': 'created',
        'application_id': 'applicationId',
        'profile_id': 'profileId',
        'coupon': 'coupon',
        'referral': 'referral',
        'state': 'state',
        'cart_items': 'cartItems',
        'identifiers': 'identifiers',
        'total': 'total',
        'attributes': 'attributes',
        'first_session': 'firstSession',
        'discounts': 'discounts'
    }

    def __init__(self, integration_id=None, created=None, application_id=None, profile_id=None, coupon=None, referral=None, state='open', cart_items=None, identifiers=None, total=None, attributes=None, first_session=None, discounts=None, local_vars_configuration=None):  # noqa: E501
        """CustomerSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._integration_id = None
        self._created = None
        self._application_id = None
        self._profile_id = None
        self._coupon = None
        self._referral = None
        self._state = None
        self._cart_items = None
        self._identifiers = None
        self._total = None
        self._attributes = None
        self._first_session = None
        self._discounts = None
        self.discriminator = None

        self.integration_id = integration_id
        self.created = created
        self.application_id = application_id
        self.profile_id = profile_id
        self.coupon = coupon
        self.referral = referral
        self.state = state
        self.cart_items = cart_items
        if identifiers is not None:
            self.identifiers = identifiers
        self.total = total
        self.attributes = attributes
        self.first_session = first_session
        self.discounts = discounts

    @property
    def integration_id(self):
        """Gets the integration_id of this CustomerSession.  # noqa: E501

        The integration ID for this entity sent to and used in the Talon.One system.  # noqa: E501

        :return: The integration_id of this CustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this CustomerSession.

        The integration ID for this entity sent to and used in the Talon.One system.  # noqa: E501

        :param integration_id: The integration_id of this CustomerSession.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_id`, must not be `None`")  # noqa: E501

        self._integration_id = integration_id

    @property
    def created(self):
        """Gets the created of this CustomerSession.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this CustomerSession.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CustomerSession.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this CustomerSession.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def application_id(self):
        """Gets the application_id of this CustomerSession.  # noqa: E501

        The ID of the application that owns this entity.  # noqa: E501

        :return: The application_id of this CustomerSession.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this CustomerSession.

        The ID of the application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this CustomerSession.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and application_id is None:  # noqa: E501
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def profile_id(self):
        """Gets the profile_id of this CustomerSession.  # noqa: E501

        ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID.  # noqa: E501

        :return: The profile_id of this CustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this CustomerSession.

        ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID.  # noqa: E501

        :param profile_id: The profile_id of this CustomerSession.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and profile_id is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

    @property
    def coupon(self):
        """Gets the coupon of this CustomerSession.  # noqa: E501

        Any coupon code entered.  # noqa: E501

        :return: The coupon of this CustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        """Sets the coupon of this CustomerSession.

        Any coupon code entered.  # noqa: E501

        :param coupon: The coupon of this CustomerSession.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and coupon is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                coupon is not None and len(coupon) > 100):
            raise ValueError("Invalid value for `coupon`, length must be less than or equal to `100`")  # noqa: E501

        self._coupon = coupon

    @property
    def referral(self):
        """Gets the referral of this CustomerSession.  # noqa: E501

        Any referral code entered.  # noqa: E501

        :return: The referral of this CustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._referral

    @referral.setter
    def referral(self, referral):
        """Sets the referral of this CustomerSession.

        Any referral code entered.  # noqa: E501

        :param referral: The referral of this CustomerSession.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and referral is None:  # noqa: E501
            raise ValueError("Invalid value for `referral`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                referral is not None and len(referral) > 100):
            raise ValueError("Invalid value for `referral`, length must be less than or equal to `100`")  # noqa: E501

        self._referral = referral

    @property
    def state(self):
        """Gets the state of this CustomerSession.  # noqa: E501

        Indicates the current state of the session. All sessions must start in the \"open\" state, after which valid transitions are...  1. open -> closed 2. open -> cancelled 3. closed -> cancelled   # noqa: E501

        :return: The state of this CustomerSession.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CustomerSession.

        Indicates the current state of the session. All sessions must start in the \"open\" state, after which valid transitions are...  1. open -> closed 2. open -> cancelled 3. closed -> cancelled   # noqa: E501

        :param state: The state of this CustomerSession.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["open", "closed", "cancelled"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def cart_items(self):
        """Gets the cart_items of this CustomerSession.  # noqa: E501

        Serialized JSON representation.  # noqa: E501

        :return: The cart_items of this CustomerSession.  # noqa: E501
        :rtype: list[CartItem]
        """
        return self._cart_items

    @cart_items.setter
    def cart_items(self, cart_items):
        """Sets the cart_items of this CustomerSession.

        Serialized JSON representation.  # noqa: E501

        :param cart_items: The cart_items of this CustomerSession.  # noqa: E501
        :type: list[CartItem]
        """
        if self.local_vars_configuration.client_side_validation and cart_items is None:  # noqa: E501
            raise ValueError("Invalid value for `cart_items`, must not be `None`")  # noqa: E501

        self._cart_items = cart_items

    @property
    def identifiers(self):
        """Gets the identifiers of this CustomerSession.  # noqa: E501

        Identifiers for the customer, this can be used for limits on values such as device ID.  # noqa: E501

        :return: The identifiers of this CustomerSession.  # noqa: E501
        :rtype: list[str]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this CustomerSession.

        Identifiers for the customer, this can be used for limits on values such as device ID.  # noqa: E501

        :param identifiers: The identifiers of this CustomerSession.  # noqa: E501
        :type: list[str]
        """

        self._identifiers = identifiers

    @property
    def total(self):
        """Gets the total of this CustomerSession.  # noqa: E501

        The total sum of the cart in one session.  # noqa: E501

        :return: The total of this CustomerSession.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CustomerSession.

        The total sum of the cart in one session.  # noqa: E501

        :param total: The total of this CustomerSession.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def attributes(self):
        """Gets the attributes of this CustomerSession.  # noqa: E501

        A key-value map of the sessions attributes. The potentially valid attributes are configured in your accounts developer settings.   # noqa: E501

        :return: The attributes of this CustomerSession.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CustomerSession.

        A key-value map of the sessions attributes. The potentially valid attributes are configured in your accounts developer settings.   # noqa: E501

        :param attributes: The attributes of this CustomerSession.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and attributes is None:  # noqa: E501
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def first_session(self):
        """Gets the first_session of this CustomerSession.  # noqa: E501

        Indicates whether this is the first session for the customer's profile. Will always be true for anonymous sessions.  # noqa: E501

        :return: The first_session of this CustomerSession.  # noqa: E501
        :rtype: bool
        """
        return self._first_session

    @first_session.setter
    def first_session(self, first_session):
        """Sets the first_session of this CustomerSession.

        Indicates whether this is the first session for the customer's profile. Will always be true for anonymous sessions.  # noqa: E501

        :param first_session: The first_session of this CustomerSession.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and first_session is None:  # noqa: E501
            raise ValueError("Invalid value for `first_session`, must not be `None`")  # noqa: E501

        self._first_session = first_session

    @property
    def discounts(self):
        """Gets the discounts of this CustomerSession.  # noqa: E501

        A map of labelled discount values, values will be in the same currency as the application associated with the session.  # noqa: E501

        :return: The discounts of this CustomerSession.  # noqa: E501
        :rtype: dict(str, float)
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this CustomerSession.

        A map of labelled discount values, values will be in the same currency as the application associated with the session.  # noqa: E501

        :param discounts: The discounts of this CustomerSession.  # noqa: E501
        :type: dict(str, float)
        """
        if self.local_vars_configuration.client_side_validation and discounts is None:  # noqa: E501
            raise ValueError("Invalid value for `discounts`, must not be `None`")  # noqa: E501

        self._discounts = discounts

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
        if not isinstance(other, CustomerSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerSession):
            return True

        return self.to_dict() != other.to_dict()
