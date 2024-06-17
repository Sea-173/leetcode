class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        len_n = len(numbers)
        L, R = 0, len_n-1

        while True:
            R = len_n - 1
            while L < R:
                cur_sum = numbers[L] + numbers[R]
                if cur_sum == target:
                    return [L+1, R+1]
                elif cur_sum > target:
                    R -= 1
                else:
                    break
            L += 1
        return []
