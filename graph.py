from collections import deque
class Graph:
    def __init__(self) -> None:
        self.vertices : dict[int, list[int]]={}
    def add_vertex(self, v:int):
        if v not in self.vertices:
            self.vertices[v] = []
    def add_edge(self, u: int, k:int):
        if u in self.vertices and k in self.vertices:
            self.vertices[u].append(k)
            self.vertices[k].append(u) # only if undericted 
    def bfs(self, start: int):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            curr = queue.popleft()
            for vertex in self.vertices[curr]:
                print(vertex)
                if vertex not in visited:
                    queue.append(vertex)
                    visited.add(vertex)
        return visited
    def dfs(self, start: int):
        visited = set()
        def recur(vertex):
            visited.add(vertex)
            for v in self.vertices[vertex]:
                if v not in visited:
                    recur(v)
        recur(start)





def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        curr = queue.popleft()
        for vertex in graph[curr]:
            if vertex not in visited:
                if curr == start:
                    curr = target
                queue.append(vertex)
                visited.add(vertex)
    start = target

    return graph


def bfs(graph, start, target):
    visited = set()
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        if curr not in visited:
            if curr.val == start.val:
                curr.val = target
            visited.add(curr)
            for vertex in graph[curr]:
                queue.append(vertex)

                




