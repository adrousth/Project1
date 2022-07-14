

# 	user_id SERIAL primary key,
# 	username varchar(50) unique not null,
# 	user_password varchar(50) not null,
# 	first_name varchar(50),
# 	last_name varchar(50),
# 	email varchar(50) unique not null,
# 	user_role varchar(50) not null
class User:
    def __init__(self, user_id, username, first_name, last_name, email, user_role):
        self.user_id = user_id
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.user_role = user_role

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "user_role": self.user_role
        }