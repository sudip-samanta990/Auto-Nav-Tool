# Prerequisite
1. ROS Environment
2. Install Cartographer
3. Install z3 solver 

## Description of AUTONAV

1. Generate a map-file using Cartographer

2. amcl package from ROS navigation is used for localization.
   (example: roslaunch /pkg_path move_base_demo_amcl.launch )

3. Run amcl_pose.py to store robot's pose.

3. Run map_analyzer.py, it will take the map-file as input and produces a list of obstacles.
(Each line of the obstacle lists contains the range of the x and y coordinates for each obstacle region)

4. SMT_constraint_generator generate the constraint file (SMT file).

(Note: after doing step (2) at once, we can use step (3) for several times to predict several feasible paths for different source and goal location using the same map)

5. SMT Solver: z3 is used to solve the SMT constraint file.

### Use auto_nav.py (alternative)

1. Use auto_nav.py for a readily available map-file.

