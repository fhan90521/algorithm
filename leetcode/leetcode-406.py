class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x : (x[0], -x[1]))
        current=people.pop()
        result=[current]  
        while people:
            current=people.pop()
            result.insert(current[1],current)
        return result
        