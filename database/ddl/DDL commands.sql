-- database creation
CREATE DATABASE solucxData;

-- selecting the database
USE solucxData;

-- creating the schema of the database
-- customers table
-- id_client, age, monthly_income, city, state, gender, education_level
CREATE TABLE IF NOT EXISTS customers (
	client_id INT PRIMARY KEY,
	age INT NOT NULL,
	monthly_income DECIMAL(12, 2),
	city VARCHAR(100) NOT NULL,
	state VARCHAR(50) NOT NULL,
	gender VARCHAR(20) NULL,
	education_level VARCHAR(255) NULL
);

-- cars table
-- auto_id, auto_brand, auto_model, auto_year, auto_value, id_client
CREATE TABLE IF NOT EXISTS cars (
auto_id INT PRIMARY KEY,
auto_brand VARCHAR(40) NOT NULL,
auto_model VARCHAR(100) NOT NULL,
auto_year YEAR NOT NULL,
auto_value DECIMAL(12, 2) NOT NULL,
client_id INT NOT NULL,

FOREIGN KEY (client_id)
REFERENCES customers(client_id)
);

-- customers table index
CREATE INDEX customer_index
ON customers (id_client);

-- cars table index
CREATE INDEX cars_index
ON cars (auto_id);

