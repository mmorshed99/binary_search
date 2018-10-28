class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A
        l = 2
        r = A/2
        mid = l + (r-l)/2
        while r >= l:
            if mid * mid == A:
                return mid
            if mid * mid > A:
                r = mid-1
            else:
                l = mid+1
            mid = l + (r-l)/2
        if mid * mid > A:
            mid = mid-1
        return mid
