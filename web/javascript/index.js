console.log("hello world")

fetch('http://127.0.0.1:8080/get-user')
  .then(response => response.json())
  .then(data => console.log(data));

console.log(response)
