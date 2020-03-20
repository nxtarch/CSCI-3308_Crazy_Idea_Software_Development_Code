SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

CREATE TABLE restaurants(
    restaurant_id SERIAL PRIMARY KEY,
    dish_name VARCHAR(45) NOT NULL,
    description text,
    price DECIMAL(3,2),
    restaurant_type VARCHAR(45)
);

ALTER TABLE restaurants OWNER TO postgres;

CREATE TABLE restaurant_name(
	restaurant_id INT NOT NULL,
	restaurant_name VARCHAR(45) NOT NULL
);

ALTER TABLE restaurant_name OWNER TO postgres;

CREATE TABLE users(
	user_id SERIAL NOT NULL,
	username VARCHAR(45) NOT NULL,
	preferneces VARCHAR(45)
);

ALTER TABLE users OWNER TO postgres;

ALTER TABLE ONLY restaurants
    ADD CONSTRAINT restaurants_pkey PRIMARY KEY (restaurant_id);
	
ALTER TABLE ONLY restaurant_name
    ADD CONSTRAINT restaurant_name_pkey PRIMARY KEY (restaurant_id);
	
ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
	
ALTER TABLE ONLY restaurant_name
    ADD CONSTRAINT restaurant_name_restaurant_id_fkey FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) ON UPDATE CASCADE ON DELETE RESTRICT;
