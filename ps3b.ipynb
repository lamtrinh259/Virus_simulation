# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab
# To use the pre-compiled graph module I must comment out all my codes below and\
# leave the simulationWithDrug function only
# from ps3b_precompiled_38 import *

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        # If probability of getting cleared is larger than a random number [0,1)
        if self.getClearProb() > random.random():
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        reproduceProbability = self.maxBirthProb * (1 - popDensity)
        # if reproduction chance > random number in [0,1)
        if reproduceProbability > random.random(): 
            # Make a new virus that has the same properties as its parent
            newVirus = SimpleVirus(self.maxBirthProb, self.clearProb)
            return newVirus
        # This will catch the exception where the virus doesn't reproduce
        # This exception handling already passed the test! No further modification!
        # However, this may halt the program if run for only reproduce()
        else:
            raise NoChildException()
        # except NoChildException:
            # pass 
        # try-except-else-finally The "else" clause will run if there's
        # no exception, no need in this case
        # else: #Raising the exception
        #     raise NoChildException



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)   

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        listOfViruses = self.viruses.copy()
        for v in listOfViruses:
            if v.doesClear() == True:
                self.viruses.remove(v)
        popDensity = self.getTotalPop() / self.getMaxPop()
        #Apparently, this is the correct way to catch an exception, the try-except
        #clause needs to be inside the for loop, previously I put my loop inside
        #the try-except clause, which didn't work because no exception was raised
        for i in range(len(self.viruses)):
            try:
                self.viruses.append(self.viruses[i].reproduce(popDensity))
            except NoChildException:
                pass
        return self.getTotalPop()    

# For testing
# v1 = SimpleVirus(0.97, 0.69)
# # for i in range(10):
# #     v1.reproduce(0.1)
# viruses = [
# SimpleVirus(0.99, 0.91),
# SimpleVirus(0.50, 0.62),
# SimpleVirus(0.76, 0.39)
# ]
# P1 = Patient(viruses, 6)
# Create a Patient with virus that is never cleared and always reproduces
# virus = SimpleVirus(1.0, 0.0)
# patient = Patient([virus], 100)
# for i in range(90):
#     patient.update()
# print(len(patient.getViruses()))
# for i in range(10):
#     virus.reproduce(0.5)

# Create a Patient with virus that is always cleared and always reproduces
# virus = SimpleVirus(1.0, 1.0)
# patient = Patient([virus], 100)
# for i in range(100):
#     patient.update()

