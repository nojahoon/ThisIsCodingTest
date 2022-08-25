 // 지시사항을 참고하여 solution 함수 안에 코드를 작성하세요.
function solution(str) {

    var answer=""
    len = parseInt(str.length/2);
    console.log(len);
    for (var i=0; i<len; i++) {
        if (str[i]==str[(str.length)-1-i])
            answer+="Same";
        else
            answer+="Different";
        if (i!= len-1)
            answer+='\n';
    }
  return answer;
}


// 실행 혹은 제출을 위한 코드입니다. 지우거나 수정하지 말아주세요.
module.exports = solution;
