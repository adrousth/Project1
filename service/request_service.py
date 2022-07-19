from dao.request_dao import RequestDao
from exception.exceptions import *


class RequestService:
    def __init__(self):
        self.request_dao = RequestDao()

    def get_all_requests(self):
        return self.request_dao.get_all_requests()

    def get_requests_by_status(self, status):
        return self.request_dao.get_requests_by_status(status)

    # TODO make sure user exists!
    def add_new_request(self, data, user_id):
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

        returned_request = self.request_dao.add_new_request(amount, description, request_type, user_id)
        if returned_request is None:
            raise RequestNotAddedError("Request was not added.")
        return returned_request

    def get_all_requests_for_user(self, user_id):
        return self.request_dao.get_all_requests_for_user(user_id)
