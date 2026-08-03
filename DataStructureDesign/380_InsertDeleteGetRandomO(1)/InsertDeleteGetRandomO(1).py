import random

class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return res
        
    def getRandom(self) -> int:
       random.choice(self.numList)
       
# Example usage:
randomSet = RandomizedSet()
print(randomSet.insert(1))  # Inserts 1, returns True
print(randomSet.remove(2))  # Tries to remove 2, returns False (not present)
print(randomSet.insert(2))  # Inserts 2, returns True
print(randomSet.getRandom())  # Randomly returns either 1 or 2
print(randomSet.remove(1))  # Removes 1, returns True
print(randomSet.insert(2))  # Tries to insert 2 again, returns False (already present)
print(randomSet.getRandom())  # Randomly returns 2 (only element left)