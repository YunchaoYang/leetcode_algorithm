from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        from collections import defaultdict
        connections = defaultdict(set)

        def build_path_hash(routes):
            for rou in routes:
                for i in rou:
                    for j in rou:
                        if j != i:
                            connections[i].add(j)
        
        build_path_hash(routes)
        
        num = 0
        
        print(routes)
        
        que = [source]
        visited = set()

        while que:
            n_reach = len(que)
            print(n_reach)
            for _ in range(n_reach):
                stop = que[-1]
                visited.add(stop)
                if stop == target: return num

                next_stops = connections[stop]
                print(stop, next_stops, visited)

                for s in next_stops:
                    if s not in visited:
                        que.append(s)
                print(que)
                que.pop(0)
            #print(que)
            num += 1

        return -1
    
    
s = Solution()

s.numBusesToDestination(
    [[1,2,7],[3,6,7]],
    1,
    6
)