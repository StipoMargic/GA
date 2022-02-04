def get_max_height(active):
    return max([height[1] for height in active])

def main(buildings):
    outlines = []
    edges = []
    current_height = 0

    edges.extend([building[0],building[2]] for building in buildings)
    edges = sorted(sum(edges,[]))
 
    for i in edges:
        active = []
        active.extend(building for building in buildings if (building[0] <= i and building[2] > i))

        if not active:
            current_height = 0
            outlines.append((i, current_height))
        else:
            max_height = get_max_height(active)
            if(max_height != current_height):
                current_height = max_height
                outlines.append((i, max_height))

    return  outlines


buildings = [[1,11,5], [2,6,7], [3,13,9], [12,7,16], [14,3,25], [19,18,22], [23,13,29], [24,4,28]]
print(main(buildings))