class Boat:
    def __init__(self, limit, s1):
        self.limit = limit
        self.s1 = s1
        self.s2 = None
    def hasSpace(self, val):
        return self.s1 + val <= self.limit


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = []
        people.sort()

        left = 0
        right = len(people) - 1

        while left <= right:
            b = Boat(limit, people[right])
            right -= 1
            if b.hasSpace(people[left]):
                b.s2 = people[left]
                left += 1
            boats.append(b)
        return len(boats)