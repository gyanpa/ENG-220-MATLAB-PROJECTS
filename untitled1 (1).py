# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1twa1qukiWwJoNl0yNsfMi7PyGGQzLNp6
"""

# prompt: create an output that says hello world in a text box
! pip install streamlit
from IPython.display import display, HTML

html_code = """
<textarea rows="4" cols="50">
Hello World
</textarea>
"""

display(HTML(html_code))