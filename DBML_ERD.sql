TABLE Users {
    user_id INT [primary key]
    name NVARCHAR(255) 
    email NVARCHAR(255) UNIQUE 
    password NVARCHAR(255) 
    phone_number NVARCHAR(10)
    address NVARCHAR(MAX)
    registration_date DATETIME 
    is_active BIT 
    role NVARCHAR(50) 
}

TABLE Restaurants {
    restaurant_id INT [primary key]
    name NVARCHAR(255) 
    address NVARCHAR(MAX)
    phone_number NVARCHAR(10)
    opening_hours NVARCHAR(255)
    rating FLOAT 
    is_open BIT 
}

TABLE Food {
    food_id INT [primary key]
    name NVARCHAR(255) 
    price DECIMAL(10, 2) 
    description NVARCHAR(MAX)
    is_available BIT 
    available_count INT 
    restaurant_id INT
    rating FLOAT 
}
Ref: Restaurants.restaurant_id < Food.restaurant_id



TABLE DeliveryPerson {
    delivery_person_id INT [primary key] 
    name NVARCHAR(255) 
    phone_number NVARCHAR(10)
    vehicle_type NVARCHAR(50)
    availability_status BIT
}

TABLE OrderHeader {
    order_id INT [primary key]
    order_date datetime
    total_amount DECIMAL(10, 2)
    delivery_time TIME
    status NVARCHAR(50)
    user_id INT
    restaurant_id INT
	  delivery_person_id INT
}
Ref: Users.user_id < OrderHeader.user_id
Ref: Restaurants.restaurant_id < OrderHeader.restaurant_id
Ref: DeliveryPerson.delivery_person_id < OrderHeader.delivery_person_id


TABLE OrderDetail {
    order_detail_id INT [primary key]
    order_id INT
    food_id int
    quantity INT 
    subtotal DECIMAL(10, 2)
}
Ref: OrderHeader.order_id < OrderDetail.order_id
Ref: Food.food_id - OrderDetail.food_id


TABLE Comments {
    comment_id INT [primary key]
    order_id INT UNIQUE
    rating FLOAT 
    comment_text NVARCHAR(MAX)
    comment_date DATETIME 
}

Ref: OrderHeader.order_id - Comments.order_id




