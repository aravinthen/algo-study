class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = list(
            sorted(
                {i : nums.count(i) for i in nums}.items(),
                key = lambda x: x[1],
                reverse = True,
            )
        )

        vals = [i[0] for i in count]

        return [vals[i] for i in range(k)]
