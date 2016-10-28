#!/usr/bin/phyton

import gym
import numpy
import random
observation = 0
stepChosen = None
oldObservation = None
env = gym.make('FrozenLake-v0')
env.__init__(is_slippery=False)
	
# generate and print the 4x16 matrix
Q = numpy.zeros((env.action_space.n, env.observation_space.n))
print(Q)

def setQs(row, col):
	Q[col, row] = #HIER MUSS DER NEUE Q-WERT HIN

# we need a lot of iteration to get through all possible variations
for t in range(10):
	for m in range(20):
		# epsilon is generated
		# by 20% we just randomly choose the next step (otherwise we would always
		# take the same routes and don't discover the complete array
		# by 80% we choose the next step based on the max Q
		e = random.uniform(0.0, 1.0)
		if e <= 0.2:
			# print(e)
			action = env.action_space.sample()
			oldObservation = observation
			observation, reward, done, info = env.step(action)
			stepChosen = action
			env.step(action)
			env.render()
		#Selects the column depending on the current observation
		#It then selects the position of the max Value in the Array and makes a step in 		#the direction specified by the array index		
		elif e > 0.2: 
			#print(e)
			qValues = Q[:, observation]
			maxQPosition = numpy.argmax(qValues)
			stepChosen = maxQPosition
			oldObservation = observation
			observation, reward, done, info = env.step(maxQPosition)
			env.step(maxQPosition)
			env.render()

		setQs(stepChosen, oldObservation)

		# we are breaking the loop as soon as done is true (equals Hole or Goal)
		# reward indicates whether we reached the Goal or just any Hole
		# else isn't necessary as soon as we implement the algorithmical choice
		# br is set to true to end the outer loop
		if reward == 1.0 and done == True: 
			print("Winner winner")
			br = True
			break
		elif reward == 0.0 and done == True:
			print("Fuck it!")
			br = True
			break
		else:
			br = False
	if br:
		break


