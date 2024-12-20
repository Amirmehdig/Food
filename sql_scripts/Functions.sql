DROP FUNCTION IF EXISTS dbo.GetUserFavoriteFood
GO
CREATE FUNCTION dbo.GetUserFavoriteFood (
    @user_id INT,
    @restaurant_id INT
)
RETURNS NVARCHAR(255)
AS
BEGIN
	DECLARE @favorite_food NVARCHAR(255);
	IF @restaurant_id = -1
	BEGIN 

    SET @favorite_food = (SELECT TOP 1
        f.name AS food_name
    FROM 
        OrderDetail d
    INNER JOIN 
        Food f ON d.food_id = f.food_id
    INNER JOIN 
        OrderHeader h ON d.order_id = h.order_id
    WHERE 
        h.user_id = @user_id
    GROUP BY 
        f.name
    ORDER BY 
        COUNT(d.food_id) DESC);
	END

	ELSE
	BEGIN
    set @favorite_food = (SELECT TOP 1
        f.name AS food_name
    FROM 
        OrderDetail d
    INNER JOIN 
        Food f ON d.food_id = f.food_id
    INNER JOIN 
        OrderHeader h ON d.order_id = h.order_id
    WHERE 
        h.user_id = @user_id
        AND h.restaurant_id = @restaurant_id
    GROUP BY 
        f.name
    ORDER BY 
        COUNT(d.food_id) DESC);

	END;
    RETURN @favorite_food;
END;
GO

DROP FUNCTION IF EXISTS dbo.GetRoyalty
GO
CREATE FUNCTION dbo.GetRoyalty (
	@percentage FLOAT(53)
)
RETURNS CHAR(1)
AS
BEGIN
	DECLARE @res CHAR(1);
	IF @percentage >= .66
	BEGIN
		SET @res = 'A';
	END
	IF @percentage < .66 and @percentage > .33 
	BEGIN
		SET @res = 'B';
	END
	IF @percentage <= .33
	BEGIN
		SET @res = 'C';
	END
	RETURN @res;
END
GO

DROP FUNCTION IF EXISTS dbo.MaskPhoneNumber
GO
CREATE FUNCTION MaskPhoneNumber (
    @phone_number NVARCHAR(10)
)
RETURNS NVARCHAR(10)
AS
BEGIN
	DECLARE @res NVARCHAR(10) = NULL;
    -- Ensure the input is valid
    IF LEN(@phone_number) = 10
    BEGIN
		SET @res = LEFT(@phone_number, 3) + '*****' + RIGHT(@phone_number, 2);
    END
	RETURN @res
END;
GO

DROP FUNCTION IF EXISTS dbo.GetUserFavoriteRestaurant
GO
CREATE FUNCTION GetUserFavoriteRestaurant (
    @user_id INT
)
RETURNS NVARCHAR(255)
AS
BEGIN
    DECLARE @favorite_restaurant NVARCHAR(255);

    SET @favorite_restaurant = (SELECT TOP 1 
        r.name AS restaurant_name
    FROM 
        OrderHeader h
    INNER JOIN 
        Restaurants r ON h.restaurant_id = r.restaurant_id
    WHERE 
        h.user_id = @user_id
    GROUP BY 
        r.name
    ORDER BY 
        COUNT(h.restaurant_id) DESC);

    RETURN @favorite_restaurant;
END;
GO

DROP FUNCTION IF EXISTS dbo.GetDeliveryPersonFavoriteRestaurant 
GO
CREATE FUNCTION dbo.GetDeliveryPersonFavoriteRestaurant (
    @delivery_person_id INT
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
    DECLARE @favorite_restaurant NVARCHAR(MAX);

    SET @favorite_restaurant = (SELECT TOP 1
        r.name AS restaurant_name
    FROM
        OrderHeader oh
    INNER JOIN
        Restaurants r ON oh.restaurant_id = r.restaurant_id
    WHERE
        oh.delivery_person_id = @delivery_person_id
    GROUP BY
        r.name
    ORDER BY
        COUNT(oh.restaurant_id) DESC);

    RETURN @favorite_restaurant;
END;
GO