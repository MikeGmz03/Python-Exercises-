def findNumber(arr, k): #ejemplo encontrar numero con un arreglo previo y un valor K para buscar
    for i in arr:
        if i == k:
            return "YES"
    return "NO"
