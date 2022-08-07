import paramGen.streetGen  as streetGen

buyerProvinceList = ["北京","吉林","辽宁","山东","河北","河南","山西","黑龙江","甘肃"]
sellerProvinceList =["广东","广西","福建","湖南","四川","江苏","安徽"]

def isInList(name, slist):
    for l in slist:
        if(l in name):
            return True
    return False

if __name__ == "__main__":
    for i in range(30):
        while(1):
            street = streetGen.getRandomAdress("buyer_")
            if isInList(street["buyer_state"], buyerProvinceList):
                print(streetGen.formate(street) )
                break

    for i in range(30):
        while(1):
            street = streetGen.getRandomAdress("seller_")
            if isInList(street["seller_state"], sellerProvinceList):
                print(streetGen.formate(street) )     
                break