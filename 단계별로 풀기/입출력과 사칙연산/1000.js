const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(value => +value)

const [a,b] = inputData
console.log(a+b)

/* 문제풀이가 궁금하신 분들은 아래의 링크를 참고해주세요!
https://helicopter55.tistory.com/38
*/