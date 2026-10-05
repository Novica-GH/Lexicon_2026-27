-- 2026-10-05  - The first day with SQL  - EXTRA CHALLENGES: SELECT

-- LEVEL 1  - Because this exercises are litle longer, I am goint to write sollutions in the multiple lines!
-- -----------------------------------------------------------------------------------------------------------

-- Exercise 1: Show products that are not Accessories, are in stock, and have a space in their name. 
--             Sort by category, then by price from highest to lowest.   (Expected: 6 rows) 


SELECT * FROM products WHERE category != 'Accessories' AND stock > 0 AND name LIKE '% %' ORDER BY category ASC, price DESC; 

--Exercise 2: Show customers who live in a city starting with S or M, plus customers with no city at all.  (Expected: 4 rows)

SELECT * FROM customers WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;

-- Exercise 3: Which Shoes product is the second most expensive? Show only that one. (Expected: 1 row)
SELECT * FROM products WHERE category = 'Shoes' ORDER BY price DESC LIMIT 1 OFFSET 1;

-- Exercise 4: Of the customers who joined in 2024 or 2025, show the 3 who joined most recently.
--             Solve it without BETWEEN and without >=. (Expected: 3 rows)

SELECT * FROM customers WHERE joined_date LIKE '2024%' OR joined_date LIKE '2025%' ORDER BY joined_date DESC LIMIT 3;




--Level 2  - Use the SQLite documentation: sqlite.org/lang_corefunc.html
--------------------------------------------------------------------------


--Exercise 5: Show each customer's full name in one column called full_name (like "Anna Lindqvist"), sorted by last name.
--			  Look up: ||   (Expected: 10 rows9

SELECT (first_name || ' ' || last_name) AS full_name FROM customers ORDER BY last_name ASC;


-- Exercise 6: Give every product a price level: budget under 200 kr, mid from 200 to 799 kr, premium from 800 kr.  
--             Look up: CASE WHEN ·  (Expected: 12 rows: 4 budget, 5 mid, 3 premium)

SELECT name, price,  CASE  WHEN price < 200 THEN 'budget' WHEN price < 800 THEN 'mid' ELSE 'premium' END AS price_level FROM products;  -- Uauu...

--Exercise 7: Show every customer's first name and city, but write Unknown instead of NULL.
--				Look up: COALESCE · (Expected: 10 rows)

SELECT first_name, COALESCE(city, 'Unknown') AS city FROM customers;  -- or -- Better and standard sollution, works for multiple columns simultanosely

SELECT first_name, IFNULL(city, 'Unknown') AS city FROM customers;  -- alternative solution just for two arguments, not form more - it works (if first is NULL, return another)


-- Exercise 8: Which customers joined in the first half of a year (January to June), whatever the year?
--				Look up: strftime · (Expected: 6 rows)

SELECT * FROM customers WHERE strftime('%m', joined_date) BETWEEN '01' AND '06';  -- OR without BETWEEN
SELECT * FROM customers WHERE strftime('%m', joined_date) <= '06';


--Exercise 9: Which product has the longest name?
--				Look up: LENGTH · (Expected: 1 row)
				
SELECT name, LENGTH(name) AS name_length FROM products ORDER BY LENGTH(name) DESC LIMIT 1;



--Exercise 10: Show each customer's email username: the part before the @.
--				Look up: substr and instr · (Expected: 10 rows)
																			      -- SUBSTR(novica@yahoo.com, 1, 7) -> SUBSTR returns 'novica'
SELECT email, SUBSTR(email, 1, INSTR(email, '@') - 1) AS username FROM customers; -- SUBSTR(start_string, start_character, length_of_returned_substring)
																				  -- INSTR(string, 'character') - returns position of 'character' in the string.
																				  -- Ex: INSTR(novica@yahoo.com, '@') -> INSTR returns 7 

-- 	Level 3 - -----------------
--------------------------------

-- Exercise 11: Which products cost more than the average price? Don't type the average yourself:
--                 let SQL calculate it inside the query.  (Expected: 5 rows)   

SELECT name, price FROM products WHERE price > ( SELECT AVG(price) FROM products );   -- OBS!! SubQuerry...

-- Exercise 12: Make a price list with one column that says, for example, "Socks 3-pack costs 129 kr". 
--              Only products in stock, cheapest first. Watch out: does it say 129 or 129.0? Fix it.  (Expected: 10 rows)

SELECT name || ' costs ' || CAST(price AS INTEGER) || ' kr' AS price_list FROM products  WHERE stock > 0  ORDER BY price ASC;  --- Wow - concatenation++
						-- CAST(price AS INTEGER) -> transform decimal number to integer
						-- another sollution: ROUND(price), but allso: PRINTIF('%.0f',price)
						

-- Exercise 13: How many customers live in each city? Biggest city first.
--					Look up: GROUP BY · (Expected: 6 rows)


SELECT city, COUNT(*) AS customer_count 		-- for counting customers per city uses agregat funktion COUNT() and clause GROUP BY.
FROM customers 
WHERE city IS NOT NULL 							-- OBS - litle bit hard...
GROUP BY city
ORDER BY customer_count DESC;







																			 

