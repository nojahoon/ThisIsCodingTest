 // 지시사항을 참고하여 solution 함수 안에 코드를 작성하세요.
function solution() {

  let americano = 3500;
  let cafe_latte = 3800;
  let milk_tea = 4200;

  let price1 = (americano*2 + milk_tea);
  let price2 = (cafe_latte*2 + milk_tea*2)*0.9;

  return price1 + price2;
}


// 실행 혹은 제출을 위한 코드입니다. 지우거나 수정하지 말아주세요.
module.exports = solution;
