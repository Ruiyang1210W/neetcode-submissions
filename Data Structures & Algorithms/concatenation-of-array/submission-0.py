class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        array_copy = nums[:]
        new_array = nums + array_copy
        return new_array