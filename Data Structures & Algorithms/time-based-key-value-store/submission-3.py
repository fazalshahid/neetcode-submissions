class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        values = self.data[key]

        values.sort()

        left = 0
        right = len(values) - 1
        res = ""
        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            if values[mid][0] > timestamp:
                right = mid - 1
            else:
                res = values[mid][1]
                left = mid + 1
        
        return res
            

