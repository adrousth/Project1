let requestTableElement = document.querySelector('#requests-table tbody')
fetch('http://127.0.0.1:8080/requests', {
    'credentials': 'include',
    'method': 'GET'
    
  }).then((res) => {
    res.json().then((data) => {
        console.log(data.requests)
        
        for (let request of data.requests) {
            let requestRow = document.createElement('tr');
            let requestId = document.createElement('td');
            requestId.innerHTML = request.request_id;
            let requestAmount = document.createElement('td');
            requestAmount.innerHTML = "$" + request.amount;
            let requestTimeSumbitted = document.createElement('td');
            requestTimeSumbitted.innerHTML = request.submitted;
            let requestTimeResolved = document.createElement('td');
            requestTimeResolved.innerHTML = request.resolved;
            let requestStatus = document.createElement('td');
            requestStatus.innerHTML = request.status;
            let requestType = document.createElement('td');
            requestType.innerHTML = request.request_type;
            let requestDescription = document.createElement('td');
            requestDescription.innerHTML = request.description;
            let requestReceipt = document.createElement('td')
            requestReceipt.innerHTML = request.receipt

            requestRow.appendChild(requestId);
            requestRow.appendChild(requestAmount);
            requestRow.appendChild(requestTimeSumbitted);
            requestRow.appendChild(requestTimeResolved);
            requestRow.appendChild(requestStatus);
            requestRow.appendChild(requestType);
            requestRow.appendChild(requestDescription);
            requestRow.appendChild(requestReceipt)
            requestTableElement.appendChild(requestRow);
        }

                

    })        
  }).catch((err) => {
    console.log(err);
  });

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