const axios = require('axios')


axios.get('http://jsonplaceholder.typicode.com/posts')
  .then(function (response){ // XHR 요청에 대해 처음으로 받은 promise 객체의 모습이 response
    console.log(response)
  })
  .catch(function(error){ // 요청이 잘못 되었을 때
    console.log(error) // axios가 만들어준 에러 코드가 뜬다.
  })


  axios.get('http://jsonplaceholder.typicode.com/posts')
  .then(response => { // 보통 axios는 화살표 함수 써도 중괄호는 안 없앰.
    console.log(response)
  })
  .catch(error => { 
    console.log(error)
  })

  