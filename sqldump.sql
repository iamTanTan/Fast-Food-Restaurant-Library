--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2 (Ubuntu 14.2-1.pgdg20.04+1)
-- Dumped by pg_dump version 14.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: fast_food_restaurant; Type: TABLE; Schema: public; Owner: nxwdtuddpnukbr
--

CREATE TABLE "public"."fast_food_restaurant" (
    "id" integer NOT NULL,
    "name" "text",
    "location" "text",
    "restaurant_type" "text",
    "price_range" "text"
);


ALTER TABLE public.fast_food_restaurant OWNER TO nxwdtuddpnukbr;

--
-- Name: food_item; Type: TABLE; Schema: public; Owner: nxwdtuddpnukbr
--

CREATE TABLE "public"."food_item" (
    "id" integer NOT NULL,
    "name" "text" NOT NULL,
    "price" real NOT NULL,
    "menu_id" integer NOT NULL
);


ALTER TABLE public.food_item OWNER TO nxwdtuddpnukbr;

--
-- Name: hours; Type: TABLE; Schema: public; Owner: nxwdtuddpnukbr
--

CREATE TABLE "public"."hours" (
    "day_of_week" "text" NOT NULL,
    "open_time" time without time zone NOT NULL,
    "close_time" time without time zone NOT NULL,
    "fast_food_restaurant_id" integer NOT NULL
);


ALTER TABLE public.hours OWNER TO nxwdtuddpnukbr;

--
-- Name: menu; Type: TABLE; Schema: public; Owner: nxwdtuddpnukbr
--

CREATE TABLE "public"."menu" (
    "id" integer NOT NULL,
    "fast_food_restaurant_id" integer,
    "menu_type" "text"
);


ALTER TABLE public.menu OWNER TO nxwdtuddpnukbr;

--
-- Name: review; Type: TABLE; Schema: public; Owner: nxwdtuddpnukbr
--

CREATE TABLE "public"."review" (
    "id" integer NOT NULL,
    "fast_food_restaurant_id" integer NOT NULL,
    "reviewer_name" "text" NOT NULL,
    "description" "text",
    "rating" real NOT NULL
);


ALTER TABLE public.review OWNER TO nxwdtuddpnukbr;

--
-- Data for Name: fast_food_restaurant; Type: TABLE DATA; Schema: public; Owner: nxwdtuddpnukbr
--

COPY "public"."fast_food_restaurant" ("id", "name", "location", "restaurant_type", "price_range") FROM stdin;
1	McDonalds	Tempe, AZ	American	low
2	Taco Bell	Tempe, AZ	American	low
\.


--
-- Data for Name: food_item; Type: TABLE DATA; Schema: public; Owner: nxwdtuddpnukbr
--

COPY "public"."food_item" ("id", "name", "price", "menu_id") FROM stdin;
1	McDouble	4.12	1
2	McTriple	5.21	1
3	Hamburger Happy Meal	2.49	2
4	4 piece Chicken McNuggets Happy Meal	3.25	2
5	Bacon, Egg & Cheese Biscuit	2	3
6	Sausage McMuffin	2	3
7	Crunchy Taco Supreme	2.29	4
8	Steak Nacho Fries Burrito	5.21	4
9	Kids Meal	2.49	5
10	Bell Breakfast Box	5	6
\.


--
-- Data for Name: hours; Type: TABLE DATA; Schema: public; Owner: nxwdtuddpnukbr
--

COPY "public"."hours" ("day_of_week", "open_time", "close_time", "fast_food_restaurant_id") FROM stdin;
Monday	05:00:00	22:00:00	1
Tuesday	05:00:00	22:00:00	1
Wednesday	05:00:00	22:00:00	1
Thursday	05:00:00	22:00:00	1
Friday	05:00:00	22:00:00	1
Monday	05:00:00	00:00:00	2
Tuesday	05:00:00	00:00:00	2
Wednesday	05:00:00	00:00:00	2
Thursday	05:00:00	00:00:00	2
Friday	05:00:00	00:00:00	2
Saturday	05:00:00	00:00:00	2
\.


--
-- Data for Name: menu; Type: TABLE DATA; Schema: public; Owner: nxwdtuddpnukbr
--

COPY "public"."menu" ("id", "fast_food_restaurant_id", "menu_type") FROM stdin;
1	1	regular
2	1	kids
3	1	breakfast
4	2	regular
5	2	kids
6	2	breakfast
\.


--
-- Data for Name: review; Type: TABLE DATA; Schema: public; Owner: nxwdtuddpnukbr
--

COPY "public"."review" ("id", "fast_food_restaurant_id", "reviewer_name", "description", "rating") FROM stdin;
1	1	Tiffany Day	micky D has pretty solid fries!	4
2	1	Casey Luong	This grub is fairly adequate	4
3	2	Michael Bubble	I was looking for some authentic Mexican cuisine and this was not it peeps	2
4	2	Rosé	This grub is fairly adequate	4
5	1	Tanner Rackow	Yum yum	4
\.


--
-- Name: fast_food_restaurant fast_food_restaurant_pkey; Type: CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."fast_food_restaurant"
    ADD CONSTRAINT "fast_food_restaurant_pkey" PRIMARY KEY ("id");


--
-- Name: food_item food_item_pkey; Type: CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."food_item"
    ADD CONSTRAINT "food_item_pkey" PRIMARY KEY ("id");


--
-- Name: menu menu_pkey; Type: CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."menu"
    ADD CONSTRAINT "menu_pkey" PRIMARY KEY ("id");


--
-- Name: review review_pkey; Type: CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."review"
    ADD CONSTRAINT "review_pkey" PRIMARY KEY ("id");


--
-- Name: food_item food_item_menu_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."food_item"
    ADD CONSTRAINT "food_item_menu_id_fkey" FOREIGN KEY ("menu_id") REFERENCES "public"."menu"("id") ON DELETE CASCADE;


--
-- Name: hours hours_fast_food_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."hours"
    ADD CONSTRAINT "hours_fast_food_restaurant_id_fkey" FOREIGN KEY ("fast_food_restaurant_id") REFERENCES "public"."fast_food_restaurant"("id") ON DELETE CASCADE;


--
-- Name: menu menu_fast_food_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."menu"
    ADD CONSTRAINT "menu_fast_food_restaurant_id_fkey" FOREIGN KEY ("fast_food_restaurant_id") REFERENCES "public"."fast_food_restaurant"("id") ON DELETE CASCADE;


--
-- Name: review review_fast_food_restaurant_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nxwdtuddpnukbr
--

ALTER TABLE ONLY "public"."review"
    ADD CONSTRAINT "review_fast_food_restaurant_id_fkey" FOREIGN KEY ("fast_food_restaurant_id") REFERENCES "public"."fast_food_restaurant"("id") ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

