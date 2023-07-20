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
            result.append(i[0].strip())

        return result

    def get_count_user_ref_link(self, name_link):
        self.cur.execute("SELECT COUNT(id) FROM users WHERE ref_link = %s",
                         (name_link,))

        result = self.cur.fetchone()
        return result[0]

    def edit_text(self, data, message_id, chat_id):
        self.cur.execute(
                f"UPDATE texts SET message_id = '{message_id}'\
                        WHERE data = '{data}'")
        self.cur.execute(
                f"UPDATE texts SET chat_id = '{chat_id}'\
                        WHERE data = '{data}'")

    def get_text(self, target):
        self.cur.execute(f"SELECT (message_id, chat_id) FROM texts\
                            WHERE data = '{target}'")

        result_sql = self.cur.fetchone()
        result_sql = tuple(result_sql[0][1:-1].split(','))

        result = {
                'message_id': result_sql[0],
                'chat_id': result_sql[1]
                }

        return result

    def add_sponsor(self, tg_id, link, name):
        self.cur.execute("INSERT INTO sponsors(tg_id, link, name)\
                            VALUES(%s, %s, %s)",
                         (tg_id, link, name))

    def delete_sponsor(self, name):
        self.cur.execute(f"DELETE FROM sponsors WHERE name = '{name}'")

    def get_sponsors(self):
        self.cur.execute("SELECT (tg_id, link, name) FROM sponsors")

        result_sql = self.cur.fetchall()

        result = []
        for x in range(len(result_sql)):
            seq = result_sql[x][0][1:-1]
            list = seq.split(',')
            dic = {
                    'tg_id': list[0],
                    'link': list[1],
                    'name': list[2]
            }
            result.append(dic)

        return result

    def get_admins_tg_id(self):
        self.cur.execute("SELECT tg_id FROM admins")

        result = self.cur.fetchall()
        result = list(map(lambda x: x[0], result))

        return result

    def add_admin(self, tg_id):
        self.cur.execute("INSERT INTO admins (tg_id) VALUES (%s)", (tg_id,))

    def remove_admin(self, tg_id):
        self.cur.execute(f"DELETE FROM admins WHERE tg_id = {tg_id}")

    def add_img(self, file_id, name):
        self.cur.execute("INSERT INTO file_id(file_id, name) VALUES(%s, %s)",
                         (file_id, name))

    def get_file_id(self, name):
        self.cur.execute("SELECT file_id FROM file_id WHERE name = %s",
                         (name,))

        result = self.cur.fetchone()
        return result[0]


# db = Database('dbname=tmp_v1 user=arthur')
