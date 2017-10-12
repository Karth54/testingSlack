#!/usr/bin/python
# -*- coding: utf-8 -*-
#testing push to GitHub
import os
from azure.datalake.store import core, lib, multithread 
from azure.datalake.store.multithread import ADLDownloader, ADLUploader

from Tkinter import *
# Test commit message 
root = Tk()
root.configure(background='black')
root.wm_title("Nielsen Azure Access")
root.wm_iconbitmap('nielsen_icon.ico')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def uploadToDataLake():
	# Authenticate using Service Principal
	token = lib.auth(tenant_id = tenant_id_entry.get(), client_secret = secret_entry.get(), client_id = client_id_entry.get())
	adl = core.AzureDLFileSystem(token, store_name = data_lake_entry.get())

	# ADLDownloader(adl, '/pocoutput/addfactssmry3_USQL_sub1_sub1.txt', '/data/testDownload/downloadedFile.txt', 5, 2**24, overwrite=True)
	ADLUploader(adl, data_lake_path_entry.get(), local_path_entry.get(), 5, 2**24)

def downloadToLocal():
	# Authenticate using Service Principal
	token = lib.auth(tenant_id = tenant_id_entry.get(), client_secret = secret_entry.get(), client_id = client_id_entry.get())
	adl = core.AzureDLFileSystem(token, store_name = data_lake_entry.get())

	# ADLDownloader(adl, '/pocoutput/addfactssmry3_USQL_sub1_sub1.txt', '/data/testDownload/downloadedFile.txt', 5, 2**24, overwrite=True)
	ADLDownloader(adl, data_lake_path_entry.get(), local_path_entry.get(), 5, 2**24)

def quitProgram():
	root.destroy()

tenant_id_label = Label(root, text="Tenant ID", bg = 'black', fg = 'white')
tenant_id_entry = Entry(root, bd =5)

client_id_label = Label(root, text="Client ID", bg = 'black', fg = 'white')
client_id_entry = Entry(root, bd =5)

secret_label = Label(root, text="Secret", bg = 'black', fg = 'white')
secret_entry = Entry(root, bd =5)

data_lake_label = Label(root, text="Data Lake Name", bg = 'black', fg = 'white')
data_lake_entry = Entry(root, bd =5)

local_path_label = Label(root, text="Local Path", bg = 'black', fg = 'white')
local_path_entry = Entry(root, bd =5)

data_lake_path_label = Label(root, text="Data Lake Path", bg = 'black', fg = 'white')
data_lake_path_entry = Entry(root, bd =5)

upload_button = Button(root, text ="Upload", command = uploadToDataLake, bg = 'deep sky blue', fg = 'white')
download_button = Button(root, text ="Download", command = downloadToLocal, bg = 'deep sky blue', fg = 'white')
quit_button = Button(root, text ="Exit", command = quitProgram, bg = 'deep sky blue', fg = 'white')
 
# tenant_id_label.pack(side = LEFT)
# tenant_id_entry.pack(side = LEFT)
# client_id_label.pack()
# client_id_entry.pack()
# secret_label.pack()
# secret_entry.pack()

# data_lake_label.pack()
# data_lake_entry.pack()

# local_path_label.pack()
# local_path_entry.pack()
# data_lake_path_label.pack()
# data_lake_path_entry.pack()

nielsen_logo = PhotoImage(file = 'nielsen-logo1.gif')
nielsen_logo_label = Label(root, image = nielsen_logo)
nielsen_logo_label.grid(sticky = N+E+S+W, row = 0, column = 0, columnspan = 3)

tenant_id_label.grid(sticky = E, row = 1, column = 0)
tenant_id_entry.grid(row = 1, column = 1, columnspan = 2, ipadx = 50, padx = 10, pady = 5)
client_id_label.grid(sticky = E, row = 2, column = 0)
client_id_entry.grid(row = 2, column = 1, columnspan = 2, ipadx = 50, padx = 10, pady = 5)
secret_label.grid(sticky = E, row = 3, column = 0)
secret_entry.grid(row = 3, column = 1, columnspan = 2, ipadx = 50, padx = 10, pady = 5)

data_lake_label.grid(sticky = E, row = 4, column = 0)
data_lake_entry.grid(row = 4, column = 1, columnspan = 2, ipadx = 50, padx = 10, pady = 5)

local_path_label.grid(sticky = E, row = 5, column = 0)
local_path_entry.grid(row = 5, column = 1, columnspan = 2, ipadx = 50, padx = 10, pady = 5)
data_lake_path_label.grid(sticky = E, row = 6, column = 0)
data_lake_path_entry.grid(row = 6, column = 1, columnspan = 2, ipadx = 50, padx = 10, pady = 5)

upload_button.grid(sticky = N+E+S+W, row = 7, column = 0) 
download_button.grid(sticky = N+E+S+W, row = 7, column = 1)
quit_button.grid(sticky = N+E+S+W, row = 7, column = 2)

root.mainloop()

# class Example(Frame):
  
#     def __init__(self, parent):
#         Frame.__init__(self, parent)   
         
#         self.parent = parent        
#         self.initUI()
        
        
#     def initUI(self):
      
#         self.parent.title("Test Dialog")
#         self.pack(fill=BOTH, expand=1)      
        
#         self.txt = Text(self)
#         self.txt.pack(fill=BOTH, expand=1)


#     def onOpen(self):
      
#         ftypes = [('Python files', '*.py'), ('All files', '*')]
#         dlg = tkFileDialog.Open(self, filetypes = ftypes)
#         fl = dlg.show()
        
#         if fl != '':
#             text = self.readFile(fl)
#             self.txt.insert(END, text)
            

#     def readFile(self, filename):

#         f = open(filename, "r")
#         text = f.read()
#         return text
         

# def main():
  
#     root = Tk()
#     ex = Example(root)
#     root.geometry("300x250+300+300")
#     root.mainloop()  


# if __name__ == '__main__':
#     main()