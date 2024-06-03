def flatten(sample_list):
    result = []
    for element in sample_list:
        if isinstance(element, list):
            print("List found!")
            flat_list = flatten(element)
            result += flat_list
        else:
            result.append(element)
    return result


planets = [
    "mercury",
    "venus",
    ["earth"],
    "mars",
    [["jupiter", "saturn"]],
    "uranus",
    ["neptune", "pluto"],
]

print(flatten(planets))
