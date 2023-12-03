import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk,Image
import io
class NewsApi:
    def __init__(self):
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=bb5a98f490d9470e9c191529bff595fb').json()
        #print(self.data)
        #Initiate GUI
        self.load_gui()#calling load gui methond inside dat function
        self.load_news_item(0)#loading next news one by one


    def load_gui(self):
        self.root=Tk() 
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.title("MyNews")
        self.root.configure(background='black') 

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def open_link(self,url):
        webbrowser.open(url)

    



    def load_news_item(self,index):
        self.clear()    #calling clear method
        #-----------------------finding image --------------------------------------------------------
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://demofree.sirv.com/nope-not-here.jpg'
            raw_data = urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)


        


        label=Label(self.root,image=photo)
        label.pack()



        heading=Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))


        details=Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',wraplength=350,justify='center')
        details.pack(pady=(2,20))
        details.config(font=('verdana',12))

        frame=Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if(index !=0):
            prev=Button(frame,text='Prev',width=16,height=3,command=lambda : self.load_news_item(index -1))
            prev.pack(side=LEFT)

        read=Button(frame,text='Read More',width=16,height=3,command=lambda :self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        
        if index != len(self.data['articles'])-1:

            next=Button(frame,text='Next',width=16,height=3,command=lambda :self.load_news_item(index + 1))
            next.pack(side=LEFT)
    
    
    


        self.root.mainloop()
    
    


obj=NewsApi()                   