class SnapshotArray:
    
    def __init__(self, length: int):
        self.aray = [[(0, 0)] for _ in range(length)]
        self.snapId = 0
        
    def set(self, index: int, val: int) -> None:
        self.aray[index].append([self.snapId, val])
        
    def snap(self) -> int:
        self.snapId += 1
        return self.snapId - 1
    
    def get(self, index: int, snap_id: int) -> int:
        history = self.aray[index]
        l, r = 0, len(history) - 1
        
        while l <= r:
            m = (l + r) // 2
            if history[m][0] <= snap_id:
                l = m + 1
            else:
                r = m - 1
        return history[r][1]
    
# Example usage:
snapshotArr = SnapshotArray(3)  # Initialize a SnapshotArray of length 3
snapshotArr.set(0, 5)  # Set index 0 to value 5
snap_id1 = snapshotArr.snap()  # Take a snapshot, returns snap_id 0
snapshotArr.set(0, 6)  # Set index 0 to value 6
print(snapshotArr.get(0, snap_id1))  # Get the value at index 0 for snap_id 0, should return 5
 