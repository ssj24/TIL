// const nothing = () => {
//   console.log('sleeping')
// }
// console.log('start')
// setTimeout(nothing, 3000)
// console.log('end')

// function sleep_3s() {
//   setTimeout(() => console.log('wake up'), 3000)
// }

// console.log('start')
// sleep_3s()
// console.log('end')

// function first() {
//   console.log('first')
// }
// function second() {
//   console.log('second')
// }
// function third() {
//   console.log('third')
// }

// first()
// setTimeout(second, 1000)
// third() // first - third - second


console.log('Hi')
setTimeout(function ssafy(){
  console.log('ssafy')
}, 100)

console.log('bye')


function printHello() {
  console.log('Hello')
}

function baz() {
  setTimeout(printHello, 3000)
}

function bar() {
  baz()
}

function foo() {
  bar()
}

foo()