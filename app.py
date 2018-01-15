# Interfaz grafica Brazo robotico
# Importando modulos
from tkinter import *
import serial
import struct

main = Tk()
main.title('Brazo robotico')
main.geometry('500x300');
#ser = serial.Serial('COM6') # Puerto de wemos D1

# Valores predeterminados
servoBase = 90
servoHombro = 175
servoCodo = 10
servoMuneca = 90
servoManita = 90
# Reset

def reset():
	servoBase = 90
	base.set(servoBase)
	servoHombro = 175
	hombro.set(servoHombro)
	servoCodo = 1
	codo.set(servoCodo)
	servoMuneca = 90
	muneca.set(servoMuneca)
	servoManita = 1
	manita.set(servoManita)
	b = str.encode('r')
	ser.write(b)


def cambiarValorBase(valor, valorBase):
	if int(valor) > int(valorBase):
		global servoBase
		servoBase=valor
		base.set(valor)
		b = str.encode('a')
		ser.write(b) # positivo
	elif int(valor) < int(valorBase):
		servoBase=valor
		base.set(valor)
		b = str.encode('b')
		ser.write(b) # negativo

def cambiarValorHombro(valor, valorHombro):
	if int(valor) > int(valorHombro):
		global servoHombro
		servoHombro=valor
		hombro.set(valor)
		b = str.encode('c')
		ser.write(b) # positivo
	elif int(valor) < int(valorHombro):
		servoHombro=valor
		hombro.set(valor)
		b = str.encode('d')
		ser.write(b) # negativo

def cambiarValorCodo(valor, valorCodo):
	if int(valor) > int(valorCodo):
		global servoCodo
		servoCodo=valor
		codo.set(valor)
		b = str.encode('e')
		ser.write(b) # positivo
	elif int(valor) < int(valorCodo):
		servoCodo=valor
		codo.set(valor)
		b = str.encode('f')
		ser.write(b) # negativo


def cambiarValorMuneca(valor, valorMuneca):
	if int(valor) > int(valorMuneca):
		global servoMuneca
		servoMuneca=valor
		muneca.set(valor)
		b = str.encode('g')
		ser.write(b) # positivo
	elif int(valor) < int(valorMuneca):
		servoMuneca=valor
		muneca.set(valor)
		b = str.encode('h')
		ser.write(b) # negativo


def cambiarValorManita(valor, valorManita):
	if int(valor) > int(valorManita):
		global servoManita
		servoManita=valor
		manita.set(valor)
		b = str.encode('i')
		ser.write(b) # positivo
	elif int(valor) < int(valorManita):
		servoManita=valor
		manita.set(valor)
		b = str.encode('j')
		ser.write(b) # negativo

"""def fijar1():

	entBase1.config(state=NORMAL)
	entHombro1.config(state=NORMAL)
	entCodo1.config(state=NORMAL)
	entMuneca1.config(state=NORMAL)
	entMano1.config(state=NORMAL)

	entBase1.delete(0,END)
	entHombro1.delete(0,END)
	entCodo1.delete(0,END)
	entMuneca1.delete(0,END)
	entMano1.delete(0,END)

	entBase1.insert(0,servoBase)
	entHombro1.insert(0,servoHombro)
	entCodo1.insert(0,servoCodo)
	entMuneca1.insert(0,servoMuneca)
	entMano1.insert(0,servoManita)

	entBase1.config(state=DISABLED)
	entHombro1.config(state=DISABLED)
	entCodo1.config(state=DISABLED)
	entMuneca1.config(state=DISABLED)
	entMano1.config(state=DISABLED)

def fijar2():
	entBase2.config(state=NORMAL)
	entHombro2.config(state=NORMAL)
	entCodo2.config(state=NORMAL)
	entMuneca2.config(state=NORMAL)
	entMano2.config(state=NORMAL)

	entBase2.delete(0,END)
	entHombro2.delete(0,END)
	entCodo2.delete(0,END)
	entMuneca2.delete(0,END)
	entMano2.delete(0,END)

	entBase2.insert(0,servoBase)
	entHombro2.insert(0,servoHombro)
	entCodo2.insert(0,servoCodo)
	entMuneca2.insert(0,servoMuneca)
	entMano2.insert(0,servoManita)

	entBase2.config(state=DISABLED)
	entHombro2.config(state=DISABLED)
	entCodo2.config(state=DISABLED)
	entMuneca2.config(state=DISABLED)
	entMano2.config(state=DISABLED)


def iniciarAutomatico():
	ba1 = int(entBase1.get())
	ho1 = int(entHombro1.get())
	co1 = int(entCodo1.get())
	mu1 = int(entMuneca1.get())
	ma1 = int(entMano1.get())

	ba2 = int(entBase2.get())
	ho2 = int(entHombro2.get())
	co2 = int(entCodo2.get())
	mu2 = int(entMuneca2.get())
	ma2 = int(entMano2.get())

	vcs = int(entVeces.get())
	b = str.encode('u')
	ser.write(struct.pack('>sBBBBBBBBBBB',b,ba1,ho1,co1,mu1,ma1,ba2,ho2,co2,mu2,ma2,vcs))"""
