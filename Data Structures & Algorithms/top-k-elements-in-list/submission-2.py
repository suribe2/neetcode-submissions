class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1

        heap = []

        for i, freq in count.items():
            heapq.heappush(heap, (freq, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]


