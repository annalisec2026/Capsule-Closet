# CapsuleCloset ♡

CapsuleCloset is a personalised digital wardrobe I made for my Creative Coding code prototype.

I have lots of clothes but still end up wearing combinations of the same things, so I wanted to make an app where you can easily see everything in your wardrobe and get reminded about the pieces you haven't worn in a while. The idea is to encourage people to rewear, donate or sell their clothes instead of buying more – ultimately, getting the most out of your wardrobe!

## What it does

- **Home** – shows how many items are in your wardrobe and how many haven't been worn lately, with shortcut buttons to each page (you can also use the side menu)
- **Add Clothing** – simply input the name, category, season and colour of an item, choose a photo and click add to wardrobe
- **Wardrobe** – shows all your clothes with their photos. Pick the season you're dressing for, and click 'wore it today' on what you wear
- **Reminders** – any item you haven't worn in 30+ days shows up here so you can give it some love (or donate/sell it)

Everything saves to a CSV file, so your clothes are still there next time you open the app.

## What I used

- Python 3.14
- Tkinter – for the window, buttons and drop downs
- Pillow 12.3.0 – for the clothing photos
- csv and datetime – for saving the clothes and working out the 30-day reminder

## How to run it

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Install Pillow in the terminal:
3. Download this repository (Code → Download ZIP) and unzip it
4. Open the folder in VS Code and run `capsulecloset.py`

## What's next

If I keep working on CapsuleCloset, I'd like to add a Create Outfit page and Lookbook, a category filter, and maybe automated outfit suggestions.

## Sources
Anthropic. (2025). Claude (Opus 5.5) [Large language model]. https://claude.ai
Clark, J. A., & Contributors. (2026). Pillow (PIL fork) documentation (Version 13.0.0) [Computer software documentation]. https://pillow.readthedocs.io/en/stable/
GeeksforGeeks. (2025, July 12). Python-Tkinter scrollbar. https://www.geeksforgeeks.org/python/python-tkinter-scrollbar/
GeeksforGeeks. (2026, January 23). Python Tkinter. https://www.geeksforgeeks.org/python/python-gui-tkinter/
Madecraft. (2024a, March 8). Python resources [Video]. In Python for students. LinkedIn Learning. https://www.linkedin.com/learning/python-for-students-2023/python-resources
Madecraft. (2024b, March 8). Stack Overflow [Video]. In Python for students. LinkedIn Learning. https://www.linkedin.com/learning/python-for-students-2023/stack-overflow
OpenAI. (2025). ChatGPT [Large language model]. https://chatgpt.com
Python Software Foundation. (2026a). csv — CSV file reading and writing (Version 3.15.2) [Computer software documentation]. https://docs.python.org/3/library/csv.html
Python Software Foundation. (2026b). tkinter — Python interface to Tcl/Tk (Version 3.15.2) [Computer software documentation]. https://docs.python.org/3/library/tkinter.html
Singh, R. (2025, January 7). Building a fashion recommendation system using image features. Becoming Human: Artificial Intelligence Magazine. https://becominghuman.ai/building-a-fashion-recommendation-system-using-image-features-602540ed48e5
techiestyle. (2025, January 3). 365 days of style: Using Python Tkinter to track my outfits in 2025 [Blog post]. Medium. https://medium.com/@techiestyle/365-days-of-style-using-python-tkinter-to-track-my-outfits-in-2025-24bf5da0247b
