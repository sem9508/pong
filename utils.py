def check_max_vector(vector):
    if vector[0] > 1:
        vector[0] = 1
    if vector[0] < -1:
        vector[0] = -1
    if vector[1] > 1:
        vector[1] = 1
    if vector[1] < -1:
        vector[1] = -1

    return vector 
