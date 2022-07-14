import psycopg


class UserDao:
    def __init__(self):
        self.__connection_string = "host=localhost port=5432 dbname=postgres user=postgres password=password"

    def get_user_by_username(self, username):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, username, first_name, last_name, email, user_role FROM ers_users"
                            " WHERE username = %s;", (username,))
                user = cur.fetchone()
        return user
