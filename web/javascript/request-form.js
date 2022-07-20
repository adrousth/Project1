let amountInput = document.getElementById('amount-input');
let descriptionInput = document.getElementById('description-input');
let typeButtons = document.querySelectorAll('input[name="type"]');
let requestSubmitButton = document.getElementById('request-submit-btn');
let logoutButton = document.getElementById('log-out');

requestSubmitButton.addEventListener('click', () => {
  let selectedRadioButton;
  for (let radioBtn of typeButtons) {
      if (radioBtn.checked) {
          selectedRadioButton = radioBtn
          break;
      }

  }
  fetch('http://127.0.0.1:8080/requests', {
    'method': 'POST',
    'credentials': 'include',
    'headers': {
        'Content-Type': 'application/json' 
    },
    'body': JSON.stringify({
        "amount": amountInput.value,
        "type": selectedRadioButton.value,
        "description": descriptionInput.value,
    })
}).then((res) => {
    if (res.status == 201) {

        window.location.href = '../html/success.html'
    
    } else if (res.status == 400) {

        
        res.json().then((data) => {
            let errorMessageDiv = document.getElementById("request-error-messages");
            let message = data.message;
            errorMessageDiv.innerHTML = "";
            let errorElement = document.createElement('p')
            errorElement.innerHTML = message
            
            errorMessageDiv.appendChild(errorElement)

        });

    }
}).catch((err) => {
  console.log(err);
})
});



