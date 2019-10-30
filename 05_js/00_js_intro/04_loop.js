//while문
let i = 0

while (i < 6) {
  console.log(i)
  i++
}
//0~5까지 나옴

for (let j = 0; j < 6; j++) { // 반드시 변수 선언 후 ; 조건 후 ; 증감식
  console.log(j)
} // 0~5

//python의 for~in~
const numbers= [0, 1, 2, 3, 4, 5,] // trailing comma가 권장된다.

for (let number of numbers){
  console.log(number)
} //0~5

for (let number of [0, 1, 2, 3, 4, 5,]){
  console.log(number)
} // 이렇게 써도 됨

for (const number of [0, 1, 2, 3, 4, 5,]){
  console.log(number)
} // 재할당하지 않을 거면 const써도 됨.
