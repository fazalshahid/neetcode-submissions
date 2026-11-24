class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mp = {}

        for i in range(len(position)):
            mp [position[i]] = (target - position[i]) / speed[i]
        
        position.sort()

        count = 0
        front_time = None
        #print(mp)
        while position:
            front = position.pop()
            #print(front_time)
            #position.pop()
            if front_time is None or mp[front] > front_time:
                count += 1
                front_time = mp[front]
        return count
        