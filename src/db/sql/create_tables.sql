CREATE TABLE IF NOT EXISTS users(
  id serial,
  tg_id bigint,
  live boolean DEFAULT TRUE,
  date_reg timestamp,
  ref_link text
);

CREATE TABLE IF NOT EXISTS ref_links(
  id serial,
  name char(25)
);

CREATE TABLE IF NOT EXISTS sponsors(
  id serial,
  name text,
  link text,
  tg_id bigint
);

CREATE TABLE IF NOT EXISTS admins(
  id serial,
  tg_id bigint
);
