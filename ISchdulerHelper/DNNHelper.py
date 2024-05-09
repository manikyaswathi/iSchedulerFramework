import math, json
from tapipy.tapis import Tapis
from keras.models import Sequential, model_from_json
import pandas as pd
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive 
import json,urllib.request

from GetResourceEstimator.Estimators import *

class DNNHelper:
    def __init__(self, signIn=False, credsFile=None):
        self.loginFile = credsFile
        self.TAPISclient = None
        if signIn:
            data = json.load(open('TAPISCreds.json'))
            base_url=data['base_url']
            username=data['username']
            password=data['password']

           
            self.effective_user_id=data['effective_user_id']
            self.job_working_dir=data['job_working_dir']
            self.system_id_hpc=data['system_id_hpc']
            self.target_system_cluster=data['target_system_cluster']
            self.target_system_domain=data['target_system_domain']
            self.queue_name=data['queue_name']

            print("geteting token")
            self.TAPISclient = Tapis(base_url= base_url, username=username, password=password)
            self.TAPISclient.get_tokens()


            # Execute Contaniers - estimators
            self.exec_system_hpc = None

            self.dbhook = ComputingInfoDatabase()
            self.model_predictor = ModelEstimator("RespurceEstimator", "nopathyet")
            self.model_predictorWaitTimes = ModelEstimator("Waitime predictor", "nopathyet")

            #CHAGE TO ADD IF DOENST EXISTS OR MODIFY LOOP
            # self.setupModelEstimatorSystem()

            # print("client.access_token", client.access_token)

            # self.gauth = GoogleAuth()
            # self.drive = GoogleDrive(self.gauth)
            # self.gauth.LocalWebserverAuth()

    def setupModelEstimatorSystem(self):
        # Fixed System we setup during development phase
        self.exec_system_hpc, maxmemMB, maxcores = self.get_system_config_json(self.target_system_cluster, self.system_id_hpc, self.effective_user_id, self.job_working_dir, self.queue_name) 
        self.TAPISclient.systems.createSystem(**self.exec_system_hpc)


    def get_system_config_json(self, system, system_id_hpc=None, effective_user_id=None, job_working_dir=None, queue_name=None):
        json_file = ""
        if system == "pitzer_osc":
            json_file = "pitzer_osc.json"
            maxMemoryMB = 160000
            maxcores = 40
        else:
            json_file = "stampede2_tacc.json"
            maxMemoryMB = 1
            maxcores = 1
        json_url = "https://raw.githubusercontent.com/manikyaswathi/harp/main/JSON_Templates/"+json_file
        data = urllib.request.urlopen(json_url).read()
        systemC = json.loads(data)

        systemC['id']=system_id_hpc
        systemC['effectiveUserId']=effective_user_id
        systemC['jobWorkingDir']=job_working_dir
        systemC['batchDefaultLogicalQueue']=queue_name

        for attribute, value in systemC.items():
            if value == 'True':
                systemC[attribute] = True
            elif value == 'False':
                systemC[attribute] = False

        return (systemC, maxMemoryMB, maxcores)
        

    def getModelSummaryJSON(self, model):
       return model.to_json()
    
    #private
    def getSystems(self):
        print("\t\t\t****************************************************")
        print("\t\t\t\t\tList all systems")
        print("\t\t\t****************************************************")
        my_systems = self.TAPISclient.systems.getSystems()
        # my_systems
        list_sys = []
        for idx, sys in enumerate(my_systems):
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            print(self.TAPISclient.systems.getSystem(systemId=sys.id))
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            list_sys.append([sys.id, sys.host, sys.owner, sys.effectiveUserId, sys.systemType])
        df_sys = pd.DataFrame(list_sys, columns=["System ID", "Host", "Owner", "Effective User ID", "System Type"])
        return df_sys
    

    def getResouceEstimation(self, modelJSON=None, TraningMetsData=None):
        # Push files to Shared Drive - a challenge -> moving to TAPIS File Upload
        executeOptions = []
        # way 1: Submit a TAPIS JOB to execute the DNNEstimator Contaner Inference model

        # self.getSystems()

        #Way 2 for testing - running dummy models on localbox to draft templates
        
        node_configs = self.dbhook.getNodeConfigs()
        executeOptions = self.model_predictor.predictResourceRequirements(nodeConfigs=node_configs)

        return executeOptions
    
    def getFeasibleQueues(self, modelJSON=None, TraningMetsData=None):
        executeOptions = []

        # WAY 2
        queue_configs = self.dbhook.getQueues()
        # [FIX] Missing Link between queue and node 
        node_config_exe_estimates = self.getResouceEstimation(modelJSON=modelJSON, TraningMetsData=TraningMetsData)
        executeOptions = self.model_predictor.predictFeasibilityQueue(queueConfigs=queue_configs, resEstimationPerNodeConfig=node_config_exe_estimates)
        
        return executeOptions


    # the systems the user has access to!
    def getFeasibleSystems(self, queue_vs_timecost=None):
        executeOptions = []

        # WAY 2
        availSystems = self.getSystems()
        
        for config in availSystems:
            config["QueueName"] = "ToBeFilled" 
            # fetched From Modal one - App 1
            config["memory"] = random.choice([10, 12, 16, 26, 34, 72, 100, 150]) #GB
            config["walltime"] = random.randrange(200) # mins
             # fetched From Modal two - App 2
            config["waititmes"] =  self.model_predictorWaitTimes.getWaitTimesPerQueue(config)
            executeOptions.append(config)
        
        
        return executeOptions
       
    # OnHold
    def writeFilesToCLoud(self, name, content):

        file1 = self.drive.CreateFile({'title': name})  # Create GoogleDriveFile instance with title 'Hello.txt'.
        file1.SetContentString(content) # Set content of the file from given string.
        file1.Upload()
        

# def main():
#     print("I am here")
#     dnnhelper = DNNHelper(signIn = True, credsFile="TAPISCreds.json")
#     dnnhelper.getFeasibleQueues()
#     # on Hold -> move to TAPIS file upload?
#     # dnnhelper.writeFilesToCLoud("test101.json", "{'name':'IAMAJSON}")
#     # dnnhelper.getSystems()





# if __name__ == "__main__":
#     main()
 


