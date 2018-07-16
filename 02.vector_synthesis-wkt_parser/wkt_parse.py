import numpy as np
from Tkinter import *
from tkFileDialog   import askopenfilename 
import os

master = Tk()
filename="global"


def getfile():
	global filename
	filename=askopenfilename(initialdir=os.getcwd())
	print(filename)
	master.destroy()

#raw=re.sub("\D","  ",raw.read())

	

back = Frame(master=master, width=500, height=200, bg='black')
back.pack()
errmsg = 'Error!'
Button(text='Select File', command=getfile).place(relx=0.5, rely=0.5, anchor=CENTER)
mainloop()
print(filename)
raw=open(filename)

parse_raw=raw.read().replace(',','!').replace(' ',',').replace('!',' ').replace(')',' ').replace('(',' ').split(' ')

#parse_array=np.genfromtxt(parse_raw,dtype='str')


outfile=open("dh_points.txt", "w")

for line in parse_raw:
# 	try:
# 		float(line)
# 	except ValueError:
# 		line=" "
# 		print("!") 
	if "," in line:
		print(line)
		outfile.write(line+"\n")
	
outfile.close()

stage_two=open("dh_points.txt")
xy_array=np.genfromtxt(stage_two, delimiter=',', dtype='float')
min=np.amin(xy_array)
max=np.amax(xy_array)

print(min)
print(max)

#print(str(xy_array[0][0]))

xout=open("%s_xpoints.txt"%len(xy_array), "w")
yout=open("%s_ypoints.txt"%len(xy_array), "w")

print('x')

xmax=np.amax(xy_array[:,0])
xmin=np.amin(xy_array[:,0])
ymax=np.amax(xy_array[:,1])
ymin=np.amin(xy_array[:,1])


midx=(xmax-xmin)/2
midy=(ymax-ymin)/2

xzero=xmin+midx
yzero=ymin+midy

xcentermin=xmin-xzero
ycentermin=ymin-yzero

xcentermax=xmax-xzero
ycentermax=ymax-yzero


print("midx  "+str(midx) +"  xmin   "+str(xmin)+"  xmax   "+str(xmax))
print("midy  "+str(midy) +"  ymin   "+str(ymin)+"  ymax   "+str(ymax))

print("xzero   "+str(xzero))
print("yzero   "+str(yzero))

print("xcentermin   "+str(xcentermin))
print("ycentermin   "+str(ycentermin))

print("xcentermax   "+str(xcentermax))
print("ycentermax   "+str(ycentermax))






for xp in xy_array[:,0]:

	xscaled=(xp-xzero)/(midx*2)
	
	print("xscaled   "+str(xscaled))
	xout.write(str(xscaled)+'\n')
	


for yp in xy_array[:,1]:

		
	yscaled=(yp-yzero)/(midy*2)
	
	print("yscaled   "+str(yscaled))
	yout.write(str(yscaled)+'\n')


xout.close()
yout.close()