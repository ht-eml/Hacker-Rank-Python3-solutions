#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    true_mapping = [i for i in range(101)]
    for i in range(len(ladders)):
        true_mapping[ladders[i][0]] = ladders[i][1]
    for i in range(len(snakes)):
        true_mapping[snakes[i][0]] = snakes[i][1]

    # build graph adjacency list
    graph = {}
    for i in range(1, 101):
        if i == true_mapping[i]:
            graph[i] = []
            # add a neighbor for each die result
            for j in range(1, 7):
                if i+j <= 100:
                    graph[i].append(true_mapping[i+j])

    # bfs from 1 to 100
    def shortest_path (start, end):
        if start == end: return 0
        visited = [0]*101
        queue = [(start, 0)]
        while queue:
            node, dist = queue.pop(0)
            visited[node] = 1
            if node == end:
                return dist
            for child in graph[node]:
                if not visited[child]:
                    visited[child] = 1
                    queue.append((child, dist+1))
    return shortest_path(1, 100)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + '\n')

    fptr.close()
