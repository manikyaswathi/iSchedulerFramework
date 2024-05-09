import math, json
import pandas as pd
import sys

import random

import pymongo
from pymongo import MongoClient

# This functionalyty will be moved to individual containers
class ModelEstimator:
    def __init__(self, modelType=None, modelPath=None):
        self.model_path = "path to model - google kaggle +"
        self.loadEstimationModel()


    def loadEstimationModel(self):
        # load the appropriate predictor model here
        temp = 0
        

    def predictResourceRequirements(self, modelJSON=None, TrainingMetadata=None, nodeConfigs=[]):
        response = []
        for config in nodeConfigs:
            config["memory"] = random.choice([10, 12, 16, 26, 34, 72, 100, 150]) #GB
            config["walltime"] = random.randrange(200) # mins
            response.append(config)

        return response
    

    def predictFeasibilityQueue(self, queueConfigs=[], resEstimationPerNodeConfig=[], costTable=[]):
        response = []
        for config in queueConfigs:
            config["Feasible"] = random.choice(["Yes", "No"]) #
            if config["Feasible"] == "Yes":
                config["Cost"] = random.randrange(200)*random.choice([1, 30, 1.67])  # RUs
            else:
                config["Cost"] =0
            response.append(config)

        return response


    

class ComputingInfoDatabase:
    def __init__(self, modelPath=None):
        self.cluster = MongoClient("mongodb+srv://harpuser:harpuser@harp.afryura.mongodb.net/?retryWrites=true&w=majority&appName=HARP")
        self.db = self.cluster["CI_Configurations"]
    

    def getNodeConfigs(self):
        # load the appropriate predictor model here
        NodeConfigs = self.db["nodes_config"]
        node_config = []
        for x in NodeConfigs.find():
            node_config.append(x)
        return node_config
    

    def getQueues(self):
        # load the appropriate predictor model here
        QueueConfigs = self.db["queue_config"]
        queue_config = []
        for x in QueueConfigs.find():
            queue_config.append(x)
        return queue_config

    def getWaitTimesPerQueue(self, perqueueWalltime=None):
        return random.randrange(2000) # mins

    
     
def main():
    # me= ModelEstimator()
    # model_summary = sys.argv[1]
    # model_traning = sys.argv[2]

    # ConfigList = getSystemConfig()
    print("I am here")
    dbhook = ComputingInfoDatabase()
    node_configs = dbhook.getNodeConfigs()

    model_predictor = ModelEstimator("RespurceEstimator", "nopathyet")
    




if __name__ == "__main__":
    main()
 
