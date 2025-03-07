from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count
def points_cover(starts, ends, points):
    assert len(starts) == len(ends)
    if not (starts and ends and points): return []
    counts= []
    points.sort()
    segments = list(zip(starts, ends))
    segments.sort(key= lambda x : x[1])
    segment_i = 0
    for point in points:
        count = 0
        while (segment_i < len(segments) and segments[segment_i][1] < point): segment_i += 1
        for segment in segments[segment_i:]:
            if segment[0] <= point: count += 1
        counts.append(count)
    return counts


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
