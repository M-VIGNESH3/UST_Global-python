--part - 4

--List all books along with their author names.
SELECT b.title , a.name 
FROM Books b
JOIN Authors a
ON b.author_id = a.author_id;


--Find all orders made by a particular customer
SELECT * FROM Orders WHERE customer_id=3

--List books with stock less than 5.
SELECT title, stock
FROM Books
WHERE stock < 5;


--Find the total number of books sold per book.
SELECT 
    b.title AS book_title,
    SUM(o.quantity) AS total_sold
FROM Orders o
JOIN Books b
ON o.book_id = b.book_id
GROUP BY b.title;

--Find the total revenue generated from all orders.
SELECT SUM(o.quantity * b.price) AS total_revenue
FROM Orders o
JOIN Books b
ON o.book_id = b.book_id;

