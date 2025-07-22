import tkinter as tk 
from PIL import Image, ImageTk #image library
import random
import io #input and output tools
import json # a big dictionary
import urllib.request

random.seed(57)



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
    print(moveNames)


    # print(name)
    #return - has function give you data after it runs
    return{
        "name":name, 
        'image': ImageTk.PhotoImage(image), #convert to Tkinder image format
        'moves': moveNames
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

def Showmove(p1):
    #p1 moves
    moveButton1 = []
    MoveLen1 = len(p1['moves'])
    for i in range(MoveLen1):
        BTN = tk.Button(p1_frame, text=p1['moves'][i], width= 10, height= 2, fg="black", bg="grey", font=("Arial",15))
        BTN.pack(pady=4)
        moveButton1.append(BTN)


#Labels
TitleLabel = tk.Label(screen, text="Pokemon Battle by David", font=("Arial", 30), fg="White", bg="green")
#grid, place, pack
TitleLabel.place(x = 100, y = 50)

#vs label
VsLabel = tk.Label(screen, text= "VS", font=("Arial",20), fg="ORANGE", bg="Green", anchor="w")
VsLabel.place(relx= 0.45, rely=0.5)

Showmove(p1)#Displays both users moves

#keep at bottom 
screen.mainloop()#refreshes screen infinite

