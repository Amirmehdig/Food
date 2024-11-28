CREATE PROCEDURE InsertUser
    @user_id INT,
    @name NVARCHAR(255),
    @email NVARCHAR(255),
    @password NVARCHAR(255),
    @phone_number NVARCHAR(10),
    @address NVARCHAR(MAX),
    @registration_date DATE,
    @is_active BIT,
    @role NVARCHAR(50)
AS
BEGIN
    BEGIN TRY
        INSERT INTO Users (user_id, name, email, password, phone_number, address, registration_date, is_active, role)
        VALUES (@user_id, @name, @email, @password, @phone_number, @address, @registration_date, @is_active, @role);
        
        PRINT 'User inserted successfully.';
    END TRY
    BEGIN CATCH
        PRINT 'Error inserting user: ' + ERROR_MESSAGE();
    END CATCH
END;

CREATE PROCEDURE InsertRestaurant
    @restaurant_id INT,
    @name NVARCHAR(255),
    @address NVARCHAR(MAX),
    @phone_number NVARCHAR(10),
    @opening_hours NVARCHAR(255),
    @rating FLOAT,
    @is_active BIT
AS
BEGIN
    BEGIN TRY
        INSERT INTO Restaurants (restaurant_id, name, address, phone_number, opening_hours, rating, is_active)
        VALUES (@restaurant_id, @name, @address, @phone_number, @opening_hours, @rating, @is_active);
        
        PRINT 'Restaurant inserted successfully.';
    END TRY
    BEGIN CATCH
        PRINT 'Error inserting restaurant: ' + ERROR_MESSAGE();
    END CATCH
END;

CREATE PROCEDURE InsertOrder
    @order_id INT,
    @user_id INT,
    @restaurant_id INT,
    @order_date DATETIME,
    @status NVARCHAR(50),
    @total_amount FLOAT
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = @user_id)
    BEGIN
        PRINT 'Error: User does not exist.';
        RETURN;
    END
    IF NOT EXISTS (SELECT 1 FROM Restaurants WHERE restaurant_id = @restaurant_id)
    BEGIN
        PRINT 'Error: Restaurant does not exist.';
        RETURN;
    END

    BEGIN TRY
        INSERT INTO Orders (order_id, user_id, restaurant_id, order_date, status, total_amount)
        VALUES (@order_id, @user_id, @restaurant_id, @order_date, @status, @total_amount);
        
        PRINT 'Order inserted successfully.';
    END TRY
    BEGIN CATCH
        PRINT 'Error inserting order: ' + ERROR_MESSAGE();
    END CATCH
END;

CREATE PROCEDURE InsertMenuItem
    @menu_item_id INT,
    @restaurant_id INT,
    @name NVARCHAR(255),
    @description NVARCHAR(MAX),
    @price FLOAT,
    @is_available BIT
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Restaurants WHERE restaurant_id = @restaurant_id)
    BEGIN
        PRINT 'Error: Restaurant does not exist.';
        RETURN;
    END

    BEGIN TRY
        INSERT INTO MenuItems (menu_item_id, restaurant_id, name, description, price, is_available)
        VALUES (@menu_item_id, @restaurant_id, @name, @description, @price, @is_available);
        
        PRINT 'Menu item inserted successfully.';
    END TRY
    BEGIN CATCH
        PRINT 'Error inserting menu item: ' + ERROR_MESSAGE();
    END CATCH
END;

CREATE PROCEDURE InsertOrderDetail
    @order_detail_id INT,
    @order_id INT,
    @menu_item_id INT,
    @quantity INT,
    @price FLOAT
AS
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Orders WHERE order_id = @order_id)
    BEGIN
        PRINT 'Error: Order does not exist.';
        RETURN;
    END
    IF NOT EXISTS (SELECT 1 FROM MenuItems WHERE menu_item_id = @menu_item_id)
    BEGIN
        PRINT 'Error: Menu item does not exist.';
        RETURN;
    END

    BEGIN TRY
        INSERT INTO OrderDetails (order_detail_id, order_id, menu_item_id, quantity, price)
        VALUES (@order_detail_id, @order_id, @menu_item_id, @quantity, @price);
        
        PRINT 'Order detail inserted successfully.';
    END TRY
    BEGIN CATCH
        PRINT 'Error inserting order detail: ' + ERROR_MESSAGE();
    END CATCH
END;
