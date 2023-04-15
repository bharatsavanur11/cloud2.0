# Import routines

import numpy as np
import math
import random

# Defining hyperparameters
m = 5 # number of cities, ranges from 0 ..... m-1
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger

class CabDriver():

    def __init__(self):
        """initialise your state and define your action space and state space"""
        # action_space would be like [(0,0),(0,1),(0,2)....(4,2),(4,3),(4,4)]
        self.action_space = [(p,q) for p in range(m) for q in range(m) if p!=q or p==0]
        
        # state_space would be like [(0,0,0), (0,0,1)....(4,23,5),(4,23,6)]
        self.state_space =  [(i,j,k) for i in range(m) for j in range(t) for k in range(d)]
        
        # intialise state with a random value from self.state_space
        self.state_init = random.choice(self.state_space)

        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input
    # Use this function if you are using architecture-2
    def state_encod_arch2(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""
        initial_state = [0 for i in range(m+t+d)] # m+t+d = 36
        
        # Value in state should be initialised with 1, remaining would be 0. Very much same like One-hot encoding.
        # intialise for m
        encoded_state = initial_state
        encoded_state[state[0]] = 1

        #intialise for t
        encoded_state[m +state[1]] = 1

        #initialise for d
        encoded_state[m+t+state[2]] = 1
        state_encod = encoded_state
        
        return state_encod
        #size = 36


    # Use this function if you are using architecture-1 
    def state_encod_arch1(self, state, action):
        """convert the (state-action) into a vector so that it can be fed to the NN. This method converts a given state-action pair into a vector format. Hint: The vector is of size m + t + d + m + m."""
        (x,t,d) , (p,q)
        return state_encod
        #size = 46


    ## Getting number of requests
    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations
        A=2, B=12, C=4, D=7, E=8"""
        
        location = state[0]
        if location == 0: #location = A
            requests = np.random.poisson(2) # lambda = 2
        elif location == 1: #location = B
            requests = np.random.poisson(12) # lambda = 12
        elif location == 2: #location = C
            requests = np.random.poisson(4) # lambda = 2
        elif location == 3: #location = D
            requests = np.random.poisson(7) # lambda = 2
        elif location == 4: #location = E
            requests = np.random.poisson(8) # lambda = 2
        else:
            requests=0
        
        if requests >15:
            requests = 15
        possible_actions_index = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        actions = [self.action_space[i] for i in possible_actions_index]

        
        actions.append([0,0])
        
        possible_actions_index.append(self.action_space.index((0,0)))

        return possible_actions_index,actions   


    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        ## We need to find the next state and then calculate reward for the next state
        
        next_state, ride_time, transit_time, relax_time = self.next_state_func(state, action, Time_matrix)

        chargable_time = ride_time
        non_chargable_time = relax_time + transit_time
        reward = (R * chargable_time) - (C * (chargable_time + non_chargable_time))
        
        return reward
    
    

    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        #print(state)
        curr_loc = state[0]
        curr_time = state[1]
        curr_day = state[2]
        pickup_loc = action[0]
        drop_loc = action[1]
        
        total_time = 0
        relax_time = 0
        ride_time = 0
        transit_time = 0
        
        #Consider action(0,0)
        #Add 1 hr for action(0,0)
        if (pickup_loc ==0) and (drop_loc==0):
            relax_time = 1
            ride_time = 0
            next_location = curr_loc
        
        #Picking from current location
        elif pickup_loc == curr_loc:
            relax_time = 0
            ride_time = Time_matrix[curr_loc][drop_loc][curr_time][curr_day]
            next_location = drop_loc
        
        #Picking from another location
        else :
            relax_time = 0
            ride_duration_to_pickup_location = Time_matrix[curr_loc][pickup_loc][curr_time][curr_day]
            pickup_time, pickup_day = self.get_tnd_for_next_location(curr_time, curr_day, ride_duration_to_pickup_location)
            ride_time_to_drop_location = Time_matrix[pickup_loc][drop_loc][pickup_time][pickup_day]
            ride_time = ride_time_to_drop_location
            transit_time = ride_duration_to_pickup_location
            next_location = drop_loc
            curr_time = pickup_time
            curr_day = pickup_day
        
        total_time = relax_time + ride_time
        destination_time, destination_day = self.get_tnd_for_next_location(curr_time, curr_day, total_time)
        next_state = [next_location, destination_time, destination_day]
        
        return next_state, ride_time, transit_time, relax_time #Other return values will help in calculating rewards

    def get_tnd_for_next_location(self, time, day, duration):

        if time + int(duration) < 24:     
            pickup_time = time + int(duration)
            pickup_day = day
        else:
            pickup_time = (time + int(duration)) % 24
            days = (time + int(duration)) // 24
            pickup_day = (day + days) % 7
            
        return pickup_time, pickup_day
    

    def reset(self):
        return self.action_space, self.state_space, self.state_init
