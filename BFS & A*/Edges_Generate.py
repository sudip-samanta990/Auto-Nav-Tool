lists=[]
lists2=[]

def check(lists,x,y):
	#print(len(lists))
	
	if x>= 0 and x<=A  and  y>= 0 and y<= B:
		#print("x,y--> %d,%d  index-->%d"%(x,y,(y*K)+x))
		if lists[y*K+x] == 1:
			return 0
		else:
			return 1
	else:
		return 0

A=int(input("enter the upper bound of the x axis in the grid: "))
B=int(input("enter the upper bound of the y axis in the grid: "))
K=int(input("enter the total numberof partition in the grid: "))
	
for i in range(0,((A+1)*(B+1))):
	lists.append(0)
print(len(lists))
f=open('obstacles_lists_1st_map.txt')    
for line in f:
	lists2.append(line.rstrip().split(","))
for i in range(0, len(lists2)):
	for j in range(0,len(lists2[i])): 
		lists2[i][j] = int(lists2[i][j])



for i in range (0,len(lists2)):
	for y in range(lists2[i][2],lists2[i][3]+2,1):
		for x in range(lists2[i][0],lists2[i][1]+2,1):
			p= y*K+x
			lists[p]=1
file1=open("add_edges.txt", "w")			
for indx,val in enumerate(lists):
	if val==0:
		n=indx//K
		m=indx%K

		if check(lists,m-1,n)== 1:
			string=str(n*K+m)+","+str(n*K+(m-1))+"\n"
			file1.write(string)
			
		if check(lists,m+1,n)== 1:
			string=str(n*K+m)+","+str(n*K+(m+1))+"\n"
			file1.write(string)
			
		if check(lists,m,n-1)== 1:
			string=str(n*K+m)+","+str((n-1)*K+m)+"\n"
			file1.write(string)
			
		if check(lists,m,n+1)== 1:
			string=str(n*K+m)+","+str((n+1)*K+m)+"\n"
			file1.write(string)
			
			
		if check(lists,m-1,n-1)== 1:
			string=str(n*K+m)+","+str((n-1)*K+(m-1))+"\n"
			file1.write(string)	
			
		if check(lists,m+1,n+1)== 1:
			string=str(n*K+m)+","+str((n+1)*K+(m+1))+"\n"
			file1.write(string)
			
			
		if check(lists,m-1,n+1)== 1:
			string=str(n*K+m)+","+str((n+1)*K+(m-1))+"\n"
			file1.write(string)
			
		if check(lists,m+1,n-1)== 1:
			string=str(n*K+m)+","+str((n-1)*K+(m+1))+"\n"
			file1.write(string)
			
	
file1.close()
