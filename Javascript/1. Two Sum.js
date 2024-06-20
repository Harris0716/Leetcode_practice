/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = {};
    let complement;
    for(let i = 0; i < nums.length; i++){
        complement = target - nums[i];
        if(nums[i] in map){
            return [map[nums[i]], i];}
        else{
            map[complement] = i;
        }
    }
    return null;    
};