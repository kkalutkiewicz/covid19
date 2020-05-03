import numpy as np

def exp_rate(arr):
    """Returns the exponential rate of increase of a 1D array"""
    n=len(arr)
    output=np.zeros(n)
    for k in range(1,n):
        if arr[k]!=0 and arr[k-1]!=0:
            output[k]=np.log(arr[k]/arr[k-1])
        else:
            output[k]=0
    return output

def smooth(arr,K,r):
    """Returns a moving average of an array, K steps back and forth with weight decreasing at rate r"""
    n=len(arr)
    output=np.zeros(n)
    for k in range(n):
        output[k]=0.0
        weights=0.0
        for i in range(-K,K+1):
            if k+i in range(n):
                output[k] += arr[k+i]*(r**abs(i))
                weights += r**abs(i)
        output[k] = output[k]/weights     
    return output
