import psycopg2


class Database:
    """Connect database.
    Keyword arguments:
    db_name="dbname=name_your_database user=your_user"
    """

    def __init__(self, dns):
        self.conn = psycopg2.connect(dns)
        self.cur = self.conn.cursor()

        self.conn.autocommit = True

        with open('sql/create_tables.sql') as file:
            self.cur.execute(file.read())

    def add_user(self, tg_id, ref_link, date_reg):
        self.cur.execute(
            "INSERT INTO users(tg_id, ref_link, date_reg) VALUES(%s, %s, %s)",
            (tg_id, ref_link, date_reg))

    def user_exists(self, tg_id):
        """Checks whether the user is registered in the database.
        return True if registred.
        """
        self.cur.execute("SELECT * FROM users WHERE tg_id = %s",
                         (tg_id,))

        result = self.cur.fetchall()
        return bool(len(result))


db = Database('dbname=tmp_v1 user=arthur')
