from tkinter import *
from tkinter import ttk
import tkinter
from check import Check



def calculate(temprature,feed_rate,pressure,components,components1,components2,components3,components4,components5,z1,z2,z3,z4,z5):
	c1 = Check(temprature.get(),feed_rate.get(),pressure.get(),components.get(),components1.get(),components2.get(),components3.get(),components4.get(),components5.get(),z1.get(),z2.get(),z3.get(),z4.get(),z5.get())
	a=c1.final_answer()
	for keys,values in a.items():
		text1.insert(END,str(keys)+':'+str(values)+"\n")

root =Tk()
root.title("Quality Calculator")
root.geometry("750x500")

	#VARIABLES
temp_var = DoubleVar()
feed_var = DoubleVar()
pressure_var = DoubleVar()
component_var = IntVar()
z1_var = DoubleVar()
z2_var = DoubleVar()
z3_var = DoubleVar()
z4_var = DoubleVar()
z5_var = DoubleVar()


	#FRAMES
frame1 = Frame(root)
frame1.pack(side=TOP)

	#LABELS AND ENTRY BOX TO ENTER THE DATA

label1 = Label(frame1,text="FEED QUALITY CALCULATOR",font=("Times 15 bold")).pack()

temprature = Label(root,text="Temperature(in oC):",font="Times 12 bold")
temprature.place(x=5,y=100)

entry1 =Entry(root,textvariable=temp_var)
entry1.place(x=160,y=103)

feed_rate = Label(root,text="Feed Rate(in kmol/hr):",font="Times 12 bold")
feed_rate.place(x=5,y=140)

entry2 =Entry(root,textvariable=feed_var)
entry2.place(x=160,y=140)

pressure = Label(root,text="Pressure(in mmHg):",font="Times 12 bold")
pressure.place(x=5,y=177)

entry3 =Entry(root,textvariable=pressure_var)
entry3.place(x=160,y=177)

components = Label(root,text="Components:",font="Times 12 bold")
components.place(x=5,y=214)

entry4 =Entry(root,textvariable=component_var)
entry4.place(x=160,y=214)

	#DROPDOWN LIST FOR PROVIDING COMPONENTS

ttk.Label(root, text = "COMPONENT1:",
         font = ("Times New Roman", 10)).place(x=300,y=100)

components1 =ttk.Combobox(root, width = 27)

components1['values'] = ('methanol','ethanol','1-propanol','2-propanol','1-butanol',
							'2-butanol','1-octanol','ethylene glycol','methane','ethane','propane','n-butane','n-pentane',
							'n-hexane','hexane','n-heptane','heptane','n-octane','n-nonane','n-decane','decane',
							'cyclohexane','methylcyclohexane','isopentane','toluene','benzene','m-xylene',
							'o-xylene','p-xylene','acetone','acrolein','ethyl acetate','1,4-dioxane','2-butanone',
							'3-pentanone','water','acetonitrile','Triethylamine','acetic acid',
							'chloroform','dichloromethane','tetrachloromethane','1,2-dichloroethane',
							'Benzyl chloride','nitroethane','Biphenyl','Naphthalene',)

components1.place(x=400 , y=100)
components1.current()

ttk.Label(root, text = "COMPONENT2:",
          font = ("Times New Roman", 10)).place(x=300,y=130)

components2 =ttk.Combobox(root, width = 27)

components2['values'] = ('methanol','ethanol','1-propanol','2-propanol','1-butanol',
							'2-butanol','1-octanol','ethylene glycol','methane','ethane','propane','n-butane','n-pentane',
							'n-hexane','hexane','n-heptane','heptane','n-octane','n-nonane','n-decane','decane',
							'cyclohexane','methylcyclohexane','isopentane','toluene','benzene','m-xylene',
							'o-xylene','p-xylene','acetone','acrolein','ethyl acetate','1,4-dioxane','2-butanone',
							'3-pentanone','water','acetonitrile','Triethylamine','acetic acid',
							'chloroform','dichloromethane','tetrachloromethane','1,2-dichloroethane',
							'Benzyl chloride','nitroethane','Biphenyl','Naphthalene',)

