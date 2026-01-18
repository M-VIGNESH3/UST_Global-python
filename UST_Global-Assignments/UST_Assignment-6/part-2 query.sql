--part - 2
 -- inserting data inta Authors
INSERT INTO Authors (name, country) VALUES
('Agatha Christie', 'UK'),
('J.R.R. Tolkien', 'UK'),
('Amish Tripathi', 'India'),
('Haruki Murakami', 'Japan'),
('Stephen King', 'USA');

 -- inserting data inta Books
INSERT INTO Books (title, author_id, price, stock) VALUES
('Murder on the Orient Express', 1, 450.00, 12),
('And Then There Were None', 1, 480.00, 6),
('The Hobbit', 2, 699.00, 10),
('Lord of the Rings', 2, 999.00, 4),
('Shiva Trilogy', 3, 350.00, 20),
('Ram Trilogy', 3, 370.00, 7),
('Norwegian Wood', 4, 520.00, 9),
('Kafka on the Shore', 4, 560.00, 3),
('The Shining', 5, 620.00, 5),
('It', 5, 750.00, 2);

 -- inserting data inta Customers
INSERT INTO Customers (name, email) VALUES
('Amit Verma', 'amit@gmail.com'),
('Sachin Patel', 'sneha@gmail.com'),
('Rohit Mehta', 'rohit@gmail.com');

 -- inserting data inta Orders
INSERT INTO Orders (customer_id, book_id, quantity, order_date) VALUES
(1, 2, 1, '2025-02-05'),
(1, 4, 2, '2025-02-08'),
(2, 6, 1, '2025-02-12'),
(2, 8, 2, '2025-02-15'),
(3, 10, 1, '2025-02-18');

