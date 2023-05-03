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


class NewManagementKey(object):
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
        'name': 'str',
        'expiry_date': 'datetime',
        'endpoints': 'list[Endpoint]',
        'allowed_application_ids': 'list[int]',
        'id': 'int',
        'created_by': 'int',
        'account_id': 'int',
        'created': 'datetime',
        'key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'expiry_date': 'expiryDate',
        'endpoints': 'endpoints',
        'allowed_application_ids': 'allowedApplicationIds',
        'id': 'id',
        'created_by': 'createdBy',
        'account_id': 'accountID',
        'created': 'created',
        'key': 'key'
    }

    def __init__(self, name=None, expiry_date=None, endpoints=None, allowed_application_ids=None, id=None, created_by=None, account_id=None, created=None, key=None, local_vars_configuration=None):  # noqa: E501
        """NewManagementKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._expiry_date = None
        self._endpoints = None
        self._allowed_application_ids = None
        self._id = None
        self._created_by = None
        self._account_id = None
        self._created = None
        self._key = None
        self.discriminator = None

        self.name = name
        self.expiry_date = expiry_date
        self.endpoints = endpoints
        if allowed_application_ids is not None:
            self.allowed_application_ids = allowed_application_ids
        self.id = id
        self.created_by = created_by
        self.account_id = account_id
        self.created = created
        self.key = key

    @property
    def name(self):
        """Gets the name of this NewManagementKey.  # noqa: E501

        Name for management key.  # noqa: E501

        :return: The name of this NewManagementKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewManagementKey.

        Name for management key.  # noqa: E501

        :param name: The name of this NewManagementKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def expiry_date(self):
        """Gets the expiry_date of this NewManagementKey.  # noqa: E501

        The date the management key expires.  # noqa: E501

        :return: The expiry_date of this NewManagementKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this NewManagementKey.

        The date the management key expires.  # noqa: E501

        :param expiry_date: The expiry_date of this NewManagementKey.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and expiry_date is None:  # noqa: E501
            raise ValueError("Invalid value for `expiry_date`, must not be `None`")  # noqa: E501

        self._expiry_date = expiry_date

    @property
    def endpoints(self):
        """Gets the endpoints of this NewManagementKey.  # noqa: E501

        The list of endpoints that can be accessed with the key  # noqa: E501

        :return: The endpoints of this NewManagementKey.  # noqa: E501
        :rtype: list[Endpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this NewManagementKey.

        The list of endpoints that can be accessed with the key  # noqa: E501

        :param endpoints: The endpoints of this NewManagementKey.  # noqa: E501
        :type: list[Endpoint]
        """
        if self.local_vars_configuration.client_side_validation and endpoints is None:  # noqa: E501
            raise ValueError("Invalid value for `endpoints`, must not be `None`")  # noqa: E501

        self._endpoints = endpoints

    @property
    def allowed_application_ids(self):
        """Gets the allowed_application_ids of this NewManagementKey.  # noqa: E501

        A list of Application IDs that you can access with the management key. An empty or missing list means the management key can be used for all Applications in the account.   # noqa: E501

        :return: The allowed_application_ids of this NewManagementKey.  # noqa: E501
        :rtype: list[int]
        """
        return self._allowed_application_ids

    @allowed_application_ids.setter
    def allowed_application_ids(self, allowed_application_ids):
        """Sets the allowed_application_ids of this NewManagementKey.

        A list of Application IDs that you can access with the management key. An empty or missing list means the management key can be used for all Applications in the account.   # noqa: E501

        :param allowed_application_ids: The allowed_application_ids of this NewManagementKey.  # noqa: E501
        :type: list[int]
        """

        self._allowed_application_ids = allowed_application_ids

    @property
    def id(self):
        """Gets the id of this NewManagementKey.  # noqa: E501

        ID of the management key.  # noqa: E501

        :return: The id of this NewManagementKey.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewManagementKey.

        ID of the management key.  # noqa: E501

        :param id: The id of this NewManagementKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this NewManagementKey.  # noqa: E501

        ID of the user who created it.  # noqa: E501

        :return: The created_by of this NewManagementKey.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this NewManagementKey.

        ID of the user who created it.  # noqa: E501

        :param created_by: The created_by of this NewManagementKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def account_id(self):
        """Gets the account_id of this NewManagementKey.  # noqa: E501

        ID of account the key is used for.  # noqa: E501

        :return: The account_id of this NewManagementKey.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this NewManagementKey.

        ID of account the key is used for.  # noqa: E501

        :param account_id: The account_id of this NewManagementKey.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def created(self):
        """Gets the created of this NewManagementKey.  # noqa: E501

        The date the management key was created.  # noqa: E501

        :return: The created of this NewManagementKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this NewManagementKey.

        The date the management key was created.  # noqa: E501

        :param created: The created of this NewManagementKey.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def key(self):
        """Gets the key of this NewManagementKey.  # noqa: E501

        The management key.  # noqa: E501

        :return: The key of this NewManagementKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this NewManagementKey.

        The management key.  # noqa: E501

        :param key: The key of this NewManagementKey.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

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
        if not isinstance(other, NewManagementKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewManagementKey):
            return True

        return self.to_dict() != other.to_dict()
