from quantumtools import state_vector, state_tensor,x_gate, h_gate, cnot_gate, tcnot_gate, tx_gate, th_gate
import random, time
import matplotlib.pyplot as plt

n_qubits = []
runtimes = []

for i in range(2, 29):
    state= tuple(random.choice([0, 1]) for _ in range(i))
    index1 = random.randint(0 , len(state)-2)
    index1 = random.randint(0, len(state) - 2)
    index2 = random.randint(0, len(state) - 1)
    # Ensure index2 is different from index1
    while index2 == index1:
        index2 = random.randint(0, len(state) - 1)
    print(len(state))
    
    # Generate the state vector
    state_vec = state_tensor(state)
    start_time = time.time()
    state_vec1 = tx_gate(state_vec, index1)
    state_vec2 = th_gate(state_vec, index1)
    state_vec3 = tcnot_gate(state_vec, index1, index2)
    end_time = time.time()
    n_qubits.append(i )
    runtimes.append(end_time - start_time)

plt.plot(n_qubits, runtimes, marker='o', linestyle='-')
plt.title('Simulation Runtime vs. Number of Qubits')
plt.xlabel('Number of Qubits')
plt.ylabel('Runtime (seconds)')
plt.grid(True)
plt.show()
print(n_qubits)