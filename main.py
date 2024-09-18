# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 10:34:56 2024

@author: ATINA
"""

import capstone as cs

borrowers = [
    {
        "ID": "RM300892", 
        "First Name": "Rina",
        "Last Name": "Mahendra",
        "Date of Birth (DD-MM-YY)": "30-08-92",
        "Contact Info": "08219987654",
        "Book Title": ["The Power of Habit", "Thinking, Fast and Slow", "The Subtle Art of Not Giving a F*ck"],
        "Author": ["Charles Duhigg", "Daniel Kahneman", "Mark Manson"],
        "Date Borrowed (DD-MM-YYYY)": "15-08-2024"
    },
    {
        "ID": "JS220595", 
        "First Name": "John",
        "Last Name": "Smith",
        "Date of Birth (DD-MM-YY)": "22-05-95",
        "Contact Info": "08211234567",
        "Book Title": ["The Great Gatsby", "To Kill a Mockingbird"],
        "Author": ["F. Scott Fitzgerald", "Harper Lee"],
        "Date Borrowed (DD-MM-YYYY)": "01-09-2024"
    },
    {
        "ID": "MT150789", 
        "First Name": "Maria",
        "Last Name": "Tan",
        "Date of Birth (DD-MM-YY)": "15-07-89",
        "Contact Info": "08556677889",
        "Book Title": ["The Catcher in the Rye", "1984", "Educated"],
        "Author": ["J.D. Salinger", "George Orwell", "Tara Westover"],
        "Date Borrowed (DD-MM-YYYY)": "20-08-2024"
    },
    {
        "ID": "PR031200", 
        "First Name": "Priya",
        "Last Name": "Ravi",
        "Date of Birth (DD-MM-YY)": "03-12-00",
        "Contact Info": "08772345678",
        "Book Title": ["Becoming", "The Road", "The Alchemist"],
        "Author": ["Michelle Obama", "Cormac McCarthy", "Paulo Coelho"],
        "Date Borrowed (DD-MM-YYYY)": "14-08-2024"
    },
    {
        "ID": "KB041198", 
        "First Name": "Kevin",
        "Last Name": "Brown",
        "Date of Birth (DD-MM-YY)": "04-11-98",
        "Contact Info": "08134567990",
        "Book Title": ["Dune", "The Hobbit", "The Lean Startup"],
        "Author": ["Frank Herbert", "J.R.R. Tolkien", "Eric Ries"],
        "Date Borrowed (DD-MM-YYYY)": "10-09-2024"
    },
    {
        "ID": "LM180286", 
        "First Name": "Laura",
        "Last Name": "Martinez",
        "Date of Birth (DD-MM-YY)": "18-02-86",
        "Contact Info": "08387654321",
        "Book Title": ["Pride and Prejudice", "The Silent Patient"],
        "Author": ["Jane Austen", "Alex Michaelides"],
        "Date Borrowed (DD-MM-YYYY)": "22-08-2024"
    },
    {
        "ID": "NW230194", 
        "First Name": "Nina",
        "Last Name": "Williams",
        "Date of Birth (DD-MM-YY)": "23-01-94",
        "Contact Info": "08451237890",
        "Book Title": ["The Night Circus", "Little Fires Everywhere"],
        "Author": ["Erin Morgenstern", "Celeste Ng"],
        "Date Borrowed (DD-MM-YYYY)": "05-09-2024"
    },
    {
        "ID": "DK121288", 
        "First Name": "David",
        "Last Name": "Kim",
        "Date of Birth (DD-MM-YY)": "12-12-88",
        "Contact Info": "08123456789",
        "Book Title": ["The Art of War", "The Prince"],
        "Author": ["Sun Tzu", "Niccolò Machiavelli"],
        "Date Borrowed (DD-MM-YYYY)": "03-09-2024"
    },
    {
        "ID": "RH010198", 
        "First Name": "Rachel",
        "Last Name": "Hernandez",
        "Date of Birth (DD-MM-YY)": "01-01-98",
        "Contact Info": "08551234567",
        "Book Title": ["Brave New World", "Fahrenheit 451", "The Handmaid's Tale"],
        "Author": ["Aldous Huxley", "Ray Bradbury", "Margaret Atwood"],
        "Date Borrowed (DD-MM-YYYY)": "08-09-2024"
    }
]

# borrowers = []

cs.main(borrowers)