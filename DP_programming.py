processing_time = [
    [5, 6, 4],
    [3, 7, 2],
    [8, 5, 6]
]

transition_cost = [
    [0, 2, 3],
    [2, 0, 1],
    [3, 1, 0]
]

n = len(processing_time)
m = len(processing_time[0])
DP = [[0]*m for _ in range(n)]

for j in range(m):
    DP[0][j] = processing_time[0][j]

for i in range(1, n):
    for j in range(m):
        min_time = float('inf')
        for k in range(m):
            time = DP[i-1][k] + transition_cost[k][j]
            if time < min_time:
                min_time = time
        DP[i][j] = min_time + processing_time[i][j]

min_total_time = min(DP[n-1])
print("Minimum toplam süre:", min_total_time)

print("\nDP Tablosu (Her hücre toplam süreyi gösterir):")
for i in range(n):
    for j in range(m):
        print(f"{DP[i][j]:>4}", end=" ")
    print()