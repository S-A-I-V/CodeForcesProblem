import heapq

class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        def dijkstra(graph):
            dist = [float('inf')] * n
            dist[source] = 0
            pq = [(0, source)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))
            return dist[destination]
        
        # Build the initial graph with all -1 replaced by 1
        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1
        
        def build_graph():
            graph = [[] for _ in range(n)]
            for u, v, w in edges:
                graph[u].append((v, w))
                graph[v].append((u, w))
            return graph
        
        graph = build_graph()
        initial_dist = dijkstra(graph)
        
        if initial_dist > target:
            return []
        elif initial_dist == target:
            return edges
        
        # Adjust one -1 edge to make up the difference
        diff = target - initial_dist
        for edge in edges:
            if edge[2] == 1 and diff > 0:
                edge[2] += diff
                graph = build_graph()
                if dijkstra(graph) == target:
                    return edges
                edge[2] -= diff  # Reset if it didn't work
        
        return []