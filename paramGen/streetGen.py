import random
import os


fileName =  "street/tranStreet.txt"
filePath = os.path.join(os.path.dirname(__file__), fileName)
buildingListSample = ["一品名居","名派雅居","俊杰豪苑","逸华庭","至善名居",
"愉景名苑","盈翠华城","南国翠庭","富丽盈门","时代华亭","艺典名居",
"挹翠家园","康睦佳园","南悦华城","至善美第","放晴苑","五彩名居","宁馨家园"]

with open(filePath, encoding="utf-16") as f:
    lines = f.readlines()
    adressList = lines

def getRandomAdress(prefix="",buildingList=buildingListSample):
    result = {}
    randNum1 = int(random.random() * len(adressList))
    addressSplit = adressList[randNum1].split(" ") 
    
    randNum2 = int(random.random() *  len(buildingList))
    buliding = buildingList[randNum2]

    result[prefix+"addr"] = buliding
    result[prefix+"state"] = addressSplit[0]
    result[prefix+"city"] = addressSplit[1]
    result[prefix+"district"] = addressSplit[2]
    result[prefix+"steet"] = addressSplit[3]

    return result

def formate(result):
    str = ""
    str = str + "{\n"
    for k, v in result.items():
        str = str + "\t\"" + k + "\":\"" + v + "\",\n"  
    str = str + "}\n"
    return str

if __name__ == "__main__":
    print(formate(getRandomAdress("")) )