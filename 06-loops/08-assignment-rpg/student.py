def rpg2(n_sides, goal):
    higher = 0
    lower = 0
    total = n_sides**2
    if n_sides == 0:
        return 0
    for i in range(1,n_sides+1):
        for s in range(1, n_sides+1):
            if (i + s) >= goal:
                higher +=1
            else:
                lower +=1

    return (higher/total) * 100


def rpg3(n_sides, goal):

    higher = 0
    lower = 0
    total = n_sides**3
    if n_sides == 0:
        return 0
    for i in range(1,n_sides+1):
        for s in range(1, n_sides+1):
            for t in range(1,n_sides+1):

                if (i + s + t) >= goal:
                    higher +=1
                else:
                    lower +=1

    return (higher/total) * 100


