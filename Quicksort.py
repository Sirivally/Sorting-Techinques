def swap(arr,a,b):
    arr[a],arr[b]=arr[b],arr[a]

def partition(arr,start,end):
    pIndex=start
    pivot=arr[pIndex]
    while start<end:
        while start<len(arr)-1 and arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start>=end:
            return end
    swap(arr,start,end)
    

def quicksort(arr,start,end):
    if start<end:
        pI=partition(arr,start,end)
        quicksort(arr,start,pI)
        quicksort(arr,pI+1,end)

if  __name__=="__main__":
    arr=[78,41,90]
    quicksort(arr,0,len(arr)-1)
    print(arr)



