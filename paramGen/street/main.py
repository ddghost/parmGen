import cityMap



def preOrderSearch(dist, nowPre, streetArr):
    nowPre = nowPre + dist["name"] + " "
    if len( dist["child"]) > 0:
        for child in dist["child"]:
            preOrderSearch(child, nowPre, streetArr)   
    else:
        streetArr.append(nowPre)
        if nowPre.count(" ") == 4:
            print(nowPre)
    

if __name__ == "__main__":
    provinces = cityMap.cityMap["cityList"]
    for province in provinces:
        preOrderSearch(province,"",[])