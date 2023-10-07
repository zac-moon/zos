import socket
import tkinter as tk
from tkinter import messagebox

# Initialize the client socket and connection variables
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 11704

try:
    client_socket.connect((host, port))
except Exception as e:
    messagebox.showerror('Error', f'Server Offline or Unable To Connect: {e}')
    exit()

# Create the main application window
root = tk.Tk()
root.title('login | zOS')
root.geometry('1000x800')

def logout():
    root.destroy()

class App:
    # Add 'self' as the first parameter to class methods
    def runTexty(self, idTry):
        def textyLoad():
            pass

        def textySave():
            curIn = textyTextEntry.get("1.0", "end-1c")
            fileName = textyFileNameEntry.get()
            client_socket.send(f'f:save:{idTry}/{fileName}:{curIn}'.encode('utf-8'))

        texty = tk.Toplevel(root)
        texty.title('texty')
        texty.geometry('600x400')

        textyTextEntry = tk.Text(texty)
        textyTextEntry.pack(fill=tk.BOTH, expand=True) 

        button_frame = tk.Frame(texty)
        button_frame.pack(side=tk.TOP)

        textyLoadButton = tk.Button(button_frame, text='Load File', command=textyLoad)
        textySaveButton = tk.Button(button_frame, text='Save File', command=textySave)
        textyFileNameEntry = tk.Entry(button_frame)

        textyLoadButton.grid(row=0, column=0)
        textySaveButton.grid(row=0, column=1)
        textyFileNameEntry.grid(row=0, column=2)

def loadHome(idname):
    # Remove 'idTry' argument from 'App.runTexty'
    def run_texty():
        app = App()
        app.runTexty(idname)

    loginTitle.pack_forget()
    idLabel.pack_forget()
    idEntry.pack_forget()
    passwordLabel.pack_forget()
    passwordEntry.pack_forget()
    loginButton.pack_forget()
    errorText.pack_forget()

    homeLabel = tk.Label(root, text='home | zOS | ' + idname)
    textyBtn = tk.Button(root, text='texty', command=run_texty)  # Pass 'run_texty' as the command
    logoutBtn = tk.Button(root, text='Log Out', command=logout)

    homeLabel.pack()
    textyBtn.pack()
    logoutBtn.pack()

    root.title('home | zOS')

def login():
    idTry = idEntry.get()
    passTry = passwordEntry.get()
    client_socket.send(f'l:{idTry}:{passTry}'.encode('utf-8'))
    conf = client_socket.recv(1024).decode('utf-8')
    if conf == 'true':
        print('correct details')
        idEntry.delete(0, tk.END)
        passwordEntry.delete(0, tk.END)
        loadHome(idTry)
    elif conf == 'false1':
        errorText.config(text='Incorrect Password', foreground="red")
    elif conf == 'false2':
        errorText.config(text='Account Not Found', foreground="red")
    else:
        errorText.config(text='We were unable to Login to zOS. We don\'t know why?')

loginTitle = tk.Label(root, text='zOS - Login', font=('Arial', 26))
idLabel = tk.Label(root, text='Identifier:')
idEntry = tk.Entry(root)
passwordLabel = tk.Label(root, text='Password:')
passwordEntry = tk.Entry(root, show="*")
loginButton = tk.Button(root, text='Login', command=login)
errorText = tk.Label(root)

loginTitle.pack()
idLabel.pack()
idEntry.pack()
passwordLabel.pack()
passwordEntry.pack()
loginButton.pack()
errorText.pack()

root.mainloop()

# Close the socket when the application is closed
client_socket.close()


'''
client_socket.send(message.encode('utf-8'))
esponse = client_socket.recv(1024)
print("Server:", response.decode('utf-8'))
client_socket.close()
'''