# I used this resource to assist with the DDL
# https://myxml.in/json-to-ddl.html

# ----------------------------------------------------------------------- 
# items 
# ----------------------------------------------------------------------- 
    
DROP TABLE IF EXISTS items;

CREATE TABLE items
(
    itemsID INTEGER NOT NULL,
    price DOUBLE,
    name VARCHAR(100) NULL,
    ordersID INTEGER NOT NULL,
    PRIMARY KEY (itemsID),
    FOREIGN KEY(ordersID) REFERENCES orders (ordersID)
);
    
# ----------------------------------------------------------------------- 
# payment 
# ----------------------------------------------------------------------- 

DROP TABLE IF EXISTS payment;

CREATE TABLE payment
(
    paymentID INTEGER NOT NULL,    
    method VARCHAR(100) NULL,    
    card_type VARCHAR(100) NULL,    
    ordersID INTEGER NOT NULL,
    customersID INTEGER NULL,
    PRIMARY KEY (paymentID),
    FOREIGN KEY(ordersID) REFERENCES orders (ordersID),
    FOREIGN KEY(customersID) REFERENCES customers (customersID)
);
    
# ----------------------------------------------------------------------- 
# charges 
# ----------------------------------------------------------------------- 
    
DROP TABLE IF EXISTS charges;

CREATE TABLE charges
(
    chargesID INTEGER NOT NULL,
    date VARCHAR(100) NULL,
    total DOUBLE,
    subtotal DOUBLE,
    taxes DOUBLE,
    ordersID INTEGER NOT NULL,
    PRIMARY KEY (chargesID),
    FOREIGN KEY(ordersID) REFERENCES orders (ordersID)
);
    
# ----------------------------------------------------------------------- 
# orders 
# ----------------------------------------------------------------------- 

DROP TABLE IF EXISTS orders;

CREATE TABLE orders
(
    ordersID INTEGER NOT NULL,
    PRIMARY KEY (ordersID)
);

# ----------------------------------------------------------------------- 
# customers 
# ----------------------------------------------------------------------- 

DROP TABLE IF EXISTS customers;

CREATE TABLE customers
(
    customersID INTEGER NOT NULL,
    zip INTEGER,
    last_4_card_number INTEGER,
    name VARCHAR(100) NULL,
    PRIMARY KEY (customersID)
);

