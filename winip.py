import requests
import tkinter as tk
import win32api
#vahid.zahani@gmail.com
#https://github.com/vahidzahani

class IpApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('')
        self.overrideredirect(True)
        self.geometry('150x80')
        self.configure(bg='white')
        
        self.quit_button = tk.Button(self, text="x", command=self.quit, width=2, height=2, bg="red", fg="white")
        self.quit_button.place(x=0, y=0, anchor='nw')
       

        self.country_lbl = tk.Label(self, text='', font=('tahoma', 14), bg='white', fg='green')
        self.country_lbl.pack()

        self.ip_lbl = tk.Label(self, text='', font=('tahoma', 12), bg='white', fg='blue')
        self.ip_lbl.pack(pady=10)
        

        self.update_clock()

        # bind mouse drag event to the form
        self.bind('<ButtonPress-1>', self.start_move)
        self.bind('<ButtonRelease-1>', self.stop_move)
        self.bind('<B1-Motion>', self.on_move)

        # bind F1 key to show message
        self.bind_all('<F1>', self.show_message)

        # bind F4 key to quit application
        self.bind_all('<F4>', self.quit())

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def update_clock(self):
        try:
            r = requests.get('https://api.ipify.org')
            self.ip_lbl.config(text=r.text)
            r = requests.get(f'http://ip-api.com/json/{r.text}')
            self.country_lbl.config(text=r.json()['country'])
            self.country_lbl.configure(fg='green')
            self.ip_lbl.configure(fg='blue')
        except:
            self.ip_lbl.config(text='not connect')
            self.ip_lbl.configure(fg='red')
            self.country_lbl.config(text='')

        self.after(5000, self.update_clock)

    def show_message(self, event):
        win32api.MessageBox(0, "This program has been written by an artificial intelligence under the supervision of a human.", "message")

if __name__ == '__main__':
    app = IpApp()
    app.attributes('-topmost', True) # keep the window always on top
    app.mainloop()
