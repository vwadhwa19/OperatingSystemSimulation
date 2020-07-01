#Varun
#Operating System Simulation

import viz
import vizact
import vizdlg
import vizinfo
import viztask
import string
import math
import time


TERMINATED_THEME=viz.Theme()
TERMINATED_THEME.backColor=viz.YELLOW_ORANGE
TERMINATED_THEME.borderColor=viz.RED
TERMINATED_THEME.textColor=viz.BLUE
TERMINATED_THEME.inactiveTextColor=viz.BLUE

RUNNING_THEME=viz.Theme()
RUNNING_THEME.backColor=viz.GREEN
RUNNING_THEME.borderColor=viz.RED
RUNNING_THEME.textColor=viz.BLACK
RUNNING_THEME.inactiveTextColor=viz.BLUE

viz.go(viz.FULLSCREEN)

bigform=vizinfo.InfoPanel()
viz.clearcolor(viz.SLATE)
#create main RAM FORM
RAMFORM=vizinfo.InfoPanel(text='',title="PROCESS QUEUE(RAM)",align=viz.ALIGN_LEFT_TOP,icon=False,window=viz.MainWindow)
RAMFORM.alpha(0)
RAMFORM.getTitleBar().alpha(1)

#GUI QUEUE OF PROCESSES
tenprocessesbox=vizdlg.Panel(layout=vizdlg.LAYOUT_HORZ_TOP,margin=False,border=False,spacing=1)
titlles=vizdlg.Panel(layout=vizdlg.LAYOUT_VERT_RIGHT,fontSize=18,spacing=11,margin=None,border=False)
titlles.addItem(viz.addText("         "))
titlles.addItem(viz.addText("         "))

titlles.addItem(viz.addText("P.STATE"))
titlles.addItem(viz.addText("PC"))
titlles.addItem(viz.addText("CPU REG"))
titlles.addItem(viz.addText("M.M.I"))
titlles.addItem(viz.addText("CPU.SCHDL"))
titlles.addItem(viz.addText("TIME SLICE"))
tenprocessesbox.addItem(titlles)
PCB_GUI=[]

for a in range (0,10):	
	PCB_GUI.append(vizdlg.Panel(layout=vizdlg.LAYOUT_VERT_CENTER,margin=None,border=False))
	tenprocessesbox.addItem(PCB_GUI[a])
RAMFORM.addItem(tenprocessesbox)
bigform.addItem(RAMFORM)





#PCB ITEMS GUIs
GRAPHIC_RAM=[[0 for x in range(6)] for y in range(10)] 
MEMLOCS=['F0184BF1','F01A4BF2','F0111BF3','FFFF04F4','F0184BF5','F01A4BF6','F0111BF7','FFFF04E8','F0111B00','BFFF0401']
SCHEDUL_MEM=['B0184BF1','B01A4BF2','B0111BF3','BFFF04F4','B0184BF5','B01A4BF6','B0111BF7','BFFF04E8','B0111B00','BFFF0401']
CPUREG=['R0','R1','R2','R3','R4','R5','R6','R7','R8','R9']

for a in range(0,10):
	PCB_GUI[a].addItem(viz.addText("PCB "+str(a)))
	PCB_GUI[a].color(viz.AZURE)
	for b in range(0,6):
		GRAPHIC_RAM[a][b]=viz.addTextbox()
		GRAPHIC_RAM[a][b].setScale(0.9,1)
		
		PCB_GUI[a].addItem(GRAPHIC_RAM[a][b])
		
	GRAPHIC_RAM[a][0].message('READY')
	GRAPHIC_RAM[a][1].message('00000000')
	
	GRAPHIC_RAM[a][2].message(str(CPUREG[a]))
	GRAPHIC_RAM[a][3].message(str(viz.random.choice(MEMLOCS)))
	GRAPHIC_RAM[a][4].message(str(viz.random.choice(SCHEDUL_MEM)))
	GRAPHIC_RAM[a][5].message(str(viz.random.randrange(2,10)))
	


	#CREATE LIST OF PROCESSES
#=============================================================================
##Process1
ADD2NUMBERS="""
out('RUNNING SUM')
p=5
out("p= "+str(p))
q=8
out("q= "+str(q))
z=p+q
out(' p + q is ' +str(z))
out("End of program")
#
"""
p=0
q=0
z=0


