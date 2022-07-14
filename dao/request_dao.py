import psycopg


class RequestDao:
    def __init__(self):
        self.__connection_string = "host=localhost port=5432 dbname=postgres user=postgres password=password"

    def get_requests_by_status(self, status):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursements"
                            " WHERE status = %s;", (status,))
                requests = cur.fetchall()
        return requests
