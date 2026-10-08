--October 8 2026

SELECT * FROM orders;

SELECT orders.order_id, customers.first_name, orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;

SELECT o.order_id, c.first_name, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;

SELECT o.order_id, c.first_name
FROM orders o
JOIN customers c; -- Problem we forgot ON, and every row was poverkad - Result: 150 rows returned in 16ms

SELECT o.order_id, c.first_name, c.city
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Uppsala';    -- 9:29


SELECT o.order_id, c.first_name, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id   --Result: 5 rows returned in 13ms
ORDER BY o.order_date DESC
LIMIT 5;


SELECT oi.order_id, p.name, oi.quantity
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;    --Result: 23 rows returned in 13ms


SELECT c.first_name, o.order_date, p.name, oi.quantity
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id				--Result: 23 rows returned in 16ms
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON oi.product_id = p.product_id;


SELECT c.first_name, o.order_date, p.name, oi.quantity -- Pitanje Alesandra da se grupisu sve kolicine po osobi (na primer da Ana ima 1+2=3
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id				--Result: 23 rows returned in 16ms
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON oi.product_id = p.product_id;
GROUP BY c.customer_id, c.first_name
ORDER BY oi.quantity DESC;

--SELECT c.first_name, SUM(oi.quantity) AS order_items GROUP BY (DISTINCT p.name) AS products
--FROM order_items oi
--JOIN orders o ON oi.order_id = o.order_id
--JOIN customers c ON o.customer_id = c.customer_id
--JOIN products p ON oi.product_id = p.product_id
-- GROUP BY c.customer_id, c.first_name;


--LEFT JOIN
SELECT c.first_name, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id

--INNER JOIN
SELECT c.first_name, o.order_id
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id;




