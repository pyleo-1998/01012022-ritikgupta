import ijson
import pandas as pd

'''
        The give json formatted data in the Problem Statement is not suitable to use in the 
        pd.read_json("test_data.json",orient="records",lines=True,chunksize=1)
        so dealing with the same large json formatted file with simple pd.read_json() may raise an MemoryError Exception 
        in order to deal with large json file while considring the less memory i make my own custom Chunksize function and store the
        data in the Hierarchical Data Format (HDF) for the big data analysis using Pandas Python module . 
        
        There is another solution where we can save the pandas dataframe to (.csv) format and latter read with the Vaex python module.
        it internaly convert data from  .csv data to .hdf5 data for large data analysis and visualisation .
'''

def BMI(height,weight):

    cal_bmi=round(weight/(height/100)**2,1)
    
    if cal_bmi<=18.4:       
            return ["Underweight","Malnutrition risk",cal_bmi]
    
    elif 18.4<=cal_bmi<=24.9:
            return ["Normal weight","Low risk",cal_bmi]

    elif 25<=cal_bmi<=29.9:
            return ["Overweight","Enhanced risk",cal_bmi]

    elif 30<=cal_bmi<=34.9:
            return ["Moderately obeset","Medium risk",cal_bmi]

    elif 35<=cal_bmi<=39.9:
            return ["Severely obese","High riskk",cal_bmi]

    elif 40<=cal_bmi:
            return ["Very severely obese","Very high risk",cal_bmi]

with open('test_data.json', 'rb') as f:
        
        data={"bmi":[],"bmi_category":[],"health_risk":[],"gender":[]}
        
        #defined the chunksize
        chunksize=8
        for index,id in enumerate(ijson.items(f, 'item'),1):
                
                raw_data=BMI(id['HeightCm'],id["WeightKg"])
                data["bmi_category"].append(raw_data[0])
                data["health_risk"].append(raw_data[1])
                data["bmi"].append(raw_data[2])
                data["gender"].append(id['Gender'])
                
                if index%chunksize==0:
                        pd.DataFrame(data).to_hdf('data.h5', key='df', mode='a',append=True,index=False)
                        data={"bmi":[],"bmi_category":[],"health_risk":[],"gender":[]}
        
        # if the data left to store                
        if data["bmi"]!=[]: 
                pd.DataFrame(data).to_hdf('data.h5', key='df', mode='a',append=True,index=True)
                data={"bmi":[],"bmi_category":[],"health_risk":[],"gender":[]}