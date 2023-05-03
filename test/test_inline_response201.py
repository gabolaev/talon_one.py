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
from talon_one.models.inline_response201 import InlineResponse201  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse201(unittest.TestCase):
    """InlineResponse201 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse201
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response201.InlineResponse201()  # noqa: E501
        if include_optional :
            return InlineResponse201(
                total_result_size = 1, 
                data = [
                    talon_one.models.referral.Referral(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        start_date = '2020-11-10T23:00Z', 
                        expiry_date = '2021-11-10T23:00Z', 
                        usage_limit = 1, 
                        campaign_id = 78, 
                        advocate_profile_integration_id = 'URNGV8294NV', 
                        friend_profile_integration_id = 'BZGGC2454PA', 
                        attributes = {"channel":"web"}, 
                        import_id = 4, 
                        code = '27G47Y54VH9L', 
                        usage_counter = 1, 
                        batch_id = 'tqyrgahe', )
                    ]
            )
        else :
            return InlineResponse201(
                total_result_size = 1,
                data = [
                    talon_one.models.referral.Referral(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        start_date = '2020-11-10T23:00Z', 
                        expiry_date = '2021-11-10T23:00Z', 
                        usage_limit = 1, 
                        campaign_id = 78, 
                        advocate_profile_integration_id = 'URNGV8294NV', 
                        friend_profile_integration_id = 'BZGGC2454PA', 
                        attributes = {"channel":"web"}, 
                        import_id = 4, 
                        code = '27G47Y54VH9L', 
                        usage_counter = 1, 
                        batch_id = 'tqyrgahe', )
                    ],
        )

    def testInlineResponse201(self):
        """Test InlineResponse201"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
