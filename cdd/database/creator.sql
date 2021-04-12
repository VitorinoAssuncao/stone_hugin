CREATE TABLE IF NOT EXISTS public.stocks
(
    stock_id SERIAL,
    stock_base text not null,
    stock_value integer NOT NULL,
    CONSTRAINT stock_pkey PRIMARY KEY (stock_id)
);

CREATE TABLE IF NOT EXISTS public.tickets
(
    ticket_id SERIAL,
    ticket_date DATE not null,
	ticket_base text not null,
    ticket_country_state text not null,
	ticket_consumption integer,
    CONSTRAINT ticket_pkey PRIMARY KEY (ticket_id)
);
