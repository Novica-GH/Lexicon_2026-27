
--LAB 3 - Exercises  - Adding, changing and deleting data

-- Use webshop.db for all exercises in this part. Before you start, check that the orders are
-- there: SELECT COUNT(*) FROM orders; should give 15. If not, run webshop_reset.sql and press
-- Ctrl+S. When you are done, click Revert Changes so your data is the same as everyone else's.


SELECT COUNT(*) FROM orders;

-- Exercise 1:  Add yourself as customer number 11 (use a made-up email).

INSERT INTO customers (customer_id, first_name, last_name, email)
VALUES (11, 'Novica', 'Ivkovic', 'novica.ivkovic@dl.com');

--test
SELECT * FROM customers;

-- Exercise 2:  Add two new products in one INSERT: Scarf (Accessories, 229 kr, 15 in stock) and Gloves (Accessories, 199 kr, 20 in stock).

INSERT INTO products (name, category, price, stock)
VALUES 
    ('Scarf', 'Accessories', 229, 15),
    ('Gloves', 'Accessories', 199, 20);

--test	
SELECT * FROM products;
SELECT * FROM products ORDER BY product_id DESC LIMIT 2; -- I want to see just these two rows I added now.


-- Exercise 3: Customer 7 (Emma) orders 2 Beanies (product 10, 179 kr). Make the order (order 16) and the order item.

INSERT INTO orders (order_id, customer_id, order_date)
VALUES (16, 7, CURRENT_DATE);

--test
SELECT * FROM orders;


INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 2, 179);

--test
SELECT * FROM order_items;


-- Exercise 4: Try to add an order item with quantity 0. Which rule stops you?


INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (16, 10, 0, 179);					-- Result: CHECK constraint failed: quantity > 0 -- These rule stops me.

--test
SELECT * FROM order_items WHERE order_id = 16;

-- Exercise 5: Order 12 has been shipped. Change its status.

UPDATE orders SET status = 'shipped' WHERE order_id = 12;

--test
SELECT order_id, status FROM orders WHERE order_id = 12;  -- status = shipped - OK


-- Exercise 6: The Water Bottle (product 5) is back in stock: 50 pieces.


UPDATE products SET stock = 50 WHERE product_id = 5;

--test
SELECT product_id, name, stock FROM products WHERE product_id = 5;  -- Okey Dokey


-- Exercise 7: Raise the price of all Accessories by 10%.

UPDATE products SET price = ROUND(price * 1.10, 2) WHERE category = 'Accessories';

--test
SELECT product_id, name, category, price FROM products WHERE category = 'Accessories';


-- Exercise 8: Delete the cancelled order. Watch out: its items must go first! Why?


DELETE FROM order_items								 -- We delete first from order items and after from orders. 
WHERE order_id IN (SELECT order_id FROM orders WHERE status = 'cancelled');   -- FOREIGN KEY(customer_id) REFERENCES customers(customer_id)

DELETE FROM orders
WHERE status = 'cancelled';

--test
SELECT * FROM orders WHERE status = 'cancelled'; -- OK, Result: 0 rows returned in 18ms


-- Exercise 9: Finally: click Revert Changes so your data matches the teacher's again. Check: 15 orders?


SELECT COUNT(*) FROM orders; 



--Designing a good database ----
------------------------------------


-- Exercises 10_ to 15 are done on paper or in a drawing tool. You don't need a database for them. 
-- 	Exercise 16 is the only one where you write SQL, and it uses a new database file, not webshop.db.
-------------------------------------------

-- Exercise 10: Look at this table: student | phone_numbers | course1 | course2 | course3. List every problem you can find.

-- 1. Problem with First Normal Form - phone_numbers -> 
      -- It means that we can have more theh one phonenumber in one column (separate with , or| for exempel)...
-- 2. Also 1. NF - Multiple course (1-3) for the same typ of data...

-- 3.  - We have just 3 courses here, but whta if one student has more then 3? - It is not efficietn...
-- 4.   	-  Also if student have just 1 or 2 courses it means that we have a lot of NULL... in DB... and reserve more memory that DB should to taka...

-- 5. It is wery hard to go through all the courses and find all students that listen one specific course...


-- Exercise 11: In order_sheet, which normal form does the products column break? How would you fix it?


-- Exercise 12: A table has: order_id | customer_id | customer_email | order_date. Which column is in the wrong place? Why?


-- Exercise 13: Music school (in pairs): 'Students take lessons from teachers. A lesson has a date, time, room and instrument. 
--              One teacher can teach many instruments.' Underline the things.


-- Exercise 14: Find the relationships in the music school. Which are 1:N and which are N:M?


-- Exercise 15: Draw the ER diagram for the music school.

-- Exercise 16: Write the CREATE TABLE statements for the music school in a new file music.db.
--				Database: create a new file. C
--				Click New Database, name it music.db, and click Cancel in the 'Edit table definition' window. 
--				Don't create these tables in webshop.db.










