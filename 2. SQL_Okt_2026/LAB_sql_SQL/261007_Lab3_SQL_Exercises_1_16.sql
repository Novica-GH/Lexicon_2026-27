
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

-- It break 1NF. It is necessary that values in kolumns are atomic (non divisable), but here we have had (before normalization) for example ("Hoodie Black, Cap Logo") in one cell
-- We need to have next structuer on paper: 

-- 1. orders 
--		order_id (Primary Key)
--		customer_id (Foreign Key)
--		order_date
-- 2. products 
--		product_id (Primary Key)
--		name
--		price
-- 3. order_items 			-- Connecting table
--		order_id 	(Foreign Key -> orders.order_id)
--		product_id 	(Foreign Key -> products.product_id)
--		quantity
--		Primary Key: (order_id, product_id)

-- Exercise 12: A table has: order_id | customer_id | customer_email | order_date. Which column is in the wrong place? Why?

-- customer_email - is in the wrong place:
-- 1. customer_email depends just from customers(customer-id), nor form orders (order_id). In that way havi breaking rules 2NF and 3NF!
-- 2- Unnecessary multiplication of email with every order (for every order have we the samme adress) - Redudant/unnecessary data.
-- 2.1 - If we want to change email for our customer, we need to change every row in orders tabel, where email exists!



-- Exercise 13: Music school (in pairs): 'Students take lessons from teachers. A lesson has a date, time, room and instrument. 
--              One teacher can teach many instruments.' Underline the things.

-- ER modeling: 

-- 1. Main entities: Students, teachers, lessons, instruments;

-- 2. Main atributes/entity: for example lessons ( date, time, room, instrument-id) - instrument-id is goint to be FOREIGN KEY in table instruments!

--3. Relations: teachers <-> instruments  (N:M) more to more; "One teacher can teach many instruments" (?  One instrument can be taught by several teachers!)
--	3.1 maybe we can use one extra tabel for this situation, for example teacher_instruments...
--	 


-- Exercise 14: Find the relationships in the music school. Which are 1:N and which are N:M?

--  1. teachers <-> instruments (N:M)
--  2. students <-> lessons  (1:N)
--	3. teacher <-> lessons (1:N)
--	4. instruments <-> lessons (1:N)



-- Exercise 15: Draw the ER diagram for the music school.

-- ER modeling:

-- 1. students
--		- student_id (PRIMARY KEY)
--		- first_name
--		- last_name
--		- email
--		- phone

-- 2. teachers
--		- teacher_id (PRIMARY KEY)
--		- first_name
--		- last_name
--		- email
-- 		- phone

-- 3. instruments
--		- instrument_id (PK)
--		- instrument_name

-- 4. lessons
--		- leson_id (PRIMARY KEY)
--		- date 
--		- time
--		- room
--		- student_id 	(FOREIGN KEY -> students)
--		- teacher_id 	(FOREIGN KEY -> teachers)
--		- instrument_id (FOREIGN KEY -> instruments)

-- 5. teacher_instruments
--		- teacher_id 	(PRIMARY KEY, FOREIGN KEY -> teachers)
--		- instrument_id (PRIMARY KEY, FOREIGN KEY -> instruments)




--       +--------------+                   +---------------+
--       |   students   |                   |   teachers    |
--       +--------------+                   +---------------+
--       |  student_id  |<---+         +--->|  teacher_id   |--- N --+
--       |  first_name  |    |         |    |  first_name   |        |
--       |  last_name   |    1         1    |  last_name    |        |
--       |  email   	|	 |         |    |  email        |        |
--       |  phone       |    |         |    |  phone        |        |
--       +--------------+    |         |    +---------------+        |
--                           |         |                             |
--                           N         N                             M
--                           |         |                             |
--                   +-------+---------+-------+           +---------v-----------+
--                   |         lessons         |           | teacher_instruments |
--                   +-------------------------+           +---------------------+
--                   | lesson_id (PK)          |           | teacher_id (FK)     |
--                   | date                    |           | instrument_id (FK)  |
--                   | time                    |           +---------------------+
--                   | room                    |                             ^
--                   | student_id (FK)         |                             |
--                   | teacher_id (FK)         |                             M
--                   | instrument_id (FK)      |                             |
--                   +-------------------------+                             |
--                                ^                                          |
--                                1                                          |
--								  |  										 |
--                                N                                          |
--                                |                                          |
--                       +--------+--------+                                 |
--                       |   instruments   |                                 |
--                       +-----------------+                                 |
--                       | instrument_id   |----------------- 1 -------------+
--                       | instrument_name |
--                       +-----------------+




-- Exercise 16: Write the CREATE TABLE statements for the music school in a new file music.db.
--				Database: create a new file. C
--				Click New Database, name it music.db, and click Cancel in the 'Edit table definition' window. 
--				Don't create these tables in webshop.db.



PRAGMA foreign_keys = ON;

CREATE TABLE students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    phone TEXT
);

INSERT INTO students (student_id, first_name, last_name, email, phone)
VALUES (101, 'Ada', 'Ericsson', 'ada@ericsson.se', '+4673123123');

SELECT * FROM students;

INSERT INTO students (student_id, first_name, last_name, email, phone)
VALUES (102, 'Bob', 'Marley', 'bob@marley.usa', '+15272627455'),
	   (103, 'Mery', 'Jones', 'mery@jones.usa', '+15242677358');

CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT
);

INSERT INTO teachers (teacher_id, first_name, last_name, email)
VALUES (1, 'Mikelandjelo', 'Buonaroti', 'mika@bono.it'),
       (2, 'Rafaelo', 'Donateli', 'rafa@doni.it'),
	   (3, 'Leonardo', 'DaVinci', 'leo@vinca.it');
	   
SELECT * FROM teachers;

CREATE TABLE instruments (
    instrument_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

ALTER TABLE instruments
RENAME COLUMN name TO instrument_name;

INSERT INTO instruments (instrument_id, instrument_name)
VALUES 	(51,'Piano'),
		(52, 'Violin'),
		(53, 'Fiol'),
		(54, 'Violonchelo'),
		(55, 'Contrabass'),
		(56, 'Drums'),


INSERT INTO instruments (instrument_name) -- Lets try AUTOINCREMENT! -- WOW it works!! 2026-10-09 1:23 it is time to bed!
VALUES 	('Fluta'),
		('Clarinet'),
		('Trombon'),
		('Frula'),
		('Gitar'),
		('Accordion');
		
SELECT * FROM instruments;

	   
	   
	   

CREATE TABLE teacher_instruments (
    teacher_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    PRIMARY KEY (teacher_id, instrument_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id) ON DELETE CASCADE
);


CREATE TABLE lessons (
    lesson_id INTEGER PRIMARY KEY AUTOINCREMENT,
    lesson_date DATE NOT NULL,
    lesson_time TIME NOT NULL,
    room TEXT NOT NULL,
    student_id INTEGER NOT NULL,
    teacher_id INTEGER NOT NULL,
    instrument_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE CASCADE,
    FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id) ON DELETE CASCADE
);






