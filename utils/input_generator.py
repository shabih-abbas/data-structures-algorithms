import random
def generate_inputs(lower, upper, count, data_type):
    """Generate a list of random inputs based on type and bounds."""
    if data_type == "int":
        return [random.randint(int(lower), int(upper)) for _ in range(count)]
    else:
        return [random.uniform(lower, upper) for _ in range(count)]
def generate_boundary_inputs(bound, count, data_type):
    if data_type== "int":
        return [int(bound) for _ in range(count)]
    else:
        return [bound for _ in range(count)]