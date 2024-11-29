CREATE OR ALTER PROCEDURE InsertUser
    @name NVARCHAR(255),
    @email NVARCHAR(255),
    @password NVARCHAR(255),
    @phone_number NVARCHAR(10) = NULL,
    @address NVARCHAR(MAX) = NULL,
    @registration_date DATETIME,
    @is_active BIT = 1,
    @role NVARCHAR(50)
AS
BEGIN
    BEGIN TRY
        INSERT INTO Users (name, email, password, phone_number, address, registration_date, is_active, role)
        VALUES (@name, @email, @password, @phone_number, @address, @registration_date, @is_active, @role);
        
        PRINT 'User inserted successfully';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO

--------------------------------------------------
CREATE OR ALTER PROCEDURE InsertRestaurant
    @name NVARCHAR(255),
    @address NVARCHAR(MAX),
    @phone_number NVARCHAR(10) = NULL,
    @opening_hours NVARCHAR(255)
AS
BEGIN
    BEGIN TRY
        INSERT INTO Restaurants (name, address, phone_number, opening_hours)
        VALUES (@name, @address, @phone_number, @opening_hours);
        
        PRINT 'Restaurant inserted successfully';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO

--------------------------------------------------
CREATE OR ALTER PROCEDURE InsertFood
    @name NVARCHAR(255),
    @description NVARCHAR(MAX) = NULL,
    @price DECIMAL(10, 2),
    @restaurant_id INT,
    @availability BIT = 1
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Restaurants WHERE restaurant_id = @restaurant_id)
    BEGIN
        PRINT 'Error: Restaurant ID does not exist in Restaurants table.';
        RETURN;
    END

    BEGIN TRY
        INSERT INTO Food (name, description, price, restaurant_id, is_available)
        VALUES (@name, @description, @price, @restaurant_id, @availability);
        
        PRINT 'Food item inserted successfully';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO

--------------------------------------------------
CREATE OR ALTER PROCEDURE InsertDeliveryPerson
    @name NVARCHAR(255),
    @phone_number NVARCHAR(10),
    @is_available BIT = 1
AS
BEGIN
    BEGIN TRY
        INSERT INTO DeliveryPerson (name, phone_number, availability_status)
        VALUES (@name, @phone_number, @is_available);
        
        PRINT 'Delivery person inserted successfully';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO

--------------------------------------------------
CREATE OR ALTER PROCEDURE InsertOrderHeader
    @user_id INT,
    @restaurant_id INT,
    @order_date DATETIME,
    @total_price DECIMAL(10, 2),
    @delivery_person_id INT = NULL,
    @status NVARCHAR(50)
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = @user_id)
    BEGIN
        PRINT 'Error: User ID does not exist in Users table.';
        RETURN;
    END

    IF NOT EXISTS (SELECT 1 FROM Restaurants WHERE restaurant_id = @restaurant_id)
    BEGIN
        PRINT 'Error: Restaurant ID does not exist in Restaurants table.';
        RETURN;
    END

    IF @delivery_person_id IS NOT NULL AND NOT EXISTS (SELECT 1 FROM DeliveryPerson WHERE delivery_person_id = @delivery_person_id)
    BEGIN
        PRINT 'Error: Delivery person ID does not exist in DeliveryPerson table.';
        RETURN;
    END

    BEGIN TRY
        INSERT INTO OrderHeader (user_id, restaurant_id, order_date, total_amount, delivery_person_id, status)
        VALUES (@user_id, @restaurant_id, @order_date, @total_price, @delivery_person_id, @status);
        
        PRINT 'Order header inserted successfully';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO

--------------------------------------------------
CREATE OR ALTER PROCEDURE InsertOrderDetail
    @order_id INT,
    @food_id INT,
    @quantity INT,
    @price DECIMAL(10, 2)
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM OrderHeader WHERE order_id = @order_id)
    BEGIN
        PRINT 'Error: Order ID does not exist in OrderHeader table.';
        RETURN;
    END

    IF NOT EXISTS (SELECT 1 FROM Food WHERE food_id = @food_id)
    BEGIN
        PRINT 'Error: Food ID does not exist in Food table.';
        RETURN;
    END

    BEGIN TRY
        INSERT INTO OrderDetail (order_id, food_id, quantity, subtotal)
        VALUES (@order_id, @food_id, @quantity, @price);
        
        PRINT 'Order detail inserted successfully';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO

--------------------------------------------------
CREATE OR ALTER PROCEDURE InsertComment
    @user_id INT,
    @order_id INT,
    @comment_text NVARCHAR(MAX),
    @rating INT,
    @comment_date DATETIME
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = @user_id)
    BEGIN
        PRINT 'Error: User ID does not exist in Users table.';
        RETURN;
    END

    IF NOT EXISTS (SELECT 1 FROM OrderHeader WHERE order_id = @order_id)
    BEGIN
        PRINT 'Error: Order ID does not exist in OrderHeader table.';
        RETURN;
    END

    BEGIN TRY
        INSERT INTO Comments (order_id, comment_text, rating, comment_date)
        VALUES (@order_id, @comment_text, @rating, @comment_date);
        
        PRINT 'Comment inserted successfully';
    END TRY
    BEGIN CATCH
        PRINT 'Error: ' + ERROR_MESSAGE();
    END CATCH
END
GO
