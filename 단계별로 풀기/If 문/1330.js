const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin').toString().split(' ').map(val=>+val)
const [a,b] = inputData

if(a>b){
    console.log('>')
}
else if(a<b){
    console.log('<')
}
else{
    console.log('==')
}

/* 문제풀이가 궁금하신 분들은 아래의 링크를 참고해주세요!
https://helicopter55.tistory.com/38
*/