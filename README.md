# Ex4_OOP
Capture Pokemons in the road (represented by a directed weighted graph).
## About the project.
There are agents and Pokemons. The purpose of the game is to catch as many pokemons as possible by the agents and finish with as high a score as possible.  
Pokemons are divided into 2 types, those on the "up" edges and those on the "down" edges (reminder: the graph is directed).  
Each Pokemon has its own value, the higher the value the better.  
The agents are located at the beginning of the game near to a pokemon
##### How to catch a Pokemon?  
The pokemon are placed on the directed edges of the graph, so if there is a pokemon located on edge A -> B, then the agent has to reach vertex A and move from it on the edge to vertex B (not reversed).  
##### How do we know where to lead each agent?  
We find for each agent the shortest path from his location to a pokemon location. The 'game' is based on Dijkstra's algorithm to find the shortest path.

## Download and run - instructions.
First start the server, how? download the attached jar file, this is the server which can be run on any java machine (JDK 11 or above) in a command line,  
e.g., <java -jar Ex4_Server_v0.0.jar 0> (where the “0” parameter is a case between [0-15]). Choose the case you want.  
Then run "student_code".py and watch the game on the screen. At the end of the game the result will be printed by the server.  


## For more information about the project visit the Wiki page: https://github.com/ShaniVahav/Ex4_OOP/wiki/_new




