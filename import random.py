import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000):
        return []
    if not (min <= quantity <= max - min + 1):
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    result = sorted(numbers)
    return result