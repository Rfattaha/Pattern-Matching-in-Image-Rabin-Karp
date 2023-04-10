import cv2
img = cv2.imread("ImageBig.png", cv2.IMREAD_COLOR)
a = img.tolist()
b = []
hash_sums = []
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)    

def FindNumofColor(img,M,N,arr):
    i = 1
    j = N - 2
    while i < M:
        if img[i][j] == [0,0,0]:
            break
        while j > 0:
            if img[i][j] == [0,0,0] and img[i][j-1] != [0,0,0]:
                j -=1
            if img[i][j] == [0,0,0] and img[i][j-1] == [0,0,0]:  
                break 
            if img[i][j] not in arr:
                arr.append(img[i][j]) 
            if img[i][j] != [0,0,0]:
                j -=1
        j = N - 2
        i+=1        

FindNumofColor(a,height,width,b)



def CalcHash(arr):
    a  = arr[0] * 100
    b = arr[1] * 10
    c = arr[2] * 1
    # 13 == mod value
    return (a + b + c) % 13

def SumofHashPattern(img,M,N,hash_sums,color_Arr):
    sumofHash = 0
    i = 1
    j = N-2
    while i < M:
        if img[i][j] == [0,0,0]:
            break
        while j > 0:
            if img[i][j] == [0,0,0] and img[i][j-1] != [0,0,0]:
                j -=1
            if img[i][j] == [0,0,0] and img[i][j-1] == [0,0,0]:  
                break 
            if img[i][j] in color_Arr:
                a = (CalcHash(img[i][j]))
                sumofHash += a
                hash_sums.append(a)
            if img[i][j] != [0,0,0]:
                j -=1
        j = N - 2
        i += 1
    return sumofHash

sumofHash = SumofHashPattern(a,height,width,hash_sums,b)

def FoundRightCornerCoor(img,M,N):
    i = 1 
    j = N - 2
    x = 0
    y = 0
    while i < M:
        if img[i][j] == [0,0,0]:
            break
        while img[i][j] != [0,0,0]:
            y+=1        
            if img[i][j-1] == [0,0,0]:
                break
            j -=1
        j = N - 2
        x += 1
        i += 1 
    print("pattern height and width pixels : ",x,y)

FoundRightCornerCoor(a,height,width)

def checkTopLeftCorner(img,M,N,sumofHash_compare,color_Arr,hash_sums_compare):
    sumofHash = 0
    i = 1
    j = 1
    hash_sums = []
    while i < M:
        if img[i][j] == [0,0,0]:
            break
        while j > 0:
            if img[i][j] == [0,0,0] and img[i][j+1] != [0,0,0]:
                j +=1
            if img[i][j] == [0,0,0] and img[i][j+1] == [0,0,0]:  
                break 
            if img[i][j] in color_Arr:
                a = (CalcHash(img[i][j]))
                sumofHash += a
                hash_sums.append(a)
            if img[i][j] != [0,0,0]:
                j +=1
        j = 1
        i += 1
    if sumofHash == sumofHash_compare and hash_sums == hash_sums_compare:
        print("Pattern has found in Left Corner")
    else:
        print("Patter does not found")

def checklowerLeftCorner(img,M,N,sumofHash_compare,color_Arr,hash_sums_compare):
    sumofHash = 0
    i = M - 2
    j = 1
    hash_sums = []
    while i < M:
        if img[i][j] == [0,0,0]:
            break
        while j > 0:
            if img[i][j] == [0,0,0] and img[i][j+1] != [0,0,0]:
                j +=1
            if img[i][j] == [0,0,0] and img[i][j+1] == [0,0,0]:  
                break 
            if img[i][j] in color_Arr:
                a = (CalcHash(img[i][j]))
                sumofHash += a
                hash_sums.append(a)
            if img[i][j] != [0,0,0]:
                j +=1
        j = 1
        i -= 1
    if sumofHash == sumofHash_compare and hash_sums == hash_sums_compare:
        print("Pattern has found in Lower Left Corner")
    else:
        print("Patter does not found")

def checklowerRightCorner(img,M,N,sumofHash_compare,color_Arr,hash_sums_compare):
    sumofHash = 0
    i = M - 2
    j = N - 2
    hash_sums = []
    while i < M:
        if img[i][j] == [0,0,0]:
            break
        while j > 0:
            if img[i][j] == [0,0,0] and img[i][j+1] != [0,0,0]:
                j -=1
            if img[i][j] == [0,0,0] and img[i][j+1] == [0,0,0]:  
                break 
            if img[i][j] in color_Arr:
                a = (CalcHash(img[i][j]))
                sumofHash += a
                hash_sums.append(a)
            if img[i][j] != [0,0,0]:
                j -=1
        j = N - 2
        i -= 1
    if sumofHash == sumofHash_compare and hash_sums == hash_sums_compare:
        print("Pattern has found in Right Left Corner")
    else:
        print("Patter does not found")

print(b)
print()
print(hash_sums)
print()
print(sumofHash)
checkTopLeftCorner(a,height,width,sumofHash,b,hash_sums)
checklowerLeftCorner(a,height,width,sumofHash,b,hash_sums)
checklowerRightCorner(a,height,width,sumofHash,b,hash_sums)

# patternin x ve y deki renk sayıları bulup bunları hashden geçirip diğer köşelerle kontrol etsek
# eğer alttaki line 0 0 0 ile başlıyosa break atılır başlamıyosa i + = 1
# M = height N = Width K = top-right-Corner
# 0 0 0 black
# arrayden patterni tespit edip rabin korp ile birleştirip true false ver
# sarı ver kırmızı olan arrayleri kaydedip bir yerde tekrar görürsek
# bitwise derken sola kaydırıp daha hızlı arama yapılabilir herhalde amınaaa


