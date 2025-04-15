from sys import stdin

def segments_upper(segments, point):
    upper = len(segments)-1
    lower = 0
    index = []
    if point <= segments[lower][1] : return lower
    if point > segments[upper][1]: return upper + 1
    while(not (upper < lower or point < segments[lower][1])):
        m = lower + (upper - lower) // 2
        if segments[m][1] == point: 
            index.append(m)
            upper = m - 1
        if point > segments[m][1]: lower= m + 1
        else: upper = m - 1
    return index[-1] if index else lower

def segments_search(segments, point, index=0):
    upper = len(segments)-1
    lower = 0
    if point < segments[lower][index] : return lower
    if point >= segments[upper][index] : return upper + 1
    while(not (upper < lower or point < segments[lower][0])):
        m = lower + (upper - lower) // 2
        if segments[m][index] == point: lower = m + 1
        if point > segments[m][index]: lower= m + 1
        else: upper = m - 1
    return lower

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
    # points.sort()
    segments = list(zip(starts, ends))
    length= len(segments)
    segments_u_sorted= sorted(segments, key= lambda x : x[1])
    segments_l_sorted= sorted(segments, key= lambda x : x[0])
    for point in points:
        count = 0
        u_index= segments_upper(segments_u_sorted, point)
        l_index= segments_search(segments_l_sorted, point)
        if u_index - length < l_index :
            for i in range(u_index, length):
                if segments_u_sorted[i][0] <= point: count += 1
        else : 
            for i in range(l_index) :
                if segments_l_sorted[i][1] >= point: count += 1
        counts.append(count)
    return counts

def points_cover_fast(starts, ends, points):
    assert len(starts) == len(ends)
    if not (starts and ends and points): return []
    counts= []
    segments = list(zip(starts, ends))
    length= len(segments)
    segments_u_sorted= sorted(segments, key= lambda x : x[1])
    segments_l_sorted= sorted(segments, key= lambda x : x[0])
    for point in points:
        counts.append(segments_search(segments_l_sorted, point) - segments_search(segments_u_sorted, point - 1, 1))
    return counts

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_fast(input_starts, input_ends, input_points)
    print(*output_count)
    
    