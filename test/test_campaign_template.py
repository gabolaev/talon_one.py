# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.campaign_template import CampaignTemplate  # noqa: E501
from talon_one.rest import ApiException

class TestCampaignTemplate(unittest.TestCase):
    """CampaignTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CampaignTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.campaign_template.CampaignTemplate()  # noqa: E501
        if include_optional :
            return CampaignTemplate(
                id = 6, 
                created = '2020-06-10T09:05:27.993483Z', 
                account_id = 3886, 
                user_id = 56, 
                name = '0', 
                description = '0', 
                instructions = '0', 
                campaign_attributes = None, 
                coupon_attributes = None, 
                state = 'draft', 
                active_ruleset_id = 56, 
                tags = [
                    '0'
                    ], 
                features = [
                    'coupons'
                    ], 
                coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                    valid_characters = [A, B, C, D, E, 2, 0], 
                    coupon_pattern = 'SUMMER-####-####', ), 
                referral_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                    valid_characters = [A, B, C, D, E, 2, 0], 
                    coupon_pattern = 'SUMMER-####-####', ), 
                limits = [
                    talon_one.models.template_limit_config.TemplateLimitConfig(
                        action = 'createCoupon', 
                        limit = 1000.0, 
                        period = 'yearly', 
                        entities = [Coupon], )
                    ], 
                template_params = [
                    talon_one.models.campaign_template_params.CampaignTemplateParams(
                        name = '0', 
                        type = 'string', 
                        description = '0', 
                        attribute_id = 42, )
                    ], 
                applications_ids = [
                    56
                    ], 
                campaign_collections = [
                    talon_one.models.campaign_template_collection.CampaignTemplateCollection(
                        name = 'My collection', 
                        description = 'My collection of SKUs', )
                    ], 
                default_campaign_group_id = 42, 
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_by = '0', 
                valid_application_ids = [
                    56
                    ]
            )
        else :
            return CampaignTemplate(
                id = 6,
                created = '2020-06-10T09:05:27.993483Z',
                account_id = 3886,
                user_id = 56,
                name = '0',
                description = '0',
                instructions = '0',
                state = 'draft',
                applications_ids = [
                    56
                    ],
                valid_application_ids = [
                    56
                    ],
        )

    def testCampaignTemplate(self):
        """Test CampaignTemplate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()