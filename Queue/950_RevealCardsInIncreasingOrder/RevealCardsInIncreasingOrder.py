from typing import List
from collections import deque

def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
    deck.sort()
    q = deque(range(len(deck)))
    res = [0] * len(deck)
    
    for n in deck:
        i = q.popleft()
        res[i] = n
        
        if q:
            q.append(q.popleft())
    return res

# Example usage:
deck = [17, 13, 11, 2, 3, 5, 7]
print(deckRevealedIncreasing(None, deck))  # Output: [2, 13, 3, 11, 5, 17, 7]