import pinyin

fileName = ["item.txt"]


if __name__ == "__main__":
    for name in fileName:  
        with open(name,encoding="utf-8") as file:   
            lines = file.readlines()
            mp = {}
            for line in lines:
                line = line[:-1]
                mp[line] = pinyin.pinyin(line)
            for k,v in mp.items():
                print(v)