# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.application_customer import ApplicationCustomer  # noqa: E501
from talon_one.rest import ApiException

class TestApplicationCustomer(unittest.TestCase):
    """ApplicationCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationCustomer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.application_customer.ApplicationCustomer()  # noqa: E501
        if include_optional :
            return ApplicationCustomer(
                id = 56, 
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                integration_id = '0', 
                attributes = {"Language":"english","ShippingCountry":"DE"}, 
                account_id = 56, 
                closed_sessions = 3, 
                total_sales = 299.99, 
                loyalty_memberships = [
                    talon_one.models.loyalty_membership.LoyaltyMembership(
                        joined = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        loyalty_program_id = 323414846, )
                    ], 
                audience_memberships = [
                    talon_one.models.audience_membership.AudienceMembership(
                        id = 2, 
                        name = 'Travel audience', )
                    ], 
                last_activity = '2020-02-08T14:15:20Z', 
                sandbox = False, 
                advocate_integration_id = '0'
            )
        else :
            return ApplicationCustomer(
                id = 56,
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                integration_id = '0',
                attributes = {"Language":"english","ShippingCountry":"DE"},
                account_id = 56,
                closed_sessions = 3,
                total_sales = 299.99,
                last_activity = '2020-02-08T14:15:20Z',
        )

    def testApplicationCustomer(self):
        """Test ApplicationCustomer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
