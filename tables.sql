drop table if exists ers_users
create table ers_users (
	user_id SERIAL primary key,
	username varchar(50) unique not null,
	user_password varchar(50) not null,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(50) not null,
	user_role varchar(50) not null

);

drop table if exists ers_reimbursements
create table ers_reimbursements (
	reimbursement_id serial primary key,
	reimburesment_amount numeric(10,2) not null,
	submitted timestamp not null default current_timestamp,
	resolved timestamp,
	status varchar(50) not null,
	reimbursement_type varchar(50) not null,
	description varchar(500) not null,
	receipt bytea,
	reimbursement_author integer not null,
	reimbursement_resolver integer,
	constraint fk_ers_users_author foreign key (reimbursement_author) references ers_users(user_id),
	constraint fk_ers_users_resolver foreign key (reimbursement_resolver) references ers_users(user_id)

);