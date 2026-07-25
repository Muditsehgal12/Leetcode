class Solution(object):
    def dailyTemperatures(self, temperatures):
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        
        for i in range(n):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                u=stack.pop()
                answer[u]=i-u
           
            stack.append(i)
        return answer