PRG1=ADD2NUMBERS.splitlines(False)




##Process2
MULT2NUMBERS="""
out('RUNNING MULT.')
a=5
b=8
c=a*b
out(' a * b is ' +str(c))
out("End of program")
#
"""
a=0
b=0
c=0


PRG2=MULT2NUMBERS.splitlines(False)

#Process3
DIV2NUMBERS="""
out('RUNNING DIV')
k=20
y=5
m =k / y
out(' k / y is ' +str(m))
out("End of program")
#
"""
k=0
y=0
m=0
PRG3=DIV2NUMBERS.splitlines(False)

XPOWY="""
out('RUNNING X ^ Y')
d=5
e=5
g =pow(d,e)
out('d ^ e is ' +str(g))
out("End of program")
#
"""
d=0
e=0
g=0
PRG4=XPOWY.splitlines(False)


INS="""
for a in (0,5):
out("n= "+str(n))
out("n*2= "+str(n*2))
out(" n/2= "+str(n/2))
out("Random Number = "
str(viz.random.randrange(0,100)))

"""
FOR_LOOP="""
out('RUNNING LOOP')
out('Loop from 0 to 5')
for loop in range(0,5):	[[viz.waitTime(1)],[out("n= "+str(loop))],[out("Random Number = "+str(viz.random.randrange(0,100)))]]
out("End of program")
#
"""
loop=0
PRG5=FOR_LOOP.splitlines(False)

INPUTPRG="""
out('RUNNING INPUT.')
v=viz.input("Number")
out("The value is "+str(v))
i=int(v)*5
out("Number x 5= "+str(i))
s=v/2
out("Number /2= "+str(s))
out("End of program")
#
"""
v=0
i=0
s=0

PRG6=INPUTPRG.splitlines(False)


AVERAGE="""
out('RUNNING AVERAGE.')
n1=20
out(str(n1))
n2=45
out(str(n2))
n3=50
out(str(n3))
n4=12
out(str(n4))
avgn=(n1+n2+n3+n4)/4
out("AVG = "+str(avgn))
out("End of program")
#
"""
n1=0
n2=0
n3=0
n4=0
avgn=0

PRG7=AVERAGE.splitlines(False)

print PRG7

LARGEST="""
out('RUNNING LARGEST')
h1=20
out(str(h1))
h2=45
out(str(h2))
if h1>h2:	h3=h1
if h1<h2:	h3=h2
out("Largest= "+str(h3))
out("End of program")
#
"""
h1=0
h2=0
h3=0
PRG8=LARGEST.splitlines(False)

EVEN="""
out('RUNNING EVEN.')
num=viz.input("Number")
out("Number is "+str(num))
if num%2==0:	out(" Is even")
if num%2<>0:	out(" Is Odd")
out("End of program")
#
"""
num=0

PRG9=EVEN.splitlines(False)

SQRT="""
out('RUNNING SQRT.')
sq=25
out("Number  "+str(sq))
out("The SQRT is "+str(math.sqrt(sq)))
out("End of program")
#
"""
sq=0
PRG10=SQRT.splitlines(False)


#ARRAY THAT CONTAINS ALL THE PROGRAMS
PROGRAMSQUEUE=[PRG1,PRG2,PRG3,PRG4,PRG5,PRG6,PRG7,PRG8,PRG9,PRG10]


		
#SCRIPTS GUIs
PCBSCRIPT=vizinfo.InfoPanel(text='',title="PROCESSES SCRIPTS",align=viz.ALIGN_CENTER_BOTTOM,icon=False,window=viz.MainWindow)
tenPCBsbox=vizdlg.Panel(layout=vizdlg.LAYOUT_HORZ_TOP,margin=False,border=False,spacing=1)
PCB_GUI=[]	
for build in range (0,10):	
	PCB_GUI.append(vizdlg.Panel(layout=vizdlg.LAYOUT_VERT_CENTER,margin=None,border=False))
	tenPCBsbox.addItem(PCB_GUI[build])
PCBSCRIPT.addItem(tenPCBsbox)	

	
GRAPHIC_CODELINES=[[0 for x in range(6)] for y in range(10)] 
for build in range(0,10):
	PCB_GUI[build].addItem(viz.addText("SCRIPT "+str(build)))
	PCB_GUI[build].color(viz.SKYBLUE)
	
	
