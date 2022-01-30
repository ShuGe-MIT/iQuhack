# iQuhack

We implement a quantum version of the classic two-player game, Tic Tac Toe. Our game is played on a 3x3 grid, where each square is initialized to the quantum state:

<img src="https://latex.codecogs.com/svg.image?|\psi_0\rangle=\frac{1}{\sqrt{2}}(|0\rangle&plus;|1\rangle)" title="|\psi_0\rangle=\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)" />

One player wins with 0's, and another player wins with 1's. Upon each turn, a player may perform one of three possible moves:

### 1) Measurement

The player measures any state on the board in the <img src="https://latex.codecogs.com/svg.image?\{|0\rangle,|1\rangle\}" title="\{|0\rangle,|1\rangle\}" /> basis. The state on the board hence collapeses into the measured state.

### 2) Controlled NOT gate

The player selects two qubits, and applies a CNOT gate between them. This may result in the two states becoming entangled with each other. 

### 3) H-Z gate

The player applies a Z-gate followed by a Haddamard gate.

Future implementations of our game may include a fourth possible move:

### 4) Quantum teleportation

Each player carries an ancillary qubit, which can be used to form an EPR pair with another state on the grid and teleport an existing state to another position. Such a move would not be possible with classical bits.
