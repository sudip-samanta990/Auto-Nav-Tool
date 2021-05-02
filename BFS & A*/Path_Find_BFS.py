import networkx as nx 
import matplotlib.pyplot as plt

lists=[]
lists_x=[]
lists_y=[]
result = []
path_grid=[]

A=int(input("enter the upper bound of the x axis in the grid: "))
B=int(input("enter the upper bound of the y axis in the grid: "))
g=float(input("enter the resolution of the grid: "))
K=int(input("enter the total numberof partition in the grid: "))
x_2=int(input("enter the x-cordinate of the Goal point: "))
y_2=int(input("enter the y-cordinate of the Goal point: "))

f=open('obstacles_lists_1st_map.txt')    
for line in f:
	lists.append(line.rstrip().split(","))
for i in range(0, len(lists)):
	for j in range(0,len(lists[i])): 
		lists[i][j] = int(lists[i][j])
#print(lists)

def plotting(): 
	#print("distinct_list-b == %d"%distinct_list(b))
	plt.xlim(0, A+20)
	plt.ylim(0, B+20)
	for i in range(0,len(lists),1):
		plt.plot([lists[i][0],lists[i][0],lists[i][1],lists[i][1],lists[i][0]],[lists[i][2],lists[i][3],lists[i][3],lists[i][2],lists[i][2]],color='black') 
	
	plt.plot(lists_x,lists_y)
	plt.xlabel("width")
	plt.ylabel("height")
	plt.title("map graph")
	plt.grid(b=True)
	plt.show()


def output(path_grid,s,g):
	
	print("the path is:",end='')
	for i in range(0,len(path_grid)):
		y_1=path_grid[i]//K
		x_1=path_grid[i]%K
		lists_x.append(x_1)
		lists_y.append(y_1)	
		print("---->(%d,%d)"%(x_1,y_1),end='')
	print("length of the path = %d"%len(path_grid))
	
G = nx.DiGraph()
with open("add_edges.txt", "r") as fp:
	for i in fp.readlines():
		tmp = i.strip().split(",")
		result.append((int(tmp[0]), int(tmp[1])))
		#result.append((eval(tmp[0]), eval(tmp[1])))

for i in range(0,len(result)):
	G.add_edge(result[i][0],result[i][1] )

f=open("pose_3.txt")
x=f.readline()
y=x.rstrip().split(",")
y[0]=float(y[0])
y[1]=float(y[1])
y[0]=round((y[0]+5.5)/g)
y[1]=round((y[1]+5.5)/g)



g=y_2*K+x_2
s=y[1]*K+y[0]

path_grid=nx.shortest_path(G, source=s, target=g)

output(path_grid,s,g)
plotting()
	



