USE FoodsDB
GO

-- Drop trigger if exists
IF OBJECT_ID('trg_UpdateRestaurantRating', 'TR') IS NOT NULL
    DROP TRIGGER trg_UpdateRestaurantRating;
GO


CREATE TRIGGER trg_UpdateRestaurantRating
ON Comments
AFTER INSERT, UPDATE
AS
BEGIN
    SET NOCOUNT ON;

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
END;
