const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

let input = []
let value=0

rl.on('line',(line)=>{
    input = line.split(' ').map(_=>+_)
}).on('close',()=>{
    value = input[0]
    console.log((Math.pow(value,2)+value)/2)
})

