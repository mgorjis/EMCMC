def CreateKB(NumberOfEntities):
    import string, random
    import numpy as np
# create a database on participants with random propbabilities between their events

    ListOfEntities=[]
    for i in range(0,NumberOfEntities):
        ListOfEntities.append('t'+str(i))

    ListOfEvents=[]
    for i in range(0,len(ListOfEntities)):
        for j in range(0,len(ListOfEntities)):
            if i!=j:
                ListOfEvents.append([  ListOfEntities[i] , ListOfEntities[j] , round( random.random(),2) ])  
    PrPos=np.zeros([NumberOfEntities,NumberOfEntities])

    for i in range(0,len(ListOfEvents)):
        index1=ListOfEntities.index(ListOfEvents[i][0])
        index2=ListOfEntities.index(ListOfEvents[i][1])
        PrPos[index1,index2]=ListOfEvents[i][2]
    return ListOfEntities,ListOfEvents,PrPos

    ##########################################################

def Diag_zero(X,S):
    for j in range(0,S):
        X[j*(S+1)]=0
    return X


    ##########################################################

def Calc_likelihood(Adj,PrPos,S): #_reshaped
    import numpy as np
    #S=int(np.sqrt(np.shape(Adj)))#[0]
    Adj = Diag_zero(Adj,S)
    Adj_reshaped=np.reshape(Adj,[S,S])
    
    
    P=1
    for i in range(0,S):
        for j in range(0,S):  
            if (i!=j) :
                P=P * (PrPos[i,j]**Adj_reshaped[i,j]) * ( (1-PrPos[i,j])**(1-Adj_reshaped[i,j]))
    return P


    #########################################################


def Mutation(Adj,S):
    import random
    bit=random.randint(0,S**2-1)
    Adj[bit]=abs(1-Adj[bit])
    
    return Adj



def sketch(entities,matrix):
    S=len(entities)
    from graphviz import Digraph
    dot = Digraph()
    for i in range(0,len(entities)):
        dot.node(entities[i])
    for i in range(0,S):
        for j in range(0,S):
            if (matrix[i,j])==1:
                dot.edge(entities[i],entities[j])
    return dot