const me = {
  name: 'ssafy', //key가 한 단어일 때는 ''안에 안 넣어도 됨
  'phone number': '01012345678', //key가 여러 단어일 때는 ''안에 넣어야 함.
  appleProducts: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
  }
}

console.log(me.name) // ssafy
console.log(me['name']) // ssafy
console.log(me['phone number']) // key가 여러 단어인 경우는 반드시 []로 접근.
console.log(me.appleProducts)
console.log(me.appleProducts.ipad)

// Object Literal(객체 표현법)
// ES5 때..
var books = ['Learning JS', 'Eloquent JS'] // 배열

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers'],
} // 객체

var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop) // object
console.log(bookShop.books[0]) // Lerning JS

// ES6+
// object의 key와 value가 같다면, 마치 배열처럼 한 번만 작성 가능
let bookShopTwo = { //var해도 되는데 그냥 es6이니깐 let으로..
  books, //이름 같은 얘들을 그대로 들고옴.
  comics,
  magazines,
}
console.log(bookShop)
console.log(typeof bookShop) // object
console.log(bookShop.books[0]) // Lerning JS

///////////////////////////////////////////////

//json
const jsonData = JSON.stringify({ //JSON -> string
  coffee: 'Americano',
  iceCream: 'Mint Choco',
})
console.log(jsonData) // {"coffee":"Americano","iceCream":"Mint Choco"} 객체에서는 트레일링 컴마를 쓸 수 있지만 str에서는 트레일링 컴마 불가
console.log(typeof jsonData) // string

const parseData = JSON.parse(jsonData) // stringify의 반대. string으로 된 JSON을 다시 JSON으로
console.log(parseData) //{ coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof parseData) // object