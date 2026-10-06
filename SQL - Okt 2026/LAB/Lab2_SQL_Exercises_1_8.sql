-- Day 2: Exercises - October 6 2026 - Tuesday

-- Exercise 1: Create a table books with: book_id (primary key), title (must have a value), author, year (whole number).

CREATE TABLE books(
	book_id INTEGER PRIMARY KEY,
	title 	TEXT NOT NULL,
	author	TEXT NOT NULL,					    -- allso have a value check - my choice
	year 	INTEGER								-- interesting with year, what with Iliad or Odyssey ( - 750-680 !? BC...) OR Egypt -3000...
);												-- I leave here just INTEGER without CHECK (year >= 0) ... because priviously...


-- Exercise 2: Add a rule to books so year must be greater than 1400. (Hint: DROP and CREATE again.)

DROP TABLE books 

CREATE TABLE books(
	book_id INTEGER PRIMARY KEY,
	title 	TEXT NOT NULL,
	author	TEXT NOT NULL,					    
	year 	INTEGER CHECK (year >= 1400)					
);



-- Exercise 3  Add a column isbn to books. It should be TEXT.

ALTER TABLE books ADD COLUMN isbn TEXT;

SELECT * FROM books; 	-- checking is everything OK

-- Exercise 4: Delete the books table.

DROP TABLE books 

-- Exercise 5: Create a table reviews: review_id, product_id (points to products), rating (1 to 5), comment.


CREATE TABLE reviews(
	review_id INTEGER PRIMARY KEY,
	product_id INTEGER NOT NULL,
	rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
	comment TEXT, 				-- It can be without NOT NULL, for example for No comments.
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);


--Exercise 6:  Test reviews: try to add a review with rating 6. What happens?

INSERT INTO reviews(review_id, product_id, rating, comment)
VALUES (100, 1, 6, 'No comment' );

		-- Execution finished with errors.
		-- Result: CHECK constraint failed: rating BETWEEN 1 AND 5
		-- At line 50:
		-- INSERT INTO reviews(review_id, product_id, rating, comment)
		-- VALUES (100, 1, 6, 'No comment' );


SELECT * FROM reviews;

DROP TABLE reviews


-- Exercise 7  Test reviews: try to add a review for product 50. What happens?

INSERT INTO reviews(review_id, product_id, rating, comment)
VALUES (100, 50, 3, 'No comment2' );    						-- Problem with product_id - 50 (product_id is defined in products TABLE just BETWEEN 1-12!


		-- Execution finished with errors.
		-- Result: UNIQUE constraint failed: reviews.review_id
		-- At line 67:
		-- INSERT INTO reviews(review_id, product_id, rating, comment)
		-- VALUES (100, 50, 3, 'No comment2' );
		
		

-- Exercise 8  On paper: draw the 4 webshop tables as boxes and draw arrows for each foreign key.

-- Done on paper...		
		