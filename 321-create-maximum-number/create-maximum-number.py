class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def subseq(nums,length):
            l=0
            stack=[]
            remove=len(nums)-length
            for i in nums:
                while stack and remove>0 and i>stack[-1]:
                    a=stack.pop()
                    remove-=1
                stack.append(i)
            if remove>0:
                stack=stack[:-remove]
            return stack[0:length]
        def merge(num1,num2):
            i=0
            j=0
            a=[]
            while i<len(num1) and j<len(num2):
                if num1[i]>num2[j]:
                    a.append(num1[i])
                    i+=1
                elif num1[i]<num2[j]:
                    a.append(num2[j])
                    j+=1
                else:
                    x=i
                    y=j
                    while x<len(num1) and y<len(num2) and num1[x]==num2[y]:
                        x+=1
                        y+=1
                    
                    if x==len(num1):
                        a.append(num2[j])
                        j+=1
                    elif y==len(num2):
                        a.append(num1[i]) 
                        i+=1
                    elif num1[x]>num2[y]:
                        a.append(num1[i])
                        i+=1
                    else:
                        a.append(num2[j])
                        j+=1
            if i<len(num1):
                for k in range(i,len(num1)):
                    a.append(num1[k])    
            if j<len(num2):
                for k in range(j,len(num2)):
                    a.append(num2[k]) 
            return a   
        ans=[]
        for i in range(max(0,k-len(nums2)),min(k,len(nums1))+1):
            a=subseq(nums1,i)
            b=subseq(nums2,k-i)
            c=merge(a,b)
            if c>ans:
                ans=c
        return ans
