/*
 * 
 * Copyright (C) 2015 sharlatan <sharlatan@localhost.localdomain>
 *
 * Distributed under terms of the MIT license.
 */


function ds(num) { // recursively return digits sum of num
    if (num < 10) {
        return num;
    }
    return num % 10 + ds(Math.floor(num / 10));
}

var power = Math.pow(2, 1000)
console.log(ds(power)); 
console.log(power); 
