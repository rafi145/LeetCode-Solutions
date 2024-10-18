import heapq
class Solution:
    """
    Returns:
        int: The weight of the last remaining stone or 0 if all stones are smashed.

    Approach:
        1. Negate the weights of all stones to create a max heap.
        2. Build a max heap using the `heapify` function from the `heapq` module.
        3. While there are more than one stone:
            a. Pop the largest stone from the heap using `heappop`.
            b. Pop the next largest stone from the heap.
            c. If the largest and next largest stones are different:
                i. Calculate the difference between the largest and next largest stones.
                ii. Push the negative of the difference back onto the heap.
        4. If there is one stone left, return its positive weight. Otherwise, return 0.
    """

    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate the values in stones to create a max heap
        stones = [-x for x in stones]

        # Build max heap
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            nextLargest = heapq.heappop(stones)

            if largest != nextLargest:
                heapq.heappush(stones, largest - nextLargest)

        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0