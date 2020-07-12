const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split(' ')

const RANGE_VALUE = Number(input)

for(let i=1; i<=RANGE_VALUE; i++){
    console.log(i)
}
