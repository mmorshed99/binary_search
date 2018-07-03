#Given a sorted array of integers, find the starting and ending position of a given target value.
#
#Your algorithm’s runtime complexity must be in the order of O(log n).
#
#If the target is not found in the array, return [-1, -1].
#Example:
#
#Given [5, 7, 7, 8, 8, 10]
#
#and target value 8,
#
#return [3, 4].
'''def searchRange(self, A, B):
        def search_idx(A,start,end,my_list):
           mid = start + (end - start)//2
           if mid == start:
             if my_list[start] == A:
                return start
             elif my_list[end] == A:
                return end
             else:
                return -1
           if A > my_list[mid]:
              start = mid
           elif A < my_list[mid]:
              end = mid
           elif A == my_list[mid]:
              return mid
           return search_idx(A,start,end,my_list)
        def search_start(A,start,end,my_list):
           mid = start + (end-start)//2
           if mid == start:
             if my_list[start] < A:
               return end
             if my_list[start] == A:
               return start
           if my_list[start] == A:
              return start
           if my_list[mid] == A:
              end = mid
           if my_list[mid] < A:
              start = mid
           return search_start(A,start,end,my_list)   
        def search_end(A,start,end,my_list):
           mid= start+ (end-start)//2
           if mid == start:
              if my_list[end] > A:
                 return start
              if my_list[end] == A:
                 return end
           if my_list[end] == A:
             return end
           if my_list[mid] == A:
             start = mid
           if my_list[mid] > A:
             end =mid
           return search_end(A,start,end,my_list)
        def search_range(A,my_list):
          if len(my_list) < 1:
            return [-1, -1]
          start = 0
          end = len(my_list)-1
          found_index = search_idx(A,start,end,my_list)
          if found_index == -1:
            return [-1, -1]
          start_idx = search_start(A,start,found_index,my_list)
          end_idx = search_end(A,found_index,end,my_list)
          return [start_idx, end_idx]
        return search_range(B,A)'''
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        def find_me(A,l,r,x):
            if r>= l:
                mid = l + (r-l)/2
                if A[mid] == x:
                    return mid
                elif A[mid] < x:
                    return find_me(A,mid+1,r,x)
                else:
                    return find_me(A,l,mid-1,x)
            return -1
        def find_start(A,l,r,x):
            mid = l + (r-l)/2
            if A[mid] == x:
                if mid == 0 or A[mid-1] != x:
                    return mid
                if mid == 1 and A[mid-1] == x:
                    return mid-1
            if A[mid] >= x:
                return find_start(A,l,mid-1,x)
            if A[mid] < x:
                return find_start(A,mid+1,r,x)
            return -1
        def find_end(A,l,r,x):
            mid = l + (r-l)/2
            if A[mid] == x:
                if mid == len(A)-1 or A[mid+1] != x:
                    return mid
                if mid == len(A)-2 and A[mid+1] == x:
                    return mid+1
            if A[mid] > x:
                return find_end(A,l,mid-1,x)
            if A[mid] <= x:
                return find_end(A,mid+1,r,x)
            return -1
        x = B
        pos = find_me(A,0,len(A)-1,x)
        if pos == -1:
            return [-1,-1]
        return [find_start(A,0,pos,x),find_end(A,pos,len(A)-1,x)]
