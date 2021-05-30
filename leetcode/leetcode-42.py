class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if(len(height)==0): return 0
        total=0
        each=0
        left=0
        left_max=height[left]
        right=len(height)-1
        right_max=height[right]
        while(left!=right):
            if(height[left]<height[right]):
                if(left_max<=height[left]):
                    left_max=height[left]
                total+=left_max-height[left]
                left+=1        
            else:
                if(right_max<=height[right]):
                    right_max=height[right]
                total+=right_max-height[right]
                right-=1
        return total 