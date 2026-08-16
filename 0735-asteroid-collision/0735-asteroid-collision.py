class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for ast in asteroids:
            while stack and ast<0 and stack[-1]>0:
                diff=ast+stack[-1]
                # 3 edge cases 
                # 1.ast is bigg then +ve (stack one) so pop it out
                if diff<0: 
                    stack.pop()
                #2. ast is smaller and got detroyed by the stack[-1]
                elif diff>0:
                    break
                #3. diff==0 -- both ast and stack[-1] same and both got destroyed
                else:
                    stack.pop()
                    break
            # if it survives all collision case or never met collision then it pushed to stack
            else:
                stack.append(ast)
        return stack

                
                
            
        