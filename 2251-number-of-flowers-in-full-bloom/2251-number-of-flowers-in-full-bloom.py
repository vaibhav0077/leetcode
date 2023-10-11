class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start=sorted(flowers,key=lambda x:x[0])
        end=sorted(flowers,key=lambda x:x[1])
        ans=[]
        for man in people:
            i=bisect_left(end,man,key=lambda x:x[1])
            j=bisect_right(start,man,key=lambda x:x[0])
            ans.append(j-i)

        return ans    
        
        
       
        
#         for x in people:
#             flower_start_bloom = sb(x)
#             flower_stop_bloom = stb(x)
        
#         for x in people:
#             if not x in di:
#                 di[x] = 0
                
#         for key in di.keys():
#             for x in flowers:
                
#                 if x[0] <= key <= x[1]:
#                     di[key]+=1
        
#         ans= []
        
#         for key in people:
#             ans.append(di[key])
        
#         return ans
            