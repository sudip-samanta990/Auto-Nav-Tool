import os
import math
import matplotlib.pyplot as plt

lists=[]
f=open('obstacles_lists.txt')    
for line in f:
	lists.append(line.rstrip().split(","))
for i in range(0, len(lists)):
	for j in range(0,len(lists[i])): 
		lists[i][j] = int(lists[i][j])


def plotting(A,B): 
	
	f2=open('output_seq_path.txt')
	next(f2)
	lists1=[]
	f3=open("re_creat.txt","w")
	data=f2.read()
	data=data.replace("(/ ","")
	data=data.replace(")","")
	data=data.replace(" ",",")
	#print(data)
	f3.write(data)
	f3.close()
	f4=open('re_creat.txt')
	for line in f4:
		lists1.append(line.rstrip().split(","))

	for i in range(0, len(lists1)):
		for j in range(0,len(lists1[i])): 
			lists1[i][j] = float(lists1[i][j])
	#print(lists1)
	for i in range (0,len(lists1)):
		if len(lists1[i]) > 1:
			lists1[i][0]=round(lists1[i][0]/lists1[i][1],2)
	#print(lists)
	lists3=[]
	lists4=[]
	for i in range(0,len(lists1),2):   
		lists3.append(lists1[i][0])
	for i in range(1,len(lists1),2):
		lists4.append(lists1[i][0])
	plt.xlim(0, A+10)  
	plt.ylim(0, B+50)
	for i in range(0,len(lists),1):
		plt.plot([lists[i][0],lists[i][0],lists[i][1],lists[i][1],lists[i][0]],[lists[i][2],lists[i][3],lists[i][3],lists[i][2],lists[i][2]],color='black') 
	
	plt.plot(lists3,lists4)
	plt.xlabel("width")
	plt.ylabel("height")
	plt.title("map graph")
	plt.grid(b=True)
	plt.show()



