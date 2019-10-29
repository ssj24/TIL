//var, let, const

//let은 변수
let x = 1 //세미콜론 생략(ASI)

if (x === 1) {
  let x = 2

  console.log(x) //2
}
console.log(x) //1

// const는 상수

// const 선언시에 초기값을 생략하면 오류 발생
// const MY_FAV
const MY_FAV = 7

console.log('my favorite number is: ' + MY_FAV)
//상수를 재할당하려는 시도는 오류 발생
// MY_FAV = 20

// 상수를 재선언하려는 시도는 모두 오류 발생
// const MY_FAV = 20
// let MY_FAV = 20
// var MY_FAV = 20

if (MY_FAV === 7) {
  // 블록 유효 범위로 지정된 MY_FAV라는 변수를 만드므로 괜찮다.
  // 즉 전역이 아닌 범위 안이므로 이름 공간에서 충돌이 나지 않는다.
  const MY_FAV = 20

  console.log('my favorite number is ' + MY_FAV)
}

console.log(MY_FAV) 

//var (변수)
function varTest() {
  var x = 1
  if (true) {
    var x = 2
    console.log(x)
  }
  console.log(x)
}
varTest()

//let
function letTest() {
  let x = 1
  if (true) {
    let x = 2
    console.log(x)
  }
  console.log(x)
}
letTest()

//let과 var

var a = 1
let b = 2
if (a === 1) {
  var a = 11
  let b = 22

  console.log(a)
  console.log(b)
}
console.log(a)
console.log(b)


////////////////////////////////////////////////////////////////////////////////////
// 식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체, 변수, 함수 (=== lower-camel-case)
let dog
let variableName

//배열은 복수형 변수명을 사용
const dogs = [] 
// 얘는 const이지만 대문자가 아닌 것을 보니 절대 변하지 않는 상수는 아니구나

// 정규 표현식은 'r'로 시작
const rDecs = /.*/ 

// 함수
function getPropertyName() {
  return 1
}

// boolean을 반환하는 함수 = 'is'로 시작
let isAvailable = false


// 2. 파스칼 케이스(PascalCase) - 클래스, 생성자 (=== upper_camel_case)
class User {
  constructor(options) {
    this.name = option.name
  }
}


// 3. 대문자 스네이크 케이스(SNAKE_CASE) - 상수
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려준다.
const API_KEY = 'avcdseasr'