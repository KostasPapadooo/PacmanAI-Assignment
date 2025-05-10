# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getInitialState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getNextStates(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (nextState,
        action, stepCost), where 'nextState' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    """
    from util import Stack
    
    # Χρησιμοποιούμε στοίβα για DFS
    frontier = Stack()
    # Κρατάμε τις καταστάσεις που έχουμε επισκεφθεί
    visited = set()
    # Αποθηκεύουμε την αρχική κατάσταση μαζί με τη λίστα ενεργειών
    frontier.push((problem.getInitialState(), []))
    
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        
        if state in visited:
            continue
            
        visited.add(state)
        
        if problem.isGoalState(state):
            return actions
            
        for nextState, action, cost in problem.getNextStates(state):
            if nextState not in visited:
                frontier.push((nextState, actions + [action]))
    
    return []  # Επιστρέφουμε κενή λίστα αν δεν βρεθεί λύση

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    from util import Queue
    
    # Χρησιμοποιούμε ουρά για BFS
    frontier = Queue()
    # Κρατάμε τις καταστάσεις που έχουμε επισκεφθεί
    visited = set()
    # Αποθηκεύουμε την αρχική κατάσταση μαζί με τη λίστα ενεργειών
    frontier.push((problem.getInitialState(), []))
    visited.add(problem.getInitialState())
    
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        
        if problem.isGoalState(state):
            return actions
            
        for nextState, action, cost in problem.getNextStates(state):
            if nextState not in visited:
                visited.add(nextState)
                frontier.push((nextState, actions + [action]))
    
    return []  # Επιστρέφουμε κενή λίστα αν δεν βρεθεί λύση

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue
    
    # Χρησιμοποιούμε ουρά προτεραιότητας για UCS
    frontier = PriorityQueue()
    # Κρατάμε τις καταστάσεις που έχουμε επισκεφθεί
    visited = set()
    # Αποθηκεύουμε την αρχική κατάσταση, τη λίστα ενεργειών και το κόστος
    frontier.push((problem.getInitialState(), [], 0), 0)
    
    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()
        
        if state in visited:
            continue
            
        visited.add(state)
        
        if problem.isGoalState(state):
            return actions
            
        for nextState, action, stepCost in problem.getNextStates(state):
            if nextState not in visited:
                newCost = cost + stepCost
                frontier.push((nextState, actions + [action], newCost), newCost)
    
    return []  # Επιστρέφουμε κενή λίστα αν δεν βρεθεί λύση

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue
    
    # Χρησιμοποιούμε ουρά προτεραιότητας για A*
    frontier = PriorityQueue()
    # Κρατάμε τις καταστάσεις που έχουμε επισκεφθεί
    visited = set()
    # Αποθηκεύουμε την αρχική κατάσταση, τη λίστα ενεργειών και το κόστος
    startState = problem.getInitialState()
    frontier.push((startState, [], 0), heuristic(startState, problem))
    
    while not frontier.isEmpty():
        state, actions, cost = frontier.pop()
        
        if state in visited:
            continue
            
        visited.add(state)
        
        if problem.isGoalState(state):
            return actions
            
        for nextState, action, stepCost in problem.getNextStates(state):
            if nextState not in visited:
                newCost = cost + stepCost
                priority = newCost + heuristic(nextState, problem)
                frontier.push((nextState, actions + [action], newCost), priority)
    
    return []  # Επιστρέφουμε κενή λίστα αν δεν βρεθεί λύση


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
