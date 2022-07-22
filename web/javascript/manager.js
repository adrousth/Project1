let requestTableElement = document.querySelector('#requests-table tbody')
let requests
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
  let statusSelect = document.createElement('select')
  statusSelect.name = 'status'
  statusSelect.onchange
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
  // Array.from(document.getElementsByClassName("button")).forEach(element => {
  //   element.addEventListener("click", () => {
  //     console.log("hello")
  //   })
  // });
  }
}


