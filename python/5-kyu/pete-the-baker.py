def cakes(recipe, available):
    max_cakes = float('inf')
    for r, n in recipe.items():
        num_recipe = n

        if not(r in available):
            return 0
        num_available = available.get(r)
        num_cakes = int(num_available / num_recipe)
        if num_cakes < max_cakes:
            max_cakes = num_cakes

    return max_cakes

recipe = {'crumbles': 20, 'nuts': 99, 'chocolate': 48}

available = {'chocolate': 1767, 'milk': 5214, 'pears': 8182, 'cocoa': 9109, 'eggs': 4611, 'cream': 3100, 'crumbles': 6339, 'nuts': 9705, 'oil': 9376, 'butter': 9496}

print(cakes(recipe, available))
