// => 결과값 : 입력값에 따라서 구구단을 출력

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let fixedPoint = 0;

rl.on("line", function (line) {
  input = line.split(' ').map((_) => Number(_));
}).on("close", function () {
  fixedPoint = input[0]

  for (let i = 1; i <= 9; i++) {
    console.log(`${fixedPoint} * ${i} = ${fixedPoint * i}`);
  }
  process.exit();
});


