    def rotate(self, nums, k):
        first = nums[:-k]
        last = nums[-k:]
        
                    
        print first
        print last
        
        for i in first:
            last.append(i)
