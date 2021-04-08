from collections import OrderedDict 

programmticciphertext=''
#Method1: to convert plain text to cipher text
def PlainText_To_CipherText(plaintext,key): 
      No_of_cols = max(key)
      plainTextArray = [char for char in plaintext]
      Total_char_length = len(plainTextArray)
      while Total_char_length% No_of_cols!=0:
        plaintext= plaintext+'%'
        Total_char_length=Total_char_length+1
      plainTextArray = [char for char in plaintext]
      No_of_rows = Total_char_length/No_of_cols
      pointer=0
      Rowval = No_of_rows
      intermediateArray=[]
      finalArray=[]
      while pointer<Rowval:
          for i in range(pointer,int(Total_char_length),int(No_of_cols)):
            if plainTextArray[i]==' ':
                intermediateArray.append('%')
            else:
                intermediateArray.append(plainTextArray[i])
          finalArray.append(intermediateArray)
          intermediateArray=[]
          pointer=pointer+1
      cipherText=[]
      for k in key:
          cipherText.append("".join(finalArray[k-1]))
          programmticciphertext = "".join(cipherText)
      return programmticciphertext

#Method2: to convert cipher text to plain text      
def CipherText_To_PlainText(ciphertext,key): 
    No_of_cols = max(key)
    Total_char_length = len(ciphertext)
    No_of_rows = int(Total_char_length/No_of_cols)
    cipherTextSplit = [ciphertext[i:i+No_of_rows] for i in range(0, len(ciphertext), No_of_rows)]
    rearrangedCipherDictionary={}
    i=0
    for k in key:
           rearrangedCipherDictionary[k]=cipherTextSplit[i]
           i=i+1
    sortedcipher=[]
    for i in range(1,No_of_cols+1,1):
        sortedcipher.append(rearrangedCipherDictionary[i])
    pointer=0
    plaintextformed=''
    while pointer<No_of_rows:
        for value in sortedcipher:
            plaintextformed+=value[pointer]
        pointer=pointer+1
    finalplaintext=''
    plainTextArray = [char for char in plaintextformed]
    for val in plainTextArray:
        if val=='%':
            finalplaintext+=' '
        else:
            finalplaintext+=val
    return finalplaintext

#scenarios or cases examples tested - all  different scenarios are also specified in text file
#Example 1 (lowercase letters with space)
key=[5,4,1,3,2]
plaintext='meet at military house'
ciphertext = '%iru%tmao%malyse%th%eti%e'

#Example 2 (Uppercase letters with space)
key=[5,4,1,2,3]
plaintext='SECURITY!SECURITY!SECURITY!'
ciphertext='RSIET%U!RSI%SIETCYETCYU!CYU!R%'

#Example 3
key = [4,3,1,2]
ciphertext = 'abc%abccaabcabbc'
plaintext = 'aaaaabbbbbccccc'

#Example 4(WITH NUMBERS)
key = [4,3,1,2]
ciphertext = 'abc1%abcc4aabc2abbc3'
plaintext = 'aaaaabbbbbccccc1234'

#driver function to test the scenarios 
#change the plaintext , cipher text and key for testing different inputs
def main():
    key = [4,3,1,2]
    plaintext = 'aaaaabbbbbccccc1234'
    ciphertext = 'abc1%abcc4aabc2abbc3'
    generatedciphertext = PlainText_To_CipherText(plaintext,key)
    generatedplaintext = CipherText_To_PlainText(generatedciphertext,key)
    print("The cipher text for plaintext "+plaintext+" is "+generatedciphertext)
    print("The plain text for cipher text "+ciphertext+" is "+generatedplaintext)

if __name__=='__main__':
    main()

#code References for Exercise 2:
‌#[4] user1790915, “How do you join all items in a list?,” Stack Overflow, 01-Nov-2012. [Online]. Available: https://stackoverflow.com/questions/13174468/how-do-you-join-all-items-in-a-list/13175535. [Accessed: 19-Mar-2021]
‌#[5] “Python Split String into Specific Length Chunks - Python Examples,” Pythonexamples.org, 2021. [Online]. Available: https://pythonexamples.org/python-split-string-into-specific-length-chunks/. [Accessed: 19-Mar-2021]
‌#[6] “Python | Sort Python Dictionaries by Key or Value - GeeksforGeeks,” GeeksforGeeks, 24-Jul-2018. [Online]. Available: https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/. [Accessed: 19-Mar-2021]