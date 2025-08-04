from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruit: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(fruit)):
            count[fruit[right]] += 1

            # Shrink the window until we have at most 2 types of fruits
            while len(count) > 2:
                count[fruit[left]] -= 1
                if count[fruit[left]] == 0:
                    del count[fruit[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
