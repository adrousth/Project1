let amountInput = document.getElementById('amount-input');
let descriptionInput = document.getElementById('description-input');
let typeButtons = document.querySelectorAll('input[name="type"]');
let requestSubmitButton = document.getElementById('request-submit-btn');

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

        // res.json().then((data) => {
        //     let registrationErrorMessagesDiv = document.getElementById('registration-error-messages')
        //     registrationErrorMessagesDiv.innerHTML = '';

        //     let errorMessages = data.messages;
        //     for (let errorMessage of errorMessages) {
        //         let errorElement = document.createElement('p');
        //         errorElement.innerHTML = errorMessage;
        //         errorElement.style.color = 'red';
        //         errorElement.style.fontWeight = 'bold';

        //         registrationErrorMessagesDiv.appendChild(errorElement);
        //     }

        // });

    }
}).catch((err) => {
  console.log(err);
})
});


