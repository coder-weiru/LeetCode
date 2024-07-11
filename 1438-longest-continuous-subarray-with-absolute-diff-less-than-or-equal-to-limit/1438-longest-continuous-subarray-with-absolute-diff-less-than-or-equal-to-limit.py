class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        right = 0
        min_q = deque()
        max_q = deque()    
        length = 0
        
        for right in range(len(nums)):
            
            while max_q and max_q[-1] < nums[right]:
                max_q.pop()
            max_q.append(nums[right])

            while min_q and min_q[-1] > nums[right]:
                min_q.pop()
            min_q.append(nums[right])
                    
            #s = "".join(str(nums[left:right + 1]))
            #print(f"=>left: {left}, right: {right}, {s}, max diff |{max_q[-1]}-{min_q[-1]}| = {abs(max_q[-1] - min_q[-1])}, length: {right - left + 1}, min_q -> {min_q}, max_q -> {max_q}")
            
            if abs(max_q[0] - min_q[0]) > limit:
                if nums[left] == min_q[0]:
                    min_q.popleft()
                if nums[left] == max_q[0]:
                    max_q.popleft()
                left += 1      
                  
            length = max(length, right - left + 1)             
            #print(f"max length: {length}")
                
        return length 
