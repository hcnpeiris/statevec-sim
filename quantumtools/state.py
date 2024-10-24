import numpy as np

# Define state vector
def state_vector(state):
    if isinstance(state, int):
        state = (state,)
    
    state_vectors = [np.array([1, 0]) if x == 0 else np.array([0, 1]) for x in state]
    result = state_vectors[0]
    for state_vector in state_vectors[1:]:
        result = np.kron(result, state_vector)
    
    return result.reshape(-1, 1)

# Define state tensor
def state_tensor(state):
    if isinstance(state, int):
        state = (state,)
    
    state_vectors = [np.array([1, 0]) if x == 0 else np.array([0, 1]) for x in state]
    result = state_vectors[0]
    for state_vector in state_vectors[1:]:
        result = np.kron(result, state_vector)
    
    return result.reshape([2]*len(state))

