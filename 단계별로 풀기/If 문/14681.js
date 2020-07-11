// => 결과값 : 좌표값에 따라 1,2,3,4 사분면으로 구분됨
// => 조건 1 . x 값이 양수일때 
    // => y값이 양수이면 1 사분면
    // => y값이 음수이면 4 사분면
// => 조건 2 . x 값이 음수일때 
    // => y값이 양수이면 2 사분면
    // => y값이 음수이면 3 사분면


const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = []
const xPoint = 0
const yPoint = 0

rl.on('line', function (line) {
    input = line.split(' ').map((el) => parseInt(el));
    })
    .on('close', function () {
    xPoint = input[0]
    yPoint = input[1]
    if(xPoint >0){
        yPoint > 0 ? console.log(1) : console.log(4)
    }
    if(xPoint <0){
        yPoint > 0 ? console.log(2) : console.log(3)
    }
    process.exit();
});



/* 문제풀이가 궁금하신 분들은 아래의 링크를 참고해주세요!
https://helicopter55.tistory.com/50
*/