# Interfaz 

lbltitulo = Label(main, text="Control de brazo robótico", font=("Arial",14,"bold")).place(x=130,y=0)

lblMan = Label(main, text="Manual", font=("Arial",11,"bold")).place(x=50,y=30)

lblBase = Label(main, text="Base:").place(x=20,y=67)
base = Scale(main, from_=1, to=180, resolution=5, showvalue=0, length=400, orient=HORIZONTAL, command=lambda value: cambiarValorBase(value,servoBase))
base.set(servoBase)
base.place(x=75,y=70)

lblHombro = Label(main, text="Hombro:").place(x=20,y=118)
hombro = Scale(main, from_=175, to=1, resolution=5, showvalue=0, length=400, orient=HORIZONTAL, command=lambda value: cambiarValorHombro(value,servoHombro))
hombro.set(servoHombro)
hombro.place(x=75,y=120)

lblCodo = Label(main, text="Codo:").place(x=20,y=168)
codo = Scale(main, from_=10, to=180, resolution=5, showvalue=0, length=400, orient=HORIZONTAL, command=lambda value: cambiarValorCodo(value,servoCodo))
codo.set(servoCodo)
codo.place(x=75,y=170)

lblManita = Label(main, text="Mano")
lblManita.place(x=20,y=268)
manita = Scale(main, from_=90, to=135, resolution=5, showvalue=0, length=400, orient=HORIZONTAL, command=lambda value: cambiarValorManita(value,servoManita))
manita.set(servoManita)
manita.place(x=75,y=270)

lblMuneca = Label(main, text="Muñeca:").place(x=20,y=218)
muneca = Scale(main, from_=1, to=180, resolution=5, showvalue=0, length=400, orient=HORIZONTAL, command=lambda value: cambiarValorMuneca(value,servoMuneca))
muneca.set(servoMuneca)
muneca.place(x=75,y=220)

"""lblAuto = Label(main, text="Automático", font=("Arial",11,"bold")).place(x=50,y=320)

lblAutoBase = Label(main, text="Base")
lblAutoBase.place(x=110,y=350)

lblAutoHombro = Label(main, text="Hombro")
lblAutoHombro.place(x=165,y=350)

lblAutoCodo = Label(main, text="Codo")
lblAutoCodo.place(x=230,y=350)

lblAutoMuneca = Label(main, text="Muñeca")
lblAutoMuneca.place(x=285,y=350)

lblAutoMano = Label(main, text="Mano")
lblAutoMano.place(x=350,y=350)



lblPos1 = Label(main, text="Pocisión 1:")
lblPos1.place(x=20,y=380)


entBase1 = Entry(main, width=3, state=DISABLED)
entBase1.place(x=120,y=381)

entHombro1 = Entry(main, width=3, state=DISABLED)
entHombro1.place(x=180,y=381)

entCodo1 = Entry(main, width=3, state=DISABLED)
entCodo1.place(x=240,y=381)

entMuneca1 = Entry(main, width=3, state=DISABLED)
entMuneca1.place(x=300,y=381)

entMano1 = Entry(main, width=3, state=DISABLED)
entMano1.place(x=360,y=381)

btnFijar1 = Button(main, text="Fijar", command=fijar1)
btnFijar1.place(x=420,y=376)


lblPos2 = Label(main, text="Pocisión 2:")
lblPos2.place(x=20,y=410)

entBase2 = Entry(main, width=3, state=DISABLED)
entBase2.place(x=120,y=411)

entHombro2 = Entry(main, width=3, state=DISABLED)
entHombro2.place(x=180,y=411)

entCodo2 = Entry(main, width=3, state=DISABLED)
entCodo2.place(x=240,y=411)

entMuneca2 = Entry(main, width=3, state=DISABLED)
entMuneca2.place(x=300,y=411)

entMano2 = Entry(main, width=3, state=DISABLED)
entMano2.place(x=360,y=411)

btnFijar2 = Button(main, text="Fijar", command=fijar2)
btnFijar2.place(x=420,y=406)


lblNoVeces = Label(main, text="# de veces:")
lblNoVeces.place(x=20,y=440)

entVeces = Entry(main, width=3)
entVeces.place(x=120,y=441)

btnIniciarAuto = Button(main, text="Iniciar", command=iniciarAutomatico)
btnIniciarAuto.place(x=240,y=460)"""

reset = Button(main, text="Reset", command=reset)
reset.place(x=400,y=30)

main.mainloop()