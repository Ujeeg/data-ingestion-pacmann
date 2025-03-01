-- Create the customers table
CREATE TABLE customers (
    cust_id INT PRIMARY KEY,
    name VARCHAR(255),
    phone VARCHAR(20),
    address VARCHAR(255),
    city VARCHAR(100),
    province VARCHAR(100)
);

-- Create the categories table
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    name VARCHAR(255)
);

-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL,
    description TEXT,
    category_id INT REFERENCES categories(category_id),
    image_url VARCHAR(255)
);

-- Create the carts table
CREATE TABLE carts (
    cart_id INT PRIMARY KEY,
    cust_id INT REFERENCES customers(cust_id),
    trx_date DATE
);

-- Create the cart_items table
CREATE TABLE cart_items (
    cart_item_id INT PRIMARY KEY,
    cart_id INT REFERENCES carts(cart_id),
    product_id INT REFERENCES products(product_id),
    order_amt DECIMAL
);

-- Create the tags table
CREATE TABLE tags (
    tag_id INT PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    tag VARCHAR(255)
);

-- Create the campaigns table
CREATE TABLE campaigns (
    campaign_id INT PRIMARY KEY,
    name VARCHAR(255),
    campaign_type VARCHAR(255),
    start_date DATE
);

-- Create the campaign_items table
CREATE TABLE campaign_items (
    campaign_item_id INT,
    campaign_id INT REFERENCES campaigns(campaign_id),
    campaign_type VARCHAR(255),
    campaign_item VARCHAR(255)
);