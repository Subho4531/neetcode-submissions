class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        h={}

        s=len(numbers)-1
        i=0


        for n in numbers:
            if numbers[i]+numbers[s]==target:
                return [i+1,s+1]
            if numbers[i]+numbers[s]>target:
                s-=1
            if numbers[i]+numbers[s]<target:
                i+=1
                
        