class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer=[]
        tickets.sort()
        length=len(tickets)+1
        def dfs(each,tickets):
            if(answer):return
            if(len(each)==length):
                answer.append(each[:])
                return
            if(each):
                for one in tickets:
                
                    if(one[0]==each[-1]):
                        next_tickets = tickets[:]
                        next_tickets.remove(one)
            
                        dfs(each+[one[-1]],next_tickets)
                        
                        
            else:
                for one in tickets:
                    if(one[0]=="JFK"):
                        next_tickets = tickets[:]
                        next_tickets.remove(one)
                    
                        each=one[:]
                        dfs(each,next_tickets)
        dfs([],tickets) 
        return answer[0]