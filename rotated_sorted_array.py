#Suppose a sorted array is rotated at some pivot unknown to you beforehand.
#
#(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).
#
#You are given a target value to search. If found in the array, return its index, otherwise return -1.
#
#You may assume no duplicate exists in the array.
#
#Input : [4 5 6 7 0 1 2] and target = 4
#Output : 0
#
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
       def find_break_point(start,end,A):
          mid = start + (end-start)//2
          if len(A) <3:
            return start
          if A[mid] < A[mid-1] and A[mid] < A[mid+1]:
            return mid
          elif A[mid] > A[mid-1] and A[mid] > A[mid+1]:
            return mid
          elif A[mid] > A[len(A)-1]:
            return find_break_point(mid,len(A),A)
          elif A[mid] < A[0]:
            return find_break_point(start,mid,A)
          else:
            return -1
       def bin_search(start,end,target,A):
          mid = start + (end-start)//2
          if target == A[mid]:
            return mid
          if end-start < 3:
            if target == A[start]:
              return start
            elif target == A[end]:
      	      return end 
      	    else:
      	       return -1
      	  elif target > A[mid]:
      	      return bin_search(mid,end,target,A)
          else:
      	    return bin_search(start,mid,target,A)
       target = B	    
       break_point = find_break_point(0,len(A)-1,A)
       if break_point == -1:
           return bin_search(0,len(A)-1,target,A)
       else:
           index = bin_search(0,break_point-1,target,A)
           if index != -1:
               return index
           else:
               index = bin_search(break_point,len(A)-1,target,A)
               return index
