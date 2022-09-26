def scannarr(lst,srchtrm):
    boolean=0
    for i in range(len(lst)):
        if lst[i]==srchtrm:
            boolean=1
            break
    return boolean
lstnme=["cat","dog","monkey","cow"]
result=scannarr(lstnme,"cow")
if result==1:
    print(result,"hello")
else:
    print("no")

