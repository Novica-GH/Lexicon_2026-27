-- -- Day 2: Lectures with Haithem - 09:00 October 6 2026 - Tuesday

-- CREATING DATA BASES



CREATE TABLE pets(
	pet_id INTEGER PRIMARY KEY,
	name 	TEXT,
	species	TEXT,
	age 	INTEGER
);

INSERT INTO pets VALUES(1, 'Bella', 'dog', 3);
SELECT * FROM  pets;

INSERT INTO pets VALUES(2, NULL, 'cat', -5);

ALTER TABLE pets ADD COLUMN owner TEXT;
SELECT * FROM pets;

DROP TABLE pets;

-- kreiramo ponovo pets sa pravilima


CREATE TABLE pets(
	pet_id INTEGER PRIMARY KEY,
	name 	TEXT NOT NULL,
	species	TEXT NOT NULL,
	age 	INTEGER CHECK (age >= 0),
	vaccinated INTEGER DEFAULT0
);

--INSERT INTO pets (pet_id, name, species, age)
--VALUES (2, NULL, 'cat', 3)  --- PROBLEM name NULL

INSERT INTO pets (pet_id, name, species, age)
VALUES (2, 'Misse', 'cat', 3)

DROP TABLE pets -- ovim brisemo tabelu pets



-- NESTO NOVO: 

CREATE TABLE orders(
	order_id INTEGER PRIMARY KEY,
	customer_id INTEGER NOT NULL,
	order_date TEXT NOT NULL,
	status TEXT NOT NULL DEFAULT 'new' 
			CHECK (status IN ('new','shipped','delivered','cancelled')),
	FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

			
CREATE TABLE order_items(
	order_id INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	quantity INTEGER NOT NULL,
	unit_price REAL NOT NULL,
	PRIMARY KEY (order_id, product_id),
	FOREIGN KEY (order_id) REFERENCES orders(order_id),
	FOREIGN KEY (product_id) REFERENCES products(product_id)
	);

INSERT INTO orders(order_id, customer_id, order_date)
VALUES (100, 999, '2026-10-01');



-- Haitems codd from today Tuesday, October 6 2026:

CREATE TABLE pets ( 
	pet_id INTEGER PRIMARY KEY, 
	name TEXT, species TEXT, 
	age  INTEGER);
	
INSERT INTO pets VALUES(1,'Bella', 'dog', 3);
SELECT * FROM pets;

INSERT INTO pets 
VALUES(2, NULL, 'cat', -5);

ALTER TABLE pets ADD COLUMN owner TEXT;

SELECT * FROM pets;

DROP TABLE pets;

CREATE TABLE pets( 
	pet_id INTEGER PRIMARY KEY AUTOINCREMENT, 
	name TEXT NOT NULL, 
	species TEXT NOT NULL, 
	age  INTEGER CHECK (age >= 0), 
	vaccinated INTEGER DEFAULT 0);

INSERT INTO pets (pet_id, name, species, age)
VALUES(2, 'Misse', 'cat', 3)

SELECT * FROM pets;

DROP TABLE pets;

CREATE TABLE orders( 
	order_id INTEGER PRIMARY KEY, 
	customer_id INTEGER NOT NULL, 
	order_date TEXT NOT NULL, 
	status TEXT NOT NULL DEFAULT 'new'   
			CHECK (status IN ('new','shipped','delivered','cancelled')),
	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);
	


	
CREATE TABLE order_items( 
	order_id INTEGER NOT NULL, 
	product_id INTEGER NOT NULL, 
	quantity INTEGER NOT NULL CHECK (quantity > 0), 
	unit_price REAL NOT NULL, 
	PRIMARY KEY (order_id, product_id), 
	FOREIGN KEY (order_id)REFERENCES orders(order_id), 
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);



INSERT INTO orders(order_id, customer_id, order_date)
VALUES(100, 999, '2026-10-01');

SELECT * FROM orders;


