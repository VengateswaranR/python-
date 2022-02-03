n=int(input())
for i in range(0,n):                         
    for j in range(0,n):  
        if i<n//2:            
            if(j==n//2+i or j==n//2-i):                
                print("*",end=' ')         
            else:            
                print(end='  ')    
        else:
            if(j==0 or j==n-1 or i==n//2):                
                print("*",end=' ')         
            else:            
                print(end='  ')        
    print()
