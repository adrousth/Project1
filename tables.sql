drop table if exists ers_users
create table ers_users (
	user_id SERIAL primary key,
	username varchar(50) unique not null,
	user_password varchar(50) not null,
	first_name varchar(50),
	last_name varchar(50),
	email varchar(50) unique not null,
	user_role varchar(50) not null

);

drop table if exists ers_reimbursements;
create table ers_reimbursements (
	reimbursement_id serial primary key,
	reimbursement_amount numeric(10,2) not null,
	submitted timestamp not null default current_timestamp,
	resolved timestamp,
	status varchar(50) not null default 'pending',
	reimbursement_type varchar(50) not null,
	description varchar(500) not null,
	receipt bytea,
	reimbursement_author integer not null,
	reimbursement_resolver integer,
	constraint fk_ers_users_author foreign key (reimbursement_author) references ers_users(user_id),
	constraint fk_ers_users_resolver foreign key (reimbursement_resolver) references ers_users(user_id)

);

create table ers_statuses (
	status varchar(50) primary key
);

insert into ers_statuses
values
('pending'),
('approved'),
('denied');

select * from ers_statuses;

create table ers_types (
	reimbursement_type varchar(50) primary key 
);

insert into ers_types
values
('lodging'),
('travel'),
('food'),
('other');

select * from ers_types;


insert into ers_users (username, user_password, first_name, last_name, email, user_role)
values
('adrousth', 'foobar', 'Alex', 'Drousth', 'adrousth@gmail.com', 'employee'),
('steve245', 'foobar1', 'Steve', 'Smith', 'stevey@email.net', 'employee'),
('johnnyboy', 'foobar2', 'John', 'Boy', 'jboy@something.gov', 'employee'),
('jsmith', 'foobar3', 'Joe', 'Smith', 'jsmith@here.com', 'finance_manager'),
('btables', 'foobar', 'Bobby', 'Tables', 'btables@here.com', 'finance_manager');

select * from ers_users where username = 'adrousth';

insert into ers_reimbursements (reimbursement_amount, reimbursement_type, description, reimbursement_author)
values
(150.00, 'lodging', 'hotel stay', 1),
(200.00, 'food', 'mcdonalds', 2),
(50.00, 'travel', 'taxi', 2),
(10.50, 'other', 'pens', 3);



select * from ers_reimbursements;