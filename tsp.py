INF = float('inf')

def tsp(graph):
    n = len(graph)
    memo = [[None] * (1 << n) for _ in range(n)]

    def tsp_helper(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0]

        if memo[pos][mask] is not None:
            return memo[pos][mask]

        min_cost = INF

        for next_city in range(n):
            if (mask >> next_city) & 1 == 0:
                new_mask = mask | (1 << next_city)
                cost = graph[pos][next_city] + tsp_helper(new_mask, next_city)
                min_cost = min(min_cost, cost)

        memo[pos][mask] = min_cost
        return min_cost

    # Start from city 0
    return tsp_helper(1, 0)

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = tsp(graph)
print("Minimum cost of the TSP tour:", result)