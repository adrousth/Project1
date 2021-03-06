from dao.request_dao import RequestDao
from exception.exceptions import *


class RequestService:
    def __init__(self):
        self.request_dao = RequestDao()

    def get_all_requests(self):
        return self.request_dao.get_all_requests()

    def get_requests_by_status(self, status):
        return self.request_dao.get_requests_by_status(status)

    def add_new_request(self, data, receipt, user_id):
        print(receipt)
        try:
            amount = data['amount']
            description = data['description']
            request_type = data['type']
        except KeyError as e:
            raise InvalidParameterError(f"{e} was not found please retry.")
        try:
            amount = float(amount)
        except ValueError as e:
            raise InvalidParameterError("amount is not a number please retry.")

        if amount <= 0:
            raise InvalidParameterError("amount must be greater than zero")
        if amount >= 100000000:
            raise InvalidParameterError("amount must be less than 100,000,000")
        if len(description) > 500:
            raise InvalidParameterError("description cannot be more than 500 characters long")
        if request_type not in ('lodging', 'food', 'travel', 'other'):
            raise InvalidParameterError("request type must be lodging, food, travel or other")

        returned_request = self.request_dao.add_new_request(amount, description, request_type, receipt, user_id)
        if returned_request is None:
            raise RequestNotAddedError("Request was not added.")
        return returned_request

    def get_all_requests_for_user(self, user_id):
        return self.request_dao.get_all_requests_for_user(user_id)

    def get_request_by_id(self, request_id):
        request = self.request_dao.get_request_by_id(request_id)
        if request is None:
            raise RequestNotFoundError(f"request with id of {request_id} was not found.")
        return request

    def update_requests(self, data, user_id):
        if data is None or len(data) == 0:
            raise InvalidParameterError("No requests selected to update")
        for data_point in data:
            if data[data_point] not in ("approved", "denied"):
                raise InvalidParameterError("Can only change status to approved or denied")
        updated_requests = self.request_dao.update_requests(data, user_id)
        return updated_requests



