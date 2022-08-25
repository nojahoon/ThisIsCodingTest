 // 지시사항을 참고하여 solution 함수 안에 코드를 작성하세요.
function solution(input) {
    var answer= "";
    for(var i=0; i<input; i++) {
        for (var j=0; j<=i; j++) {
            if (j==5) { // ***** 이후는 동일
                break;
            }
            answer+="*";
        }
        if (i!=input-1)
            answer+="\n";
    }
  // 출력할 결과를 문자열로 return 하세요.

  return answer;
}


// 실행 혹은 제출을 위한 코드입니다. 지우거나 수정하지 말아주세요.
module.exports = solution;
