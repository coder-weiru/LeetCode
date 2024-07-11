class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        max_q = deque()
        max_window = []
        for r in range(len(nums)):
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            max_q.append(nums[r])

            #s = "".join(str(nums[l:r + 1]))
            #print(f"=>left: {l}, right: {r}, {s}, length: {r - l + 1}, max_q -> {max_q}")
            
            if r - l + 1 >= k:
                max_window.append(max_q[0])
                if nums[l] == max_q[0]:
                    max_q.popleft()
                l += 1      
         
        #print(f"window -> {max_window}")
        return max_window
                    