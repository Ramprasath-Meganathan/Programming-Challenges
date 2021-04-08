import re
from string import ascii_uppercase
finalMatrix=[]

#Method1: to form a key matrix from the key
def Key_To_Matrix(key):
    keyArray=[]
    keyMatrix=[]
    if key != '':
        keyArray= [char for char in key]
        for character in keyArray:
            if character not in keyMatrix:
                keyMatrix.append(character)
        for alphabet in ascii_uppercase:
            if alphabet not in keyMatrix:
                keyMatrix.append(alphabet)
    count=0
    intermediateMatrix=[]

    for keyValue in keyMatrix:
     if keyValue!='J':
      if count<5:
        count=count+1
        intermediateMatrix.append(keyValue)
      else:
        count=1
        finalMatrix.append(intermediateMatrix)
        intermediateMatrix =[]
        intermediateMatrix.append(keyValue)
    finalMatrix.append(intermediateMatrix)
    return finalMatrix

#Method2: to convert plain text to cipher text
def PlainCipher_To_CipherText(plaintext,finalMatrix):
    plaintext=plaintext.replace(" ","")
    plainTextArray = [char for char in plaintext]
    count=0
    finalList=[]
    intermediateList=[]
    leftout=''
    for val in plainTextArray:
        if count<2:
          if leftout!='':
                intermediateList.append(leftout)
                count=count+1
                if leftout==val:
                    intermediateList.append('X')
                    leftout=val
                    count=count+1
                else:
                    if count==2:
                        finalList.append(intermediateList)
                        intermediateList=[]
                        count=0
                    intermediateList.append(val)
                    leftout=''
                    count=count+1
          else:
              intermediateList.append(val)
              count=count+1
        else:
            count=0
            finalList.append(intermediateList)
            intermediateList=[]
            if leftout!='':
                intermediateList.append(leftout)
                count=count+1
            leftout=val
    if intermediateList!='':
        finalList.append(intermediateList)
    cipherDict={}
    cipherTextDict={}
    for val in finalList:
        firstLetter=val[0]
        secondLetter = val[1]
        Row_Number=0
        Col_Number=0
        for row in finalMatrix:
            Row_Number=Row_Number+1
            for col in row:
                Col_Number=Col_Number+1
                if col == firstLetter:
                    cipherTextDict[firstLetter] = [Row_Number,Col_Number]
                if col==secondLetter:
                    cipherTextDict[secondLetter] = [Row_Number,Col_Number]
            Col_Number=0
        if str(val) in cipherDict:
            val=str(val)+"1"
        if cipherTextDict[firstLetter][0] != cipherTextDict[secondLetter][0] and cipherTextDict[firstLetter][1]!=cipherTextDict[secondLetter][1]:
            cipherDict[str(val)] = [[cipherTextDict[firstLetter][0],int(cipherTextDict[secondLetter][1])],[cipherTextDict[secondLetter][0],int(cipherTextDict[firstLetter][1])]]
        if cipherTextDict[firstLetter][0] == cipherTextDict[secondLetter][0]:
            if cipherTextDict[firstLetter][1]==5:
                   cipherDict[str(val)] = [[cipherTextDict[firstLetter][0],1],[cipherTextDict[secondLetter][0],int(cipherTextDict[secondLetter][1])+1]]
            elif cipherTextDict[secondLetter][1]==5:
               cipherDict[str(val)] =  [[cipherTextDict[firstLetter][0],int(cipherTextDict[firstLetter][1])+1],[cipherTextDict[secondLetter][0],1]]
            else:
                cipherDict[str(val)] = [[cipherTextDict[firstLetter][0],int(cipherTextDict[firstLetter][1])+1],[cipherTextDict[secondLetter][0],int(cipherTextDict[secondLetter][1])+1]]
        if cipherTextDict[firstLetter][1] == cipherTextDict[secondLetter][1]:
            if cipherTextDict[firstLetter][0]==5:
                   cipherDict[str(val)] = [[1,cipherTextDict[firstLetter][1]],[int(cipherTextDict[secondLetter][0])+1,cipherTextDict[secondLetter][1]]]
            elif cipherTextDict[secondLetter][0]==5:
               cipherDict[str(val)] = [[int(cipherTextDict[firstLetter][0])+1,cipherTextDict[firstLetter][1]],[1,cipherTextDict[secondLetter][1]]]
            else:
                cipherDict[str(val)] = [[int(cipherTextDict[firstLetter][0])+1,cipherTextDict[firstLetter][1]],[int(cipherTextDict[secondLetter][0])+1,cipherTextDict[secondLetter][1]]]
        Row_Number=0
    intermediatecipherText=''
    intermediatecipherDict={}
    for key,val in cipherDict.items():
        for val1 in val:
                for row in finalMatrix:
                     Row_Number= Row_Number+1
                     for col in row:
                        Col_Number=Col_Number+1
                        if  Row_Number==val1[0] and Col_Number==val1[1]:
                                intermediatecipherText+=col
                                continue
                     Col_Number=0
                Row_Number=0
        intermediatecipherDict[key]=intermediatecipherText
       
    return intermediatecipherText