PCB_GUI[0].addItem(viz.addText(ADD2NUMBERS))
PCB_GUI[1].addItem(viz.addText(MULT2NUMBERS))
PCB_GUI[2].addItem(viz.addText(DIV2NUMBERS))
PCB_GUI[3].addItem(viz.addText(XPOWY))
PCB_GUI[4].addItem(viz.addText(INS))
PCB_GUI[5].addItem(viz.addText(INPUTPRG))
PCB_GUI[6].addItem(viz.addText(AVERAGE))
PCB_GUI[7].addItem(viz.addText(LARGEST))
PCB_GUI[8].addItem(viz.addText(EVEN))
PCB_GUI[9].addItem(viz.addText(SQRT))




PID=0#PROCESS id
TIMESLICE=5#tIME SLICE
ACTUALTIME=0

PC=0

END=False	


procspace=vizdlg.Panel(layout=vizdlg.LAYOUT_HORZ_CENTER,align=viz.ALIGN_CENTER_CENTER,border=False)
START=procspace.addItem(viz.addButtonLabel("    Start OS     "))	
START.fontSize(25)

def RunProgram(prg,timeslice,pc):
	global PGCOMPLETE
	global END
#	global output
#	listitems=output.getItems()
#		#clear output
#	for i in listitems:
#		output.removeItem(i,True)
#-------------------------------
	oldpc=pc
	global PC
	global PID
	
	proc.visible(True)
		
	ACTUALTIME=0
	global p
	global q
	global z
	global sq
	global num
	global h1
	global h2
	global h3
	global n1
	global n2
	global n3
	global n4
	global avgn
	global v
	global i
	global s
	global loop
	global k
	global y
	global m
	global d
	global e
	global g


	#PRG2=MULT2NUMBERS.splitlines(False)



	out("*******************************")
	while(ACTUALTIME<timeslice):
		exec prg[pc]
		PID.message("RUNNING")
		
		PC.message(str(pc))
	
		if str(prg[pc])=="#":
			PID.message("TERMINATED")
			viz.setTheme(TERMINATED_THEME,True,PID)
			ACTUALTIME=timeslice
			PGCOMPLETE=PGCOMPLETE+1
			if PGCOMPLETE==10: #all programs have been completed
				END=True
				viz.message("All programs have been completed successfuly!")
				
		else:
			viz.setTheme(RUNNING_THEME,True,PID)
			pc=pc+1
			ACTUALTIME=ACTUALTIME+1
		
PGCOMPLETE=0#how many programs have been completed	
			
			
def getPCB():
	
	global END
			#this would be a for-ever loop
	while END==False:	
		global PC
		PC=0
		global PID
		PID=0
		for r in range(0, 10):
			PID=GRAPHIC_RAM[r][0]
			PC=GRAPHIC_RAM[r][1]
			if GRAPHIC_RAM[r][0].get()!="TERMINATED":
				RunProgram(PROGRAMSQUEUE[r],int(GRAPHIC_RAM[r][5].get()),int(GRAPHIC_RAM[r][1].get()))
				yield time.sleep(1)
vizact.onbuttondown(START,viztask.schedule,getPCB)

for build in range(0,5):
	procspace.addItem(viz.addText("                  "))
	procspace.alpha(0)
	
proc=procspace.addItem(viz.add('Processor.osgb'))
proc.visible(False)
#==============================================================

procspace.addItem(viz.addText('                                                                                '))
#output=vizdlg.Panel(layout=vizdlg.ALIGN_LEFT_TOP,border=False,align=viz.ALIGN_LEFT_TOP,fontSize=20)
output=vizinfo.InfoPanel(align=viz.ALIGN_RIGHT_CENTER,fontSize=20)
output.drawOrder(2)
output.setLineSpacing(10)
output.addItem(viz.addText("          OUTPUT                           "))
output.addItem(viz.addText(" ----------------------------------------"))
#output.alpha(0.5)

#procspace.addItem(output)
procspace.drawOrder(8)
bigform.addItem(procspace)
bigform.addItem(PCBSCRIPT)


#OUTPUT INTERFACE
def out(n):
	global output
	tx=viz.addText(n)
	tx.fontSize(20)
	output.addItem(tx)	

