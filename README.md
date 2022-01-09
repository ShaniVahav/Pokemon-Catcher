# Ex4_OOP
Capture Pokemons in the road (represented by a directed weighted graph).
## About the project.
There are agents and Pokemons. The purpose of the game is to catch as many Pokemons as possible by the agents and finish with as high a score as possible.  
Pokemons are divided into 2 types, those on the "up" edges and those on the "down" edges (reminder: the graph is directed).  
Each Pokemon has its own value, the higher the value the better.  
The agents are located at the beginning of the game at random.
##### How to catch a Pokemon?  
The Pokemon are placed on the directed sides of the graph, so if there is a Pokemon located on side A -> B, then the agent has to reach vertex A and move from it on the edge to vertex B (not reversed).  
##### How do we know where to lead each agent?  
We find for each agent the shortest path from his location to the Pokemon location. The 'game' is based on Dijkstra's algorithm to find the shortest path.

## Main Functions.
### shortestPath(A,B):
Returns the shortest path from node A to node B using Dijkstra's Algorithm.  
(Dijkstra's Algorithm info: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)

### initializeView() & display_update():
The first builds the graph, the agents and the Pokemons,
The second updates the view at any moment,  
such as the 'end of game timer', the location of the pokemosn and agents, and changing the resolution if required.


## Download and run - instructions.
First start the server, how? download the attached jar file, this is the server which can be run on any java machine (JDK 11 or above) in a command line,  
e.g., <java -jar Ex4_Server_v0.0.jar 0> (where the “0” parameter is a case between [0-15]). Choose the case you want.  
Then run "student_code".py and watch the game on the screen. At the end of the game the result will be printed by the server.  
## Run Time.
For more information on runtime, visit my wiki page!  
--> https://github.com/ShaniVahav/Ex4_OOP/wiki

## Class Diagram.





