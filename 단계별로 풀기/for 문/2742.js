const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ')

const RANGE_VALUE = Number(input)

for(let i=RANGE_VALUE; i>=1; i--){
    console.log(i)
}
