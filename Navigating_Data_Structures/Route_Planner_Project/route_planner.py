from helpers import Map, load_map_10, load_map_40, show_map
import math
from test import test

map_40 = load_map_40()

'''

The Algorithm
Writing your algorithm
The algorithm written will be responsible for generating a path like the one passed into show_map above. In fact, when called with the same map, start and goal, as above you algorithm should produce the path [5, 16, 37, 12, 34]. However you must complete several methods before it will work.

> PathPlanner(map_40, 5, 34).path
[5, 16, 37, 12, 34]
PathPlanner class
The below class is already partly implemented for you - you will implement additional functions that will also get included within this class further below.

Let's very briefly walk through each part below.

__init__ - We initialize our path planner with a map, M, and typically a start and goal node. If either of these are None, the rest of the variables here are also set to none. If you don't have both a start and a goal, there's no path to plan! The rest of these variables come from functions you will soon implement.

closedSet includes any explored/visited nodes.
openSet are any nodes on our frontier for potential future exploration.
cameFrom will hold the previous node that best reaches a given node
gScore is the g in our f = g + h equation, or the actual cost to reach our current node
fScore is the combination of g and h, i.e. the gScore plus a heuristic; total cost to reach the goal
path comes from the run_search function, which is already built for you.
reconstruct_path - This function just rebuilds the path after search is run, going from the goal node backwards using each node's cameFrom information.

_reset - Resets most of our initialized variables for PathPlanner. This does not reset the map, start or goal variables, for reasons which you may notice later, depending on your implementation.

run_search - This does a lot of the legwork to run search once you've implemented everything else below. First, it checks whether the map, goal and start have been added to the class. Then, it will also check if the other variables, other than path are initialized (note that these are only needed to be re-run if the goal or start were not originally given when initializing the class, based on what we discussed above for __init__.

From here, we use a function you will implement, is_open_empty, to check that there are still nodes to explore (you'll need to make sure to feed openSet the start node to make sure the algorithm doesn't immediately think there is nothing to open!). If we're at our goal, we reconstruct the path. If not, we move our current node from the frontier (openSet) and into explored (closedSet). Then, we check out the neighbors of the current node, check out their costs, and plan our next move.

This is the main idea behind A*, but none of it is going to work until you implement all the relevant parts, which will be included below after the class code.

'''

# Do not change this cell
# When you write your methods correctly this cell will execute
# without problems
class PathPlanner():
    """Construct a PathPlanner Object"""
    def __init__(self, M, start=None, goal=None):
        """ """
        self.map = M
        self.start= start
        self.goal = goal
        self.closedSet = self.create_closedSet() if goal != None and start != None else None
        self.openSet = self.create_openSet() if goal != None and start != None else None
        self.cameFrom = self.create_cameFrom() if goal != None and start != None else None
        self.gScore = self.create_gScore() if goal != None and start != None else None
        self.fScore = self.create_fScore() if goal != None and start != None else None
        self.path = self.run_search() if self.map and self.start != None and self.goal != None else None
    
    def reconstruct_path(self, current):
        """ Reconstructs path after search """
        total_path = [current]
        while current in self.cameFrom.keys():
            current = self.cameFrom[current]
            total_path.append(current)
        return total_path
    
    def _reset(self):
        """Private method used to reset the closedSet, openSet, cameFrom, gScore, fScore, and path attributes"""
        self.closedSet = None
        self.openSet = None
        self.cameFrom = None
        self.gScore = None
        self.fScore = None
        self.path = self.run_search() if self.map and self.start and self.goal else None

    def run_search(self):
        """ """
        if self.map == None:
            raise(ValueError, "Must create map before running search. Try running PathPlanner.set_map(start_node)")
        if self.goal == None:
            raise(ValueError, "Must create goal node before running search. Try running PathPlanner.set_goal(start_node)")
        if self.start == None:
            raise(ValueError, "Must create start node before running search. Try running PathPlanner.set_start(start_node)")

        self.closedSet = self.closedSet if self.closedSet != None else self.create_closedSet()
        self.openSet = self.openSet if self.openSet != None else  self.create_openSet()
        self.cameFrom = self.cameFrom if self.cameFrom != None else  self.create_cameFrom()
        self.gScore = self.gScore if self.gScore != None else  self.create_gScore()
        self.fScore = self.fScore if self.fScore != None else  self.create_fScore()

        while not self.is_open_empty():
            current = self.get_current_node()

            if current == self.goal:
                self.path = [x for x in reversed(self.reconstruct_path(current))]
                return self.path
            else:
                self.openSet.remove(current)
                self.closedSet.add(current)

            for neighbor in self.get_neighbors(current):
                if neighbor in self.closedSet:
                    continue    # Ignore the neighbor which is already evaluated.

                if not neighbor in self.openSet:    # Discover a new node
                    self.openSet.add(neighbor)
                
                # The distance from start to a neighbor
                #the "dist_between" function may vary as per the solution requirements.
                if self.get_tentative_gScore(current, neighbor) >= self.get_gScore(neighbor):
                    continue        # This is not a better path.

                # This path is the best until now. Record it!
                self.record_best_path_to(current, neighbor)
        print("No Path Found")
        self.path = None
        return False
		
