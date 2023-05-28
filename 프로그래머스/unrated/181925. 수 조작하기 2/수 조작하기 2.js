function solution(numLog) {
    let answer = '';
    const postion = {'1':'w', '-1':'s', '10':'d', '-10':'a'};
    const numLogLen = numLog.length
    
    for (let idx =0;idx<numLogLen;idx++){
        
        if(idx ===0 ) continue
        
        let calc = numLog[idx] - numLog[idx-1]
        
        answer+= postion[calc.toString()]
    }
    
    return answer;
}

        
