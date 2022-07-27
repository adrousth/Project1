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

    # TODO make sure add user to reimbursement
    def add_new_request(self, amount, description, request_type, receipt, user_id):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:

                cur.execute("INSERT INTO ers_reimbursements (reimbursement_amount, description, reimbursement_type,"
                            "receipt, reimbursement_author) VALUES (%s, %s, %s, %s, %s) RETURNING *",
                            (amount, description, request_type, receipt, user_id))
                request = cur.fetchone()

        returned_request = Request(request[0], request[1], request[2], request[3], request[4], request[5],
                                   request[6], request[7], request[8], request[9]).to_dict()

        return returned_request

    def get_all_requests_for_user(self, user_id):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursements WHERE reimbursement_author = %s;", (user_id,))
                requests = []
                for request in cur:

                    requests.append(Request(request[0], request[1], request[2], request[3], request[4], request[5],
                                            request[6], request[7], request[8], request[9]).to_dict())

        return requests

    def get_request_by_id(self, request_id):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM ers_reimbursements WHERE reimbursement_id = %s;", (request_id,))
                request = cur.fetchone()

        return request

    def update_requests(self, data, user_id):
        with psycopg.connect(self.__connection_string) as conn:
            with conn.cursor() as cur:
                for data_point in data:
                    cur.execute("UPDATE ers_reimbursements"
                                " SET status = %s, reimbursement_resolver = %s, resolved = current_timestamp"
                                " WHERE reimbursement_id = %s RETURNING *", (data[data_point], user_id, data_point))
                    requests = []
                    # for request in cur:
                    #     requests.append(Request(request[0], request[1], request[2], request[3], request[4], request[5],
                    #                             request[6], request[7], request[8], request[9]).to_dict())
                    cur.execute("SELECT * FROM ers_reimbursements")
                    for request in cur:
                        requests.append(Request(request[0], request[1], request[2], request[3], request[4], request[5],
                                                request[6], request[7], request[8], request[9]).to_dict())

        return requests


