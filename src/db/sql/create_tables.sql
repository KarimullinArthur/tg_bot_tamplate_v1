CREATE TABLE IF NOT EXISTS users(
  id serial,
  tg_id bigint,
  acitve boolean DEFAULT TRUE,
  date_reg timestamp,
  ref_link text
);

CREATE TABLE IF NOT EXISTS ref_links(
  id serial,
  name char(25)
);
