USE FoodsDB
GO

IF OBJECT_ID('trg_UpdateRatings', 'TR') IS NOT NULL
    DROP TRIGGER trg_UpdateRatings;
GO

CREATE TRIGGER trg_UpdateRatings
ON Comments
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    -- Update the average rating for the restaurant
    UPDATE Restaurants
    SET rating = (
        SELECT AVG(CAST(c.rating AS FLOAT))
        FROM Comments c
        INNER JOIN OrderHeader o ON c.order_id = o.order_id
        WHERE o.restaurant_id = Restaurants.restaurant_id
    )
    FROM Restaurants
    INNER JOIN OrderHeader o ON Restaurants.restaurant_id = o.restaurant_id
    INNER JOIN inserted i ON o.order_id = i.order_id;

    -- Update the average rating for all food items in the order
    UPDATE Food
    SET rating = (
        SELECT AVG(CAST(c.rating AS FLOAT))
        FROM Comments c
        INNER JOIN OrderDetail od ON c.order_id = od.order_id
        WHERE od.food_id = Food.food_id
    )
    FROM Food
    WHERE food_id IN (
        SELECT od.food_id
        FROM OrderDetail od
        INNER JOIN inserted i ON od.order_id = i.order_id
    );
END;
GO




IF OBJECT_ID('trg_AdjustFoodAvailability', 'TR') IS NOT NULL
    DROP TRIGGER trg_AdjustFoodAvailability;
GO

CREATE TRIGGER trg_AdjustFoodAvailability
ON OrderDetail
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;

    -- Decrement the available_count for each food item in the new order
    UPDATE Food
    SET available_count = available_count - i.quantity
    FROM Food
    INNER JOIN inserted i ON Food.food_id = i.food_id;

    -- Set is_available to 0 if available_count reaches 0
    UPDATE Food
    SET is_available = 0
    WHERE food_id IN (
        SELECT food_id
        FROM Food
        WHERE available_count <= 0
    );
END;
GO




IF OBJECT_ID('trg_PreventRestaurantDeletion', 'TR') IS NOT NULL
    DROP TRIGGER trg_PreventRestaurantDeletion;
GO

CREATE TRIGGER trg_PreventRestaurantDeletion
ON Restaurants
INSTEAD OF DELETE
AS
BEGIN
    SET NOCOUNT ON;

    -- Check if there are active orders for the restaurant being deleted
    IF EXISTS (
        SELECT 1
        FROM deleted d
        INNER JOIN OrderHeader o ON d.restaurant_id = o.restaurant_id
        WHERE o.status IN ('Pending', 'Processing') -- Modify statuses as per your system
    )
    BEGIN
        RAISERROR ('Cannot delete a restaurant with active orders.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END;

    -- Proceed with the deletion if no active orders
    DELETE FROM Restaurants
    WHERE restaurant_id IN (SELECT restaurant_id FROM deleted);
END;
GO
