DROP VIEW IF EXISTS dbo.vRestaurantCustomers
GO
CREATE VIEW dbo.vRestaurantCustomers
AS
SELECT
	r.restaurant_id,
	r.name,
	h.user_id,
	dbo.MaskPhoneNumber(u.[phone_number]) phone_number,
	SUM(h.[total_amount]) total,
	COUNT(h.order_id) total_order,
	dbo.GetRoyalty(PERCENT_RANK() OVER (PARTITION BY r.restaurant_id ORDER BY SUM(h.[total_amount]))) loyalty,
	dbo.GetUserFavoriteFood(h.user_id, r.restaurant_id) favorite_food
FROM 
	Restaurants r
INNER JOIN
	OrderHeader h ON r.restaurant_id = h.restaurant_id
INNER JOIN
	Users u ON h.user_id = u.user_id 
GROUP BY
	r.restaurant_id,
	r.name,
	h.user_id, 
	u.phone_number
GO

DROP VIEW IF EXISTS dbo.vCustomers
GO
CREATE VIEW dbo.vCustomers
AS
SELECT
	u.user_id,
	u.name, 
	dbo.MaskPhoneNumber(u.phone_number) phone_number,
	dbo.GetUserFavoriteFood(u.user_id, -1) favorite_food, 
	dbo.GetUserFavoriteRestaurant(u.user_id) favorite_restaurant,
	SUM(h.[total_amount]) total_amount,
	COUNT(h.order_id) total_order 
FROM
	Users u
LEFT OUTER JOIN 
	OrderHeader h on u.user_id = h.user_id
GROUP BY 
	u.user_id,
	u.name,
	u.phone_number
GO

DROP VIEW IF EXISTS dbo.vDeliveryPersonSummary
GO
CREATE VIEW dbo.vDeliveryPersonSummary
AS
SELECT 
	d.delivery_person_id,
	d.name,
	dbo.MaskPhoneNumber(d.phone_number) phone_number,
	dbo.GetDeliveryPersonFavoriteRestaurant(d.delivery_person_id) most_serviced_restaurant,
	COUNT(h.order_id) total_order_delivered,
	dbo.GetRoyalty(PERCENT_RANK() OVER (ORDER BY COUNT(h.order_id))) loyalty
FROM 
	DeliveryPerson d 
INNER JOIN
	OrderHeader h on d.delivery_person_id = h.delivery_person_id
GROUP BY 
	d.delivery_person_id,
	d.name, 
	d.phone_number
GO