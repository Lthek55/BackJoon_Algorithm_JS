const fs = require('fs')
const inputData = fs.readFileSync('/dev/stdin')
const a = inputData


if(100>= a && a>=90){
    console.log('A')
}
else if(89>= a && a>=80){
    console.log('B')
}
else if(79>= a && a>=70){
    console.log('C')
}
else if(69>= a && a>=60){
    console.log('D')
}
else
    console.log('F')


/* 문제풀이가 궁금하신 분들은 아래의 링크를 참고해주세요!
https://helicopter55.tistory.com/48
*/