import math

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        
        circles = []
        for _ in range(n):
            x, y = map(int, input().split())
            circles.append((x, y))
        
        xs, ys, xt, yt = map(int, input().split())
        
        uf = UnionFind(n + 2)
        
        start_index = n
        target_index = n + 1
        
        for i in range(n):
            dist_start = distance(xs, ys, circles[i][0], circles[i][1])
            dist_target = distance(xt, yt, circles[i][0], circles[i][1])
            
            if dist_start <= dist_target:
                if dist_start <= dist_target:
                    uf.union(start_index, i)
        
        if uf.find(start_index) == uf.find(target_index):
            results.append("NO")
        else:
            results.append("YES")
    
    # Output all results at once
    print("\n".join(results))

# Entry point
solve()
