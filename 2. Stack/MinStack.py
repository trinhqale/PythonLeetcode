'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2'''


'''
class MinStack:

    def __init__(self):
        # Initialize your data structure here.
        self.minStack = []
        self.minList = []

    def push(self, val: int) -> None:
        # Push element onto stack.
        self.minStack.append(val)
        val = min(val, self.minList[-1] if self.minList else val)
        
        # min_val
        # if minList:
        #     if minList[-1] < val:
        #         val = minList[-1]
        
        self.minList.append(val)

    def pop(self) -> None:
        # Removes the element on the top of the stack.
        self.minStack.pop()
        self.minList.pop()

    def top(self) -> int:
        # Get the top element.
        if self.minStack:
            return self.minStack[-1]
        return None

    def getMin(self) -> int:
        # Retrieve the minimum element in the stack.
        if self.minList:
            return self.minList[-1]
        return None



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
'''