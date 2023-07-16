from difflib import get_close_matches
import webbrowser
from tkinter import *
import random
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests
from collections import defaultdict
root = Tk()
root.geometry("850x300") 
root.config(bg='#FF731D')

class Price:

  def __init__(self, master) :
    self.var = StringVar()

    self.type_of_sDeal1 = StringVar()
    self.type_of_sDeal2 = StringVar()

    image1 = Image.open("sastra4.png")
    test = ImageTk.PhotoImage(image1)
    label1 = Label(image=test)
    label1.image = test

# Position image 
    label1.place(x=100,y=150)

    name = Label(master, text='Input For Product Name ', font=('Times', 15, 'italic'), fg='black', bg='#FFF7E9')
    name.grid(row=0, column=0,padx=30 ,pady=30)

    query = Entry(master, textvariable=self.var)
    query.config(font=('Times',16, 'italic'))
    query.grid(row=0, column=1, padx=10)

    bsearch = Button(master, text='Go Search', bd=3, bg='#A0937D' ,command=self.trace)
    bsearch.grid(row=1, column=1, sticky=W, pady=2)

    dev = Label(master, text='Developed By : SURESH BALAJI S', font=('Times', 15, 'italic'), fg='black', bg='#FFF7E9')
    dev.grid(row=10, column=10,padx=30 ,pady=30)

    rno = Label(master, text='Register No : 124003326', font=('Times', 15, 'italic'), fg='black', bg='#FFF7E9')
    rno.grid(row=11, column=10,padx=30 ,pady=30)

    self.gPort = 0

  def trace(self):

    self.item = self.var.get()
    self.item_arr = self.item.split()
    self.n = 1 
    self.key = ""
    self.title_sDeal1_var = StringVar()
    self.title_sDeal2_var = StringVar()
    self.variable_sDeal1 = StringVar()
    self.variable_sDeal2 = StringVar()

    for word in self.item_arr:
      if self.n == 1:
        self.key = self.key + str(word)
        self.n += 1
      else:
        self.key = self.key + '+' + str(word)

    self.window = Toplevel(root)
    self.window.title('Product Showcasing Container')
    self.window.config(bg='#2B3A55')
    self.window.geometry('1500x300')

    name_of_sDeal1 = Label(self.window, text='Snapdeals Product Name 1 :' , font=('Times',12,'bold italic'),fg='black', bg='#7DE5ED')
    name_of_sDeal1.grid(row=0, column=0, sticky=W, padx=(5,10), pady=5)

    price_of_sDeal1 = Label(self.window, text='Product 1 Price (Rs):' , font=('Times',12,'bold italic'),fg='black', bg='#7DE5ED')
    price_of_sDeal1.grid(row=1, column=0, sticky=W, padx=(5,10), pady=5)

    input_for_sDeal1 = Entry(self.window, textvariable=self.type_of_sDeal1)
    input_for_sDeal1.config(font=('Times',12,'bold italic'),fg='black', bg='#FEF5AC')
    input_for_sDeal1.grid(row=1, column=1, sticky=W)

    name_of_sDeal2 = Label(self.window, text='Snapdeals Product Name 2 :' , font=('Times',12,'bold italic'),fg='black', bg='#7DE5ED')
    name_of_sDeal2.grid(row=3, column=0, sticky=W, padx=(5,10), pady=5)

    price_of_sDeal2 = Label(self.window, text='Product 2 price (Rs):' , font=('Times',12,'bold italic'),fg='black', bg='#7DE5ED')
    price_of_sDeal2.grid(row=4, column=0, sticky=W, padx=(5,10), pady=5)

    input_for_sDeal2 = Entry(self.window, textvariable=self.type_of_sDeal2)
    input_for_sDeal2.config(font=('Times',12,'bold italic'),fg='black', bg='#FEF5AC')
    input_for_sDeal2.grid(row=4, column=1, sticky=W)

    self.getsDeal1(self.key)
    self.getsDeal2(self.key)

    try:
      self.variable_sDeal1.set(self.found_sDeal1[0])
    except:
      self.variable_sDeal1.set('Given Product is unavailable!')
    try:
      self.variable_sDeal2.set(self.found_sDeal2[0])
    except:
      self.variable_sDeal2.set('Given Product is unavailable!')

    value_for_sDeal1 = OptionMenu(self.window, self.variable_sDeal1, *self.found_sDeal1)
    value_for_sDeal1.config(font=('Times',12,'bold italic'),fg='black', bg='#FEF5AC')
    value_for_sDeal1.grid(row=0, column=1, sticky=W, pady=5)

    suggestion_for_sDeal1 = Label(self.window, text='Looking For Some Other Product? Try using the Title Box for Various Suggestions ! ')
    suggestion_for_sDeal1.config(font=('Times',12,'bold italic'),fg='black', bg='#A0E4CB')
    suggestion_for_sDeal1.grid(row=0, column=2, padx=5)

    value_for_sDeal2 = OptionMenu(self.window, self.variable_sDeal2, *self.found_sDeal2)
    value_for_sDeal2.config(font=('Times',12,'bold italic'),fg='black', bg='#FEF5AC')
    value_for_sDeal2.grid(row=3, column=1, sticky=W, pady=5)

    suggestion_for_sDeal2 = Label(self.window, text='Looking For Some Other Product? Try using the Title Box for Various Suggestions ! ')
    suggestion_for_sDeal2.config(font=('Times',12,'bold italic'),fg='black', bg='#A0E4CB')
    suggestion_for_sDeal2.grid(row=3, column=2, padx=5)

    key_find = Button(self.window, text='Search', command=self.go_search, bd=4)
    key_find.config(font=('Times',12,'bold italic'),fg='black', bg='#ECE5C7')
    key_find.grid(row=2, column=2, sticky=E, padx=10, pady=4)

    key_find_sDeal1 = Button(self.window, text='Link For the Product 1', command=self.search_sDeal1, bd=4)
    key_find_sDeal1.config(font=('Times',12,'bold italic'),fg='black', bg='#A0E4CB')
    key_find_sDeal1.grid(row=1, column=2, sticky=W, padx=3)

    key_find_sDeal2 = Button(self.window, text='Link For the Product 2', command=self.search_sDeal2, bd=4)
    key_find_sDeal2.config(font=('Times',12,'bold italic'),fg='black', bg='#A0E4CB')
    key_find_sDeal2.grid(row=4, column=2, sticky=W, padx=3)

  def getsDeal1(self, key):

    ports = [3001, 5001, 8001]
    self.gPort = random.choice(ports)

    url_sDeal1 = 'http://127.0.0.1:'+ str(self.gPort) +'/getData/' +str(key)

    map = defaultdict(list)

    source_code = requests.get(url_sDeal1)
  
    source_code = source_code.json()
    
    self.value_name = StringVar()
    
    for html in source_code["products"]:
    
      title, link = None, None
      
      title = html["name"]
      
      price = html["price"]
      
      link = html["link"]
      if title and link:
        map[title] = [price, link]

    client_product = self.var.get().title()

    self.found_sDeal1 = get_close_matches(client_product, list(map.keys()), 20, 0.01)
    self.view_datatable_snap1 = {}

    for title in self.found_sDeal1:
      self.view_datatable_snap1[title] = map[title]

    self.value_name.set(self.found_sDeal1[0])
    self.type_of_sDeal1.set(self.view_datatable_snap1[self.found_sDeal1[0]][0] + '.00')
    self.product_link1 = self.view_datatable_snap1[self.found_sDeal1[0]][1]

  def getsDeal2(self, key):

    ports = [3001, 5001, 8001]
    p = random.choice(ports)

    if (p == self.gPort):
      
      ports.remove(self.gPort)
      p = random.choice(ports)

    url_sDeal2 = 'http://127.0.0.1:'+ str(p) +'/getData/' +str(key)

    map = defaultdict(list)

    source_code = requests.get(url_sDeal2)
  
    source_code = source_code.json()
    
    self.value_name = StringVar()
    
    for html in source_code["products"]:
    
      title, link = None, None
      
      title = html["name"]
      
      price = html["price"]
      
      link = html["link"]
      if title and link:
        map[title] = [price, link]

    client_product = self.var.get().title()

    self.found_sDeal2 = get_close_matches(client_product, list(map.keys()), 20, 0.01)

    self.view_datatable_snap2 = {}
    for title in self.found_sDeal2:
      self.view_datatable_snap2[title] = map[title]

    self.value_name.set(self.found_sDeal2[0])
    self.type_of_sDeal2.set(self.view_datatable_snap2[self.found_sDeal2[0]][0] + '.00')
    self.product_link2 = self.view_datatable_snap2[self.found_sDeal2[0]][1]

  def go_search(self):

    sDeal1_get = self.variable_sDeal1.get()
    sDeal2_get = self.variable_sDeal2.get()

    sDeal1_price, self.product_link1 = self.view_datatable_snap1[sDeal1_get][0], self.view_datatable_snap1[sDeal1_get][1]
    self.type_of_sDeal1.set(sDeal1_price + '.00')

    sDeal2_price, self.product_link2 = self.view_datatable_snap2[sDeal2_get][0], self.view_datatable_snap2[sDeal2_get][1]
    self.type_of_sDeal2.set(sDeal2_price + '.00')
    
  def search_sDeal1(self):
    webbrowser.open(self.product_link1)
  def search_sDeal2(self):
    webbrowser.open(self.product_link2)

if __name__ == "__main__":
    c = Price(root)
root.title('Product Showcasing Container')
root.mainloop()