components2.place(x=400 , y=130)
components2.current()

ttk.Label(root, text = "COMPONENT3:",
         font = ("Times New Roman", 10)).place(x=300,y=160)

components3 =ttk.Combobox(root, width = 27)

components3['values'] = ('methanol','ethanol','1-propanol','2-propanol','1-butanol',
							'2-butanol','1-octanol','ethylene glycol','methane','ethane','propane','n-butane','n-pentane',
							'n-hexane','hexane','n-heptane','heptane','n-octane','n-nonane','n-decane','decane',
							'cyclohexane','methylcyclohexane','isopentane','toluene','benzene','m-xylene',
							'o-xylene','p-xylene','acetone','acrolein','ethyl acetate','1,4-dioxane','2-butanone',
							'3-pentanone','water','acetonitrile','Triethylamine','acetic acid',
							'chloroform','dichloromethane','tetrachloromethane','1,2-dichloroethane',
							'Benzyl chloride','nitroethane','Biphenyl','Naphthalene',)

components3.place(x=400 , y=160)
components3.current()

ttk.Label(root, text = "COMPONENT4:",
          font = ("Times New Roman", 10)).place(x=300,y=190)

components4 =ttk.Combobox(root, width = 27)

components4['values'] = ('methanol','ethanol','1-propanol','2-propanol','1-butanol',
							'2-butanol','1-octanol','ethylene glycol','methane','ethane','propane','n-butane','n-pentane',
							'n-hexane','hexane','n-heptane','heptane','n-octane','n-nonane','n-decane','decane',
							'cyclohexane','methylcyclohexane','isopentane','toluene','benzene','m-xylene',
							'o-xylene','p-xylene','acetone','acrolein','ethyl acetate','1,4-dioxane','2-butanone',
							'3-pentanone','water','acetonitrile','Triethylamine','acetic acid',
							'chloroform','dichloromethane','tetrachloromethane','1,2-dichloroethane',
							'Benzyl chloride','nitroethane','Biphenyl','Naphthalene',)

components4.place(x=400 , y=190)
components4.current()

ttk.Label(root, text = "COMPONENT5:",
          font = ("Times New Roman", 10)).place(x=300,y=220)

components5=ttk.Combobox(root, width = 27)

components5['values'] = ('methanol','ethanol','1-propanol','2-propanol','1-butanol',
							'2-butanol','1-octanol','ethylene glycol','methane','ethane','propane','n-butane','n-pentane',
							'n-hexane','hexane','n-heptane','heptane','n-octane','n-nonane','n-decane','decane',
							'cyclohexane','methylcyclohexane','isopentane','toluene','benzene','m-xylene',
							'o-xylene','p-xylene','acetone','acrolein','ethyl acetate','1,4-dioxane','2-butanone',
							'3-pentanone','water','acetonitrile','Triethylamine','acetic acid',
							'chloroform','dichloromethane','tetrachloromethane','1,2-dichloroethane',
							'Benzyl chloride','nitroethane','Biphenyl','Naphthalene',)

components5.place(x=400 , y=220)
components5.current()

	#ENTRY FOR VALUE OF Z
z1 = Entry(root,textvariable=z1_var)
z1.place(x=600,y=100)

z2 = Entry(root,textvariable=z2_var)
z2.place(x=600,y=130)

z3 = Entry(root,textvariable=z3_var)
z3.place(x=600,y=160)

z4 = Entry(root,textvariable=z4_var)
z4.place(x=600,y=190)

z5 = Entry(root,textvariable=z5_var)
z5.place(x=600,y=220)

	#BUTTON FOR CALCULATING AND SENDING DATA BACK AND FORTH THE CLASS AND DEFINED FUNCTION
button1 = Button(root,text="CALCULATE",padx=10,command = lambda:calculate(entry1,entry2,entry3,entry4,components1,components2
									,components3,components4,components5,z1,z2,z3,z4,z5) )
button1.place(x=120,y=250)

	#TEXTAREA
text1 = Text(root,height=11,width=87)
text1.place(x=20,y=300)
	#CONTINOUS UPDATION
root.mainloop()

