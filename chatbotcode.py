from tkinter import *
root = Tk()
def send():
    send="User: "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="Hello"):
        txt.insert(END, "\n" + "Bot: Heyyy:)")
    elif(e.get() == "How are you?"):
        txt.insert(END, "\n" + "Bot: I am good :) Thanks for asking")
    elif(e.get() == "What is your name?"):
        txt.insert(END, "\n" + "Bot: My name is Jimmy!")
    elif (e.get() == "Who created you?"):
        txt.insert(END, "\n" + "Bot: I was created by Hisana and I love her!")
    elif (e.get() == "How old are you?"):
        txt.insert(END, "\n" + "Bot: I am just one day old!!!")
    elif (e.get() == "What is your opinion about Covid?"):
        txt.insert(END, "\n" + "Bot: I don't know much about it but I could probably know that my master is worried about it:(")
    elif (e.get() == "It was nice talking to you! jimmy"):
        txt.insert(END, "\n" + "Bot: Thankyou so much It was nice talking to you")
    else:
        txt.insert(END, "\n" + "Bot: Sorry I  didn't get it :(")
    e.delete(0,END)
txt = Text(root)
txt.grid(row=0,column=0,columnspan=3)
e=Entry(root,width=100)
send=Button(root,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()