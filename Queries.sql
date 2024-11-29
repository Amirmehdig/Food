CREATE OR ALTER PROCEDURE GetCommentsForRestaurant
    @restaurant_id INT
AS
BEGIN
    BEGIN TRY
        IF NOT EXISTS (SELECT 1 FROM Restaurants WHERE restaurant_id = @restaurant_id)
        BEGIN
            PRINT 'Error: Restaurant ID does not exist.';
            RETURN;
        END

        SELECT 
            c.comment_id,
            c.user_id,
            u.name AS user_name,
            c.comment_text,
            c.rating,
            c.comment_date
        FROM 
            Comments c INNER JOIN 
            Users u ON c.user_id = u.user_id INNER JOIN 
            OrderHeader oh ON c.order_id = oh.order_id
        WHERE 
            oh.restaurant_id = @restaurant_id
        ORDER BY 
            c.rating DESC, c.comment_date DESC;

        PRINT 'Query executed successfully.';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO

------------------------------------------------------
CREATE OR ALTER PROCEDURE GetOrdersForUser
    @user_id INT
AS
BEGIN
    BEGIN TRY
        IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = @user_id)
        BEGIN
            PRINT 'Error: User ID does not exist.';
            RETURN;
        END

        SELECT 
            oh.order_id,
            oh.restaurant_id,
            r.name AS restaurant_name,
            oh.order_date,
            oh.total_price,
            oh.status,
            dp.name AS delivery_person_name
        FROM 
            OrderHeader oh INNER JOIN 
            Restaurants r ON oh.restaurant_id = r.restaurant_id LEFT JOIN 
            DeliveryPerson dp ON oh.delivery_person_id = dp.delivery_person_id
        WHERE 
            oh.user_id = @user_id
        ORDER BY 
            oh.order_date DESC;

        PRINT 'Query executed successfully.';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO
