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
from talon_one.models.inline_response2003 import InlineResponse2003  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse2003(unittest.TestCase):
    """InlineResponse2003 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse2003
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response2003.InlineResponse2003()  # noqa: E501
        if include_optional :
            return InlineResponse2003(
                total_result_size = 1, 
                data = [
                    talon_one.models.application.Application(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        modified = '2021-09-12T10:12:42Z', 
                        account_id = 3886, 
                        name = 'My Application', 
                        description = 'A test Application', 
                        timezone = 'Europe/Berlin', 
                        currency = 'EUR', 
                        case_sensitivity = 'sensitive', 
                        attributes = talon_one.models.attributes.attributes(), 
                        limits = [
                            talon_one.models.limit_config.LimitConfig(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                period = 'yearly', 
                                entities = [Coupon], )
                            ], 
                        campaign_priority = 'universal', 
                        exclusive_campaigns_strategy = 'listOrder', 
                        default_discount_scope = 'sessionTotal', 
                        enable_cascading_discounts = True, 
                        enable_flattened_cart_items = True, 
                        attributes_settings = talon_one.models.attributes_settings.AttributesSettings(
                            mandatory = talon_one.models.attributes_mandatory.AttributesMandatory(
                                campaigns = [
                                    '0'
                                    ], 
                                coupons = [
                                    '0'
                                    ], ), ), 
                        sandbox = True, 
                        enable_partial_discounts = False, 
                        default_discount_additional_cost_per_item_scope = 'price', 
                        loyalty_programs = [
                            talon_one.models.loyalty_program.LoyaltyProgram(
                                id = 56, 
                                created = '2020-06-10T09:05:27.993483Z', 
                                title = 'Point collection', 
                                description = 'Customers collect 10 points per 1$ spent', 
                                subscribed_applications = [132, 97], 
                                default_validity = '2W_U', 
                                default_pending = 'immediate', 
                                allow_subledger = False, 
                                users_per_card_limit = 111, 
                                sandbox = True, 
                                account_id = 1, 
                                name = 'my_program', 
                                tiers = [{name=Gold, minPoints=300, id=3, created=2021-06-10T09:05:27.993483Z, programID=139}, {name=Silver, minPoints=200, id=2, created=2021-06-10T09:04:59.355258Z, programId=139}, {name=Bronze, minPoints=100, id=1, created=2021-06-10T09:04:39.355258Z, programId=139}], 
                                timezone = 'Europe/Berlin', 
                                card_based = True, )
                            ], )
                    ]
            )
        else :
            return InlineResponse2003(
                total_result_size = 1,
                data = [
                    talon_one.models.application.Application(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        modified = '2021-09-12T10:12:42Z', 
                        account_id = 3886, 
                        name = 'My Application', 
                        description = 'A test Application', 
                        timezone = 'Europe/Berlin', 
                        currency = 'EUR', 
                        case_sensitivity = 'sensitive', 
                        attributes = talon_one.models.attributes.attributes(), 
                        limits = [
                            talon_one.models.limit_config.LimitConfig(
                                action = 'createCoupon', 
                                limit = 1000.0, 
                                period = 'yearly', 
                                entities = [Coupon], )
                            ], 
                        campaign_priority = 'universal', 
                        exclusive_campaigns_strategy = 'listOrder', 
                        default_discount_scope = 'sessionTotal', 
                        enable_cascading_discounts = True, 
                        enable_flattened_cart_items = True, 
                        attributes_settings = talon_one.models.attributes_settings.AttributesSettings(
                            mandatory = talon_one.models.attributes_mandatory.AttributesMandatory(
                                campaigns = [
                                    '0'
                                    ], 
                                coupons = [
                                    '0'
                                    ], ), ), 
                        sandbox = True, 
                        enable_partial_discounts = False, 
                        default_discount_additional_cost_per_item_scope = 'price', 
                        loyalty_programs = [
                            talon_one.models.loyalty_program.LoyaltyProgram(
                                id = 56, 
                                created = '2020-06-10T09:05:27.993483Z', 
                                title = 'Point collection', 
                                description = 'Customers collect 10 points per 1$ spent', 
                                subscribed_applications = [132, 97], 
                                default_validity = '2W_U', 
                                default_pending = 'immediate', 
                                allow_subledger = False, 
                                users_per_card_limit = 111, 
                                sandbox = True, 
                                account_id = 1, 
                                name = 'my_program', 
                                tiers = [{name=Gold, minPoints=300, id=3, created=2021-06-10T09:05:27.993483Z, programID=139}, {name=Silver, minPoints=200, id=2, created=2021-06-10T09:04:59.355258Z, programId=139}, {name=Bronze, minPoints=100, id=1, created=2021-06-10T09:04:39.355258Z, programId=139}], 
                                timezone = 'Europe/Berlin', 
                                card_based = True, )
                            ], )
                    ],
        )

    def testInlineResponse2003(self):
        """Test InlineResponse2003"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
