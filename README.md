#Prerequisite
install z3 solver 

##Description of Auto-Nav-Tool

i) generate a map-file by cartographer

ii) THen use map_analyzer to cover the obstacle points by rectangular block region and creat a obstacle lists.
(Each line of the obstacle lists contains the range of the x and y axis for each block obstacles region)

iii) Then use SMT_constraint_generator to solve and predict a feasible path from source to goal location.

(Note: after doing step (ii) at once, we can use step iii) for several times to predict several feasible paths for different source and goal location using the same map)

iv) To predict feasible path from source to goal location for different map, then use auto_nav.py