def create_closedSet(self):
    """ Creates and returns a data structure suitable to hold the set of nodes already evaluated"""
    # EXAMPLE: return a data structure suitable to hold the set of nodes already evaluated
    return set()
	
def create_openSet(self):
    """ Creates and returns a data structure suitable to hold the set of currently discovered nodes 
    that are not evaluated yet. Initially, only the start node is known."""
    if self.start != None:
        # TODO: return a data structure suitable to hold the set of currently discovered nodes 
        # that are not evaluated yet. Make sure to include the start node.
        open_set = set()
        open_set.add(self.start)
        return open_set
    
    raise(ValueError, "Must create start node before creating an open set. Try running PathPlanner.set_start(start_node)")
	
def create_cameFrom(self):
    """Creates and returns a data structure that shows which node can most efficiently be reached from another,
    for each node."""
    # TODO: return a data structure that shows which node can most efficiently be reached from another,
    # for each node. 
    return dict()

def create_gScore(self):
    """Creates and returns a data structure that holds the cost of getting from the start node to that node, 
    for each node. The cost of going from start to start is zero."""
    # TODO:  return a data structure that holds the cost of getting from the start node to that node, for each node.
    # for each node. The cost of going from start to start is zero. The rest of the node's values should 
    # be set to infinity. https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python 
    # Need 2d array
    #{} create dictioary for tow
    gScore = [] 
    for row_idx in range(len(self.map.intersections)):
        row = {}
        for col_idx in range(len(self.map.intersections)):
            if(row_idx == col_idx):
                row[col_idx] = 0
            else: 
                row[col_idx] = float('inf')
        gScore.append(row)
        
    return gScore
    
    
def create_fScore(self):
    """Creates and returns a data structure that holds the total cost of getting from the start node to the goal
    by passing by that node, for each node. That value is partly known, partly heuristic.
    For the first node, that value is completely heuristic."""
    # TODO: return a data structure that holds the total cost of getting from the start node to the goal
    # by passing by that node, for each node. That value is partly known, partly heuristic.
    # For the first node, that value is completely heuristic. The rest of the node's value should be 
    # set to infinity.
    fScore = {}
    for row_idx in range(self.goal):
        if(row_idx == self.goal):
            fScore[row_idx] = self.heuristic_cost_estimate(row_idx)
        else: 
            fScore[row_idx] = float("inf")
            
    return fScore

def set_map(self, M):
    """Method used to set map attribute """
    self._reset(self)
    self.start = None
    self.goal = None
    # TODO: Set map to new value. 
    self.map = M

def set_start(self, start):
    """
	Method used to set start attribute 
	"""
    self._reset(self)
    # TODO: Set start value. Remember to remove goal, closedSet, openSet, cameFrom, gScore, fScore, 
    # and path attributes' values.
    self.start = start
    self.goal = None

