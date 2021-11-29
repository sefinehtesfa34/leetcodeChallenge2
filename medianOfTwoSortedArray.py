class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        self.nums1=nums1
        self.nums2=nums2
        self.nums1.extend(self.nums2)
        if len(self.nums1)==0:
            return 
        self.nums1.sort()
        length=len(self.nums1)
        if length%2==0:
            median=(self.nums1[length//2-1]+self.nums1[length//2])/2
        if length%2!=0:
            median=self.nums1[length//2]
        return median
            
