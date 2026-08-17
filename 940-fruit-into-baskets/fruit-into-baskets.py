class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        f={}
        m=0
        for r in range(len(fruits)):
            f[fruits[r]]=f.get(fruits[r],0)+1
            while len(f)>2:
                f[fruits[l]]-=1
                if f[fruits[l]]==0:
                    del f[fruits[l]]
                l+=1
            if m<r-l+1:
                m=r-l+1
        return m