def set_goal(self, goal):
    """Method used to set goal attribute """
    self._reset(self)
    # TODO: Set goal value. 
    self.goal = goal

def is_open_empty(self):
    """returns True if the open set is empty. False otherwise. """
    # TODO: Return True if the open set is empty. False otherwise.
    if len(self.openSet) == 0:
        return True
    else:
        return False

def get_current_node(self):
    """ Returns the node in the open set with the lowest value of f(node)."""
    # TODO: Return the node in the open set with the lowest value of f(node).
    lowest_idx = 0 
    lowest_f_node =  1000000
    current_f_node = 0 
    for openSet_idx in self.openSet:
        current_f_node = self.calculate_fscore(openSet_idx)
        if(current_f_node < lowest_f_node):
            lowest_idx = openSet_idx
            lowest_f_node = current_f_node
        else:
            lowest_idx = lowest_idx
            lowest_f_node = lowest_f_node
            
    return lowest_idx

def get_neighbors(self, node):
    """Returns the neighbors of a node"""
    # TODO: Return the neighbors of a node
    return self.map.roads[node]

def get_gScore(self, node):
    """Returns the g Score of a node"""
    # TODO: Return the g Score of a node
    return self.gScore[self.start][node]
    
def distance(self, node_1, node_2):
    """ Computes the Euclidean L2 Distance"""
    # TODO: Compute and return the Euclidean L2 Distance
    x1 = self.map.intersections[node_1][0]
    y1 = self.map.intersections[node_1][1]
    x2 = self.map.intersections[node_2][0]
    y2 = self.map.intersections[node_2][1]
    delta_x = abs(x1-x2)
    delta_y = abs(y1-y2)
    return math.sqrt(delta_x**2 + delta_y**2)

def get_tentative_gScore(self, current, neighbor):
    """Returns the tentative g Score of a node"""
    # TODO: Return the g Score of the current node 
    # plus distance from the current node to it's neighbors
    return self.get_gScore(current)+self.distance(current,neighbor)

def heuristic_cost_estimate(self, node):
    """ Returns the heuristic cost estimate of a node """
    # TODO: Return the heuristic cost estimate of a node
    return self.distance(node,self.goal)

def calculate_fscore(self, node):
    """Calculate the f score of a node. """
    # TODO: Calculate and returns the f score of a node. 
    # REMEMBER F = G + H
    return self.get_gScore(node)+self.heuristic_cost_estimate(node)
    
def record_best_path_to(self, current, neighbor):
    """
	Record the best path to a node
	"""
    # TODO: Record the best path to a node, by updating cameFrom, gScore, and fScore
    self.cameFrom[neighbor]= current
    self.gScore[self.start][neighbor] = self.get_tentative_gScore(current,neighbor)
    self.fScore[neighbor] = self.calculate_fscore(current)

# Associates implemented functions with PathPlanner class
PathPlanner.create_closedSet = create_closedSet
PathPlanner.create_openSet = create_openSet
PathPlanner.create_cameFrom = create_cameFrom
PathPlanner.create_gScore = create_gScore
PathPlanner.create_fScore = create_fScore
PathPlanner.set_map = set_map
PathPlanner.set_start = set_start
PathPlanner.set_goal = set_goal
PathPlanner.is_open_empty = is_open_empty
PathPlanner.get_current_node = get_current_node
PathPlanner.get_neighbors = get_neighbors
PathPlanner.get_gScore = get_gScore
PathPlanner.distance = distance
PathPlanner.get_tentative_gScore = get_tentative_gScore
PathPlanner.heuristic_cost_estimate = heuristic_cost_estimate
PathPlanner.calculate_fscore = calculate_fscore
PathPlanner.record_best_path_to = record_best_path_to

planner = PathPlanner(map_40, 5, 34)
path = planner.path
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)

print()
test(PathPlanner)


	
