/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    let currentPos = binarySearch(nums, target, 0, nums.length - 1);
    if (currentPos === -1) return [-1, -1]
    let startPos = currentPos;
    let lastStartPos = currentPos;
    let endPos = currentPos;
    let lastEndPos = currentPos;
    // finding start position from the left side
    while (startPos !== -1) {
        lastStartPos = startPos;
        startPos = binarySearch(nums, target, 0, startPos - 1);
    }
    // finding start position from the right side
    while (endPos !== -1) {
        lastEndPos = endPos;
        endPos = binarySearch(nums, target, endPos + 1, nums.length - 1);
    }
    return [lastStartPos, lastEndPos];
};


var binarySearch = function(nums, target, leftPointer, rightPointer) {
    while (leftPointer <= rightPointer) {
        let mid = Math.floor((leftPointer + rightPointer)/ 2);
        let currentNum = nums[mid];
        if (currentNum === target) {
            return mid;
        } else if (currentNum < target) {
            leftPointer = mid + 1;
        } else {
            rightPointer = mid - 1;
        }
    }
    return -1;
}