CREATE TABLE public.stocks
(
    stock_id SERIAL,
    cdd_name text not null,
    actual_stock integer NOT NULL,
    CONSTRAINT stock_pkey PRIMARY KEY (stock_id)
)


INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('AC - RIO BRANCO' ::text, ' 379'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('AL - MACEIO' ::text, ' 98'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('AM - MANAUS' ::text, ' 220'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('AP - MACAPA' ::text, ' 116'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('BA - ALAGOINHAS' ::text, ' 49'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('BA - BUNKER SALVADOR' ::text, ' 371'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('BA - FEIRA DE SANTANA' ::text, ' 132'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('BA - VITORIA DA CONQUISTA' ::text, ' 242'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('CE - CASCAVEL' ::text, ' 153'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('CE - FORTALEZA' ::text, ' 236'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('CE - JUAZEIRO DO NORTE' ::text, ' 399'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('CE - SOBRAL' ::text, ' 362'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('DF - BRASILIA' ::text, ' 304'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('DF - PLANALTINA' ::text, ' 299'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('ES - ARACRUZ' ::text, ' 100'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('ES - CACHOEIRO DE ITAPEMIRIM' ::text, ' 287'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('ES - GUARAPARI' ::text, ' 304'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('ES - VITORIA' ::text, ' 160'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('GO - CATALAO' ::text, ' 187'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('GO - GOIANIA' ::text, ' 396'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('GO - ITUMBIARA' ::text, ' 286'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('GO - RIO VERDE' ::text, ' 153'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('GO - VALPARAISO DE GOIAS' ::text, ' 28'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MA - SAO LUIS' ::text, ' 193'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MG - ALFENAS' ::text, ' 33'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MG - BELO HORIZONTE' ::text, ' 94'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MG - JUIZ DE FORA' ::text, ' 185'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MG - PATOS DE MINAS' ::text, ' 367'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MG - POÃ‡OS DE CALDAS' ::text, ' 75'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MG - POUSO ALEGRE' ::text, ' 36'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MS - CAMPO GRANDE' ::text, ' 66'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MS - DOURADOS' ::text, ' 274'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MT - CUIABA' ::text, ' 241'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('MT - PRIMAVERA DO LESTE' ::text, ' 277'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PA - CASTANHAL' ::text, ' 299'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PA - MARABA' ::text, ' 52'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PB - CAMPINA GRANDE' ::text, ' 360'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PB - JOAO PESSOA' ::text, ' 12'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PB - PATOS' ::text, ' 130'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PE - BUNKER RECIFE 1' ::text, ' 58'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PE - CARUARU' ::text, ' 130'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PE - GRAVATA' ::text, ' 309'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PE - JABOATAO DOS GUARARAPES' ::text, ' 336'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PE - OLINDA' ::text, ' 293'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PE - VALE DO SAO FRANCISCO' ::text, ' 358'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PI - TERESINA' ::text, ' 322'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PR - APUCARANA' ::text, ' 394'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PR - CURITIBA' ::text, ' 17'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PR - FOZ DO IGUAÃ‡U' ::text, ' 80'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PR - LONDRINA' ::text, ' 365'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('PR - MARINGA' ::text, ' 11'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - BANGU' ::text, ' 258'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - BUNKER 1' ::text, ' 280'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - CABO FRIO' ::text, ' 299'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - CAMPO GRANDE' ::text, ' 73'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - CAMPOS' ::text, ' 167'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - DUQUE DE CAXIAS' ::text, ' 393'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - ITAPERUNA' ::text, ' 368'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - MACAE' ::text, ' 239'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - NITEROI' ::text, ' 72'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - RECREIO' ::text, ' 60'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - RESENDE' ::text, ' 125'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - RIO DAS OSTRAS' ::text, ' 156'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - SANTA CRUZ' ::text, ' 224'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - SAO GONÃ‡ALO' ::text, ' 240'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - SAQUAREMA' ::text, ' 173'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RJ - VOLTA REDONDA' ::text, ' 360'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RN - NATAL' ::text, ' 344'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RO - PORTO VELHO' ::text, ' 388'::integer);
INSERT INTO public.stocks (cdd_name, actual_stock) VALUES ('RS - CAXIAS DO SUL' ::text, ' 137'::integer);


CREATE TABLE public.tickets
(
    ticket_id SERIAL,
    ticket_date DATE not null,
	ticket_base text not null,
    ticket_country_state text not null,
	ticket_consumption integer,
    CONSTRAINT ticket_pkey PRIMARY KEY (ticket_id)
)



