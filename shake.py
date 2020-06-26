
import tkinter as tk

    class MyApp:
        def __init__(self):
            MyApp.main = tk.Tk()
            MyApp.main.title("Shakespeare")
            self.create_widgets()
            MyApp.main.mainloop()
        def create_widgets(self):
            MyApp.label = tk.Label(MyApp.main, text="To be or not to be...", font = ('Snell Roundhand',30))
            MyApp.label.pack(side="left")
            self.logo = tk.PhotoImage(file="shake.gif")
            my_label2 = tk.Label(image=self.logo)
            my_label2.pack(side="top")
            my_button1 = tk.Button(MyApp.main, text="Afrikaans", command=MyApp.callback1)
            my_button1.pack(side="bottom")
            my_button2 = tk.Button(MyApp.main, text="Finnish", command=MyApp.callback2)
            my_button2.pack(side="bottom")
            my_button3 = tk.Button(MyApp.main, text="Chinese", command=MyApp.callback3)
            my_button3.pack(side="bottom")
            my_button4 = tk.Button(MyApp.main, text="English", command=MyApp.callback4)
            my_button4.pack(side="bottom")
            my_button5 = tk.Button(MyApp.main, text="Southern Sotho", command=MyApp.callback5)
            my_button5.pack(side="bottom")
        def callback1():
            MyApp.label.configure(text="Om te wees of nie te wees nie...")
        def callback2():
            MyApp.label.configure(text="Ollakko vai eikö olla...")
        def callback3():
            MyApp.label.configure(text="生存还是毁灭...")
        def callback4():
            MyApp.label.configure(text="To be or not to be...")
        def callback5():
            MyApp.label.configure(text="Ho ba kapa ho se be...")

    my_app = MyApp()
