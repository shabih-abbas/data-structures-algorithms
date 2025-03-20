def edit_distance(first_string, second_string):
    dist= []
    n = len(first_string)
    m = len(second_string)
    for i in range(0, m + 1): dist.append([i])
    for j in range(1, n + 1): dist[0].append(j)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insr= dist[i-1][j] + 1
            dele= dist[i][j-1] + 1
            matc= dist[i-1][j-1]
            subs= dist[i-1][j-1] + 1
            if first_string[j-1] == second_string[i-1]: dist[i].append(min(insr, dele, matc))
            else: dist[i].append(min(insr, dele, subs))
    return dist[m][n]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
