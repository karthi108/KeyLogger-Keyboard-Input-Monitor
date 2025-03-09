# KeyLogger-Keyboard-Input-Monitor  

This project demonstrates how to monitor keyboard inputs on a system. It logs keystrokes and sends them via email. It can be used for **educational purposes, testing, or automating specific tasks** with user input. Please ensure you have **permission from the system owner** and follow ethical guidelines when using this tool.  

## Features  
- Captures keystrokes from the keyboard.  
- Sends keystroke data to a specified email address every 10 keystrokes.  
- Stops logging when the `ESC` key is pressed.  

## How to Set Up and Run  

### Clone the repository  
```bash
git clone https://github.com/yourusername/keyboard-input-monitor.git
cd keyboard-input-monitor
```

### Install dependencies  
Make sure you have Python installed. Then, install the required dependencies:  
```bash
pip install pynput python-dotenv
```

### Set up environment variables  
Create a `.env` file in the root of the project directory and add your email credentials:  

```env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_password_or_app_password
```

> **Note:** If using Gmail, you may need to enable **"Less secure apps"** or use an **app-specific password** if you have **2-factor authentication** enabled.  

### Run the project  
To start logging keyboard input, run the `keylogger.py` file:  
```bash
python keylogger.py
```

### Stopping the program  
Press the `ESC` key to stop the program from logging keystrokes.  

---

### Disclaimer  
This tool must only be used **with explicit consent** and for **ethical purposes**. Unauthorized use of keyloggers is illegal and may violate privacy laws. Ensure compliance with legal and ethical guidelines.
---

## THANK YOU!  
