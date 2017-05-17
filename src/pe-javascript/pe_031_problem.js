/*
 * File :  31-problem.js
 *
 * Copyright (C) 2015 sharlatan <sharlatan@localhost.localdomain>
 *
 * Distributed under terms of the MIT license.
 */


var INIT_TIME = new Date().getTime();


function perf() {
    var end = new Date().getTime();
    return end - INIT_TIME;
}


function count(coins, amount) {
    if (amount === 0) {
        return 1;
    }
    else if (amount < 0 || coins.length === 0) {
        return 0;
    }
    else {
        var first = coins[0];
        var rest = coins.slice(1);

        return count(rest, amount) + count(coins, amount - first);
    }
}


// UK common counage, must be ordered high to low
var coinage = [200, 100, 50, 20, 10, 5, 2, 1];

// £2.00
var total = 200;

var result = count(coinage, total);

console.log(total + " can be made up in " + result + " ways."); 
console.log("Perfomance time: " + perf() + " ms."); 
