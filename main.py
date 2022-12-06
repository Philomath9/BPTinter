import tkinter as tk

class App:      
    def __init__(self, root):
        self.root = root 
        
        root.geometry("900x480")
        self.CreateMain()

    def CreateMain(self):
        self.framemain = tk.Frame(self.root, bg="#121214")
        self.framemain.pack(side="top", fill=tk.BOTH, expand=1) 
        bt = tk.Button(self.framemain, text="Quiz", command=lambda:self.GoQuiz())
        bt.pack()
    def GoQuiz(self):
        self.framemain.destroy()
        self.CreateQuiz()
    def CreateQuiz(self):
        self.framemain = tk.Frame(self.root, bg="#121214")
        self.framemain.pack(side="top", fill=tk.BOTH, expand=1) 
        bt = tk.Button(self.framemain, text="Main", command=lambda:self.GoMain())
        bt.pack()
    def GoMain(self):
        self.framemain.destroy()
        self.CreateMain()
root = tk.Tk()
app = App(root)
root.mainloop()
