igbo_dicitionary ={"ehi":"cow",
                   "bia":"come",
                   "aziza":"broom",
                   "oche":"chair",
                   "ewu":"goat",
                   "umaka":"children",
                   "ebubechukwu":"glory of god ",
                   "water":"mmiri",
                   "soap":"nncha",
                   "papa":"Nna",
                   "mama":"Nnne",
                   "kedu":"how are you",
                   "gozie":"goodbye",
                   "okuko":"chicken",
                  "akpu":"fufu",
                   "ututu oma":"good morning",
                   "Ehihie oma":"good afternoon",
                   "Anyasi oma":"good evening",
                   "dalu":"thank you",
                   "Ji":"yam",
                   "Umunna":"family",
                   "onyekuzi":"teacher",}






from tkinter import Tk, Entry,Button,Label,StringVar

window = Tk()
window.geometry("600x250")
window.title("igbo dictionary")

entry_text =Entry(window)
entry_text.pack()

result =StringVar()
result_label =Label(window,textvariable=result)

def search(word):
    if word in igbo_dicitionary:
        result.set(igbo_dicitionary[word])
        print(igbo_dicitionary[word])

    else:
        result.set("Not found")
        print("Not found")

search_btn = Button(window,text="search",command=lambda:search(entry_text.get()))
search_btn.pack()
window.mainloop()







