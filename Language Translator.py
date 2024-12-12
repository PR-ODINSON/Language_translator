#!/usr/bin/env python
# coding: utf-8

# In[7]:


from tkinter import Tk, Label, Text, Button, ttk
from deep_translator import GoogleTranslator

# Create a translator instance
translator_instance = GoogleTranslator(source="auto", target="en")

# Fetch supported languages (full names and ISO codes)
supported_languages = translator_instance.get_supported_languages(as_dict=True)
language_names = list(supported_languages.keys())  # Full names
language_iso_codes = list(supported_languages.values())  # ISO codes

def translate_text():
    """Translate the text input using deep-translator."""
    # Get user input and selected languages
    source_text = input_text.get("1.0", "end-1c")  # Input text
    source_lang_name = source_lang_var.get()       # Full name of source language
    target_lang_name = target_lang_var.get()       # Full name of target language

    try:
        # Map full names to ISO codes
        source_lang = supported_languages.get(source_lang_name, "auto")  # Default to 'auto'
        target_lang = supported_languages[target_lang_name]

        # Perform translation
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(source_text)
        output_text.delete("1.0", "end")  # Clear previous translation
        output_text.insert("1.0", translated)  # Display translated text
    except Exception as e:
        # Handle errors
        output_text.delete("1.0", "end")
        output_text.insert("1.0", f"Error: {str(e)}")

# Set up the main tkinter window
root = Tk()
root.title("Real-Time Language Translator")
root.geometry("700x500")

# Input text section
Label(root, text="Enter Text:").pack(pady=5)
input_text = Text(root, height=6, width=60)
input_text.pack(pady=5)

# Language selection dropdowns
Label(root, text="Source Language:").pack(pady=5)
source_lang_var = ttk.Combobox(root, values=["Auto-detect"] + language_names, state="readonly")
source_lang_var.set("Auto-detect")  # Default to auto-detect
source_lang_var.pack(pady=5)

Label(root, text="Target Language:").pack(pady=5)
target_lang_var = ttk.Combobox(root, values=language_names, state="readonly")
target_lang_var.set("English")  # Default to English
target_lang_var.pack(pady=5)

# Translate button
translate_button = Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=20)

# Output text section
Label(root, text="Translated Text:").pack(pady=5)
output_text = Text(root, height=6, width=60)
output_text.pack(pady=5)

# Run the tkinter event loop
root.mainloop()


# In[ ]:




