import base64
print("enter the data you want to encrypt")
for_Encription=raw_input()
encrypted=base64.b64encode(for_Encription)
print("your incripted ata is : "+encrypted)

##dat=base64.b64decode(encrypted)
##print("your decreapted data is : " +dat)