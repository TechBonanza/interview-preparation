EXPECTED_BAKE_TIME = 40
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time

#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """
    Return preparation time in minutes

    :param number_of_layers: int number of layers to be baked
    :return int preparation time required from 'PREPARATION_TIME'
    """
    preparation_time = PREPARATION_TIME * number_of_layers
    return preparation_time

def elapsed_time_in_minutes(number_of_layers = 1, elapsed_bake_time = 0):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    
    return preparation_time_in_minutes(number_of_layers) + (elapsed_bake_time)