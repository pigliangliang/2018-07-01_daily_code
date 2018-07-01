#author_by zhuxiaoliang
#2018-07-01 上午10:15

def QuickSort(l,s,e):
    if s <e:
        i,j = s,e
        #设置基准
        base = l[i]

        while i<j:
            while (i<j) and (base<=l[j]):
                j -=1

            l[i]=l[j]
            while i <j and l[i]<=base:
                i +=1
            l[j]=l[i]
        l[i]=base

        #递归
        QuickSort(l,s,i-1)
        QuickSort(l,j+1,e)
    return  l

if __name__=="__main__":
    myList = [49,38,65,97,76,13,27,49]
    print("Quick Sort: ")
    QuickSort(myList,0,len(myList)-1)
    print(myList)
