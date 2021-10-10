from models.component.baseComponent import BaseComponent
from threading import Thread
import logging
import imp
import inspect
import time 
import math

class Pipeline(BaseComponent):
    def __init__(self,componentIn,length,diameter,flowIn=0,flowOut=0):
        super().__init__()
        self._componentIn=componentIn
        self._length=length
        self._diameter=diameter
        self._flowIn=flowIn
        self._flowOut=flowOut
        self._flow=0
        self._chlorineFlowComponentIn=0
        self._chlorineFlowClTank=0
        self._chlorineConcentrationAtStart=0
        self._chlorineAfterDecay=0
        self._chlorineConcentrationHistory=[0]*50
        self._flowInHistory=[0]*50

        self._tempCl=0

        self._refreshingTime=5

        Thread(target=self.updateChlorineConcentration).start()
    
    def addComponentOut(self,componentOut):
        self._componentOut=componentOut
        self.attach(componentOut)
        self.updateFlow()
    
    def updateFlowOut(self,flowOut):
        print("Flowout updated to "+str(flowOut))
        self._flowOut=flowOut
        #print ("Pipeline flowout changed, flowout:"+str(self._flowOut))
        self.updateFlow()
    
    def updateFlowIn(self,flowIn, chlorineIn, id):
        self._flowIn=flowIn
        self._tempCl=chlorineIn
        #print ("Pipeline flowin changed, flowin:"+str(flowIn))
        self.updateFlow()

    def updateChlorineFromTankIn(self, chlorineFromTank):
        if(self._flow>0):
            self._chlorineFlowClTank = chlorineFromTank
        else:
            self._chlorineFlowClTank =0

    def updateFlow(self):
        self._flow=min(self._flowIn,self._flowOut)
        # print ("pipeline flow changed, flow:" + str(self._flow))
        if(self._flow>0):
            self._chlorineFlowComponentIn=self._tempCl

        clEnd=self.getChlorineConcentration(self._length)
        self.updateSensors()
        self._update_observers(self._flow, clEnd, id(self))

    def getFlow(self):
        return self._flow

    def decayChlorine(self):
        self._chlorineAfterDecay=self._chlorineConcentrationAtStart*(0.35*math.exp(-2*self._refreshingTime)+0.65*math.exp(-0.015*self._refreshingTime))
        
    def updateChlorineConcentration(self):
        while(True):
            
            if(self._flow>0):
                self._chlorineConcentrationAtStart=(self._chlorineFlowClTank / self._flow) + self._chlorineFlowComponentIn
            
            elif(self._flow==0):
                self._chlorineConcentrationAtStart=self._chlorineFlowClTank + self._chlorineAfterDecay
            
            #if(len(self._chlorineConcentrationHistory)>50):
                #self._chlorineConcentrationHistory.pop(0)
                #logging.debug("Update cl concentration")
                #print (self._chlorineConcentrationHistory)

            self._chlorineConcentrationHistory.insert(0,self._chlorineConcentrationAtStart)
            #print (self._chlorineConcentrationHistory)

            #print("Pipeline:"+str(inspect.stack()[0].frame))
            clEnd=self.getChlorineConcentration(self._length)
            #print(self.observers)
            self.updateSensors()
            self._update_observers(self._flow, clEnd, id(self))

            
            # print("Test "+str(self._flow)+" "+str(self._chlorineConcentrationAtStart)+" "+str(self._chlorineFlowClTank))

            #print ("Chlorine concentration in pipeline: " + str(self._chlorineConcentrationAtStart))
            time.sleep(self._refreshingTime)
            
    def getChlorineConcentration(self, x):
        # x is the disantce from the start of the pipeline, where we want to measure the Cl concentration
        if(x==0):
            return self._chlorineConcentrationAtStart
        
        else:

            if(self._flow>0):
                #print ("Flow :" + str(self._flow))
                #print (x)
                #print (math.pi*pow(self._diameter,2))
                timeToFlow=(self._flow*4)/(math.pi*pow(self._diameter,2))
                timeToFlow= x/timeToFlow

                #print("Time to flow:"+str(timeToFlow))
                chlorineHistoryIndex=(int(timeToFlow/self._refreshingTime)+1)%50
                #print ("Cl history index:"+str(chlorineHistoryIndex)+"\n")

                chlorineAtX=self._chlorineConcentrationHistory[chlorineHistoryIndex]*(0.35*math.exp(-2*timeToFlow)+0.65*math.exp(-0.015*timeToFlow))
                #chlorineAtX=self._chlorineConcentrationAtStart*(0.35*math.exp(-2*timeToFlow)+0.65*math.exp(-0.015*timeToFlow))
                return chlorineAtX

            elif (self._flow==0):
                #should find a equation to model with the dispersion
                return 0

    def getHydroPressure(self):
        return 350000

    def __call__(self):
        self.updateFlowIn(self._componentIn.getFlow())

