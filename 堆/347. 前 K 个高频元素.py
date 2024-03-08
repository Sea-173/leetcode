"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
"""

"""
思路总结
    这道题用堆的思路做，首先用字典统计每个元素出现的次数，
    然后遍历字典，构建小顶堆（因为需要统计出现次数最多的元素）
        如果堆的大小小于k，就插入堆中，此时需要插入到堆尾部，然后上浮
        如果大于k，就判断当前元素出现频率是否大于堆顶元素，如果大于，就替换堆顶元素，然后下沉
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}
        for num in nums:
            if num not in frequent:
                frequent[num] = 0
            frequent[num] += 1
        print('frequent', frequent)
        heap = []

        def siftUp(heap, cur_value, cur_frequent):
            heap.append([cur_value, cur_frequent])
            child = len(heap) - 1
            parent = (child - 1) // 2
            while parent >= 0:
                if heap[parent][1] > cur_frequent:
                    heap[child], heap[parent] = heap[parent], heap[child]
                    child = parent
                    parent = (child - 1) // 2
                else:
                    break
            return
        
        def siftDown(heap, cur_value, cur_frequent):
            print('heap1', heap, cur_value, cur_frequent)
            if heap[0][1] >= cur_frequent:
                return
            else:
                heap[0] = [cur_value, cur_frequent]
            print('heap2', heap, cur_value, cur_frequent)
            parent = 0
            while True:
                child = parent * 2 + 1
                if child >= len(heap):
                    break
                if child + 1 < len(heap) and heap[child + 1][1] < heap[child][1]:
                    child += 1
                if heap[parent][1] <= heap[child][1]:
                    break
                else:
                    heap[parent], heap[child] = heap[child], heap[parent]
                    parent = child
            return

        for key, value in frequent.items():
            if len(heap) < k:
                siftUp(heap, key, value)
                continue
            else:
                siftDown(heap, key, value)
        return [heap[i][0] for i in range(k)]
        # return heap
    
s = Solution()
nums = [5,2,5,3,5,3,1,1,3]
k = 2
print(s.topKFrequent(nums, k))

        