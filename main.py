n = int(input())
min_size = 0
count = 0
for i in range(1, n + 1):
    count_way = int(input())
    max_height_tunnel = 500
    for j in range(1, count_way + 1):
        tunnel_height = int(input())
        if max_height_tunnel > tunnel_height:
            max_height_tunnel = tunnel_height
            continue
    if min_size < max_height_tunnel:
        min_size = max_height_tunnel
        count = i
print(count, min_size)
