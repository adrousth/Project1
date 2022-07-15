from dao.request_dao import RequestDao


class RequestService:
    def __init__(self):
        self.request_dao = RequestDao()

    def get_all_requests(self):
        return self.request_dao.get_all_requests()

    def get_requests_by_status(self, status):
        return self.request_dao.get_requests_by_status(status)

