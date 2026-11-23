class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        s = len(numbers) - 1
        i = 0

        while i < s:
            if numbers[i] + numbers[s] == target:
                return [i + 1, s + 1]
            if numbers[i] + numbers[s] > target:
                s -= 1
            if numbers[i] + numbers[s] < target:
                i += 1