#check if the repeated characters check Reference [3]
def repeatedCharacterscheck(intermediatecipherText):
    count = {}
    for characters in intermediatecipherText:
        if characters in count:
            count[characters] += 1
        else:
            count[characters] = 1
    for key in count:
        if count[key] > 1:
            return True
    return False

#Method3: to convert cipher text to plain text
def CipherText_To_PlainText(ciphertext,keyMatrix):
    cipherTextArray = [char for char in ciphertext] 
    count=0
    finalCipherTextList=[]
    intermediateCipherTextList=[]
    leftout=''
    for val in cipherTextArray:
        if count<2:
            if leftout!='':
                intermediateCipherTextList.append(leftout)
                count=count+1
            intermediateCipherTextList.append(val)
            count= count+1
        else:
            finalCipherTextList.append(intermediateCipherTextList)
            leftout=val
            intermediateCipherTextList=[]
            count=0
    if intermediateCipherTextList!='':
        finalCipherTextList.append(intermediateCipherTextList)
    cipherDict={}
    cipherTextDict={}
    for val in finalCipherTextList:
        firstLetter=val[0]
        secondLetter = val[1]
        Row_Number=0
        Col_Number=0
        for row in finalMatrix:
            Row_Number=Row_Number+1
            for col in row:
                Col_Number=Col_Number+1
                if col == firstLetter:
                    cipherTextDict[firstLetter] = [Row_Number,Col_Number]
                if col==secondLetter:
                    cipherTextDict[secondLetter] = [Row_Number,Col_Number]
            Col_Number=0
        if str(val) in cipherDict:
            val=str(val)+"1"
        if cipherTextDict[firstLetter][0] != cipherTextDict[secondLetter][0] and cipherTextDict[firstLetter][1]!=cipherTextDict[secondLetter][1]:
            cipherDict[str(val)] = [[cipherTextDict[firstLetter][0],int(cipherTextDict[secondLetter][1])],[cipherTextDict[secondLetter][0],int(cipherTextDict[firstLetter][1])]]
        if cipherTextDict[firstLetter][0] == cipherTextDict[secondLetter][0]:
            if cipherTextDict[firstLetter][1]==1:
                   cipherDict[str(val)] = [[cipherTextDict[firstLetter][0],5],[cipherTextDict[secondLetter][0],int(cipherTextDict[secondLetter][1])-1]]
            elif cipherTextDict[secondLetter][1]==1:
               cipherDict[str(val)] =  [[cipherTextDict[firstLetter][0],int(cipherTextDict[firstLetter][1])-1],[cipherTextDict[secondLetter][0],5]]
            else:
                cipherDict[str(val)] = [[cipherTextDict[firstLetter][0],int(cipherTextDict[firstLetter][1])-1],[cipherTextDict[secondLetter][0],int(cipherTextDict[secondLetter][1])-1]]
        if cipherTextDict[firstLetter][1] == cipherTextDict[secondLetter][1]:
            if cipherTextDict[firstLetter][0]==1:
                   cipherDict[str(val)] = [[5,cipherTextDict[firstLetter][1]],[int(cipherTextDict[secondLetter][0])-1,cipherTextDict[secondLetter][1]]]
            elif cipherTextDict[secondLetter][0]==1:
               cipherDict[str(val)] = [[int(cipherTextDict[firstLetter][0])-1,cipherTextDict[firstLetter][1]],[5,cipherTextDict[secondLetter][1]]]
            else:
                cipherDict[str(val)] = [[int(cipherTextDict[firstLetter][0])-1,cipherTextDict[firstLetter][1]],[int(cipherTextDict[secondLetter][0])-1,cipherTextDict[secondLetter][1]]]
        Row_Number=0
    intermediatecipherText=''
    intermediatecipherDict={}
    for key,val in cipherDict.items():
        for val1 in val:
                for row in finalMatrix:
                     Row_Number= Row_Number+1
                     for col in row:
                        Col_Number=Col_Number+1
                        if  Row_Number==val1[0] and Col_Number==val1[1]:
                                intermediatecipherText+=col
                                continue
                     Col_Number=0
                Row_Number=0
        intermediatecipherDict[key]=intermediatecipherText
        if 'X' in intermediatecipherText  and repeatedCharacterscheck(intermediatecipherText) :
            intermediatecipherText = intermediatecipherText.replace("X","")
    return intermediatecipherText

