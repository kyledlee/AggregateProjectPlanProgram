# Kyle Lee
# Progam for TIM105 Midterm
# Problem 4






def bitfield(n, numProjects):
	binaryValues = [int(digit) for digit in bin(n)[2:]] 
	while(len(binaryValues) < numProjects):
		binaryValues.insert(0, 0)
	return binaryValues

class project:
	"""A class for an individual project, including the Cost (cost) and Expected Monetary Value (emv)"""	
	def __init__(self):
		name = ""
		cost = 0
		emv = 0


class projectGroup:
	"""A class for a group of projects"""

	def __init__(self, numProjects, potentialProjects, bitNumber): #bitNumber is the number of the simulation which decides which projects are being run
		self.alphaValues = bitfield(bitNumber, numProjects) 
		self.Ct = 0
		self.Vt = 0

		for i in range(0,numProjects):
			self.Ct += (potentialProjects[i].cost)*(self.alphaValues[i]) 

		for i in range(0,numProjects):
			self.Vt += (potentialProjects[i].emv)*(self.alphaValues[i])

#MAIN

#Input variables
print("Welcome to the Aggregate Project Planning Program.")
Budget = int(input("What is your budget? (in dollars) "))
numProjects = int(input("How many potential projects do you have? "))

#potentialProjects[] holds all of the project objects
potentialProjects = [0 for i in range(numProjects)]

#input each individual projects variables
for i in range(0, numProjects):
	potentialProjects[i] = project()
	potentialProjects[i].name = str(input("What is the name of project #"+str(i+1)+"? "))
	potentialProjects[i].cost = int(input("What is the cost of "+potentialProjects[i].name+"? (in dollars) "))
	potentialProjects[i].emv = int(input("What is the expected monetary value of "+potentialProjects[i].name+"? (in dollars) "))
	
#projectGroups[] holds all 2^n group possibilities objects
numProjectGroups = 2**numProjects
projectGroups = [0 for i in range(numProjectGroups)]

#assign values for each project group
for i in range(0, numProjectGroups):
	projectGroups[i] = projectGroup(numProjects, potentialProjects, i)

#compare Ct and Vt for each project to find the best one.
bestCt = 0
bestVt = 0
bestProjectIndex = 0
for i in range(0, numProjectGroups):
	if(projectGroups[i].Ct <= Budget and projectGroups[i].Vt > bestVt):
		bestCt = projectGroups[i].Ct
		bestVt = projectGroups[i].Vt
		bestProjectIndex = i


print("The best combination of projects is: ")

for i in range(0,numProjects):
	if(projectGroups[bestProjectIndex].alphaValues[i] == 1):
		print(potentialProjects[i].name)



print("Total EMV = $"+str(bestVt), " dollars")
print("Total Cost = $"+ str(bestCt), " dollars")
print("Budget remaining = $"+ str(Budget-bestCt), " dollars")
