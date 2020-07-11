// => 결과값 1 또는 0
// => 조건 1 . 4의 배수 0 , 100의 배수 X
// => 조건 2 . 4의 배수 0 , 400의 배수 0

const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin')
const originalData = inputData

if(originalData % 4 == 0 && originalData % 100 != 0){
    console.log(1)
}
else if(originalData % 4 == 0 && originalData % 400 == 0){
    console.log(1)
}
else
    console.log(0)


/* 문제풀이가 궁금하신 분들은 아래의 링크를 참고해주세요!
https://helicopter55.tistory.com/49
*/