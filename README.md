# OOP-Assignment-4
## Preface


In this Assignment we asked to design a “Pokemon game” in which given a weighted graph,  a set of “Agents” should be located on it so they could “catch” as many “Pokemons” as possible.
The pokemons are located on the graph’s (directed) edges, therefore, the agent needs to take (aka walk) the proper edge to “grab” the pokemon.
Our goal is to maximize the overall sum of weights of the “grabbed” pokemons (while not exceeding the maximum amount of server calls allowed in a second - 10 max).
 
 ## About the game
 
 The game is being played on a “server” that is given to us, we design and implement the client-side (only).
 We chose to implement the client side with python.
 After the server is running a client can connect to it (play with it).
 
 ## The GUI
 We created a clear scalable GUI with a resizable window.
 Additional elements are represented in the GUI, such as- overall points, moves counter, and time to end in seconds are presented, as well as a “stop” button to gracefully stop the game at any time point.
After the game ends (each game has a fixed time - commonly 30-120 seconds) the results are printed - by the server.


