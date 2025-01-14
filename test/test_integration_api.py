# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you access the Campaign Manager at `https://yourbaseurl.talon.one/`, the URL for the [updateCustomerSessionV2](https://docs.talon.one/integration-api#operation/updateCustomerSessionV2) endpoint is `https://yourbaseurl.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import talon_one
import os
from talon_one.api.integration_api import IntegrationApi  # noqa: E501
from talon_one.rest import ApiException
from pprint import pprint


class TestIntegrationApi(unittest.TestCase):
    """IntegrationApi unit test stubs"""

    def setUp(self):
        configuration = talon_one.Configuration(
            host = "http://host.docker.internal:9000",
            api_key_prefix = {
                "Authorization": "ApiKey-v1"
            },
            api_key = {
                "Authorization": os.getenv("IAPI_KEY")
            }
        )
        self.api = talon_one.api.IntegrationApi(talon_one.ApiClient(configuration))  # noqa: E501

    def tearDown(self):
        pass

    def test_create_audience_v2(self):
        """Test case for create_audience_v2

        Create audience  # noqa: E501
        """
        pass

    def test_create_coupon_reservation(self):
        """Test case for create_coupon_reservation

        Create coupon reservation  # noqa: E501
        """
        pass

    def test_create_referral(self):
        """Test case for create_referral

        Create referral code for an advocate  # noqa: E501
        """
        pass

    def test_create_referrals_for_multiple_advocates(self):
        """Test case for create_referrals_for_multiple_advocates

        Create referral codes for multiple advocates  # noqa: E501
        """
        pass

    def test_delete_audience_memberships_v2(self):
        """Test case for delete_audience_memberships_v2

        Delete audience memberships  # noqa: E501
        """
        pass

    def test_delete_audience_v2(self):
        """Test case for delete_audience_v2

        Delete audience  # noqa: E501
        """
        pass

    def test_delete_coupon_reservation(self):
        """Test case for delete_coupon_reservation

        Delete coupon reservations  # noqa: E501
        """
        pass

    def test_delete_customer_data(self):
        """Test case for delete_customer_data

        Delete customer's personal data  # noqa: E501
        """
        pass

    def test_get_customer_inventory(self):
        """Test case for get_customer_inventory

        List customer data  # noqa: E501
        """
        pass

    def test_get_customer_session(self):
        """Test case for get_customer_session

        Get customer session  # noqa: E501
        """
        try:
            customer_session_id = 'test_session_id'
            session = self.api.get_customer_session(customer_session_id)
            pprint(session)
            pass
        except ApiException as e:
            print("Exception when calling IntegrationApi->get_customer_session: %s\n" % e)

    def test_get_loyalty_balances(self):
        """Test case for get_loyalty_balances

        Get customer's loyalty points  # noqa: E501
        """
        pass

    def test_get_loyalty_card_balances(self):
        """Test case for get_loyalty_card_balances

        Get card's point balances  # noqa: E501
        """
        pass

    def test_get_loyalty_card_transactions(self):
        """Test case for get_loyalty_card_transactions

        List card's transactions  # noqa: E501
        """
        pass

    def test_get_loyalty_program_profile_transactions(self):
        """Test case for get_loyalty_program_profile_transactions

        List customer's loyalty transactions  # noqa: E501
        """
        pass

    def test_get_reserved_customers(self):
        """Test case for get_reserved_customers

        List customers that have this coupon reserved  # noqa: E501
        """
        pass

    def test_link_loyalty_card_to_profile(self):
        """Test case for link_loyalty_card_to_profile

        Link customer profile to card  # noqa: E501
        """
        pass

    def test_reopen_customer_session(self):
        api_response = self.api.reopen_customer_session("customer_session_py_4_1")
        pprint(api_response)
        pass

    def test_return_cart_items(self):
        """Test case for return_cart_items

        Return cart items  # noqa: E501
        """
        pass

    def test_sync_catalog(self):
        """Test case for sync_catalog

        Sync cart item catalog  # noqa: E501
        """
        pass

    def test_track_event(self):
        """Test case for track_event

        Track event  # noqa: E501
        """
        pass

    def test_track_event_v2(self):
        """Test case for track_event_v2

        Track event V2  # noqa: E501
        """
        pass

    def test_update_audience_customers_attributes(self):
        """Test case for update_audience_customers_attributes

        Update profile attributes for all customers in audience  # noqa: E501
        """
        pass

    def test_update_audience_v2(self):
        """Test case for update_audience_v2

        Update audience name  # noqa: E501
        """
        pass

    def test_update_customer_profile_audiences(self):
        """Test case for update_customer_profile_audiences

        Update multiple customer profiles' audiences  # noqa: E501
        """
        pass

    def test_update_customer_profile_v2(self):
        """Test case for update_customer_profile_v2

        Update customer profile  # noqa: E501
        """
        pass

    def test_update_customer_profiles_v2(self):
        """Test case for update_customer_profiles_v2

        Update multiple customer profiles  # noqa: E501
        """
        pass

    def test_update_customer_session_v2(self):
        # Preparing a NewCustomerSessionV2 object
        customer_session = talon_one.NewCustomerSessionV2(
        profile_id="PROFILE_ID_py_4",
        state="closed",
        )
        customer_session.cart_items = [
            talon_one.CartItem(name="Red Spring Blouse",
                            sku="rdbs-1111",
                            quantity=1,
                            price=49.4,
                            category="Shirts"),
            talon_one.CartItem(name="Denim Trousers",
                            sku="dtr-2222",
                            quantity=1,
                            price=74.3,
                            category="Trousers"),
        ]
        customer_session.coupon_codes = [
            "Cool_Stuff"
        ]

        # Instantiating a new IntegrationRequest object
        integration_request = talon_one.IntegrationRequest(
            customer_session,
            # Optional list of requested information to be present on the response.
            # See models/integration_request.py for full list
            # ["customerSession", "loyalty"]
        )

        try:
            # Create/update a customer session using `update_customer_session_v2` function
            api_response = self.api.update_customer_session_v2("customer_session_py_4_1", integration_request)
            pprint(api_response)

            # Parsing the returned effects list, please consult https://developers.talon.one/Integration-API/handling-effects-v2 for the full list of effects and their corresponding properties
            for effect in api_response.effects:
                if effect.effect_type == "setDiscount":
                    # Initiating right props instance according to the effect type
                    setDiscountProps = self.api.api_client.deserialize_model(effect.props, talon_one.SetDiscountEffectProps)

                    # Access the specific effect's properties
                    print("Set a discount '{name}' of {value}".format(
                        name = setDiscountProps.name,
                        value = setDiscountProps.value
                    ))
                elif effect.effect_type == "rejectCoupon":
                    rejectCouponEffectProps = self.api.api_client.deserialize_model(effect.props, talon_one.RejectCouponEffectProps)

                    # Work with AcceptCouponEffectProps' properties
                    # ...
        except ApiException as e:
            print("Exception when calling IntegrationApi->update_customer_session_v2: %s\n" % e)
        pass


if __name__ == '__main__':
    unittest.main()
