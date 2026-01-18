--part - 4 
-- Insert new author
INSERT INTO Authors (name, country)
VALUES ('Neil Gaiman', 'UK');

-- Insert new book by the newly added author
INSERT INTO Books (title, author_id, price, stock)
VALUES ('American Gods', 6, 499.00, 10);

--Update the price of a book.
UPDATE Books
SET price = 550.00
WHERE title = 'American Gods';

--Delete a customer from the database.
DELETE FROM Orders WHERE customer_id = 2;
DELETE FROM Customers WHERE customer_id = 2;

--Insert a new order for a customer.
INSERT INTO Orders (customer_id, book_id, quantity, order_date)
VALUES (1, 6, 1, '2025-03-01');
