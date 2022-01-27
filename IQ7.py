a= input("Enter the symbol:")
b=[]
for i in range(0,len(a)):
    b.append(a[i])
for k in range(0,len(a)):
    if a[k] in ["(","{","["]:
        for j in range(k,len(a)):
            if b[k]=="{" and b[j]=="}" and b.index(b[k])%2!= b.index(b[j])%2:
                b[k]=0
                b[j]=0
                break
            elif b[k]=="[" and b[j]=="]" and b.index(b[k])%2 != b.index(b[j])%2:
                b[k]=0
                b[j]=0
                break
            elif b[k]=="(" and  b[j]==")" and b.index(b[k])%2!= b.index(b[j])%2:
                b[k]=0
                b[j]=0           
                break  
for l in range(0,len(b)):
    if b[l]==0:
        continue
    else:
        print("Not Balanced")
        break
else:
    print("Balanced")
