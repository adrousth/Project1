let usernameInput = document.getElementById('username-login-input');
let passwordInput = document.getElementById('password-login-input');
let loginButton = document.getElementById('login-btn')


loginButton.addEventListener('click', () => {
    
    fetch('http://127.0.0.1:8080/login', {
      'method': 'POST',
      
      'headers': {
          'Content-Type': 'application/json' 
      },
      'body': JSON.stringify({
          "username": usernameInput.value,
          "password": passwordInput.value,
      })
  }).then((res) => {
      if (res.status == 200) {
  
          window.location.href = '../html/success.html'
      
      } else if (res.status == 400) {
  
          res.json().then((data) => {
              let registrationErrorMessagesDiv = document.getElementById('login-error-messages')
              registrationErrorMessagesDiv.innerHTML = '';
  
              let errorMessage = data.message;
          
              let errorElement = document.createElement('p');
              errorElement.innerHTML = errorMessage;
              errorElement.style.color = 'red';
              errorElement.style.fontWeight = 'bold';
  
              registrationErrorMessagesDiv.appendChild(errorElement);
              
  
          });
  
      }
  }).catch((err) => {
    console.log(err);
  })
  });