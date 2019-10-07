import numpy as np
import ast
from copy import deepcopy
from copy import copy
from sys import argv
script, Nodes, NodesInfo, NodesPath = argv

""" ******************* 8 Puzzle Game ********************* """


#Defining nodes and initialising: --------------------------------------------------------------------------------------------
class Node():

	def __init__(self,state,parent,move,position):

		self.state=initial_state #present state
		self.parent=parent #parent node or the previous node position
		self.move=move #moving the zero/blank tile
		self.position=position 

		#child node
		#self.to_move_up=None
		#self.to_move_down=None
		#self.to_move_right=None
		#self.to_move_left=None
		
#root_node=Node(initial_state,None,None,0)
#root_node=Node()	

	# For number moving up and zero/blank tile moving down : ---------------------------------------------------------------
	def to_move_up(self):
		blank_tile=[x[0] for x in np.where(self.state==0)]
		if blank_tile[0]==2:
			return False
		else:
			new_state=self.state.copy()
			down_value=self.state[blank_tile[0]+1,blank_tile[1]]
			new_state[blank_tile[0],blank_tile[1]]=down_value
			new_state[blank_tile[0]+1,blank_tile[1]]=0
			return new_state,down_value

	# For number moving down and blank tile/zero moving up : ---------------------------------------------------------------
	def to_move_down(self):
		blank_tile=[x[0] for x in np.where(self.state==0)]
		if blank_tile[0]==0:
			return False
		else:
			new_state=self.state.copy()
			up_value=self.state[blank_tile[0]-1,blank_tile[1]]
			new_state[blank_tile[0],blank_tile[1]]=up_value
			new_state[blank_tile[0]-1,blank_tile[1]]=0
			return new_state,up_value

	# For number moving right and blank tile/zero moving left : ------------------------------------------------------------
	def to_move_right(self):
		blank_tile=[x[0] for x in np.where(self.state==0)]
		if blank_tile[1]==0:
			return False
		else:
			new_state=self.state.copy()
			left_value=self.state[blank_tile[0],blank_tile[1]-1]
			new_state[blank_tile[0],blank_tile[1]]=left_value
			new_state[blank_tile[0],blank_tile[1]-1]=0
			return new_state,left_value

	# For number moving left and blank tile/zero moving right : -------------------------------------------------------------
	def to_move_left(self):
		blank_tile=[x[0] for x in np.where(self.state==0)]
		if blank_tile[1]==2:
			return False
		else:
			new_state=self.state.copy()
			right_value=self.state[blank_tile[0],blank_tile[1]+1]
			new_state[blank_tile[0],blank_tile[1]]=right_value
			new_state[blank_tile[0],blank_tile[1]+1]=0
			return new_state,right_value

	# Breadth First Search : ------------------------------------------------------------------------------------------------
	
	def breadth_first_search(self,goal_state):
		queue=[self]
		queue_numnodes_popped=0
		queue_maxlength=1
		position_queue=[0]
		visited=set([])
	
		while queue:

		# Giving max length of queue : -----------------------------------------------------------------------------------
			if len(queue)>queue_maxlength:
				queue_maxlength=len(queue)
			
			current_node=queue.pop(0)
			queue_numnodes_popped+=1

			current_position=position_queue.pop(0)
			visited.add(tuple(current_node.state.reshape(3,3)[0]))

	

			# When the goal state is found,tracing back to the root node and printing path : ---------------------------
	
			if np.array_equal(current_node.state,goal_state):
	
				current_node.print_path()

				print(str(queue_numnodes_popped),'nodes popped off the queue.')
				print(str(queue_maxlength),'nodes in the queue at its max.')
				return (str(queue_numnodes_popped),str(queue_maxlength))
				return True

			else:
				# To check if moving upper tile down is a valid move :-----------------------
				if current_node.to_move_down():
					new_state,up_value=current_node.to_move_down()
	
					# Checking if the resulting node is visited : -----------------------
					if tuple(new_state.reshape(3,3)[0]) not in visited:
						# Creating a new child node : -------------------------------
						current_node.to_move_down=Node(new_state,current_node,'down',current_position+1)
						queue.append(current_node.to_move_down)
						position_queue.append(current_position+1)
				# To check if moving left tile to right is a valid move : -------------------
				if current_node.to_move_right():
					new_state,left_value=current_node.to_move_right()
				
					# Checking if the resulting node is visited : -----------------------
					if tuple(new_state.reshape(3,3)[0]) not in visited:
						# Creating a new child node : ------------------------------- 
						current_node.to_move_right=Node(new_state,current_node,'right',current_position+1)
						queue.append(current_node.to_move_right)
						position_queue.append(current_position+1)
	
				# To check if moving lower tile up is a valid move : ------------------------
				if current_node.to_move_up():
					new_state,down_value=current_node.to_move_up()
		
					# Checking if the resulting node is visited : -----------------------
					if tuple(new_state.reshape(3,3)[0]) not in visited:
						# Creating a new child node : -------------------------------
						current_node.to_move_up=Node(new_state,current_node,'up',current_position+1)
						queue.append(current_node.to_move_up)
						position_queue.append(current_position+1)
					

				# To check if moving right tile to left is a valid move : -------------------
				if current_node.to_move_left():
					new_state,right_value=current_node.to_move_left()

					# Checking if the resulting node is visited : -----------------------
					if tuple(new_state.reshape(3,3)[0]) not in visited:
						# Creating a new child node : -------------------------------
						current_node.to_move_left=Node(new_state,current_node,'left',current_position+1)
						queue.append(current_node.to_move_left)
						position_queue.append(current_position+1)
		#return(print(visited),print(position_queue))

	# Tracing back to the path and initial state after the goal is found : ----------------------------------------------------
	def print_path(self):
		state_trace=[self.state]
		move_trace=[self.move]
		position_trace=[self.position]
		
		# Defining the node info to trace back : --------------------------------------------------------------------------
		while self.parent:
			self=self.parent
			state_trace.append(self.state)
			move_trace.append(self.move)
			position_trace.append(self.position)
			print(state_trace.append(self.state),move_trace.append(self.move))
			return(state_trace.append(self.state))

		# The defined path as the output : --------------------------------------------------------------------------------
		move_counter=0
		while state_trace:
			print('move',move_counter)
			print (state_trace.pop())
				
			move_counter+=1
			return state_trace
		return(print(state_trace),print(move_trace),print(position_trace))

