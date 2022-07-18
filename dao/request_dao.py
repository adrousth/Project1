import psycopg
from model.request import Request


class RequestDao:
    def __init__(self):
        self.__connection_string = "host=localhost port=5432 dbname=postgres user=postgres password=password"

    def get_requests_by_status(self, status):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursements"
                            " WHERE status = %s;", (status,))
                requests = []
                for request in cur:
                    requests.append(Request(request[0], request[1], request[2], request[3], request[4], request[5],
                                            request[6], request[7], request[8], request[9]).to_dict())
        return requests

    def get_all_requests(self):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursements")
                requests = []
                for request in cur:
                    requests.append(Request(request[0], request[1], request[2], request[3], request[4], request[5],
                                            request[6], request[7], request[8], request[9]).to_dict())
        return requests

