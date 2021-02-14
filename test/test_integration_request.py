# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.integration_request import IntegrationRequest  # noqa: E501
from talon_one.rest import ApiException

class TestIntegrationRequest(unittest.TestCase):
    """IntegrationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IntegrationRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.integration_request.IntegrationRequest()  # noqa: E501
        if include_optional :
            return IntegrationRequest(
                customer_session = talon_one.models.new_customer_session_v2.NewCustomerSessionV2(
                    profile_id = '0', 
                    coupon_codes = [
                        '0'
                        ], 
                    referral_code = '0', 
                    state = 'open', 
                    cart_items = [
                        talon_one.models.cart_item.CartItem(
                            name = '0', 
                            sku = '0', 
                            quantity = 1, 
                            price = 1.337, 
                            category = '0', 
                            weight = 1.337, 
                            height = 1.337, 
                            width = 1.337, 
                            length = 1.337, 
                            position = 1.337, 
                            attributes = talon_one.models.item_attributes.Item attributes(), )
                        ], 
                    additional_costs = {
                        'key' : talon_one.models.additional_cost.AdditionalCost(
                            price = 1.337, )
                        }, 
                    identifiers = [
                        '0'
                        ], 
                    attributes = talon_one.models.attributes.attributes(), ), 
                response_content = [
                    'customerSession'
                    ]
            )
        else :
            return IntegrationRequest(
                customer_session = talon_one.models.new_customer_session_v2.NewCustomerSessionV2(
                    profile_id = '0', 
                    coupon_codes = [
                        '0'
                        ], 
                    referral_code = '0', 
                    state = 'open', 
                    cart_items = [
                        talon_one.models.cart_item.CartItem(
                            name = '0', 
                            sku = '0', 
                            quantity = 1, 
                            price = 1.337, 
                            category = '0', 
                            weight = 1.337, 
                            height = 1.337, 
                            width = 1.337, 
                            length = 1.337, 
                            position = 1.337, 
                            attributes = talon_one.models.item_attributes.Item attributes(), )
                        ], 
                    additional_costs = {
                        'key' : talon_one.models.additional_cost.AdditionalCost(
                            price = 1.337, )
                        }, 
                    identifiers = [
                        '0'
                        ], 
                    attributes = talon_one.models.attributes.attributes(), ),
        )

    def testIntegrationRequest(self):
        """Test IntegrationRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