#
# PROBLEM 2
#

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    viruses = []
    for i in range(numViruses): 
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    # How to create a list of lists
    virusPops = [[] for i in range(numTrials)]
    averageVirusPops = []
    for i in range(numTrials):
        sickP = Patient(viruses,maxPop)
        for j in range(300):
            sickP.update()
            virusPops[i].append(float(sickP.getTotalPop()))
    for i in range(300):
        #Reset after each time step
        tempSum = 0
        for j in range(numTrials):
        #Sum up the total of all trials at same time step i
            tempSum += virusPops[j][i]
        averageVirusPops.append(tempSum/numTrials)
    # This line below is only necessary for the grader
    plotData = list(averageVirusPops)
    # figure = plt.figure() #plot an empty figure with no axes
    # figure, ax = plt.subplots() #plot a figure with a single axes
    # x-values come before y-values
    # plt.plot(x_range, averageVirusPops)
    # plt.xlabel("Time steps")
    # plt.ylabel("Average Virus Population")
    # plt.legend(loc = "best")
    # plt.title("SimpleVirus simulation")
    # plt.show()
    
    # For use in the grader only
    pylab.plot(plotData, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")
    pylab.show()
    
    
# simulationWithoutDrug(100, 1000, 0.1, 0.05, 10)
# simulationWithoutDrug(1, 10, 1, 0, 1)
# simulationWithoutDrug(100, 200, 0.2, 0.8, 1)
# simulationWithoutDrug(1, 90, 0.8, 0.1, 1)

#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        for drugName in self.resistances: 
            if drug == drugName:
                return self.resistances[drugName]


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        numberOfActiveDrugs = len(activeDrugs)
        count = 0
        reproduceProbability = self.maxBirthProb * (1 - popDensity)
        for drugName in activeDrugs:
            # Increase count to see how many drugs the virus is resistant to
            if self.isResistantTo(drugName) == True: 
                count += 1
            else:
                pass
        #If the virus is resistant to all drugs, this code is also correct
        if count == numberOfActiveDrugs:
            if reproduceProbability > random.random():
                # Defining resistance traits of new offspring
                newResistances = self.resistances.copy()
                for drugName in newResistances:
                    # Virus is already resistant to drugName
                    if newResistances[drugName] == True:
                        # 1 - mutProb of inheriting resistance
                        if (1 - self.mutProb) > random.random():
                            newResistances[drugName] = True
                        # mutProb of not inheriting resistance
                        #else: alternative is also correct
                        elif self.mutProb > random.random():  
                            newResistances[drugName] = False
                    # in case virus is not resistant to drugName
                    elif newResistances[drugName] == False:
                        # mutProb of getting resistance
                        if self.mutProb > random.random():
                            newResistances[drugName] = True
                        # 1 - mutProb of not getting resistance
                        elif (1 - self.mutProb) > random.random():
                            newResistances[drugName] = False
                offSpring = ResistantVirus(self.maxBirthProb, self.clearProb,\
                                            newResistances, self.mutProb)
                return offSpring
            else:
                raise NoChildException
        else: # virus is not resistant to ALL drugs
            raise NoChildException

# For testing
# virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, \
#                                   'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
# virus.reproduce(0,[])
        # It is not a good idea since each virus particle should have its
        # own set of resistances, and it should not change
        # if count == numberOfActiveDrugs:
        #     if reproduceProbability > random.random():
        #         # Defining resistance traits of new offspring
        #         newResistances = self.resistances.copy()
        #         for drugName in self.resistances:
        #             # Virus is already resistant to drugName
        #             if self.resistances[drugName] == True:
        #                 # 1 - mutProb of inheriting resistance
        #                 if (1 - self.mutProb) > random.random():
        #                     self.resistances[drugName] = True
        #                 # mutProb of not inheriting resistance
        #                 #else: alternative is also correct
        #                 elif self.mutProb > random.random():  
        #                     self.resistances[drugName] = False
        #             # in case virus is not resistant to drugName
        #             elif newResistances[drugName] == False:
        #                 # mutProb of getting resistance
        #                 if self.mutProb > random.random():
        #                     self.resistances[drugName] = True
        #                 # 1 - mutProb of not getting resistance
        #                 elif (1 - self.mutProb) > random.random():
        #                     self.resistances[drugName] = False
        #         offSpring = ResistantVirus(self.maxBirthProb, self.clearProb,\
        #                                    self.resistances, self.mutProb)
# virus = ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)
# for i in range(10):
#     virus.reproduce(0,[])

    
class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.prescription = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug in self.prescription:
            pass
        else:
            self.prescription.append(newDrug)
        
        
        #Old code, but couldn't pass test 6, apparently, existing viruses will
        #not be affected by new prescription drug, this is incorrect
        # for virus in self.viruses: 
        #     for drugName in virus.resistances:
        #         if drugName == newDrug: 
        #             virus.resistances[newDrug] = False


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.prescription


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        countVirus = 0
        # Still not sure how to use the all(list of booleans) or any(list of booleans)        
        #Old method, which is correct
        countDrugResistTo = 0
        numberOfDrug = len(drugResist)
        for virus in self.viruses: 
            countDrugResistTo = 0 #Reset this count after each virus
            #drugResist must be in the form of a list of strings, or else this won't work
            for drug in drugResist: 
                if virus.isResistantTo(drug) == True:
                    countDrugResistTo += 1
            #If the current virus is resistant to all drugs in drugResist
            if countDrugResistTo == numberOfDrug:
                countVirus += 1
        return countVirus


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        #Make a copy so I don't mutate the list while iterating over it
        activeDrugs = self.prescription
        listOfViruses = self.viruses.copy()
        for v in listOfViruses:
            if v.doesClear() == True:
                self.viruses.remove(v)
        popDensity = self.getTotalPop() / self.getMaxPop()
        # I need a new copy of self.viruses after it was changed after virus getting cleared
        virusInPatients = self.viruses.copy()
        #Apparently, I should not mutate the list while running over it
        #Previous code was for virus in self.viruses <-- This is wrong, infinite loop
        for virus in virusInPatients:
            try:
                self.viruses.append(virus.reproduce(popDensity, activeDrugs))
            except NoChildException:
                pass


#For testing
# virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
# virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
# patient = TreatedPatient([virus1, virus2], 1000000)
# patient.getResistPop(["drug1"])
# patient.addPrescription("drug1")
# for i in range(5):
#     patient.update()


#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                        mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                  (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
              (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    #For redo: learn how to use numpy array
    mutantViruses = []
    for i in range(numViruses):
        mutantViruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    for i in range(150):
        sickP = TreatedPatient(mutantViruses, maxPop)
    totalVirusPops = [[] for i in range(numTrials)]
    resistantVirusPops = [[] for i in range(numTrials)]
    averageVirusPops = []
    averageResistantVirusPops = []
    for i in range(numTrials):
        sickP = TreatedPatient(mutantViruses, maxPop)
        for j in range(150):
            sickP.update()
            totalVirusPops[i].append(float(sickP.getTotalPop()))
            resistantVirusPops[i].append(float(sickP.getResistPop(["guttagonol"])))
        # Add the prescription to the patient
        sickP.addPrescription("guttagonol")
        # Run again for 150 timesteps
        for h in range(150):
            sickP.update()
            totalVirusPops[i].append(float(sickP.getTotalPop()))
            resistantVirusPops[i].append(float(sickP.getResistPop(["guttagonol"])))
    for i in range(300):
        #Reset after each time step
        tempSum = 0
        tempResistantVirus = 0
        for j in range(numTrials):
        #Sum up the total of all trials at same time step i
            tempSum += totalVirusPops[j][i]
            tempResistantVirus += resistantVirusPops[j][i]
        averageVirusPops.append(tempSum/numTrials)
        averageResistantVirusPops.append(tempResistantVirus/numTrials)
    
    pylab.plot(averageVirusPops, label = "Total Virus")
    pylab.plot(averageResistantVirusPops, label = "guttagonol-resistant Virus")
    pylab.title("Resistant Virus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    # This optional line below adds a divider to make the graph more clear
    # pylab.axvline(150, color='r', label='Guttagonol administered')
    pylab.legend(loc = "best")
    pylab.show() 

#For testing        
# simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)
simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
