let requestTableElement = document.querySelector('#requests-table tbody')
let requests
let changeStatusButton = document.getElementById('update-statuses')
fetch('http://127.0.0.1:8080/manager/requests', {
    'credentials': 'include',
    'method': 'GET'
    
  }).then((res) => {
    res.json().then((data) => {
        console.log(data.requests)
        requests = data.requests
        displayRequests(requests, 'all')
    })        
  }).catch((err) => {
    console.log(err);
  });

let statusElement = document.getElementById("status")
statusElement.addEventListener("change", () => {
  let filter = statusElement.options[statusElement.selectedIndex].value
  displayRequests(requests, filter)

})


function displayRequests(requests, filter) {
  requestTableElement.innerHTML = ''
  // = '<select name="status"><option value="pending">Pending</option><option value="approved">Approved</option><option value="denied">Denied</option></select>'

  // let statusSelect2 = '<button class="button is-link">Update Status</button>'
  for (let request of requests) {
    if (request.status == filter || filter == 'all') {
      
      
    
      let requestRow = document.createElement('tr');
      let requestId = document.createElement('td');
      requestId.innerHTML = request.request_id;
      let requestAuthorId = document.createElement('td');
      requestAuthorId.innerHTML = request.author;
      let requestAmount = document.createElement('td');
      requestAmount.innerHTML = "$" + request.amount;
      let requestTimeSumbitted = document.createElement('td');
      requestTimeSumbitted.innerHTML = request.submitted;
      let requestTimeResolved = document.createElement('td');
      requestTimeResolved.innerHTML = request.resolved;
      let requestResolver = document.createElement('td')
      requestResolver.innerHTML = request.resolver
      let requestStatus = document.createElement('td');
      if (request.status == 'pending') {
        
        let statusSelect = document.createElement('select')
        statusSelect.name = 'status'
        statusSelect.class = 'status'
        statusSelect.id = request.request_id
        
        let statusOptionPending = document.createElement('option')
        statusOptionPending.innerHTML = 'pending'
        statusOptionPending.value = 'pending'
        
        statusSelect.appendChild(statusOptionPending)
        let statusOptionApproved = document.createElement('option')
        statusOptionApproved.innerHTML = 'approved'
        statusOptionApproved.value = 'approved'
        
        statusSelect.appendChild(statusOptionApproved)
        let statusOptionDenied = document.createElement('option')
        statusOptionDenied.innerHTML = 'denied'
        statusOptionDenied.value = 'denied'
        
        statusSelect.appendChild(statusOptionDenied)
        requestStatus.appendChild(statusSelect.cloneNode(true));
      } else {
        requestStatus.innerHTML = request.status;
      }
              
      let requestType = document.createElement('td');
      requestType.innerHTML = request.request_type;
      let requestDescription = document.createElement('td');
      requestDescription.innerHTML = request.description;


      requestRow.appendChild(requestId);
      requestRow.appendChild(requestAuthorId);
      requestRow.appendChild(requestAmount);
      requestRow.appendChild(requestTimeSumbitted);
      requestRow.appendChild(requestTimeResolved);
      requestRow.appendChild(requestResolver)
      requestRow.appendChild(requestStatus);
      requestRow.appendChild(requestType);
      requestRow.appendChild(requestDescription);
      requestTableElement.appendChild(requestRow);
  }
  '<div class="field"><div class="control"><button id="update-statuses" class="button is-link">Update Statuses</button></div></div>'
  // Array.from(document.getElementsByClassName("button")).forEach(element => {
  //   element.addEventListener("click", () => {
  //     console.log("hello")
  //   })
  // });
  }
}

changeStatusButton.addEventListener('click', () => {
  let selectElements = document.getElementsByName('status')
  let requestsToChange = {}
  for (element of selectElements) {   
    if (element.options[element.selectedIndex].value != "pending") {
      requestsToChange[element.id] = element.options[element.selectedIndex].value
    }
  }
  console.log(requestsToChange)
  fetch('http://127.0.0.1:8080/update-requests', {
      'method': 'POST',
      'credentials': 'include',
      'headers': {
          'Content-Type': 'application/json' 
      },
      'body': JSON.stringify(requestsToChange)
    }).then((res) => {
      console.log(res)
      if (res.status == 201) {
        res.json().then((data) => {
          requests = data.requests
          console.log(requests)
          displayRequests(requests, 'all')
        })
    }
      
})})

let logoutButton = document.getElementById('log-out');
logoutButton.addEventListener('click', () => {
    fetch('http://127.0.0.1:8080/logout', {
        'method': 'POST',
        'credentials': 'include',
        
        }).then((res) => {
            if (res.status == 200) {
              window.location.href = '../html/login.html'
            }
          })})