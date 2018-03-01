import numpy
def binsearch(arr,key,low,high):
    while high >= low : 
        mid = int(low+(high-low)/2)
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid-1
    
    return False

    
def main():
    arr = numpy.array(list(map(int,input("enter the elements :").split())),'i')
    low = 0
    high = len(arr)-1
    key=int(input("enter the key u wanna search for :"))
    result = binsearch(arr,key,low,high)
    print(result)
    print("array elements are :",*arr)
    if result is not False:
        print("the key is found at {}".format(result))
    else:
        print("the key is not found")

main()
