# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class LoyaltyCard(object):
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
        'program_id': 'int',
        'status': 'str',
        'identifier': 'str',
        'users_per_card_limit': 'int',
        'profiles': 'list[LoyaltyCardProfileRegistration]',
        'ledger': 'LedgerInfo',
        'subledgers': 'dict(str, LedgerInfo)',
        'modified': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'program_id': 'programID',
        'status': 'status',
        'identifier': 'identifier',
        'users_per_card_limit': 'usersPerCardLimit',
        'profiles': 'profiles',
        'ledger': 'ledger',
        'subledgers': 'subledgers',
        'modified': 'modified'
    }

    def __init__(self, id=None, created=None, program_id=None, status=None, identifier=None, users_per_card_limit=None, profiles=None, ledger=None, subledgers=None, modified=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyCard - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._program_id = None
        self._status = None
        self._identifier = None
        self._users_per_card_limit = None
        self._profiles = None
        self._ledger = None
        self._subledgers = None
        self._modified = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.program_id = program_id
        self.status = status
        self.identifier = identifier
        self.users_per_card_limit = users_per_card_limit
        if profiles is not None:
            self.profiles = profiles
        if ledger is not None:
            self.ledger = ledger
        if subledgers is not None:
            self.subledgers = subledgers
        if modified is not None:
            self.modified = modified

    @property
    def id(self):
        """Gets the id of this LoyaltyCard.  # noqa: E501

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :return: The id of this LoyaltyCard.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoyaltyCard.

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :param id: The id of this LoyaltyCard.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this LoyaltyCard.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this LoyaltyCard.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this LoyaltyCard.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this LoyaltyCard.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def program_id(self):
        """Gets the program_id of this LoyaltyCard.  # noqa: E501

        The ID of the loyalty program that owns this entity.  # noqa: E501

        :return: The program_id of this LoyaltyCard.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this LoyaltyCard.

        The ID of the loyalty program that owns this entity.  # noqa: E501

        :param program_id: The program_id of this LoyaltyCard.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and program_id is None:  # noqa: E501
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def status(self):
        """Gets the status of this LoyaltyCard.  # noqa: E501

        Status of the loyalty card. Can be one of: ['active', 'disabled']   # noqa: E501

        :return: The status of this LoyaltyCard.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LoyaltyCard.

        Status of the loyalty card. Can be one of: ['active', 'disabled']   # noqa: E501

        :param status: The status of this LoyaltyCard.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def identifier(self):
        """Gets the identifier of this LoyaltyCard.  # noqa: E501

        The alphanumeric identifier of the loyalty card.  # noqa: E501

        :return: The identifier of this LoyaltyCard.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this LoyaltyCard.

        The alphanumeric identifier of the loyalty card.  # noqa: E501

        :param identifier: The identifier of this LoyaltyCard.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501

        self._identifier = identifier

    @property
    def users_per_card_limit(self):
        """Gets the users_per_card_limit of this LoyaltyCard.  # noqa: E501

        The max amount of user profiles a card can be shared with. 0 means unlimited.   # noqa: E501

        :return: The users_per_card_limit of this LoyaltyCard.  # noqa: E501
        :rtype: int
        """
        return self._users_per_card_limit

    @users_per_card_limit.setter
    def users_per_card_limit(self, users_per_card_limit):
        """Sets the users_per_card_limit of this LoyaltyCard.

        The max amount of user profiles a card can be shared with. 0 means unlimited.   # noqa: E501

        :param users_per_card_limit: The users_per_card_limit of this LoyaltyCard.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and users_per_card_limit is None:  # noqa: E501
            raise ValueError("Invalid value for `users_per_card_limit`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                users_per_card_limit is not None and users_per_card_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `users_per_card_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._users_per_card_limit = users_per_card_limit

    @property
    def profiles(self):
        """Gets the profiles of this LoyaltyCard.  # noqa: E501

        Integration IDs of the customers associated with the card.  # noqa: E501

        :return: The profiles of this LoyaltyCard.  # noqa: E501
        :rtype: list[LoyaltyCardProfileRegistration]
        """
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        """Sets the profiles of this LoyaltyCard.

        Integration IDs of the customers associated with the card.  # noqa: E501

        :param profiles: The profiles of this LoyaltyCard.  # noqa: E501
        :type: list[LoyaltyCardProfileRegistration]
        """

        self._profiles = profiles

    @property
    def ledger(self):
        """Gets the ledger of this LoyaltyCard.  # noqa: E501


        :return: The ledger of this LoyaltyCard.  # noqa: E501
        :rtype: LedgerInfo
        """
        return self._ledger

    @ledger.setter
    def ledger(self, ledger):
        """Sets the ledger of this LoyaltyCard.


        :param ledger: The ledger of this LoyaltyCard.  # noqa: E501
        :type: LedgerInfo
        """

        self._ledger = ledger

    @property
    def subledgers(self):
        """Gets the subledgers of this LoyaltyCard.  # noqa: E501

        Displays point balances of the card in the subledgers of the loyalty program.  # noqa: E501

        :return: The subledgers of this LoyaltyCard.  # noqa: E501
        :rtype: dict(str, LedgerInfo)
        """
        return self._subledgers

    @subledgers.setter
    def subledgers(self, subledgers):
        """Sets the subledgers of this LoyaltyCard.

        Displays point balances of the card in the subledgers of the loyalty program.  # noqa: E501

        :param subledgers: The subledgers of this LoyaltyCard.  # noqa: E501
        :type: dict(str, LedgerInfo)
        """

        self._subledgers = subledgers

    @property
    def modified(self):
        """Gets the modified of this LoyaltyCard.  # noqa: E501

        Timestamp of the most recent update of the loyalty card.  # noqa: E501

        :return: The modified of this LoyaltyCard.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this LoyaltyCard.

        Timestamp of the most recent update of the loyalty card.  # noqa: E501

        :param modified: The modified of this LoyaltyCard.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

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
        if not isinstance(other, LoyaltyCard):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyCard):
            return True

        return self.to_dict() != other.to_dict()