#Programa para apagar la computadora con buen entorno visual #
from tkinter import *
from tkinter import messagebox
import subprocess


############################################################## Root ###########################################################################
root=Tk()
root.title("Winshut")
root.resizable(0,0)
root.iconbitmap("Ws.ico") 
##root.config(bd=35)


tiempo=StringVar()
comp=StringVar()
############################################################# Frame ###########################################################################
Frame=Frame(root,width=600,height=400)
Frame.pack()
Frame.config(bg="white")#color


############################################################ Funciones #########################################################################

def Ejecutar():
   
        lel=tiempo.get()
        if lel!="":
            try:
                LOLM=int(lel)
                LOLS=60*LOLM
                messagebox.showinfo("Aviso","tu computadora se apagara en "+ str(lel) + " minutos")
                tiempo.set(' ')
                comp.set("1")
                subprocess.call("shutdown -s -t %d" %LOLS) 
            except ValueError:
             messagebox.showinfo("Aviso","Ingresa los minutos, por favor")
             tiempo.set(' ')
             comp.set("0")

        else:
            pass
            messagebox.showinfo("Aviso","Ingresa los minutos, por favor")
            tiempo.set(' ')
            comp.set("0")
         



def Cancelar():
    lel=comp.get()
    if lel=="1":
        tiempo.set(' ')
        messagebox.showinfo("Aviso","Fue cancelado el apagado automatico")
        comp.set("0")
        subprocess.call("shutdown -a" )
    else:
        tiempo.set(' ')
        messagebox.showinfo("Aviso","No se ha programado ningun apagado")

   



############################################################ LABEL ###########################################################################
Label(Frame,text="WindShut",bg="white",fg="blue",font=("Time new roman",18)).grid(row=0,column=0,padx=10,pady=10,columnspan=4)

TiempoA=Label(Frame,text="Cantidad de minutos para apagar su PC:",bg="white",fg="blue",font=("Time new roman",8),).grid(row=1,column=0,padx=10,pady=10)



########################################################### Entrys ###########################################################################
Text0=Entry(Frame,textvariable=tiempo).grid(row=1,column=1,padx=10,pady=10)





########################################################### Botones ###########################################################################

boton1=Button(Frame,text='Aceptar',command=Ejecutar).grid(row=3,column=0,padx=10,pady=10)
boton2=Button(Frame,text='Cancelar',command=Cancelar).grid(row=3,column=1,padx=10,pady=10)



#######################################################################################################################################################

root.mainloop()
