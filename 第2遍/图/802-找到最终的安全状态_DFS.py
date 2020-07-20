from collections import defaultdict
class Solution(object):
    def eventualSafeNodes(self, graph):
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)
        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                if color[nei] == GRAY or not dfs(nei):
                    return False
            color[node] = BLACK
            return True

        return list(filter(dfs, range(len(graph))))

