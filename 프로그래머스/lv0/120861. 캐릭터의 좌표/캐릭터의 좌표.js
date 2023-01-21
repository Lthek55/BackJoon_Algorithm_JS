function solution(keyinput, board) {
    const ret = moveEvent(keyinput,board);
    return ret
}

function moveEvent(event, board) {
    const [x, y] = board;
    const result = [0,0]
    const xLimit = Math.trunc(x/2)
    const yLimit = Math.trunc(y/2)
    const DEBUG = true 

    console.log("yLimit", yLimit)

   for(let i = 0; i<event.length; i++){
       /// x 좌표 이동 ( 가로 )
        if(event[i] === "left" && result[0] > -xLimit){ /// 조건 1. 이벤트 타입 필터링, 조건 2. 보드의 최대 이동거리 필터링
            result[0] = result[0] - 1
        }
        if(event[i] === "right" && xLimit > result[0]){
            result[0] = result[0] + 1
        }

       /// y 좌표 이동 ( 세로 )
        if(event[i] === "up" && yLimit > result[1]){
            result[1] = result[1] + 1
        }
        if(event[i] === "down" && result[1] > -yLimit){
            result[1] = result[1] - 1
        }


       if(DEBUG){
           console.log("========================================================")
           console.log("event", event[i])
           console.log("position X : ", result[0])
           console.log("position Y : ", result[1])
           console.log("========================================================")
       }
   }
    return result
}
