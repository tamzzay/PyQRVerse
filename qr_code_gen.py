import qrcode
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Create the main window
cp = Tk()
cp.title("QR Code Generator")
cp.geometry("500x400")
cp.config(bg='#f7f7f7')

# Function to generate and save QR code
def generate():
    text = msg.get().strip()
    filename = save_name.get().strip()

    if not text or not filename:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return

    try:
        img = qrcode.make(text)
        img.save(f"{filename}.png")
        messagebox.showinfo("Success", f"QR Code saved as {filename}.png")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file: {e}")

# Function to preview the QR code
def show():
    text = msg.get().strip()
    if not text:
        messagebox.showwarning("Input Error", "Enter text or URL!")
        return

    img = qrcode.make(text)
    img.show()

    # Display the image in the interface
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    preview_label.config(image=img)
    preview_label.image = img

# Create interface components
frame = Frame(cp, bg='#f7f7f7', padx=20, pady=20)
frame.pack(expand=True)

Label(frame, text='Enter the Text or URL:', font='Arial 14', bg='#f7f7f7').grid(row=0, column=0, sticky='w', pady=5)
msg = Entry(frame, width=30, font='Arial 12')
msg.grid(row=0, column=1, pady=5)

Label(frame, text='File Name (Save As):', font='Arial 14', bg='#f7f7f7').grid(row=1, column=0, sticky='w', pady=5)
save_name = Entry(frame, width=30, font='Arial 12')
save_name.grid(row=1, column=1, pady=5)

# Buttons
Button(cp, text='Show QR Code', command=show, bd=3, width=15, bg='#4caf50', fg='white', font='Arial 12').pack(pady=5)
Button(cp, text='Save QR Code', command=generate, bd=3, width=15, bg='#2196f3', fg='white', font='Arial 12').pack(pady=5)

# Image preview label
preview_label = Label(cp, bg='#f7f7f7')
preview_label.pack(pady=10)

cp.mainloop()
