--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

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
-- Name: airport; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.airport (
    id integer NOT NULL,
    name character varying(255),
    city character varying(255),
    country character varying(255)
);


ALTER TABLE public.airport OWNER TO postgres;

--
-- Name: airport_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.airport_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.airport_id_seq OWNER TO postgres;

--
-- Name: airport_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.airport_id_seq OWNED BY public.airport.id;


--
-- Name: flight; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.flight (
    id integer NOT NULL,
    flight_number character varying(20) NOT NULL,
    price integer NOT NULL,
    datetime timestamp with time zone NOT NULL,
    from_airport_id integer,
    to_airport_id integer
);


ALTER TABLE public.flight OWNER TO postgres;

--
-- Name: flight_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.flight_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.flight_id_seq OWNER TO postgres;

--
-- Name: flight_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.flight_id_seq OWNED BY public.flight.id;


--
-- Name: airport id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.airport ALTER COLUMN id SET DEFAULT nextval('public.airport_id_seq'::regclass);


--
-- Name: flight id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flight ALTER COLUMN id SET DEFAULT nextval('public.flight_id_seq'::regclass);


--
-- Data for Name: airport; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.airport (id, name, city, country) FROM stdin;
1	(Шереметьево)	Москва	Россия
2	(Пулково)	Санкт-Петербург	Россия
3	(Адлер)	Сочи	Россия
4	(им.Чкалова)	Нижний Новгород	Россия
5	(Домодедово)	Москва	Россия
\.


--
-- Data for Name: flight; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.flight (id, flight_number, price, datetime, from_airport_id, to_airport_id) FROM stdin;
1	AFL031	1500	2026-10-08 20:00:00+00	2	1
2	SU1226	4800	2026-09-09 12:00:00+00	1	4
3	S72046	3900	2026-08-06 20:00:00+00	3	1
4	SU6190	5600	2026-08-15 06:00:00+00	4	1
5	S72051	6700	2026-08-20 20:00:00+00	2	4
6	SU6039	8500	2026-08-13 20:00:00+00	5	2
7	S72053	2500	2026-08-14 20:00:00+00	1	2
8	U6-256	3700	2026-08-14 20:30:00+00	1	3
9	SU1890	7400	2026-08-14 18:00:00+00	3	4
10	U6-2803	3300	2026-12-31 20:00:00+00	4	3
11	AFL032	1500	2026-10-08 20:00:00+00	2	1
12	SU1227	4800	2026-09-09 12:00:00+00	5	4
13	S72047	3900	2026-08-06 20:00:00+00	3	1
14	SU6191	5600	2026-08-15 06:00:00+00	4	5
15	S72052	6700	2026-08-20 20:00:00+00	2	4
16	SU6040	8500	2026-08-13 20:00:00+00	3	2
17	S72054	2500	2026-08-14 20:00:00+00	1	2
18	U6-257	3700	2026-08-14 20:30:00+00	5	3
19	SU1891	7400	2026-08-14 18:00:00+00	3	4
20	U6-2804	3300	2026-12-31 20:00:00+00	4	3
21	AFL033	1500	2026-10-08 20:00:00+00	2	5
22	SU1228	4800	2026-09-09 12:00:00+00	1	4
23	S72048	3900	2026-08-06 20:00:00+00	3	1
24	SU6192	5600	2026-08-15 06:00:00+00	4	5
25	S72062	6700	2026-08-20 20:00:00+00	2	4
\.


--
-- Name: airport_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.airport_id_seq', 5, true);


--
-- Name: flight_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.flight_id_seq', 25, true);


--
-- Name: airport airport_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.airport
    ADD CONSTRAINT airport_pkey PRIMARY KEY (id);


--
-- Name: flight flight_flight_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flight
    ADD CONSTRAINT flight_flight_number_key UNIQUE (flight_number);


--
-- Name: flight flight_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flight
    ADD CONSTRAINT flight_pkey PRIMARY KEY (id);


--
-- Name: ix_airport_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_airport_id ON public.airport USING btree (id);


--
-- Name: ix_flight_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_flight_id ON public.flight USING btree (id);


--
-- Name: flight flight_from_airport_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flight
    ADD CONSTRAINT flight_from_airport_id_fkey FOREIGN KEY (from_airport_id) REFERENCES public.airport(id);


--
-- Name: flight flight_to_airport_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flight
    ADD CONSTRAINT flight_to_airport_id_fkey FOREIGN KEY (to_airport_id) REFERENCES public.airport(id);


--
-- PostgreSQL database dump complete
--

