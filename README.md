# Qic Qac Qoe


## Overview

We implement a quantum version of the classic two-player game, Tic Tac Toe. Our game is played on a 3x3 grid, where each square is a qubit initialized to the state:

<img src="https://latex.codecogs.com/svg.image?|\psi_0\rangle=\frac{1}{\sqrt{2}}(|0\rangle&plus;|1\rangle)" title="|\psi_0\rangle=\frac{1}{\sqrt{2}}(|0\rangle+|1\rangle)" />

One player wins with 0's, and another player wins with 1's. Upon each turn, a player may perform one of six possible moves:

#### 1) Measurement

The player measures any state on the board in the <img src="https://latex.codecogs.com/svg.image?\{|0\rangle,|1\rangle\}" title="\{|0\rangle,|1\rangle\}" /> basis. The state on the board hence collapses into the measured state. 

Additionally, the player may apply single-qubit gates on a particular quantum state:

#### 2) Hadamard gate

The player selects one qubit and applies 

<img src="https://latex.codecogs.com/svg.image?H&space;=&space;\frac{1}{\sqrt{2}}\begin{bmatrix}1&space;&&space;1&space;\\&space;1&space;&&space;-1\end{bmatrix}" title="H = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix}" />

It is represented by "plus -> O" gate in the game.

#### 3) Z gate followed by Hadammard gate

The player selects one qubit and applies 

<img src="https://latex.codecogs.com/svg.image?H\sigma_z&space;=&space;\frac{1}{\sqrt{2}}\begin{bmatrix}1&space;&&space;-1&space;\\&space;1&space;&&space;1\end{bmatrix}" title="H\sigma_z = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & -1 \\ 1 & 1\end{bmatrix}" />

It is represented by "plus -> X" gate in the game.

#### 4) Controlled NOT gate

The player selects two qubits, and applies

<img src="https://latex.codecogs.com/svg.image?CNOT&space;=&space;\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}" title="CNOT = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}" />

This may result in the two states becoming entangled with each other. 

#### 5) SWAP gate

<img src="https://latex.codecogs.com/svg.image?SWAP&space;=&space;\begin{bmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{bmatrix}" title="SWAP = \begin{bmatrix}1&0&0&0\\0&0&1&0\\0&1&0&0\\0&0&0&1\end{bmatrix}" />

Finally, to showcase the full range of the capabilities of quantum computation, the player may also teleport a quantum state across the board:

#### 6) Quantum teleportation

Each player carries an ancillary qubit m, which can be used to form an EPR pair with another state on the grid j and teleport an existing state at square i to j. A C-NOT gate is applied to qubit i and m (i is the control qubit and m is the target qubit). After applying Hadamard to qubit i, we measure both quibits i and m. 

Such a move would not be possible with classical bits.

## Gameplay

Gameplay begins by running the file `main.py`, upon which the players will see an initialized board, with buttons for each action that may be performed on the qubits.

<img src="https://user-images.githubusercontent.com/36899444/151707898-f3802d94-4efb-49a3-8b3c-efc35ef1d69c.png" width="200" >

The player may then select a qubit and a possible operation on the qubit from the selection menu. 

<img src="https://user-images.githubusercontent.com/36899444/151708033-9edd71f7-ff19-4f60-97af-f4cccc249fe4.png" width="200" >

Each player takes turns, performing actions on the qubits. 

<img src="https://user-images.githubusercontent.com/36899444/151708161-5fcb9572-ef5a-4a6f-a8a9-5d10fabf7e43.png" width="200" >

The winning condition is checked after all qubits have been measured or after 20 moves (to prevent infinite gameplay). It is important to note that once a state has been measured, no further actions may be performed on that state. Furthermore, all states are measured prior to the winning condition being checked.

## Resources

Our game is inspired by 

M. Nagy and N. Nagy, "Quantum Tic-Tac-Toe: A Genuine Probabilistic Approach," Applied Mathematics, Vol. 3 No. 11A, 2012, pp. 1779-1786. doi: 10.4236/am.2012.331243.

In our project, we have extended their ideas and implemented additional gates and actions. 

## About the team

We are a diverse group of MIT undergraduate students studying subjects from physics to chemistry, from mathematics to computer science. We came together as a group to pursue our shared interests in quantum computing and quantum technologies. Our time at MIT has granted us the opportunity to meet and learn from leading experts in the field. These experiences have been extremely valuable and will certainly have an impact on our futures.
