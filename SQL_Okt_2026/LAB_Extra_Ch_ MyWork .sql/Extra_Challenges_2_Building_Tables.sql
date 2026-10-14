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

ALTER TABLE suppliers RENAME COLUMN email TO contact_email;

-- Nastavak - Petak 9. oktobar 2026. 


-- Exercise 7: Show the columns of the products table using SQL, not the Database Structure tab.
--			Look up: PRAGMA table_info 		(Expected: 5 rows, one per column)

INSERT INTO suppliers (name, contact_email) 
VALUES ('Nordic Sport Equipment', 'info@nordicsport.se');


-- Exercise 8: A product can come from many suppliers, and a supplier can deliver many products. 
--              Create the middle table product_suppliers with a purchase price that must be more than 0. 
-- 				The same pair can only appear once. Then try to connect product 1 to supplier 99.
--			Look up: PRIMARY KEY with two columns · 	(Expected: The table is created, the INSERT gives an error)


CREATE TABLE product_suppliers (
    product_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    purchase_price REAL NOT NULL CHECK (purchase_price > 0),
    PRIMARY KEY (product_id, supplier_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);

SELECT * FROM product_suppliers;


INSERT INTO product_suppliers (product_id, supplier_id, purchase_price) -- ERROR: Result: FOREIGN KEY constraint failed
VALUES (1, 99, 150.00);

PRAGMA foreign_keys;  -- OK - Result: 1 rows returned in 22ms (FOREIGN KEY are ON!) 
-- If we need to include PRAGMA, we do next: 
--PRAGMA foreign_keys = ON;



-- Exercise 9: Create a table campaigns with name, start_date and end_date. 
--				Add a rule that end_date can never be before start_date. 
-- 				Test it with a campaign that ends before it starts.
--			Look up: CHECK that compares two columns ·  (xpected: The table is created, the INSERT gives an error)

CREATE TABLE campaigns (
    campaign_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    CHECK (end_date >= start_date)
);

SELECT * FROM campaigns;

INSERT INTO campaigns (name, start_date, end_date)			-- ERROR - Result: CHECK constraint failed: end_date >= start_date - This is OK, the base works propreately! As we wish.
VALUES ('Prolećna Rasprodaja', '2026-05-15', '2026-05-01');


INSERT INTO campaigns (name, start_date, end_date)			  -- OK Result: query executed successfully. Took 0ms, 1 rows affected
VALUES ('Prolećna Rasprodaja', '2026-05-01', '2026-05-15');




-- Level 3 -------------------------------------

-- Exercise 10: Create a table product_sizes with an own id, product_id (points to products), 
--				size (only S, M, L or XL) and stock (0 if nothing is given). 
--				The same product can't have the same size twice. Test it by adding size M for product 1 twice.
--			Look up: UNIQUE on two columns · 	(Expected: The first INSERT works, the second gives an error)


CREATE TABLE product_sizes (
    size_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    size TEXT NOT NULL CHECK (size IN ('S', 'M', 'L', 'XL')),
    stock INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    UNIQUE (product_id, size)
);

SELECT * FROM product_sizes;

INSERT INTO product_sizes (product_id, size, stock)   -- OK
VALUES (1, 'M', 10);

INSERT INTO product_sizes (product_id, size, stock)   -- Result: UNIQUE constraint failed: product_sizes.product_id, product_sizes.size
VALUES (1, 'M', 5);    

-- Exercise 11: Create a table employees where each employee can have a manager, who is also an employee in the same table. 
--				The boss has no manager. Add the boss and two employees who report to the boss.
--			Look up: a foreign key that points to its own table · 		(Expected: 3 rows)


CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- OK: Result: query executed successfully. Took 0ms
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT NOT NULL,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id) ON DELETE SET NULL
);

SELECT * FROM employees; -- OK


INSERT INTO employees (first_name, last_name, title, manager_id)		--OK
VALUES ('Marko', 'Marković', 'CEO', NULL);


INSERT INTO employees (first_name, last_name, title, manager_id)   -- OK
VALUES ('Ana', 'Anić', 'Sales Manager', 1);

INSERT INTO employees (first_name, last_name, title, manager_id)	-- OK
VALUES ('Petar', 'Petrović', 'Lead Developer', 1);


-- Check if Marko - CEO has a boos itself?
SELECT  e.employee_id, e.first_name || ' ' || e.last_name AS employee_name, e.title,
    COALESCE(m.first_name || ' ' || m.last_name, 'No (Boss)') AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;




-- Exercise 12: Create two tables: teams and players, where a player belongs to a team. 
--				Make it so that when a team is deleted, its players are deleted automatically. 
--				Add one team with two players, delete the team, and check the players table.
--			Look up: ON DELETE CASCADE · 			(Expected: 0 rows left in players)


CREATE TABLE teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT NOT NULL
);


CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT NOT NULL,
    team_id INTEGER NOT NULL,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

SELECT * FROM teams;
SELECT * FROM players;

INSERT INTO teams (team_name) VALUES ('Tigers');

SELECT * FROM teams; -- Result: 1 rows returned in 19ms

INSERT INTO players (player_name, team_id) VALUES ('Marko', 1);
INSERT INTO players (player_name, team_id) VALUES ('Petar', 1);

SELECT * FROM players; -- Result: 2 rows returned in 13ms

DELETE FROM teams WHERE team_id = 1;

SELECT * FROM players;  --Result: 0 rows returned in 19ms   -- Q.E.D. (Quad Erat Demonstrandum for today).

