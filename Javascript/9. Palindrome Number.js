/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    if(x<0){return false;}
    return reverseInt(x) == x;
};

var reverseInt = function (x) {
    let rev = 0;
    while (x != 0) {
        rev = rev * 10 + x % 10;
        x = x/10 >> 0;
        // x = Math.floor(x/10)
    }
    return rev;
}