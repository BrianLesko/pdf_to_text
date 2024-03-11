# Brian Lesko
# 11/24/2023

import streamlit as st
from customize_gui import gui as gui 
gui = gui()

import PyObjC 

gui.setup(wide=True, text="Extract Text from PDF files")
