class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}

        #uses enumerate to pair both index and item
        for i, num in enumerate(nums):
            #calculate the counterpart of current indexed item
            counterpart = target - num
            
            #checks dictonary if for same counterpart "value" (less runs)
            if counterpart in num_dict:
                #gives answer
                return [num_dict[counterpart], i]
            #otherwise, store the current num and it's index in the dict
            num_dict[num] = i
            
        #no solution   
        return []

        