SELECT * FROM orders;

INSERT INTO orders(order_id,customer_id,order_date,status)
VALUES (1,1, '2026-01-01', 'delivered');

INSERT INTO order_items(order_id, product_id,quantity,unit_price)
VALUES (1,1,1,599),
		(1,3,4,199);	--two rows in one inser
		
SELECT * FROM order_items;

-- Haithem inser 30+ rows here... 9:25

SELECT COUNT * FROM orders; -- ERROR: nema zagrada oko *

SELECT COUNT (*) FROM orders;		--OK
SELECT COUNT (*) FROM order_items;	--OK

--- Idemo dalje na nesto novo 9:28

INSERT INTO orders(order_id, customer_id, order_date)
VALUES (17, 8, 2026-04-01);
SELECT * FROM orders WHERE order_id = 17; -- and 16 as well


INSERT INTO orders (order_id, customer_id, order_date, status)  -- failed because 'lost' is not defined
VALUES (17, 2, '2026-04-02', 'lost');

INSERT INTO orders (order_id, customer_id, order_date) -- Error as well - Result: UNIQUE constraint failed: orders.order_id
VALUES (1, 2, '2026-04-02');


SELECT * FROM orders WHERE order_id = 9;   -- it works, but I do not have a base (these rows), like Haithem...

UPDATE orders SET status = 'delivered' WHERE order_id = 9;
SELECT * FROM orders WHERE order_id = 9;

UPDATE products SET price = price * 0.8 WHERE category = 'Shoes';
SELECT name, price FROM products WHERE category = 'Shoes';  -- OK it works


SELECT * FROM customers WHERE customer_id = 9;
DELETE FROM customers WHERE customer_id = 9;

UPDATE products SET price = 0;   --- Result: query executed successfully. Took 0ms, 12 rows affected
SELECT name, price FROM products;  --  




INSERT INTO orders (order_id, customer_id, order_date, status) VALUES(2, 2, '2026-01-12', 'delivered'),(3, 1, '2026-01-20', 'delivered'),(4, 3, '2026-01-28', 'delivered'),(5, 4, '2026-02-03', 'delivered'),(6, 5, '2026-02-10', 'delivered'),(7, 6, '2026-02-14', 'cancelled'),(8, 2, '2026-02-21', 'delivered'),(9, 8, '2026-02-27', 'shipped'),(10, 9, '2026-03-04', 'shipped'),(11, 1, '2026-03-09', 'shipped'),(12, 3, '2026-03-15', 'new'),(13, 6, '2026-03-18', 'new'),(14, 4, '2026-03-22', 'new'),(15, 2, '2026-03-28', 'new');INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES(2, 4, 1, 1199),(3, 9, 3, 129),(4, 2, 2, 249), (4, 6, 1, 499),(5, 8, 1, 1399),(6, 1, 1, 599), (6, 10, 1, 179),(7, 7, 1, 749),(8, 2, 1, 249), (8, 9, 2, 129),(9, 11, 1, 1299),(10, 3, 1, 199), (10, 2, 3, 249),(11, 6, 2, 499),(12, 4, 1, 1199), (12, 9, 1, 129),(13, 1, 2, 599),(14, 10, 2, 179), (14, 3, 1, 199),(15, 8, 1, 1399), (15, 2, 1, 249);





