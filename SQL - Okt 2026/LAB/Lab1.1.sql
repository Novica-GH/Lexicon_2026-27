--1. Show the first name and email of all customers. (10 rows)
--SELECT first_name, email 
--FROM customers


--2. Show all products in the Shoes category. (3 rows)
--SELECT products.* FROM products   -- ALL from products - 12 lines
--SELECT products.* FROM products WHERE category = 'Shoes';


--3. Which customers live in Uppsala? (3 rows)
--SELECT * FROM customers WHERE city = 'Uppsala';


--4. Which product costs exactly 199 kr? (1 row)
-- SELECT * FROM products WHERE price = 199;


--5. Show all products sorted by name, A to Z. (12 rows)
--SELECT * FROM products ORDER BY name ASC;

--6. Show all customers, the one who joined first at the top. (10 rows)
--SELECT * FROM customers ORDER BY joined_date ASC;

--7. Which products are sold out (stock is 0)? (2 rows)
--SELECT * FROM products WHERE stock = 0;

--8. Show the 3 newest customers. (3 rows)
-- SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;

--9. Show customers from Stockholm or Göteborg. Use IN. (4 rows)
-- SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');

--10. Show product name and price, but call the columns product and price_sek. (12 rows)
--SELECT name AS product, price AS price_sek FROM products;

BONUS Puestions: 

1. Show products that are Clothing or Shoes and cost more than 1000 kr. Hint: you need brackets. Try without them too: why is the answer different? (3 rows)