def smt ():
	V=int(input("enter the max. velocity of the bot: " ))
	A=int(input("enter the upper bound of the x axis in the grid: "))
	B=int(input("enter the upper bound of the y axis in the grid: "))
	r=int(input("enter the padding length for obstacles block: " ))
	
	X=int(input("enter the x co-ordinte of inital position of the bot: "))
	Y=int(input("enter the y co-ordinate of initial position of the bot: "))
	#print("enter the goal region \n")
	'''X1=int(input("enter the lower bound of the x co-ordinate of the goal region: "))
	X2=int(input("enter the upper bound of the x co-ordinate of the goal region: "))
	Y1=int(input("enter the lower bound of the y co-ordinate of the goal region: "))
	Y2=int(input("enter the upper bound of the y co-ordinate of the goal region: "))'''
	X1=int(input("enter the x co-ordinate of the goal position: "))
	Y1=int(input("enter the y co-ordinate of the goal position: "))
	t=2
	for var1 in range (0,30):
		file1 = open("path_plan.smt2", "w")
		file1.write("(set-option :timeout 30000)\n") # time bound 30s 
		for i in range(0,t):
			file1.write("(declare-const Q1T%dX  Real)\n"%i)
			file1.write("(declare-const Q1T%dY  Real)\n"%i)
			
		for i in range(0,len(lists)):
			file1.write("(declare-const obs%dX_tl  Real)\n"%i)
			file1.write("(declare-const obs%dX_tr  Real)\n"%i)
			file1.write("(declare-const obs%dX_bl  Real)\n"%i)
			file1.write("(declare-const obs%dX_br  Real)\n"%i)
			file1.write("(declare-const obs%dY_tl  Real)\n"%i)
			file1.write("(declare-const obs%dY_tr  Real)\n"%i)
			file1.write("(declare-const obs%dY_bl  Real)\n"%i)
			file1.write("(declare-const obs%dY_br  Real)\n"%i)
			
		for i in range(1,t):
			for j in range(0,len(lists)):
				file1.write("(declare-const a_%d_%d  Real)\n"%(i,j))
				file1.write("(declare-const b_%d_%d  Real)\n"%(i,j))
				file1.write("(declare-const c_%d_%d  Real)\n"%(i,j))
		'''for i in range (1,t)
			file1.write("(declare-const c_%d  Real)\n"%i)'''
				
		#initialize the boundary		
		for i in range(0,t):
			file1.write("(assert ( and (>= Q1T%dX 0) (<= Q1T%dX 1089)))\n"%(i,i))
			file1.write("(assert ( and (>= Q1T%dY 0) (<= Q1T%dY 1122)))\n"%(i,i))	

		#define obstacles
		for i in range(0,len(lists)): 
			file1.write("(assert (= obs%dX_tl %d))\n"%(i,lists[i][0]-r))
			file1.write("(assert (= obs%dY_tl %d))\n"%(i,lists[i][3]+r))
			file1.write("(assert (= obs%dX_tr %d))\n"%(i,lists[i][1]+r))
			file1.write("(assert (= obs%dY_tr %d))\n"%(i,lists[i][3]+r))
			file1.write("(assert (= obs%dX_br %d))\n"%(i,lists[i][1]+r))
			file1.write("(assert (= obs%dY_br %d))\n"%(i,lists[i][2]-r))
			file1.write("(assert (= obs%dX_bl %d))\n"%(i,lists[i][0]-r))
			file1.write("(assert (= obs%dY_bl %d))\n"%(i,lists[i][2]-r))
		
		#initialize the positions
		file1.write("(assert (= Q1T0X %d))\n"%X)
		file1.write("(assert (= Q1T0Y %d))\n"%Y)	
		
		file1.write(";MOVEMENT OF ROBOT\n")  #bound the maximum velocity
		
		for i in range(1,t):
			file1.write("(assert (and (< (abs (- Q1T%dX Q1T%dX)) %d) (< (abs (- Q1T%dY Q1T%dY)) %d)))\n "%(i,i-1,V,i,i-1,V))
		file1.write("\n\n")
		
		# constraint for obstacles avoidence 
		for i in range(1,t):
			for j in range(0,len(lists)):
				file1.write("(assert (or (and (< (+ (* a_%d_%d  Q1T%dX) (* b_%d_%d Q1T%dY)  c_%d_%d) 0)\n"%(i,j,i-1,i,j,i-1,i,j))	
				file1.write("(< (+ (* a_%d_%d  Q1T%dX) (* b_%d_%d Q1T%dY)  c_%d_%d) 0)\n"%(i,j,i,i,j,i,i,j))
				file1.write("(> (+ (* a_%d_%d  obs%dX_tl) (* b_%d_%d obs%dY_tl)  c_%d_%d) 0)\n"%(i,j,j,i,j,j,i,j))
				file1.write("(> (+ (* a_%d_%d  obs%dX_tr) (* b_%d_%d obs%dY_tr)  c_%d_%d) 0)\n"%(i,j,j,i,j,j,i,j))
				file1.write("(> (+ (* a_%d_%d  obs%dX_bl) (* b_%d_%d obs%dY_bl)  c_%d_%d) 0)\n"%(i,j,j,i,j,j,i,j))
				file1.write("(> (+ (* a_%d_%d  obs%dX_br) (* b_%d_%d obs%dY_br)  c_%d_%d) 0))\n"%(i,j,j,i,j,j,i,j))
				file1.write("(and (> (+ (* a_%d_%d  Q1T%dX) (* b_%d_%d Q1T%dY)  c_%d_%d) 0)\n"%(i,j,i-1,i,j,i-1,i,j))	
				file1.write("(> (+ (* a_%d_%d  Q1T%dX) (* b_%d_%d Q1T%dY)  c_%d_%d) 0)\n"%(i,j,i,i,j,i,i,j))
				file1.write("(< (+ (* a_%d_%d  obs%dX_tl) (* b_%d_%d obs%dY_tl)  c_%d_%d) 0)\n"%(i,j,j,i,j,j,i,j))
				file1.write("(< (+ (* a_%d_%d  obs%dX_tr) (* b_%d_%d obs%dY_tr)  c_%d_%d) 0)\n"%(i,j,j,i,j,j,i,j))
				file1.write("(< (+ (* a_%d_%d  obs%dX_bl) (* b_%d_%d obs%dY_bl)  c_%d_%d) 0)\n"%(i,j,j,i,j,j,i,j))
				file1.write("(< (+ (* a_%d_%d  obs%dX_br) (* b_%d_%d obs%dY_br)  c_%d_%d) 0))))\n"%(i,j,j,i,j,j,i,j))
		
		#goal position
		
		#file1.write("(assert (and (and (>= Q1T%dX %d) (<= Q1T%dX %d)) (and (>= Q1T%dY %d) (<= Q1T%dY %d)))) "%(t-1,X1,t-1,X2,t-1,Y1,t-1,Y2))
		file1.write("(assert (and (= Q1T%dX %d) (= Q1T%dY %d)))" %(t-1,X1,t-1,Y1))
		file1.write("(check-sat)")
		for i in range(0,t):
			file1.write("(eval Q1T%dX)\n"%i)
			file1.write("(eval Q1T%dY)\n"%i)
			
		file1.close()
		cmd='z3 path_plan.smt2 > output_seq_path.txt'
		os.system(cmd)
		file3=open("output_seq_path.txt",'r')
		row1 = file3.readline().strip()
		file3.close()
		if row1 == "sat":
			print("successfull")
			#print(lists2)
			plotting(A,B)
			break
		else:
			t=t+1
			print("the value value of t= %d"%t)
			print("the value of itaration var1= %d"%var1)
					
				
		
if __name__ == '__main__':
	smt()			
		
		
					
