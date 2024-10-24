import numpy as np

I = np.array([[1, 0],
              [0, 1]])  
X = np.array([[0, 1], 
              [1, 0]])  
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]]) 
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0], 
                 [0, 0, 0, 1], 
                 [0, 0, 1, 0]])  

def h_gate(state_vector, qubit_index):
    num_of_states=len(state_vector)
    num_qubits = int(np.log2(num_of_states))
    I = np.eye(2)
    operation = 1
    for i in range(num_qubits):
        if i == qubit_index:
            operation = np.kron(operation, H) if isinstance(operation, np.ndarray) else H
        else:
            operation = np.kron(operation, I) if isinstance(operation, np.ndarray) else I
    
    new_state_vector = operation @ state_vector  
    return new_state_vector

def x_gate(state_vector, qubit_index):
    num_of_states=len(state_vector)
    num_qubits = int(np.log2(num_of_states))
    operation = 1
    for i in range(num_qubits):
        if i == qubit_index:
            operation = np.kron(operation, X) if isinstance(operation, np.ndarray) else X
        else:
            operation = np.kron(operation, I) if isinstance(operation, np.ndarray) else I
    new_state_vector = operation @ state_vector  
    return new_state_vector

def cnot_gate(state_vector, control_qubit_index):
    num_of_states = len(state_vector)
    num_qubits = int(np.log2(num_of_states))
    
    operation = 1 
    i = 0
    while i < num_qubits:
        if i == control_qubit_index:  
            operation = np.kron(operation, CNOT)
            i += 2  
        else:
            operation = np.kron(operation, I)
            i += 1
    
    new_state_vector = operation @ state_vector  
    return new_state_vector

def tx_gate(state_vector, qubit_index):
    # Apply the X gate to the specific qubit axis using tensordot
    new_state_vector = np.tensordot(X, state_vector, axes=([1], [qubit_index]))
    
    # Move the contracted axis (the qubit the gate was applied to) back to its original position
    new_state_vector = np.moveaxis(new_state_vector, 0, qubit_index)
    
    return new_state_vector

def th_gate(state_vector, qubit_index):
    # Apply the H gate to the specific qubit axis using tensordot
    new_state_vector = np.tensordot(H, state_vector, axes=([1], [qubit_index]))
    
    # Move the contracted axis (the qubit the gate was applied to) back to its original position
    new_state_vector = np.moveaxis(new_state_vector, 0, qubit_index)
    
    return new_state_vector
def tcnot_gate(state_vector, control_qubit_index, target_qubit_index):
    # Apply the CNOT gate to the control and target qubits using tensordot
    CNOT_tensor = CNOT.reshape(2, 2, 2, 2)
    new_state_vector = np.tensordot(CNOT_tensor, state_vector, axes=([1, 0], [control_qubit_index, target_qubit_index]))
    
    # Move the contracted axes back to their original positions
    new_state_vector = np.moveaxis(new_state_vector, [0, 1], [control_qubit_index, target_qubit_index])
    
    return new_state_vector
