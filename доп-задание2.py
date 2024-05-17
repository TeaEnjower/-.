from __future__ import annotations
from typing import Dict, List


def tsp_solver(weights: Dict[int, Dict[int, int]]):
    amount_of_cities = len(weights)
    routes: Dict[List[int]] = dict()
    prev: Dict[List[int]] = dict()
    routes[0] = [0]
    prev[0] = [0]
    for length in range(1, amount_of_cities):
        routes[length] = float('inf')
        for j in range(1, amount_of_cities):
            if j in prev:
                continue
            if j not in weights[prev[length - 1]].keys():
                continue
            if routes[length] < routes[length - 1] + weights[prev[length - 1]][j]:
                routes[length] = routes[length - 1] + weights[prev[length - 1]][j]
                prev = j
    return routes[amount_of_cities - 1], prev


print(tsp_solver({0: {1: 3}, 1: {0: 3}}))