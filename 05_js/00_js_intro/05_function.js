// 1. 선언식 statement, declaration
// 함수 선언식은 코드가 실행되기 전에 로드된다.

function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7))

// 2. 표현식 expression
// 이름이 없는 익명함수를 변수에 할당한다.
// 함수 표현식은 인터프리터가 해당 코드에 도달했을 때 로드된다.

const sub = function(num1, num2) {
  return num1 - num2
}
console.log(sub(7, 2))

console.log(typeof add) // function
console.log(typeof sub) // function

// Arrow Function 화살표 함수
// 화살표 함수의 경우 일반 function키워드로 정의한 함수와 100% 동일한 것이 아니다.
// 항상 익명함수 -> 표현식으로 작성
// 변수에 할당할 수는 있지만 이름 붙은 함수(생성자)로는 만들 수 없습니다.

const ssafy1 = function(name) {
  return `hello, ${name}`
}

// 리팩토링(refactoring)
// 1. function 키워드 삭제: 그럼 =>얘가 생김
const ssafy1 = (name) => {
  return `hello, ${name}`
}

// 2. 매개변수의 '()' 소괄호 생략(함수 매개변수가 하나일 경우만)
const ssafy1 = name => {
  return `hello, ${name}`
}

// 3. {} && return 생략 (함수의 바디에 표현식이 한 개일 경우만
// 함수의 바디에 여러 줄이 써있으면 안 됨)
const ssafy1 = name => `hello, ${name}`


// Arrow function refactoring
let square = function(num) {
  return num ** 2
}

let square = (num) => {return num ** 2}
let square = num => {return num ** 2}
let square = num => num ** 2

// 매개변수가 없다면? ()나 _를 사용
let noArgs = () => 'No args'
let noArgs = _ => 'No args'

// object를 return한다면
// js 의 object {return{키: 'value}}. 반드시 return을 명시적으로 적음
let returnObject = () => {return{key: 'value'}}
console.log(returnObject()) //{ key: 'value' }

// object를 리턴하는데 return을 사용하지 않을 경우 {}가 아니라 ()로 감싼다.
let returnObject = () => ({key: 'value'})

// object return시 문제상황
// 1. return이 없는데 ()를 안 쓴 경우
let returnObject = () => {key: 'value'}
const test = returnObject()
console.log(typeof test) // undefined

// 기본 매개변수를 줄 때는 매개변수의 개수와 상관 없이 무조건 ()를 해야한다.
const sayHello = (name='noName') =>  `hi ${name}`

// Anonymous Function 익명함수, 1회용 함수
// 1. 기명함수로 만들기 (변수/상수에 할당하기) - 생성과 동시에 함수의 인수로 할당
const cube = function(num) { return num ** 3 } // 변수 할당
const squareRoot = num => num ** 0.5 // 루트값

console.log(cube(2))
console.log(squareRoot(4))

// 2. 익명함수 즉시 실행
// 표현식 전체를 ()로 감싼 뒤 표현식 뒤에 ()로 인자를 넣어줌.
console.log((function(num) {return num ** 3})(2)) // 인자를 뒤에 넣는 것.
console.log((num => num ** 0.5)(4)) 

// 함수 호이스팅
// 함수의 선언만 끌어올려줌
// 다만 변수에 할당한 함수(표현식)는 호이스팅 되지 않는다.
// 이것은 변수의 유효범위 규칙을 따르기 때문이다.
ssafy()

function ssafy() {
  console.log('hoisting')
}

//let
ssafy2()

let ssafy2 = function() {
  console.log('HHHHHHoist')
}
// let (JS가 이해한 코드)
let ssafy2 // 1. 변수 선언

ssafy2() // 2. 함수 호출 : ssafy2는 초기화도 안 됐는데 함수를 호출? Reference Error

ssafy2 = function() {
  console.log('HHHHHHoist')
} // 3. 변수에 함수 할당

// var
ssafy3()
var ssafy3 = function(){
  console.log('HHHHHHoist')  
} // TypeError: ssafy3 is not a function. ssafy3은 초기화는 됐지만 함수는 아니다.
//var(JS가 이해한 코드)
var ssafy3 // 1. 변수 선언 및 초기화
ssafy3()// 2. 함수 호출: ssafy3은 변수인데 호출?? 얘는 함수 아냐. 
ssafy3 = function(){
  console.log('HHHHHHoist')
}