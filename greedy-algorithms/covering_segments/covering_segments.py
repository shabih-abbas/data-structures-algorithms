# Input: A sequence of n segments [l1,r1 ],..., [ln,rn] on a line.
# Output: A set of points of minimum size such that each segment
# [li,ri] contains a point, i.e., there exists a point x from this set such
# that li ≤ x ≤ ri.
# Constraints. 1 ≤ n ≤ 100; 0 ≤ li ≤ ri ≤ 10^9 for all i.

from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

def optimal_points_fast(segments):
    if not segments: return []
    points = []
    # write your code here
    segments.sort(key= lambda x: x.end)
    points.append(segments[0].end)
    for s in segments:
        if s.start > points[-1]: points.append(s.end)
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points_fast(segments)
    print(len(points))
    print(*points)
