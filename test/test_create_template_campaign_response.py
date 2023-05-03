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
from talon_one.models.create_template_campaign_response import CreateTemplateCampaignResponse  # noqa: E501
from talon_one.rest import ApiException

class TestCreateTemplateCampaignResponse(unittest.TestCase):
    """CreateTemplateCampaignResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTemplateCampaignResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.create_template_campaign_response.CreateTemplateCampaignResponse()  # noqa: E501
        if include_optional :
            return CreateTemplateCampaignResponse(
                campaign = talon_one.models.campaign.Campaign(
                    id = 4, 
                    created = '2020-06-10T09:05:27.993483Z', 
                    application_id = 322, 
                    user_id = 388, 
                    name = 'Summer promotions', 
                    description = 'Campaign for all summer 2021 promotions', 
                    start_time = '2021-07-20T22:00Z', 
                    end_time = '2021-09-22T22:00Z', 
                    attributes = talon_one.models.attributes.attributes(), 
                    state = 'enabled', 
                    active_ruleset_id = 6, 
                    tags = [summer], 
                    features = [coupons, referrals], 
                    coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                        valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        coupon_pattern = 'SUMMER-####-####', ), 
                    referral_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                        valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        coupon_pattern = 'SUMMER-####-####', ), 
                    limits = [
                        talon_one.models.limit_config.LimitConfig(
                            action = 'createCoupon', 
                            limit = 1000.0, 
                            period = 'yearly', 
                            entities = [Coupon], )
                        ], 
                    campaign_groups = [1, 3], 
                    coupon_redemption_count = 163, 
                    referral_redemption_count = 3, 
                    discount_count = 288.0, 
                    discount_effect_count = 343, 
                    coupon_creation_count = 16, 
                    custom_effect_count = 0, 
                    referral_creation_count = 8, 
                    add_free_item_effect_count = 0, 
                    awarded_giveaways_count = 9, 
                    created_loyalty_points_count = 9.0, 
                    created_loyalty_points_effect_count = 2, 
                    redeemed_loyalty_points_count = 8.0, 
                    redeemed_loyalty_points_effect_count = 9, 
                    call_api_effect_count = 0, 
                    reservecoupon_effect_count = 9, 
                    last_activity = '2022-11-10T23:00Z', 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by = 'John Doe', 
                    updated_by = 'Jane Doe', 
                    template_id = 3, ), 
                ruleset = talon_one.models.ruleset.Ruleset(
                    id = 6, 
                    created = '2020-06-10T09:05:27.993483Z', 
                    user_id = 388, 
                    rules = [
                        talon_one.models.rule.Rule(
                            id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            parent_id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            title = 'Give discount via coupon', 
                            description = 'Creates a discount when a coupon is valid', 
                            bindings = [
                                talon_one.models.binding.Binding(
                                    name = 'my property', 
                                    type = 'templateParameter', 
                                    expression = [
                                        None
                                        ], 
                                    value_type = 'string', )
                                ], 
                            condition = [and, [couponValid]], 
                            effects = [catch, [noop], [setDiscount, 10% off, [*, [., Session, Total], [/, 10, 100]]]], )
                        ], 
                    strikethrough_rules = [
                        talon_one.models.rule.Rule(
                            id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            parent_id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            title = 'Give discount via coupon', 
                            description = 'Creates a discount when a coupon is valid', 
                            condition = [and, [couponValid]], 
                            effects = [catch, [noop], [setDiscount, 10% off, [*, [., Session, Total], [/, 10, 100]]]], )
                        ], 
                    bindings = [], 
                    rb_version = 'v2', 
                    activate = True, 
                    campaign_id = 320, 
                    template_id = 3, 
                    activated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                collections = [
                    talon_one.models.collection.Collection(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        account_id = 3886, 
                        modified = '2021-09-12T10:12:42Z', 
                        description = 'My collection of SKUs', 
                        subscribed_applications_ids = [1, 2, 3], 
                        name = 'My collection', 
                        modified_by = 48, 
                        created_by = 134, 
                        application_id = 1, 
                        campaign_id = 7, 
                        payload = [KTL-WH-ET-1, KTL-BL-ET-1], )
                    ]
            )
        else :
            return CreateTemplateCampaignResponse(
                campaign = talon_one.models.campaign.Campaign(
                    id = 4, 
                    created = '2020-06-10T09:05:27.993483Z', 
                    application_id = 322, 
                    user_id = 388, 
                    name = 'Summer promotions', 
                    description = 'Campaign for all summer 2021 promotions', 
                    start_time = '2021-07-20T22:00Z', 
                    end_time = '2021-09-22T22:00Z', 
                    attributes = talon_one.models.attributes.attributes(), 
                    state = 'enabled', 
                    active_ruleset_id = 6, 
                    tags = [summer], 
                    features = [coupons, referrals], 
                    coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                        valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        coupon_pattern = 'SUMMER-####-####', ), 
                    referral_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                        valid_characters = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                        coupon_pattern = 'SUMMER-####-####', ), 
                    limits = [
                        talon_one.models.limit_config.LimitConfig(
                            action = 'createCoupon', 
                            limit = 1000.0, 
                            period = 'yearly', 
                            entities = [Coupon], )
                        ], 
                    campaign_groups = [1, 3], 
                    coupon_redemption_count = 163, 
                    referral_redemption_count = 3, 
                    discount_count = 288.0, 
                    discount_effect_count = 343, 
                    coupon_creation_count = 16, 
                    custom_effect_count = 0, 
                    referral_creation_count = 8, 
                    add_free_item_effect_count = 0, 
                    awarded_giveaways_count = 9, 
                    created_loyalty_points_count = 9.0, 
                    created_loyalty_points_effect_count = 2, 
                    redeemed_loyalty_points_count = 8.0, 
                    redeemed_loyalty_points_effect_count = 9, 
                    call_api_effect_count = 0, 
                    reservecoupon_effect_count = 9, 
                    last_activity = '2022-11-10T23:00Z', 
                    updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    created_by = 'John Doe', 
                    updated_by = 'Jane Doe', 
                    template_id = 3, ),
                ruleset = talon_one.models.ruleset.Ruleset(
                    id = 6, 
                    created = '2020-06-10T09:05:27.993483Z', 
                    user_id = 388, 
                    rules = [
                        talon_one.models.rule.Rule(
                            id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            parent_id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            title = 'Give discount via coupon', 
                            description = 'Creates a discount when a coupon is valid', 
                            bindings = [
                                talon_one.models.binding.Binding(
                                    name = 'my property', 
                                    type = 'templateParameter', 
                                    expression = [
                                        None
                                        ], 
                                    value_type = 'string', )
                                ], 
                            condition = [and, [couponValid]], 
                            effects = [catch, [noop], [setDiscount, 10% off, [*, [., Session, Total], [/, 10, 100]]]], )
                        ], 
                    strikethrough_rules = [
                        talon_one.models.rule.Rule(
                            id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            parent_id = '7fa800a8-ac8d-4792-85dc-c4650dcc8f23', 
                            title = 'Give discount via coupon', 
                            description = 'Creates a discount when a coupon is valid', 
                            condition = [and, [couponValid]], 
                            effects = [catch, [noop], [setDiscount, 10% off, [*, [., Session, Total], [/, 10, 100]]]], )
                        ], 
                    bindings = [], 
                    rb_version = 'v2', 
                    activate = True, 
                    campaign_id = 320, 
                    template_id = 3, 
                    activated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
        )

    def testCreateTemplateCampaignResponse(self):
        """Test CreateTemplateCampaignResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
