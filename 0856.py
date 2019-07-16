class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[]
        for s in S:
            if s =='(':
                stack.append(s)
            else :
                temp=[]
                m=stack.pop()
                while m!='(':
                    temp.append(m)
                    m=stack.pop()
                if temp:
                    stack.append(2*sum(temp))
                else:
                    stack.append(1)
        return sum(stack)
#and here i share an answer by others that is very clever
    def scoreOfParentheses(self, S):
        return eval(S.replace(')(', ')+(').replace('()', '1').replace(')', ')*2'))
# a little tricky
