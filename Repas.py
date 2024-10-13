#_____________________________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________________
#          /A\              /M\       /M\    /Z/Z/Z/Z/Z/Z/Z/     [O[O/O/O/O]O]         /222\       /222\         /1111\       
#         /AAA\           /M/\M\    /M/\M\             /Z/       [O]     O [O]       /2/  \2\    /2/  \2\      /1/  |1|
#        /A/ \A\         /M/  \M\  /M/  \M\           /Z/        [O]    O  [O]       \2\  /2/    \2\  /2/     /1/   |1|
#       /A/   \A\       /M/    \M\/M/    \M\         /Z/         [O]   O   [O] ======    /2/         /2/     /1/    |1|
#      /A/<<A>>\A\     /M/       MM       \M\       /Z/          [O]  O    [O] ======  /2/          /2/             |1|
#     /A/       \A\   /M/                  \M\     /Z/           [O] O     [O]       /2/    |2|   /2/    |2|        |1|
#    /A/         \A\ /M/                    \M\ /Z/Z/Z/Z/Z/Z/Z/  [O[O\O\O\O]O]     |2/2/2/2/2/  |2/2/2/2/2/    |1|1|1|1|1|1|
#_____________________________________________________________________________________________________________________________
#_____________________________________________________________________________________________________________________________


#IMPORTER LES DIFFERENTS MODULES
import os
import random
from tkinter import *

#---------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#CRÉATION DE LA FENÉTRE TKINTER
fen = Tk()
fen.title("REPAS DU JOUR")
fen.geometry("300x400")
fen.resizable(False,False)
#L'ICON DU L'APPLI
fen.iconbitmap('C:\\Users\\HP\\Desktop\\BUREAU\\mes projets\\python fill\\choisir plat\\image cuisinier.ico')
#LA COULEUR DE L'ARRIÉRE PLAN
fen['bg'] = '#454EFF'

#---------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#CRÉATION DE L'IMAGE DU CUISINIER
canvas = Canvas(width=80,height=80,bg='#454EFF')
my_image = PhotoImage(file='C:\\Users\\HP\\Desktop\\BUREAU\\mes projets\\python fill\\choisir plat\\image cuisinier100x100.png')
canvas.create_image(40,40,image=my_image)
canvas.pack(pady=2)
#image_label = Label(fen,image=my_image).place(x=0,y=0,relwidth=1,relheight=1)

#-----------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#LA VARIABLE message QUI VA CONTENIR LES DIFFÉRENTS PLATS
message = StringVar()

#------------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#CREATION DE LA FONCTION QUI S'EXECUTE QUAND ON CLICK SUR LE BOUTTON 
def choisir_repas():
    #ON VERIFIE SI LE FICHIER TEXT EXISTE AVANT DE L'OUVRIR
    if os.path.exists('C:\\Users\HP\\Desktop\\BUREAU\\mes projets\\python fill\\choisir plat\\repas.txt'):
        #OUVERTURE DU FICHIER TEXT COMME VARIABLE QU'ON VAS AFFECTER Á file
        with open("C:\\Users\\HP\\Desktop\\BUREAU\\mes projets\\python fill\\choisir plat\\repas.txt","r+")as file:
            #ON AFFECTE Á repas LA LECTURE SUR PLUSIEURS LIGNES DU FICHIER TXT
            repas = file.readlines()
            #dejeuner PREND DE MANIERE ALÉATOIRE UN DES PLATS DE repas
            dejeuner = random.choice(repas)
            #message  VA PRENDRE dejeuner COMME ENTRER
            message.set(dejeuner)
            #ON FERME LE FICHIER TXT POUR MONTRER QUE  LA LECTURE EST TERMINER
            file.close()
    else:
        #SI L'ORDINATEUR NE TROUVE PAS LE FICHIER TEXT IL RENVOI message
        message.set("LE DOCUMENT N'EXISTE PAS!!")

#------------------------------------------------------------------------------------------------------
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#TEXT DE PRESENTATION  DE L'APPLI
presentation = Label(fen,text='Bienvenu dans ce programe\nqui vous permet de choisir\nvotre REPAS du jour',
                    fg='white',
                    bg ='#454EFF',
                    font=('helvatica',11,'bold')
                    ).pack(pady=5)

#TEXT POUR DIRE COMMENT UTILISER L'APPLI
instruction = Label(fen,text='Clicker sur le boutton pour\ngénérer des plats',
                    fg='white',
                    bg = '#454EFF',
                    font=('arial',10,'bold')).pack()

# UN ESPACE DE TEXTINPUT EN READONLY (LECTURE SEULE) POUR AFFICHER LES DIFFÉRENTS PLATS
entry = Entry(fen,
            font=('courrier',12,'bold'),
            fg='black',
            textvariable=message,
            width=30,
            justify=CENTER,
            state='readonly',
            highlightbackground='red',
            highlightthickness=1).pack(pady=20,ipady=10)

#BOUTTON POUR LA GÉNERATION DE PLATS
boutton = Button(fen,text='Générer',
                bg='red',
                fg='white',
                font=('helvetica',12,'bold'),
                height=1,
                width=14,
                borderwidth=0,
                command= choisir_repas).pack(ipady=5)

# MA TOUCHE PERSONNELLE
copyright = Label(fen,text='Copyright © 2024 NDIAW_NDIAYE ',
                    fg='white',
                    bg = '#454EFF',
                    font=('arial',8,'bold')).pack(pady=30)

#LA BOUCLE QUI FAIT QUE LA FENETRE NE SE FERME PAS AUSSITOT APRES SON OUVERTURE
fen.mainloop()