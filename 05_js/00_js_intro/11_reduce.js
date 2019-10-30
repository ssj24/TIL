// Array Helper Method

// 4. .reduce(callback())
// 배열의 각 요소에 대해 주어진 reduce 함수를 실행하고, 하나의 결과값을 반환한다.
// reduce는 배열 내의 숫자 총합, 평균 등 배열의 값을 하나로 줄이는 동작을 한다.
// map은 배열의 각 요소를 변형한다면, reduce는 배열 자체를 변형한다.

// 총합
const ssafyTests = [90, 90, 80, 77,]
// const sum = ssafyTests.reduce(function(total, x){ // 보통 인자는 total, x의 두 개를 씀
//   return total += x
// })
///////////////
// const sum = ssafyTests.reduce(function(total, x){ // 보통 인자는 total, x의 두 개를 씀
//   return total += x
// }, 0) // return있는데 0 쓰려면 이렇게(reduce의 두 번째 인자니깐)

// const sum = ssafyTests.reduce((total, x) => total += x, 0)
const sum = ssafyTests.reduce((total, x) => total += x)
console.log(sum)
// callback함수의 첫번째 매개변수는 누적 값.전 단계의 결과. === total
// 두번째 매개변수는 현재 배열 요소, 현재 인덱스, 배열 자체 순이다. === x
// 초기값 === 0(첫 total 값)
// 0, 90 - 90, 90 - 180, 80 - 260, 77  - 337
// 초기값이 생략되면 배열의 첫번째 요소가 초기값이 된다.(return구문이 있으면 0을 쓰면 안 됨.)

// 4-1 연습
// 다음 배열 내의 요소의 총합을 구하시오.
const arr = [0, 1, 2, 3]
const SUM = arr.reduce((total, x) => total += x)
console.log(SUM)