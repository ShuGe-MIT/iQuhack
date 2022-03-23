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
        # four qubits for the player to teleport their state
        # amp = np.random.rand(9+4)
        # for a,i in enumerate(amp):
        #    self.circuit.initialize([i,np.sqrt(1-i**2)],a)
        
        #try equal amplitudes first

        # x = 1/np.sqrt(3)
        # for q in [0,2,6,8]:
        #    self.circuit.initialize([x, -np.sqrt(1-x**2)], q)
        # for q in [1,3,4,5,7]:
        #    self.circuit.initialize([x, np.sqrt(1-x**2)], q)
       
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
        job = execute(self.circuit, backend=self.backend, shots=1)
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

class classic_board:

    def __init__(self):
        """
        This is a classic table to keep track of the state that has been measured and return o the player
        """
        self.result = {str(i): None for i in range(9)}
    
    def update(self,record):
        """
        rec: a dictionary that maps pos (string of integer from 0 to 8) to the measured state (int)
        Update the state of the board (if the square has been measured, the measured state will be kept here)
        """
        if len(record) == 0:
            return "Continue"
        for key in record:
            if not isinstance(self.result[key], int):
                self.result[key] = record[key]
        
        if isinstance(self.end_game(),str):
            return self.end_game()
        else:
            return "continue"
        
        #return self.end_game() if not isinstance(self.end_game(),str) else "Continue"
    
    def return_board(self):
        """
        return the current state of the board
        """
        board, temp = [], [None for i in range(len(self.result.keys()))]
        row = []
        for key in self.result:
            temp[int(key)] = self.result[key]
        for item in temp:
            row.append(item)
            if len(row) == 3:
                board.append(row)
                row = []
        return board
    
input = [("cnot", 1,2), ("hadamard",3), ("sigmaz",2),("hadamard",2),("cnot",3,4),("hadamard",8),("cnot",4,5),("measure",8), ("teleport", 2 ,4), ("measure",6)]

super_board = classic_board()
backend = Aer.get_backend('qasm_simulator')
info_for_classic_board = []
# Sample input
#while super_board.update(info_for_classic_board) == "Continue":
   
def instruction(input_seq):
    """
    Given an input_seq (a list of tuple),
    Return a Quantum Circuit that will be submitted to the Azure Quantum
    """
    #intitilaize the board
    qc = Qtic(backend)
    for item in input_seq:
        if item[0] == "cnot":
            i,j = item[1], item[2]
            qc.cnot(i,j)
        elif item[0] == "hadamard":
            qc.hadamard(item[1])
        elif item[0] == "sigmaz":
            qc.pauliz(item[1])
        elif item[0] == "swap":
            i,j = item[1], item[2]
            qc.swap(i,j)
        elif item[0] == "teleport":  # Remember to fix this code
            qc.teleportation(item[1],item[2], 10)
        elif item[0] == "measure":  # Remember to fix this code
            qc.measure([item[1]])
    return qc


def get_the_final_state(input_1):
    """
    Input_1: a list of dictionaries of marginal counts e.g: [{'1': 1046, '0': 1002}, {'1': 1001, '0': 1047}] (e.g: output of Qtic.simulate)
    Return the state that corresponds to higher frequency for each qubit
    """
    record = []
    for item in input_1:
        if len(item) == 1:
            record.append(int(list(item.keys())[0]))
        elif item['1'] > item['0']:
            record.append(1)
        else:
            record.append(0)
    return record


def get_measured_qubit(quantum_board):
    """
    Args:
        quantum_board: (an instance of the Qtic) contains information about the quantum board
    Return:
        a list of index for qubits that have been measured by the player
    """
    result = []
    for i in range(9):
        #result.append(i)
        if quantum_board.check_measure(i) == "measured":
            result.append(i)
    return result


def extract_measured_states(record, measured_list):
    """
    Given the following input:
        record: a list of all final states where the index of the list corresponds to the index in the quantum board
        measured_list: a list of index for qubits that have been measured by the player
    Return a dictionary of that maps the position that has been measured to the correspond state from record (This will be used to update the classic board)
    """
    result = {}
    for index in measured_list:
        result[str(index)] = record[index]
    return result


# backend_str = "ionq.qpu"
backend_str = "ionq.simulator"
def submit_job(quantum_circuit, shot, backend_str):
    """
    Submit the job to Azure Quantum
    Return the job for future investigation
    """
    from azure.quantum.qiskit import AzureQuantumProvider
    provider = AzureQuantumProvider (
    subscription_id = "b1d7f7f8-743f-458e-b3a0-3e09734d716d",
    resource_group = "aq-hackathons",
    name = "aq-hackathon-01",
    location = "eastus"
    )
    qpu_backend = provider.get_backend(backend_str)
    qpu_job = qpu_backend.run(quantum_circuit, shots=shot)
    return qpu_job