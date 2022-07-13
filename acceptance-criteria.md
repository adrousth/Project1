## User Stories
* Login (2 user stories)
        - given I am at the login page, when I input a valid username and invalid password, then I should receive a message say 'invalid username and/or password'
        - given I am at the login page, when I input a invalid username, then I should receive a message say 'invalid username and/or password'
    - As an employee, I want to be able to login, so that I can view my past requests and add new reimbursement requests
        - given I am at the login page, when I input a valid username and valid password for an employee, then I should be redirected to that employee's user page.
    - As a finance manager, I want to be able to login, so that I can manage and view all reimbursements for all employees
        - given I am at the login page, when I input a valid username and valid password for a finance manager, then I should be redirected to that finance manager's user page.
* View reimbursement (2 user stories)
    - As an employee, I want to be able to view all of my reimbursements, so that I can see the data of all of my reimbursement requests and the status of them (pending, approved, denied)
        - given I am an employee who is logged in, when I am on my user page, then all of my reimburesement requests and their status should be displayed/accessable



    - As a finance manager, I want to be able to view ALL employee reimbursements, so that I can see the data of the entire company's reimbursement requests and approve/deny the requests that are pending
        - given I am a finance manager who is logged in, when I am on my user page, then all employees' reimbursement requests should be displayed/accessable




* Filter reimbursement requests by status (2 user stories)
    - As an employee, I want to be able to filter my past requests by status (approved, denied, pending), so that I can more easily view them
        - given I am an employee who is logged in and on my user page, when I chose a filter by status for requests, then all my requests with that status should be displayed/accessable




    - As a finance manager, I want to be able to filter all past requests by all employees by status (approved, denied, pending), so that I can more easily view them
        - given I am a finance manager who is logged in and on my user page, when i chose a filter by status for requests, then all employees' requests with that status should be displayed/accessable



* Add reimbursement request (1 user story)
    - As an employee, I want to be able to add a reimbursement request, so that they can either be approved or denied by a finance manager
        - given I am an employee who is logged in and at the reimbursement request form, when I input valid information for a reimbursement request in the form and submit it, then a new request should be added to the database with the given information with the current time stamp and a status of pending for the employee.
        - given I am an employee who is logged in and at the reimbursement request form, when I input invalid information for a reimbursement request in the form and submit it, then I should receive a message which says why the given information is not valid.



* Approve/deny reimbursement request (1 user story)
    - As a finance manager, I want to be able to approve/deny a pending reimbursement request, so that I can proceed with transferring money to the employee if the reimbursement is approved or not if it's denied
        - given I am a finance manager who is logged in and looking at a request, when the request status is pending, then I should be able to change the status to denied or approved.




