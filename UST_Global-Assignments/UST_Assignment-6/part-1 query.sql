--part 1

--create database
CREATE DATABASE sql-assignment-6;
USE Database;

--authors table
CREATE TABLE Authors (
    author_id INT IDENTITY  PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50)
);

--Books table
CREATE TABLE Books (
    book_id INT  IDENTITY PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author_id INT,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

--Customers table
CREATE TABLE Customers (
    customer_id INT  IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

--Orders table
CREATE TABLE Orders (
    order_id INT IDENTITY PRIMARY KEY,
    customer_id INT,
    book_id INT,
    quantity INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
