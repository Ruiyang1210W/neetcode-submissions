class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        const n = nums.length;
        const count = new Map();

        for (const x of nums){
            count.set(x, (count.get(x)||0) + 1);
            if (count.get(x) > n/2) return x;

        }

    }
}
