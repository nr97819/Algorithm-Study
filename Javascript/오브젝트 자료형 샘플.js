var Player = function(name) {
    var name = name;
    var hp = 100;
    var mp = 300;
    
    return {
        hit: function (damage) {
            hp -= damage;
            console.log(name + ' hit damage : ' + damage);
            return this.isDie();
        },
        isDie: function () {
            if (hp <= 0) {
                console.log(name + ' is die...');
                return true;
            }
            return false;
        }
    }
}

// * 'medic'에 대한 Player 함수가 생성되고, 
// 해당 함수에서 또 damage를 받는 함수를 불러온다.
var medic = new Player('medic');
medic.hit(50);
// medic hit damage : 50

var fireBet = new Player('fireBet');
fireBet.hit(100);
// fireBet hit damage : 100
// fireBet is die...