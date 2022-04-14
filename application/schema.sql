
CREATE TABLE IF NOT EXISTS fast_food_restaurant (
	id integer,
	name text,
	location text,
	restaurant_type text,
	price_range text,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS review (
	id integer,
	fast_food_restaurant_id integer not null,
	reviewer_name text not null,
	description text,
    rating real not null,
	PRIMARY KEY (id),
    FOREIGN KEY(fast_food_restaurant_id) REFERENCES fast_food_restaurant(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS menu (
	id integer, 
    fast_food_restaurant_id integer,
    menu_type text,
    PRIMARY KEY(id),
    FOREIGN KEY (fast_food_restaurant_id) REFERENCES fast_food_restaurant(id) ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS food_item (
	id integer,
	name text not null,
	price real not null,
	menu_id integer not null,
	PRIMARY KEY (id),
	FOREIGN KEY (menu_id) REFERENCES menu(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS hours (
	day_of_week text not null,
	open_time time not null,
	close_time time not null,
	fast_food_restaurant_id integer not null,
	FOREIGN KEY (fast_food_restaurant_id) REFERENCES fast_food_restaurant(id) ON DELETE CASCADE
);

/* first restaurant */
INSERT INTO fast_food_restaurant VALUES ( 
1, 'McDonalds', 'Tempe, AZ', 'American', 'low'
);

INSERT INTO review VALUES (
	1, 1, 'Tiffany Day', 'micky D has pretty solid fries!', 4
);

INSERT INTO review VALUES (
	2, 1, 'Casey Luong', 'This grub is fairly adequate', 4
);

/* The following statements create 3 menus for restaurants with id 1) */
INSERT INTO menu VALUES (
	1, 1, 'regular'
);

INSERT INTO menu VALUES (
	2, 1, 'kids'
);

INSERT INTO menu VALUES (
	3, 1, 'breakfast'
);

INSERT INTO food_item VALUES (
	1, 'McDouble', '4.12', 1
);

INSERT INTO food_item VALUES (
	2, 'McTriple', '5.21', 1
);

INSERT INTO food_item VALUES (
	3, 'Hamburger Happy Meal', '2.49', 2
);

INSERT INTO food_item VALUES (
	4, '4 piece Chicken McNuggets Happy Meal', '3.25', 2
);

INSERT INTO food_item VALUES (
	5, 'Bacon, Egg & Cheese Biscuit', '2.00', 3
);

INSERT INTO food_item VALUES (
	6, 'Sausage McMuffin', '2.00', 3
);

INSERT INTO hours VALUES (
	'Monday', '05:00:00', '22:00:00', 1
);

INSERT INTO hours VALUES (
	'Tuesday', '05:00:00', '22:00:00', 1
);

INSERT INTO hours VALUES (
	'Wednesday', '05:00:00', '22:00:00', 1
);

INSERT INTO hours VALUES (
	'Thursday', '05:00:00', '22:00:00', 1
);

INSERT INTO hours VALUES (
	'Friday', '05:00:00', '22:00:00', 1
);




/* second restaurant */
INSERT INTO fast_food_restaurant VALUES ( 
2, 'Taco Bell', 'Tempe, AZ', 'American', 'low'
);

INSERT INTO review VALUES (
	3, 2, 'Michael Bubble', 'I was looking for some authentic Mexican cuisine and this was not it peeps', 2
);

INSERT INTO review VALUES (
	4, 2, 'Rosé', 'This grub is fairly adequate', 4
);

/* The following statements create 3 menus for restaurants with id 2 */
INSERT INTO menu VALUES (
	4, 2, 'regular'
);

INSERT INTO menu VALUES (
	5, 2, 'kids'
);

INSERT INTO menu VALUES (
	6, 2, 'breakfast'
);

INSERT INTO food_item VALUES (
	7, 'Crunchy Taco Supreme', '2.29', 4
);

INSERT INTO food_item VALUES (
	8, 'Steak Nacho Fries Burrito', '5.21', 4
);

INSERT INTO food_item VALUES (
	9, 'Kids Meal', '2.49', 5
);



INSERT INTO food_item VALUES (
	10, 'Bell Breakfast Box', '5.00', 6
);

INSERT INTO hours VALUES (
	'Monday', '05:00:00', '00:00:00', 2
);

INSERT INTO hours VALUES (
	'Tuesday', '05:00:00', '00:00:00', 2
);

INSERT INTO hours VALUES (
	'Wednesday', '05:00:00', '00:00:00', 2
);

INSERT INTO hours VALUES (
	'Thursday', '05:00:00', '00:00:00', 2
);

INSERT INTO hours VALUES (
	'Friday', '05:00:00', '00:00:00', 2
);

INSERT INTO hours VALUES (
	'Saturday', '05:00:00', '00:00:00', 2
);

