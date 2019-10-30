// Array Helper Method

// 5. .find(callback())
// 주어진 콜백 함수를 만족하는 첫번째 요소의 값을 반환.
// 없다면 undefined를 반환
// 조건에 맞는 인덱스가 아니라 요소 자체를 원할 때 사용

// for
var users = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]

// 원하는 object를 찾아도 users를 끝까지 돌게 된다.
for (var i = 0; i < users.length; i++){
  if (users[i].name === 'Tony Stark') {
    user = users[i]
    break // break를 안 걸면 원하는 조건에 도달해도 범위 끝까지 돌게 됨.
  }
}
console.log(user) // 45 tony stark, break 안 걸면 23, tony stark

//find
const USERS = [
  { name: 'Tony Stark', age: 45 },
  { name: 'Steve Rogers', age: 32 },
  { name: 'Thor', age: 40 },
  { name: 'Tony Stark', age: 23 },
]
// const user = USERS.find(function(user){
//   return user.name == 'Tony Stark'
// }) // 함수라서 break 안 걸어도 찾자마자 끝남.
const nUser = USERS.find(user => user.name == 'Tony Stark')
console.log(nUser)