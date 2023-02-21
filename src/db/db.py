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

        with open('db/sql/create_tables.sql') as file:
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

    def get_all_tg_id(self, only_live=False):
        if only_live:
            self.cur.execute("SELECT tg_id FROM users WHERE live = True")
        else:
            self.cur.execute("SELECT tg_id FROM users")

        result = self.cur.fetchall()
        result = list(map(lambda x: x[0], result))

        return result

    def set_user_activity(self, tg_id, status):
        self.cur.execute(
                f"UPDATE users SET live = {status} WHERE tg_id = {tg_id}")

    def add_ref_link(self, name_link):
        self.cur.execute("INSERT INTO ref_links(name) VALUES(%s)",
                         (name_link,))

    def remove_ref_link(self, name_link):
        self.cur.execute("DELETE FROM ref_links WHERE name = %s",
                         (name_link,))

    def get_ref_links(self):
        self.cur.execute("SELECT name FROM ref_links")

        result_sql = self.cur.fetchall()

        result = []
        for i in result_sql:
            result.append(i[0])

        return result

    def get_admins_tg_id(self):
        self.cur.execute("SELECT tg_id FROM admins")

        return self.cur.fetchall()[0]


# db = Database('dbname=tmp_v1 user=arthur')
# print(db.get_admins_tg_id())
# print(db.get_all_tg_id())
