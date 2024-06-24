/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let prefix = strs[0];
    let max_len = strs[0].length;
    for(let j = 1; j < strs.length; j++){
            if(strs[j].length < max_len){
                max_len = strs[j].length;
            }
            while(prefix.substring(0,max_len) !== strs[j].substring(0,max_len)){
                max_len--;
            }
        }
        return prefix.substring(0, max_len);
};