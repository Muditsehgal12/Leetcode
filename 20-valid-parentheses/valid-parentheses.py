class Solution(object):
    def isValid(self, s):
        stack=[]
        top=-1
        for i in s:
            if i in ('(','{','['):
                stack.append(i)
                top+=1
            elif i in (']','}',')'):
                if top==-1:
                    return False
                elif i==')' and stack[top]=='(':
                    stack.pop()
                    top-=1
                elif i==']' and stack[top]=='[':
                    stack.pop()
                    top-=1
                elif i=='}' and stack[top]=='{':
                    stack.pop()
                    top-=1
                else:
                    return False
        if top==-1:
            return True
        else:
            return False

