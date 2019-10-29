// hoisting: 나중에 선언된 변수를 참조할 수 있음
// console.log(a)
// var a = 10
// console.log(a)

// js가 이해한 코드
var a // 선언 & 초기화
console.log(a)
a = 10 // 할당
console.log(a)


//let은 ReferenceError
// console.log(b)
// let b = 5
// console.log(b)

// 마찬가지로 호이스팅 과정을 거치지만
let b // 선언 & TDZ
console.log(b) // 초기화 안 됐는데 왜 불러
b = 5 // 할당하려 하지만 할당 할 수 없음. 초기화가 안 됐기 때문
console.log(b)


if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3, var은 블록 함수 아님
}

if (x === 1) {
  console.log(y) // 3 var은 블록 함수 아님
}


// js가 이해한 코드
var x
var y
if (x !== 1) {
  console.log(y) 
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) 
}

if (x === 1) {
  console.log(y) 
}