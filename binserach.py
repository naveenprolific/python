import numpy
def binsearch(arr,key,low,high):
    if high >= low : 
        mid = int(low+(high-low)/2)
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binsearch(arr,key,low,mid-1)
        else:
            return binsearch(arr,key,mid+1,high)
    else:
        return -1

    
def main():
    arr = numpy.array(list(map(int,input("enter the elements :").split())),'i')
    low = 0
    high = len(arr)-1
    key=int(input("enter the key u wanna search for :"))
    result = binsearch(arr,key,low,high)

    print("array elements are :",*arr)
    if result != -1:
        print("the key is found at {}".format(result))
    else:
        print("the key is not found")

main()
