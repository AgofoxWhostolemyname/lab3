import tkinter as tk
import random
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Key Generator")
window.geometry("600x600")

bg_image = ImageTk.PhotoImage(Image.open("PoEBestgame.jpg"))
bg_label = tk.Label(window, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

key_var = tk.StringVar()
key_entry = tk.Entry(window, textvariable=key_var, width=25, justify='center')
key_entry.pack(pady=100)

def generate_key():
    start_char = random.randint(0, 25)
    end_char = random.randint(start_char, 25)
    
    block1 = f"{start_char + 1:02d}"
    block3 = f"{end_char + 1:02d}"
    
    block2 = ''.join(chr(random.randint(ord('A') + start_char, ord('A') + end_char)) for _ in range(7))
    
    key = f"{block1} {block2} {block3}"
    key_var.set(key)

generate_btn = tk.Button(window, text="Сгенерировать ключ", command=generate_key)
generate_btn.pack()

window.mainloop()