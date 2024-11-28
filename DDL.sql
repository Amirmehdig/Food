USE FoodsDB
GO

-- Drop all foreign key constraints
DECLARE @SQL varchar(4000) = '';
SELECT @SQL = @SQL + 'ALTER TABLE ' + s.name + '.' + t.name + ' DROP CONSTRAINT [' + RTRIM(f.name) + '];' + CHAR(13)
FROM sys.Tables t
INNER JOIN sys.foreign_keys f ON f.parent_object_id = t.object_id
INNER JOIN sys.schemas s ON s.schema_id = f.schema_id;
EXEC(@SQL);


-- Users Table
DROP TABLE IF EXISTS dbo.Users
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    email NVARCHAR(255) UNIQUE NOT NULL,
    password NVARCHAR(255) NOT NULL,
    phone_number NVARCHAR(10),
    address NVARCHAR(MAX),
    registration_date DATE NOT NULL,
    is_active BIT DEFAULT 1,
    role NVARCHAR(50) NOT NULL
);

-- Restaurants Table
DROP TABLE IF EXISTS dbo.Restaurants
CREATE TABLE Restaurants (
    restaurant_id INT PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    address NVARCHAR(MAX),
    phone_number NVARCHAR(10),
    opening_hours NVARCHAR(255),
    rating FLOAT DEFAULT 0,
    is_open BIT DEFAULT 1
);

-- Food Table
DROP TABLE IF EXISTS dbo.Food
CREATE TABLE Food (
    food_id INT PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description NVARCHAR(MAX),
    is_available BIT DEFAULT 1,
    restaurant_id INT,
    rating FLOAT DEFAULT 0,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);

-- OrderHeader Table
DROP TABLE IF EXISTS dbo.OrderHeader
CREATE TABLE OrderHeader (
    order_id INT PRIMARY KEY,
    order_date DATETIME DEFAULT GETDATE(),
    total_amount DECIMAL(10, 2) NOT NULL,
    delivery_time TIME,
    status NVARCHAR(50) NOT NULL,
    user_id INT,
    restaurant_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES Restaurants(restaurant_id)
);

-- OrderDetail Table
DROP TABLE IF EXISTS dbo.OrderDetail
CREATE TABLE OrderDetail (
    order_detail_id INT PRIMARY KEY,
    order_id INT,
    food_id INT,
    quantity INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES OrderHeader(order_id),
    FOREIGN KEY (food_id) REFERENCES Food(food_id)
);

-- Delivery Person Table
DROP TABLE IF EXISTS dbo.DeliveryPerson
CREATE TABLE DeliveryPerson (
    delivery_person_id INT PRIMARY KEY,
    name NVARCHAR(255) NOT NULL,
    phone_number NVARCHAR(10),
    vehicle_type NVARCHAR(50),
    availability_status BIT DEFAULT 1,
    current_order_id INT,
    FOREIGN KEY (current_order_id) REFERENCES OrderHeader(order_id)
);

-- Comments Table
DROP TABLE IF EXISTS dbo.Comments
CREATE TABLE Comments (
    comment_id INT PRIMARY KEY,
    order_id INT UNIQUE,  -- Ensure one comment per order
    rating FLOAT CHECK (rating BETWEEN 1 AND 5), -- Rating between 1 and 5
    comment_text NVARCHAR(MAX),
    comment_date DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (order_id) REFERENCES OrderHeader(order_id)
);

	