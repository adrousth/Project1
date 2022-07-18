fetch('http://127.0.0.1:8080/login-status', {
    'credentials': 'include',
    'method': 'GET',


  }).then((res) => {
    res.json().then((data) => {
        console.log(data.login_status)
    })
  
          
  }).catch((err) => {
    console.log(err);
  })
  ;