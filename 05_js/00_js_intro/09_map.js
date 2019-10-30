// Array Helper Method

// 2. .map(callback())
// 배열 내의 모든 요소에 대하여 각각 주어진 함수(callback)를 호출한 결과를 모아 
// 새로운 배열을 return하거나 일정한 형식의 배열을 다른 형식으로 바꿔야 할 때 사용한다.
// map은 원본을 안 바꿈

// for
var numbers = [1, 2, 3,]
var doubleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  doubleNumbers.push(numbers[i]*2)
}

console.log(doubleNumbers)
console.log(numbers) // 원본 유지

// map
const NUMBERS = [1, 2, 3,]
const DOUBLE_NUMBERS = NUMBERS.map(function(number){
  return number * 2
})
console.log(DOUBLE_NUMBERS)
console.log(NUMBERS) // 원본 유지

// const DOUBLE_NUMBERS = NUMBERS.map(number => number * 2)

// 2-1 연습
const newNumbers = [4, 9, 16,]
const roots = newNumbers.map(Math.sqrt) // 제곱근

console.log(roots)

// 2-2 map을 사용해 images 배열 안의 Object들의 height들만 저장되어 있는
// heights 배열을 만드시오.
const images = [
  { height: '34px', width: '35px'},
  { height: '4px', width: '3px'},
  { height: '2px', width: '5px'},
]
const heights = images.map(image => image.height)
console.log(heights)

// 2-3 map을 사용해 trips 배열의 값들을 계산해서 속도 값을 저장하는 배열
// speeds를 만드시오.
const trips = [
  {distance: 35, time: 10},
  {distance: 70, time: 20},
  {distance: 5, time: 2},
]
const speeds = trips.map(trip => trip.distance/trip.time)

console.log(speeds)

// 2-4
const brands = ['Marvel', 'DC',]
const movies = ['IronMan', 'Batman',]

// const comics = brands.map(function(x, i){// x는 brands의 객체, i는 x의 인덱스 like python`s enumerate
//   return {name: x, hero: movies[i]}
// })

// 객체를 return하려면 return과 {} 없앨 때 ()를 추가해줘야 한다.
// 파이썬의 dict형태가 js의 객체
const comics = brands.map( (x, i) => ({name: x, hero: movies[i]}))


console.log(comics)
// [
//   {name: 'Marvel', hero: 'IronMan'},
//   {name: 'DC', hero: 'BatMan'},
// ]