# Create a class called Person

# Create init method with two attributes (name, birthday)

# Create an object from the Person class

import tkinter as tk
import datetime
from tkinter import *
import webbrowser

chromePath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
webbrowser.register('google-chrome', None, webbrowser.BackgroundBrowser(chromePath), 1)
chrome = webbrowser.get('google-chrome')

# Build a frame
root = tk.Tk()

# Set title of frame
root.title("Age Calculator App")

# Set geometry
root.geometry("500x400")

root.configure(bg="black")

# Create Labels
name_label=Label(text="Name", bg='black', fg='white')
year_label=Label(text="Year (YYYY)", bg='black', fg='white')
month_label=Label(text="Month (MM)", bg='black', fg='white')
day_label=Label(text="Day (DD)", bg='black', fg='white')

# Create Grids for Labels
name_label.grid(row=5, column=0, rowspan=1, columnspan=1)
year_label.grid(row=7, column=0, rowspan=1, columnspan=1)
month_label.grid(row=9, column=0, rowspan=1, columnspan=1)
day_label.grid(row=11, column=0, rowspan=1, columnspan=1)

# Create Entries
name_entry = Entry()
year_entry = Entry()
month_entry = Entry()
day_entry = Entry()

# Create Grids for Entries
name_entry.grid(row=5, column=1, rowspan=1, columnspan=1)
year_entry.grid(row=7, column=1, rowspan=1, columnspan=1)
month_entry.grid(row=9, column=1, rowspan=1, columnspan=1)
day_entry.grid(row=11, column=1, rowspan=1, columnspan=1)

image1 = PhotoImage(file='age.png')
image2 = PhotoImage(file='calc.png')

P1=Label(height=75, width=210, image=image1)
P2=Label(height=75, width=210, image=image2)

P1.grid(row=1,column=1,rowspan=1,columnspan=1)
P2.grid(row=3,column=1,rowspan=1,columnspan=1)

# Calculate age function for when button is clicked
def calculate(age):
    get_name = name_entry.get()
    get_year = int(year_entry.get())
    get_month = int(month_entry.get())
    get_day = int(day_entry.get())

    if age=='a':
        print(year_entry.get())
        print(month_entry.get())
        print(day_entry.get())
        person = Person(get_name,  datetime.date(get_year, get_month, get_day))
        print(person.age())

        text_entry = Text(master=root, height=5, width=40)
        text_entry.grid(row=15, column=1, rowspan=1, columnspan=1)
        text_input = ('Hi {name},\n\nYou are {age} years old today.').format(name=person.name, age=person.age())
        text_entry.insert(END, text_input)

    else:
        exit()

# Create Button
age_button = Button(text="Calculate Age", width=16, bg='orange', fg='black', command=lambda:calculate('a'))

# Create Grids for Entries
age_button.grid(row=13, column=1, rowspan=1, columnspan=1)

# Create Person class
class Person(object):

    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


    # Create a method that handles the age for the Person() class
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


# tim = Person('Tim', datetime.date(a, b, c))
# print(tim.name)
# print("Birthdate is", tim.birthdate)
# print(tim.age())

root.mainloop()