const numbers = [1, 2, 3, 4,]
console.log(numbers[0]) // 1
console.log(numbers[-1]) // undefined: 정확한 양의 정수 index만 가능
console.log(numbers.length) // 4
console.log(numbers.reverse()) // [4, 3, 2, 1]. 원본을 파괴함...
console.log(numbers) // [4, 3, 2, 1]
console.log(numbers.reverse()) // 원상복구
console.log(numbers)

// push
console.log(numbers.push('a')) // push의 리턴값은 배열의 길이
console.log(numbers)

// pop . 배열의 가장 마지막 요소 제거 후 return
console.log(numbers.pop())
console.log(numbers)

// unshift. 배열의 가장 앞에 요소를 추가하고 return은 길이
console.log(numbers.unshift('a')) // 5
console.log(numbers) // ['a', 1, 2, 3, 4]

//shift. 배열의 가장 앞의 요소를 제거 후 return
console.log(numbers.shift()) //a
console.log(numbers) //[1, 2, 3, 4]

//includes 배열에 해당 값이 포함되어 있는지 true/false
console.log(numbers.includes(1)) //true
console.log(numbers.includes(0)) //false

console.log(numbers.push('a', 'a'))
console.log(numbers)
console.log(numbers.indexOf('a')) // 4. 첫번째 'a'의 인덱스를 반환
console.log(numbers.indexOf('b')) // -1. 찾고자 하는 요소가 없으면 -1을 반환

// join . 배열의 요소를 join함수의 이자를 기준으로 문자열로 바꿔줌, join에 아무 인자도 넣지 않으면 ,를 기준으로 가져옴
console.log(numbers.join()) // 1, 2, 3, 4, a, a 
console.log(numbers.join('')) // 1234aa
console.log(numbers.join('-')) // 1-2-3-4-a-a
console.log(numbers) // join은 원본을 변화시키지는 않음
