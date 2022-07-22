let usernameInput = document.getElementById('username-login-input');
let passwordInput = document.getElementById('password-login-input');
let loginButton = document.getElementById('login-btn')


loginButton.addEventListener('click', () => {
    
    fetch('http://127.0.0.1:8080/login', {
      'method': 'POST',
      'credentials': 'include',
      'headers': {
          'Content-Type': 'application/json' 
      },
      'body': JSON.stringify({
          "username": usernameInput.value,
          "password": passwordInput.value,
      })
  }).then((res) => {
    if (res.status == 200) {
        res.json().then((data) => {
            if (data.user_info.user_role == "employee") {
                window.location.href = '../html/user.html'
            } else if (data.user_info.user_role == "finance_manager") {
                window.location.href = '../html/manager.html'
            }
        })
    } else if (res.status == 400) {
  
          res.json().then((data) => {
              let loginErrorMessageDiv = document.getElementById('login-error-messages')
              loginErrorMessageDiv.innerHTML = '';
  
              let errorMessage = data.message;
          
              let errorElement = document.createElement('p');
              errorElement.innerHTML = errorMessage;
              errorElement.style.color = 'red';
              errorElement.style.fontWeight = 'bold';
  
              loginErrorMessageDiv.appendChild(errorElement);
              
  
          });
  
      }
  }).catch((err) => {
    console.log(err);
  })
  });