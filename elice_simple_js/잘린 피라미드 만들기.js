 // 지시사항을 참고하여 solution 함수 안에 코드를 작성하세요.
function solution(a, b) {
    answer = "";
    if (a>=b | a>=15) {
        return "오류";
    }
    if (b>15) {
        b=15
    }
    for (var i=a; i<=b; i++) {
        for (var j=0; j<i; j++){
            answer+="*";
        }
        if (i!=b) {
            answer+="\n";
        }
    }
  return answer;
}


// 실행 혹은 제출을 위한 코드입니다. 지우거나 수정하지 말아주세요.
module.exports = solution;
