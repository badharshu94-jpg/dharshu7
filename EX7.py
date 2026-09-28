n= int(input("enter number of elements:"))
a=[]
print("enter elements:")
for i in range(n):
 a.append(int(input()))
key= int(input("enter element to search:"))
found=False
for i in range(n):
   if a[i]==key:
      print("element found at position",i+1)
      found=True
      break
   if not found:
       print("element not found")
       
 
