
#   reimbursement_id serial primary key,
# 	reimbursement_amount numeric(10,2) not null,
# 	submitted timestamp not null default current_timestamp,
# 	resolved timestamp,
# 	status varchar(50) not null,
# 	reimbursement_type varchar(50) not null,
# 	description varchar(500) not null,
# 	receipt bytea,
# 	reimbursement_author integer not null,
# 	reimbursement_resolver integer,
# 	constraint fk_ers_users_author foreign key (reimbursement_author) references ers_users(user_id),
# 	constraint fk_ers_users_resolver foreign key (reimbursement_resolver) references ers_users(user_id)
class Request:
    def __init__(self, request_id, amount, submitted, resolved, status, request_type, description, receipt, author, resolver):
        self.request_id = request_id
        self.amount = amount
        self.submitted = submitted
        self.resolved = resolved
        self.status = status
        self.request_type = request_type
        self.description = description
        self.receipt = receipt
        self.author = author
        self.resolver = resolver

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "amount": self.amount,
            "submitted": self.submitted,
            "resolved": self.resolved,
            "status": self.status,
            "request_type": self.request_type,
            "description": self.description,
            "receipt": self.receipt,
            "author": self.author,
            "resolver": self.resolver
        }



