# CustomerProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**integration_id** | **str** | The ID used for this entity in the application system. | 
**created** | **datetime** | The exact moment this entity was created. | 
**attributes** | **object** | Arbitrary properties associated with this item | 
**account_id** | **int** | The ID of the Talon.One account that owns this profile. | 
**closed_sessions** | **int** | The total amount of closed sessions by a customer. A closed session is a successful purchase. | 
**total_sales** | **float** | Sum of all purchases made by this customer | 
**loyalty_memberships** | [**list[LoyaltyMembership]**](LoyaltyMembership.md) | A list of loyalty programs joined by the customer | [optional] 
**last_activity** | **datetime** | Timestamp of the most recent event received from this customer | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

