import tkinter as tk 
from PIL import Image, ImageTk #image library
import random
import io #input and output tools
import json # a big dictionary
import urllib.request
from tkinter import messagebox
import time #wait on anything time related
import os #operating system

#random.seed(57)



#Tkinter
screen = tk.Tk()#tk.Tk is screen
screen.geometry("700x700")
screen.title("Pokemon Battle By David")
screen.configure(bg="green")#bg is background 

#Making requests to fetch pokemon data from API
def get_pokemon(id_or_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{id_or_name}"
    #try except - similar to if then statement, if cant run try run except so code continues running
    try:
        with urllib.request.urlopen(url) as response:
            if response.status != 200: #api request fails
                return None
            data = json.loads(response.read().decode())#reads request and save to variable
           # print(data)
    except Exception as e:
        print(e)
    
    #Get name
    name = data["name"].title()#access a value from a dictionary with a key
    
    hp = 0
    for stat in data['stats']:
        #print(stat)
        if stat['stat']['name'] == 'hp':
            hp = stat['base_stat']
        
    #image sprite
    img_url = data['sprites']['front_default']
    image_data = urllib.request.urlopen(img_url).read() #download image
    #Pillow to resize and open image
    image = Image.open(io.BytesIO(image_data)).resize((200,200))

    #moves
    AllMoves = data['moves']
    # print(AllMoves)
    moveNames = []
    #for loop for definite/repeat
    #while = repeat until infinite
    for move in AllMoves:
        moveNames.append(move['move']['name'])
    random.shuffle(moveNames)
    if len(moveNames) >= 4:
        moveNames = moveNames[:4] #slices it to length 4
    else:
        pass
    #print(moveNames)


    # print(name)
    #return - has function give you data after it runs
    return{
        "name":name, 
        'image': ImageTk.PhotoImage(image), #convert to Tkinder image format
        'moves': moveNames,
        'hp': hp
    }

p1_num = random.randint(1,1025)
p1 = get_pokemon(p1_num)
#frame for pokemon 1 
p1_frame = tk.Frame(screen,bg="green")
p1_frame.pack(side="left", padx=50)


p1_info = tk.StringVar() #changes variable into string
p1_info.set(f"{p1['name']}")
tk.Label(p1_frame, textvariable=p1_info, bg="green", font=("Arial", 14)).pack(pady=(10))#top and bottom

image_label1 = tk.Label(p1_frame, bg="green")
image_label1.config(image=p1['image'])
image_label1.pack(padx=20)#padx = space on left and right

hpLabel = tk.Label(p1_frame, text=f"Hp: {p1['hp']}", fg= "white", bg="grey", font=("Arial", 16))
hpLabel.place (x=90, y= 50)



#p2
p2_num = random.randint(1,1025)
if p1_num == p2_num:
    p2_num = random.randint(1,1025)
p2 = get_pokemon(p2_num)
#frame for pokemon 1 
p2_frame = tk.Frame(screen,bg="green")
p2_frame.pack(side="right", padx=50)



p2_info = tk.StringVar() #changes variable into string
p2_info.set(f"{p2['name']}")
tk.Label(p2_frame, textvariable=p2_info, bg="green", font=("Arial", 14)).pack(pady=(10))#top and bottom

image_label2 = tk.Label(p2_frame, bg="green")
image_label2.config(image=p2['image'])
image_label2.pack(padx=20)

hpLabel2 = tk.Label(p2_frame, text=f"Hp: {p2['hp']}", fg= "white", bg="grey", font=("Arial", 16))
hpLabel2.place(x=90, y=50)

def Showmove(p1):
    global moveButton1
    #p1 moves
    moveButton1 = []
    MoveLen1 = len(p1['moves'])
    for i in range(MoveLen1):
        BTN = tk.Button(p1_frame, text=p1['moves'][i], width= 10, height= 2, fg="black", bg="grey", font=("Arial",15))
        BTN.pack(pady=4)
        moveButton1.append(BTN)


def Showmoves2(p2):
    #p1 moves
    global moveButton2
    moveButton2 = []
    MoveLen2 = len(p2['moves'])
    for i in range(MoveLen2):
        BTN = tk.Button(p2_frame, text=p2['moves'][i], width= 10, height= 2, fg="black", bg="grey", font=("Arial",15))
        BTN.pack(pady=4)
        moveButton2.append(BTN)

def CompAttack(attacker, defender):
    CurrMove = random.choice(attacker['moves'])
    damage = random.randint(0,40)

    message = (f"{attacker['name']} used {CurrMove} on {defender['name']} for {damage} damage")
    messagebox.showinfo("Attack", message)

# CompAttack(p2,p1)
def TurnBased(p1, p2):
    turn = 1
    if turn == 1:
        for button in moveButton1:
            button.config(state=tk.ACTIVE)
        for button in moveButton2:
            button.config(state=tk.DISABLED)
        #CompAttack(p1,p2) 
        turn = 2
        #time.sleep()
    elif turn == 2:
        for button in moveButton1:
            button.config(state=tk.DISABLED)
        CompAttack(p2,p1)
        turn = 1


#Labels
TitleLabel = tk.Label(screen, text="Pokemon Battle by David", font=("Arial", 30), fg="White", bg="green")
#grid, place, pack
TitleLabel.place(x = 120, y = 30)

#vs label
VsLabel = tk.Label(screen, text= "VS", font=("Arial",20), fg="ORANGE", bg="Green", anchor="w")
VsLabel.place(relx= 0.45, rely=0.5)

Showmove(p1)#Displays both users moves
Showmoves2(p2)

#while True:
TurnBased(p1,p2)
#keep at bottom 
screen.mainloop()#refreshes screen infinite
