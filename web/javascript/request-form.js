let amountInput = document.getElementById('amount-input');
let descriptionInput = document.getElementById('description-input');
let typeButtons = document.querySelectorAll('input[name="type"]');
let receipt = document.getElementById('receipt');
let requestSubmitButton = document.getElementById('request-submit-btn');
let formElement = document.getElementById("request-form")

requestSubmitButton.addEventListener('click', () => {
  let selectedRadioButton;
  for (let radioBtn of typeButtons) {
      if (radioBtn.checked) {
          selectedRadioButton = radioBtn
          break;
      }

  }
  let formData = new FormData()
  formData.append("amount", amountInput.value)
  formData.append("type", selectedRadioButton.value)
  formData.append("description", descriptionInput.value)
  formData.append("receipt", receipt.files[0])
  console.log(...formData)
  
  fetch('http://127.0.0.1:8080/requests', {
    'method': 'POST',
    'credentials': 'include',
   
    'body': formData
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

