class Item():
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def knapsack(capacity, items):
    ''' A  method to determine the maximum value of the items included in the knapsack 
    without exceeding the capacity  C

        Parameters: 
        C= 50
        items = (("boot", 10, 60),
            ("tent", 20, 100),
            ("water", 30, 120),
            ("first aid", 15, 70))
        Returns: max value
    '''

    #base case
    if len(items) == 0 or capacity == 0:
        return (0, [])

    item = items[0]

    # if item weights more than the available capacity, ignore the item, call recursive function again
    if item.weight > capacity:
        return knapsack(capacity, items[1:])

    # if item weight is fittable,

    # first calculate the value of rest of the item including this current item, until it reaches capacity
    value_with, items_used_with = knapsack(capacity - item.weight, items[1:])
    value_with += item.value
    
    # second calculate the value of rest of the items, excluding the current item
    value_without, items_used_without = knapsack(capacity, items[1:])

    # check which calculation has higher value
    if value_with >= value_without:
        # if the value is higher including the item, use this item
        items_used_with.append(item.name)
        return (value_with, items_used_with)

    # if the value is higher without the item, ignore this item, call this function again 
    return (value_without, items_used_without)

items = (Item("boot", 10, 60),
        Item("tent", 20, 100),
        Item("water", 30, 120),
        Item("first aid", 15, 70))

print(knapsack(50, items))