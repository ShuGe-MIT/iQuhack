from qiskit import QuantumCircuit, Aer, execute
from qiskit.aqua import QuantumInstance
from qiskit import *
from qiskit.visualization import plot_histogram
from qiskit.result import marginal_counts
from qiskit.tools.monitor import job_monitor

import matplotlib.pyplot as plt
import numpy as np

class Qtic:
    def __init__(self,backend):
        """"
        Configuration of the board:

        || 0 || 1 || 2 ||
        || 3 || 4 || 5 ||
        || 6 || 7 || 8 ||

        A circuit of 13 qubits and 9 classical bits
        Each qubit represents a state of the square (either Black or White)
        Each classical bit represents 
        """
        self.result = {str(i): None for i in range(9)} #store the result
        self.backend = backend
        self.circuit = QuantumCircuit(9+4, 9+4)
        self.circuit.h([i for i in range(9+4)])
       
    def hadamard(self,i):
        """
        i: square i in the board [from 0 to 8] 
        Apply Hadamard gate to the state in square i
        """
        self.circuit.h([i])
        print("Add a Haddamard to square " + str(i))

    def pauliz(self, i):
        """
        i: square i in the board [from 0 to 8] 
        Apply sigma_z to the 
        """
        self.circuit.z(i)
        print("Add a sigma_z to square " + str(i))

    def cnot(self, i, j):
        """
        i: square i in the board [from 0 to 8] 
        j: square j in the board [from 0 to 8]
        """
        self.circuit.cx(i,j)
        print("Add a CNOT gate to the board between " + str(i) + " and " + str(j))

    def swap(self, i, j):
        """
        i: square i in the board [from 0 to 8]
        j: square j in the board [from 0 to 8]
        swaps the qubit i with the qubit j
        """
        self.circuit.swap(i,j)
        print("Swap qubit " + str(i) + " with qubit " + str(j))


    def teleportation(self,i,j,m):
        """
        i: square i in the board [from 0 to 8] 
        j: square j in the board [from 0 to 8]
        m: This is the helper qubit [9,10,11,12] (depends on the number of times that a player are allowed to teleport)
        Teleport the state at square i to square j with the help of the extra qubit
        """
        #reinitialize Bell pair qubits
        self.circuit.initialize([1,0],j)
        self.circuit.initialize([1,0],m)
        #create Bell pair
        self.circuit.h(m)
        self.circuit.cx(m,j)
        self.circuit.barrier()
        #sender's protocol 
        self.circuit.cx(i,m)
        self.circuit.h(i)
        self.circuit.measure(i,i)
        self.circuit.measure(m,m)
        self.circuit.barrier()
        self.circuit.x(j).c_if(self.circuit.clbits[m], 1) 
        self.circuit.z(j).c_if(self.circuit.clbits[i], 1)
        print("Teleport between " + str(i) + " and " + str(j))

    def measure(self, i):
        """
        i: a list of squares in the box [only from 0 to 8]
        Perform a measurement on the square i and store it to the 
        classical qubit i
        """
        self.circuit.measure([j for j in i], [j for j in i])
        print("measure the state in square " + str(i))
        
    def plot(self):
        """
        Return the plot of the quantum circuit that corresponds to what players have put in now
        """
        return self.circuit.draw()

    def simulate(self, shot):
        """
        Shots: number of time to run it on the backend
        Submit the whole circuit to the backend and execute it
        Return a histogram of the outcome.
        """
        #measure all qubits before running job
        self.measure([i for i in range(9)])
        job = execute(self.circuit, backend=self.backend, shots=shot)
        job_monitor(job)
        def print_status(jb):
            print(jb.status+" | "+jb.name + " | " + jb.target + " | " + jb.creation_time + " | " + jb.end_execution_time)
        #job = execute(self.circuit,backend = QuantumInstance(self.backend, shots = shot))
        print("Successfully execute the job")
        result = job.result()
        marginals = [marginal_counts(result.get_counts(),[i]) for i in range(9)]  # not accounting for the last four qubits
        plot_histogram(marginals)
        return marginals
        ##########################
        #counts = marginal_counts(self.result, indices=[_ for _ in range(9+4)]).get_counts()
        #if shot == 1:
        #    return counts.keyes()
        #    #return counts.keys()[0]
        #else: #return outcome with highest probability
        #    d = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
        #    return d.keys()[0]
        #########################################

    def check_measure(self,i):
        """
        i is the index of the qubit (or the square that we want to check) that we need to check [from 0 to 8]
        Return "measured" if the player has measured the qubit and "not measured" otherwise
        """
        gate = []
        for j in self.circuit.data:
            if j[1][0].index == i:
                gate.append(j[0].name)
        if 'measure' in gate:
            return "measured"
        else: 
            return "not measured"

    def return_board(self):
        """
        Return the quantum circuit that represents the game
        """
        return self.circuit

