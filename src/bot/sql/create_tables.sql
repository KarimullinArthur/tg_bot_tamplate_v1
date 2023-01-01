CREATE TABLE IF NOT EXISTS users(
  id serial,
  tg_id bigint,
  acitve boolean DEFAULT TRUE
)
