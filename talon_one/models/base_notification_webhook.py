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


class BaseNotificationWebhook(object):
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
        'modified': 'datetime',
        'url': 'str',
        'headers': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'url': 'url',
        'headers': 'headers'
    }

    def __init__(self, id=None, created=None, modified=None, url=None, headers=None, local_vars_configuration=None):  # noqa: E501
        """BaseNotificationWebhook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._modified = None
        self._url = None
        self._headers = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.modified = modified
        self.url = url
        self.headers = headers

    @property
    def id(self):
        """Gets the id of this BaseNotificationWebhook.  # noqa: E501

        Internal ID of this entity.  # noqa: E501

        :return: The id of this BaseNotificationWebhook.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseNotificationWebhook.

        Internal ID of this entity.  # noqa: E501

        :param id: The id of this BaseNotificationWebhook.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this BaseNotificationWebhook.  # noqa: E501

        The time this entity was created.  # noqa: E501

        :return: The created of this BaseNotificationWebhook.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BaseNotificationWebhook.

        The time this entity was created.  # noqa: E501

        :param created: The created of this BaseNotificationWebhook.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this BaseNotificationWebhook.  # noqa: E501

        The time this entity was last modified.  # noqa: E501

        :return: The modified of this BaseNotificationWebhook.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this BaseNotificationWebhook.

        The time this entity was last modified.  # noqa: E501

        :param modified: The modified of this BaseNotificationWebhook.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified is None:  # noqa: E501
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def url(self):
        """Gets the url of this BaseNotificationWebhook.  # noqa: E501

        API URL for the given webhook-based notification.  # noqa: E501

        :return: The url of this BaseNotificationWebhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BaseNotificationWebhook.

        API URL for the given webhook-based notification.  # noqa: E501

        :param url: The url of this BaseNotificationWebhook.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def headers(self):
        """Gets the headers of this BaseNotificationWebhook.  # noqa: E501

        List of API HTTP headers for the given webhook-based notification.  # noqa: E501

        :return: The headers of this BaseNotificationWebhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this BaseNotificationWebhook.

        List of API HTTP headers for the given webhook-based notification.  # noqa: E501

        :param headers: The headers of this BaseNotificationWebhook.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and headers is None:  # noqa: E501
            raise ValueError("Invalid value for `headers`, must not be `None`")  # noqa: E501

        self._headers = headers

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
        if not isinstance(other, BaseNotificationWebhook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseNotificationWebhook):
            return True

        return self.to_dict() != other.to_dict()