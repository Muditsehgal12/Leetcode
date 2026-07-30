class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        sign=[]
        num=0
        def precedence(op):
            if op == '+' or op == '-':
                return 1
            return 2
        def calculate():
            b = stack.pop()
            a =stack.pop()
            op = sign.pop()

            if op == '+':
                stack.append(a+b)
            elif op == '-':
                stack.append(a-b)
            elif op == '*':
                stack.append(a*b)
            else:
                stack.append(int(a/b))
        for i in range(len(s)):
            if s[i].isdigit():
                num=num*10+int(s[i])
            elif s[i]==" ":
                continue
            else:
                stack.append(num)
                num=0
                curr=s[i]
                while sign and precedence(sign[-1])>=precedence(curr):
                    calculate()
                sign.append(curr)
        stack.append(num)
        while sign:
            calculate()
        return stack[-1]
