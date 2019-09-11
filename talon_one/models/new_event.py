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


class NewEvent(object):
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
        'profile_id': 'str',
        'type': 'str',
        'attributes': 'object',
        'session_id': 'str'
    }

    attribute_map = {
        'profile_id': 'profileId',
        'type': 'type',
        'attributes': 'attributes',
        'session_id': 'sessionId'
    }

    def __init__(self, profile_id=None, type=None, attributes=None, session_id=None):  # noqa: E501
        """NewEvent - a model defined in Swagger"""  # noqa: E501

        self._profile_id = None
        self._type = None
        self._attributes = None
        self._session_id = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        self.type = type
        self.attributes = attributes
        self.session_id = session_id

    @property
    def profile_id(self):
        """Gets the profile_id of this NewEvent.  # noqa: E501

        ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID.  # noqa: E501

        :return: The profile_id of this NewEvent.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this NewEvent.

        ID of the customers profile as used within this Talon.One account. May be omitted or set to the empty string if the customer does not yet have a known profile ID.  # noqa: E501

        :param profile_id: The profile_id of this NewEvent.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def type(self):
        """Gets the type of this NewEvent.  # noqa: E501

        A string representing the event. Must not be a reserved event name.  # noqa: E501

        :return: The type of this NewEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NewEvent.

        A string representing the event. Must not be a reserved event name.  # noqa: E501

        :param type: The type of this NewEvent.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this NewEvent.  # noqa: E501

        Arbitrary additional JSON data associated with the event.  # noqa: E501

        :return: The attributes of this NewEvent.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this NewEvent.

        Arbitrary additional JSON data associated with the event.  # noqa: E501

        :param attributes: The attributes of this NewEvent.  # noqa: E501
        :type: object
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

    @property
    def session_id(self):
        """Gets the session_id of this NewEvent.  # noqa: E501

        The ID of the session that this event occurred in.  # noqa: E501

        :return: The session_id of this NewEvent.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this NewEvent.

        The ID of the session that this event occurred in.  # noqa: E501

        :param session_id: The session_id of this NewEvent.  # noqa: E501
        :type: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501
        if session_id is not None and len(session_id) < 1:
            raise ValueError("Invalid value for `session_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._session_id = session_id

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
        if issubclass(NewEvent, dict):
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
        if not isinstance(other, NewEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