#scenarios or cases examples tested - all  different scenarios are also specified in text file 
#Example1(REPEATED CHARACTERS IN A PAIR)
cipherkey = "PLAYFIRE"
ciphertext="QMBNBNRTVR"
plaintext = "THIS IS COOL"

#Example2(ODD NUMBER OF CHARACTERS AND REPEATED CHARACTERS)
cipherkey="SECURITY"
plaintext="COME QUICKLY WE NEED HELP"
ciphertext = "UNVTXSYSDPGCCMUVSFFUML"

#Example3 (REPEATED NUMBER OF CHARACTERS)
cipherkey = "MICROSOFT"
plaintext="NEXT VERSION BEING RELEASED"
ciphertext = "WNCGWDMACMUFNFPEIHNDBFGE"

#Example 4 (UNIQUE CHARACTERS)
cipherkey = "GRAPHIC"
iphertext="UPBOSOBUODUFBOBHTX"
plaintext = "THIS QUESTION IS EASY"

#Example 5
cipherkey="ABRACADABRA"
ciphertext="ecakckhdiacv"
plaintext='HAVE A NICE DAY'

#driver function to test the scenarios 
#change the plaintext , cipher text and key for testing different inputs
def main():
    cipherkey = "ABRACADABRA"
    ciphertext="ECAKCKHDIACV"
    plaintext = "HAVE A NICE DAY"
    finalMatrix = Key_To_Matrix(cipherkey)
    print("Key Matrix: ")
    for val in finalMatrix:
        print(val)
    generatedciphertext= PlainCipher_To_CipherText(plaintext,finalMatrix)
    generatedplaintext = CipherText_To_PlainText(generatedciphertext,finalMatrix)
    print("The cipher text for plain text "+plaintext+" is ",generatedciphertext)
    print("The plaintext for cipher text "+ciphertext+" is ", generatedplaintext)

if __name__=="__main__":
    main()

#code References for Exercise 1:
#[1] “Python | Split string into list of characters - GeeksforGeeks,” GeeksforGeeks, 05-Feb-2019. [Online]. Available: https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/. [Accessed: 19-Mar-2021]
#‌[2] MillsOnWheels, “How do I iterate through the alphabet?,” Stack Overflow, 19-Jun-2013. [Online]. Available: https://stackoverflow.com/questions/17182656/how-do-i-iterate-through-the-alphabet. [Accessed: 19-Mar-2021]
#[3] “check for repeated characters in a string python Code Example,” Codegrepper.com, 2020. [Online]. Available: https://www.codegrepper.com/code-examples/python/check+for+repeated+characters+in+a+string+python. [Accessed: 19-Mar-2021]
