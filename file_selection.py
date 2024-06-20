import sys
from tkinter import Tk, filedialog

def get_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()  
    root.destroy()
    return file_path

if __name__ == "__main__":
    file_path = get_file_path()
    if file_path:
        print(file_path)
    else:
        sys.exit(1)