# Text files for the nodes, nodespath and nodesinfo:-------------------------------------------------------------------------------
out=open(Nodes,'w')
for i in Nodes:
	out.write(str(i)+'\n')
out.close()

out=open(NodesInfo,'w')
for i in NodesInfo:
	out.write(str(i)+'\n')
out.close()

out=open(NodesPath,'w')
for i in NodesPath:
	out.write(str(i)+'\n')
out.close()

# Input and Output given : --------------------------------------------------------------------------------------------------------

#To give the input in matrix form:
unsol_string=input("Enter the 8 Game Puzzle to be solved \n")
#[2,3,6],[1,7,4],[0,5,8]

unsol_list=ast.literal_eval(unsol_string)

initial_state=np.array(unsol_list).reshape(3,3)  
print("The unsolved puzzle is:\n",initial_state)
	

#Given input(constant)
#initial_state=np.array([1,0,2,4,5,3,7,6,8]).reshape(3,3)  
#print("The unsolved puzzle is:\n",initial_state)

 
goal_state=np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)
#print("The final solved puzzle is:\n",goal_state)

#Printing Outputs : ---------------------------------------------------------------------------------------------------------------

#root_node=Node(state=initial_state,parent=None,move=None,position=0)	
root_node = Node(initial_state,0,1,0)

#root_node=Node()
print(root_node.to_move_right())
print(root_node.to_move_up())
print(root_node.to_move_down())
print(root_node.to_move_left())
print(root_node.print_path())
print(root_node.breadth_first_search(goal_state))




#######################################################################################################################################

"""  -------------------------------------------------------------END---------------------------------------------------------------"""
#######################################################################################################################################

			
	

	



		






		



