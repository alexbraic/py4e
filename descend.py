
mountain_list = [0, 8, 7, 6, 5, 4, 3, 2]

while True:
    # for i in range(8):
        # mountain_h = int(input())  # represents the height of one mountain.
        # mountain_list.append(mountain_h)
        # mountain_list.sort()

    for i in mountain_list:
        print(mountain_list.index(max(mountain_list)))
        # mountain_list.remove(mountain_list.index(min(mountain_list)))
