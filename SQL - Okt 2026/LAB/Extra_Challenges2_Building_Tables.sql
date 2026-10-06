-- Day 2: EXTRA CHALLENGES: Building tables - October 6 2026 - Tuesday


-- Level 1 -----------------------

-- Exercise 1: Create a table suppliers with supplier_id (primary key), name (must have a value and must be unique), 
-- country (Sweden if nothing is given) and email.    (Expected: Runs without errors)


CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    country TEXT DEFAULT 'Sweden',
    email TEXT
);
 
-- testing... 
INSERT INTO suppliers (name, email)  -- test
VALUES ('Elgiganten', 'info@elgiganten.se');

SELECT * FROM suppliers;

INSERT INTO suppliers (email)   -- test -> ERROR-PROBLEM: NOT NULL constraint failed: suppliers.name
VALUES ('name@test.com');		--         name is required!





-- Exercise 2: Add a supplier without giving a country. Then show all suppliers. What does the country column say?
--				(Expected: 1 row, country is Sweden)


INSERT INTO suppliers (name, email)
VALUES ('Power', 'office@power.se'); -- It is OK, country is already defined ('Sweden')

--my test
SELECT * FROM suppliers;

DELETE FROM suppliers
WHERE supplier_id = 3;



-- Exercise 3: Try to add a second supplier with the same name, Nordic Textiles. What happens, and which rule stopped you?
-- 				(Expected: An error)

INSERT INTO suppliers (name, email)
VALUES ('Nordic Textiles', 'info@nordictextiles.se');  --- OK


INSERT INTO suppliers (name, email)
VALUES ('Nordic Textiles', 'sales@nordictextiles.se');   -- ERROR: Result: UNIQUE constraint failed: suppliers.name

	
	

-- Exercise 4: Create a table coupons where the code itself (for example 'SUMMER20') is the primary key.
--				discount_percent must be between 1 and 90, and valid_until must have a value. 
--				Then try to add a coupon with 95 percent off.
--				(Expected: The table is created, the INSERT gives an error)


CREATE TABLE coupons (
    code TEXT PRIMARY KEY,
    discount_percent INTEGER NOT NULL CHECK (discount_percent BETWEEN 1 AND 90),
    valid_until TEXT NOT NULL
);
--Then try to add a coupon with 95 percent off.
INSERT INTO coupons (code, discount_percent, valid_until)
VALUES ('Lexicon95', 95, '2026-12-31');			-- ERROR - Result: CHECK constraint failed: discount_percent BETWEEN 1 AND 90

-------------------------------


-- Level 2 - Use the SQLite documentation: sqlite.org/lang_createtable.html and 
--										   sqlite.org/lang_altertable.html
----------------------------------------------------

-- Exercise 5: Add a supplier without giving a supplier_id. Which id does it get? Why?
--			Look up: INTEGER PRIMARY KEY · (Expected: 1 new row)

INSERT INTO suppliers (name, email)
VALUES ('WebHallen', 'office@webhallen.se'); -- without specifying supplier_id, SQLite givs next number to the new line (4)

SELECT * FROM suppliers WHERE name = 'WebHallen';


--Exercise 6: Rename the column email in suppliers to contact_email.
--			Look up: ALTER TABLE ... RENAME COLUMN · (Expected: Runs without errors)




-- Exercise 7: Show the columns of the products table using SQL, not the Database Structure tab.
--			Look up: PRAGMA table_info · 		(Expected: 5 rows, one per column)



-- Exercise 8: A product can come from many suppliers, and a supplier can deliver many products. 
--              Create the middle table product_suppliers with a purchase price that must be more than 0. 
-- 				The same pair can only appear once. Then try to connect product 1 to supplier 99.
--			Look up: PRIMARY KEY with two columns · 	(Expected: The table is created, the INSERT gives an error)



-- Exercise 9: Create a table campaigns with name, start_date and end_date. 
--				Add a rule that end_date can never be before start_date. 
-- 				Test it with a campaign that ends before it starts.
--			Look up: CHECK that compares two columns ·  (xpected: The table is created, the INSERT gives an error)



-- Level 3 -------------------------------------

-- Exercise 10: Create a table product_sizes with an own id, product_id (points to products), 
--				size (only S, M, L or XL) and stock (0 if nothing is given). 
--				The same product can't have the same size twice. Test it by adding size M for product 1 twice.
--			Look up: UNIQUE on two columns · 	(Expected: The first INSERT works, the second gives an error)


-- Exercise 11: Create a table employees where each employee can have a manager, who is also an employee in the same table. 
--				The boss has no manager. Add the boss and two employees who report to the boss.
--			Look up: a foreign key that points to its own table · 		(Expected: 3 rows)

-- Exercise 12: Create two tables: teams and players, where a player belongs to a team. 
--				Make it so that when a team is deleted, its players are deleted automatically. 
--				Add one team with two players, delete the team, and check the players table.
--			Look up: ON DELETE CASCADE · 			(Expected: 0 rows left in players)





