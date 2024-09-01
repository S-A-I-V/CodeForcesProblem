# class Solution(object):
#     def resultsArray(self, queries, k):
#         """
#         :type queries: List[List[int]]
#         :type k: int
#         :rtype: List[int]
#         """
#         distances = []
#         results = []
        
#         for x, y in queries:
#             distance = abs(x) + abs(y)            
#             distances.append(distance)            
#             distances.sort()            
#             if len(distances) < k:
#                 results.append(-1)
#             else:
#                 # The k-th nearest distance is the (k-1)th element in the sorted list
#                 results.append(distances[k-1])
        
#         return results





