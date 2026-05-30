import collections

class TimeMap:
    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 因为 timestamp 严格递增，直接 append 即可保持有序
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        entries = self.store[key]
        # 二分查找：寻找最后一个 <= timestamp 的位置
        left, right = 0, len(entries) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            ts, val = entries[mid]
            
            if ts <= timestamp:
                result = val  # 记录当前合法值，尝试找更大的 timestamp
                left = mid + 1
            else:
                right = mid - 1
                
        return result