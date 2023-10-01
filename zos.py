import socket
import tkinter as tk

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'  
port = 11704   
try:    
    client_socket.connect((host, port))
except Exception as e:
    tk.messagebox(f'Server Offline or Unable To Connect :{e}')

root = tk.Tk()
root.title('zOS-Login')
root.geometry

def main():
    print('msioflgha')

def login():
    idTry = idEntry.get()
    passTry = passwordEntry.get()
    client_socket.send(f'l:{idTry}:{passTry}'.encode('utf-8'))
    conf = client_socket.recv(1024).decode('utf-8')
    if conf == 'true':
        main()
    elif conf == 'false1':
        errorText.config(text='Incorect Password',foreground="red")
    elif conf == 'false2':
        errorText.config(text='Account Not Found',foreground="red")
    else:
        errorText.config(text='We were unable to Login to zOS. We don\'t know why?')


loginTitle = tk.Label(root, text='zOS - Login',font=('Arial',26))
idLabel = tk.Label(root, text='Identifier :')
idEntry = tk.Entry(root)
passwordLabel = tk.Label(root, text='Password :')
passwordEntry = tk.Entry(root ,show="*")
loginButton = tk.Button(root, text='Login',command=login)
errorText = tk.Label(root)

loginTitle.pack()
idLabel.pack()
idEntry.pack()
passwordLabel.pack()
passwordEntry.pack()
loginButton.pack()
errorText.pack()

root.mainloop()

'''
client_socket.send(message.encode('utf-8'))
esponse = client_socket.recv(1024)
print("Server:", response.decode('utf-8'))
client_socket.close()
'''