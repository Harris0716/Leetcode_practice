/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let i = 1;
    for(let j = 0; j < nums.length-1; j++){
        if(nums[j] != nums[j+1]){
            nums[i++] = nums[j+1];
        }
    }
    return i;
    
};