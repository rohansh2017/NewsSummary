import tkinter as tk
from tkinter import font
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    
    # Read the url and download, parse, and analyze it using the imported libraries.
    url = utext.get('1.0', "end").strip()

    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # Work with tkinter to configure each of the text boxes and add in the parsed information.
    title.config(state = 'normal')
    author.config(state = 'normal')
    publication.config(state = 'normal')
    summary.config(state = 'normal')
    sentiment.config(state = 'normal')
    keywords.config(state = 'normal')
    

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    #insert the appropriate sentiment text using polarity analysis. 
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    keywords.delete('1.0', 'end')
    keywords.insert('1.0', article.keywords)

    title.config(state = 'disabled')
    author.config(state = 'disabled')
    publication.config(state = 'disabled')
    summary.config(state = 'disabled')
    sentiment.config(state = 'disabled')
    keywords.config(state = 'disabled')

# Create a window and add the necessary labels, textboxes, buttons with pre-chosen colors.   
root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x730')
root.config(background='#0099d3')

tlabel = tk.Label(root, text = "Title", font= font.Font(size= 20, weight='bold',), bg= '#0099d3', fg= '#302e55')
tlabel.pack()

title = tk.Text(root, height = 2, width = 140)
title.config(state='disabled', bg = '#dddddd')
title.pack()

alabel = tk.Label(root, text = "Author", font= font.Font(size= 20, weight='bold'), bg= '#0099d3', fg= '#302e55')
alabel.pack()

author = tk.Text(root, height = 2, width = 140)
author.config(state='disabled', bg = '#dddddd')
author.pack()

plabel = tk.Label(root, text = "Publishing Date", font= font.Font(size= 20, weight='bold'), bg= '#0099d3', fg= '#302e55')
plabel.pack()

publication = tk.Text(root, height = 2, width = 140)
publication.config(state='disabled', bg = '#dddddd')
publication.pack()

slabel = tk.Label(root, text = "Summary", font= font.Font(size= 20, weight='bold'), bg= '#0099d3', fg= '#302e55')
slabel.pack()

summary = tk.Text(root, height = 20, width = 140)
summary.config(state = 'disabled', bg = '#dddddd')
summary.pack()

selabel = tk.Label(root, text = "Sentiment Analysis", font= font.Font(size= 20, weight='bold'), bg= '#0099d3', fg= '#302e55')
selabel.pack()

sentiment = tk.Text(root, height = 2, width = 140)
sentiment.config(state = 'disabled', bg = '#dddddd')
sentiment.pack()

klabel = tk.Label(root, text = "Keywords", font= font.Font(size= 20, weight='bold'), bg= '#0099d3', fg= '#302e55')
klabel.pack()

keywords = tk.Text(root, height = 2, width = 140)
keywords.config(state='disabled', bg = '#dddddd')
keywords.pack()

ulabel = tk.Label(root, text = "URL", font= font.Font(size= 20, weight='bold'), bg= '#0099d3', fg= '#302e55')
ulabel.pack()

utext = tk.Text(root, height = 2, width = 140)
utext.pack()

btn = tk.Button(root, text = "Summarize", command = summarize, highlightbackground= '#0099d3')
btn.pack()

root.mainloop()