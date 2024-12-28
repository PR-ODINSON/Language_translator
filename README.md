# Real-Time Language Translator

Real-Time Language Translator is a desktop application built using Python and Tkinter that enables users to translate text between various languages in real time. The application leverages the powerful `deep-translator` library to provide accurate and efficient translations.

## Features

- **Real-Time Translation**: Instantly translate text between numerous languages.
- **Auto-Detection**: Automatically detect the source language if unsure.
- **User-Friendly Interface**: Easy-to-use graphical interface built with Tkinter.
- **Wide Language Support**: Supports a vast range of languages through the Google Translator API.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.6 or higher.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/real-time-language-translator.git
   cd real-time-language-translator
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   The main dependencies include:

   - `deep-translator`
   - `tkinter` (usually included with Python)

## Usage

1. Run the application:

   ```bash
   python translator_app.py
   ```

2. Use the interface to:

   - Enter the text you want to translate.
   - Select the source and target languages from the dropdown menus.
   - Click on the **Translate** button to get the translated text.

## Supported Languages

The application supports a wide range of languages provided by the Google Translator API. The source language can also be set to "Auto-detect" for convenience.

## Code Overview

- **Input Text Section**: Textbox to input the text to be translated.
- **Language Selection**: Dropdown menus for source and target language selection.
- **Translation Logic**: Utilizes `deep-translator` to perform translations.
- **Output Text Section**: Displays the translated text.

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m 'Add some feature'
   ```

4. Push to your branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Deep Translator](https://pypi.org/project/deep-translator/) for powering the translations.
- Python’s Tkinter library for the graphical user interface.
