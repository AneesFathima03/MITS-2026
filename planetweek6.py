def sort_planets(planets):
    '''sort planets by surface area in descending order'''
    # surface area is at index 1
    sorted_list = sorted(planets, key=lambda x: x[1], reverse=True)
    return sorted_list


def display(sorted_planets):
    '''display output'''
    print("Sorted by surface area in descending order:")
    for planet in sorted_planets:
        print(planet[0], end=" ")


def getinput():
    '''return the planets list'''
    planets = [
        ('Mercury', 75, 1),
        ('Venus', 460, 2),
        ('Mars', 140, 4),
        ('Earth', 510, 3),
        ('Jupiter', 62000, 5),
        ('Neptune', 7640, 8),
        ('Saturn', 42700, 6),
        ('Uranus', 8100, 7)
    ]
    return planets


def main():
    planets = getinput()
    sorted_planets = sort_planets(planets)
    display(sorted_planets)


main()
