import os
import sys
from tkinter import *
import math, re
print(os.getcwd())


root = Tk()
root.title("Calculator")
root.configure(bg="#1c1c1e")
root.resizable(False, False) 

def about():
    win = Toplevel(root)
    win.title("About")

    Label(
        win,
        text="Scientific Calculator\nVersion 1.0\nDeveloped by Bhargavi",
        
        font=("Arial",14)
    ).pack(padx=20,pady=20)

memory = 0
def memory_add():
    global memory

    try:
        memory += float(current)
    except:
        pass
def memory_subtract():
    global memory

    try:
        memory -= float(current)
    except:
        pass
def memory_recall():
    append(memory)

def memory_clear():
    global memory
    memory=0


BG      = "#1c1c1e"
DBG     = "#000000"
DFG     = "#ffffff"
DSMALL  = "#9ca3af"

NUM_BG  = "#2c2c2e"; NUM_FG  = "#ffffff"
OP_BG   = "#3a3a3c"; OP_FG   = "#ffffff"
EQ_BG   = "#2563eb"; EQ_FG   = "#ffffff"
CLR_BG  = "#dc2626"; CLR_FG  = "#ffffff"
SCI_BG  = "#1e2a3a"; SCI_FG  = "#93c5fd"
RAD_FG  = "#34d399"  
DEG_FG  = "#fb923c" 
BAR_BG  = "#111111"; BAR_FG  = "#d1d5db"

FL = ("Arial", 15, "bold")   
FM = ("Arial", 11, "bold")  
FS = ("Arial", 10)         

sci_visible = False
history = []

if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


history_file = os.path.join(BASE_DIR, "history.txt")
exported_history_file = os.path.join(BASE_DIR, "exported_history.txt")

print("BASE_DIR =", BASE_DIR)
print("Saving to:", history_file)
print("Exporting to:", exported_history_file)


try:
    with open(history_file, "r") as file:
        for line in file:
            history.append(line.strip())
except:
    pass
use_radians = True

disp_frame = Frame(root, bg=DBG, pady=4, padx=10)
disp_frame.pack(fill=X, padx=10, pady=(10, 2))

expr_var   = StringVar(value="")
result_var = StringVar(value="0")

Label(disp_frame, textvariable=expr_var,
        font=("Arial", 12), fg=DSMALL, bg=DBG,
        anchor="e", justify="right").pack(fill=X)

Label(disp_frame, textvariable=result_var,
        font=("Arial", 34, "bold"), fg=DFG, bg=DBG,
        anchor="e", justify="right").pack(fill=X)

current = ""       

def refresh():
    result_var.set(current if current else "0")

def append(val):
    global current
    current += str(val)
    refresh()

def clear():
    global current
    current = ""
    expr_var.set("")
    result_var.set("0")

def backspace():
    global current
    current = current[:-1]
    refresh()

def do_percent():
    global current
    try:
        val = float(current)
        r = val / 100
        current = str(int(r) if float(r).is_integer() else round(r, 10))
        refresh()
    except Exception:
        pass

def do_sign():
    global current
    try:
        val = float(current)
        r = -val
        current = str(int(r) if float(r).is_integer() else r)
        refresh()
    except Exception:
        pass

def calculate():
    global current
    if not current:
        return
    try:
        expr = current
        expr_var.set(expr + " =")

        safe = expr
        safe = safe.replace("x", "*")
        safe = safe.replace("/", "/")
        safe = safe.replace("-", "-")
        safe = safe.replace("π", str(math.pi))
        safe = re.sub(r'(?<![a-zA-Z])e(?![a-zA-Z])', str(math.e), safe)

        def _sin(x):  return math.sin(x if use_radians else math.radians(x))
        def _cos(x):  return math.cos(x if use_radians else math.radians(x))
        def _tan(x):  return math.tan(x if use_radians else math.radians(x))

        env = {
            "sin":  _sin,  "cos":  _cos,  "tan":  _tan,
            "ln":   math.log,
            "log":  math.log10,
            "sqrt": math.sqrt,
            "abs":  abs,
            "fact": lambda x: math.factorial(int(x)),
            "exp":  math.exp,
            "__builtins__": {},
        }
        result = eval(safe, env)

        if isinstance(result, float):
            result = int(result) if result.is_integer() else round(result, 10)

        history.append(f"{expr} = {result}")
        with open(history_file, "a") as file:
            file.write(f"{expr} = {result}\n")
        current = str(result)
        result_var.set(current)
    except Exception:
        result_var.set("Error")
        expr_var.set(current + " =")
        current = ""

def sci_insert(token):
    append(token)


def toggle_rad():
    global use_radians
    use_radians = not use_radians
    rad_btn.config(text="Rad" if use_radians else "Deg",
                    fg=RAD_FG if use_radians else DEG_FG)

def show_history():
    win = Toplevel(root)
    win.title("History")
    win.configure(bg=BG)
    win.geometry("340x280")
    txt = Text(win, bg="#111111", fg="#e5e7eb", font=("Arial", 12),
                relief="flat", bd=8, wrap=WORD)
    txt.pack(fill=BOTH, expand=True, padx=8, pady=8)
    txt.insert(END, "\n".join(history) if history else "No history yet.")
    txt.config(state=DISABLED)

def export_history():
    with open(history_file, "r") as file:
        data = file.read()
    with open(exported_history_file, "w") as export:
        export.write(data)

def clear_history():
    history.clear()
    with open(history_file, "w") as file:
        file.write("")

all_buttons = []
def mkbtn(parent, text, cmd, bg=NUM_BG, fg=NUM_FG, font=FL, px=3, py=3):
    b = Button(
        parent,
        text=text,
        command=cmd,
        bg=bg,
        fg=fg,
        activebackground=bg,
        activeforeground=fg,
        font=font,
        relief="flat",
        bd=0,
        cursor="hand2",
        padx=6,
        pady=8
    )

    b.pack(side=LEFT, expand=True, fill=X, padx=px, pady=py)

    all_buttons.append(b)

    return b

def row(parent, py=2):
    f = Frame(parent, bg=BG)
    f.pack(fill=X, padx=6, pady=py)
    return f

sci_panel = Frame(root, bg=BG)

sr0 = row(sci_panel, 2)
rad_btn = mkbtn(sr0, "Rad", toggle_rad,SCI_BG, RAD_FG, FM)
mkbtn(sr0, "√(",   lambda: sci_insert("sqrt("),SCI_BG, SCI_FG, FM)
mkbtn(sr0, "|x|",  lambda: sci_insert("abs("),SCI_BG, SCI_FG, FM)
mkbtn(sr0, "xʸ",   lambda: append("**"),SCI_BG, SCI_FG, FM)

sr1 = row(sci_panel, 2)
mkbtn(sr1, "sin(", lambda: sci_insert("sin("), SCI_BG, SCI_FG, FM)
mkbtn(sr1, "cos(", lambda: sci_insert("cos("), SCI_BG, SCI_FG, FM)
mkbtn(sr1, "tan(", lambda: sci_insert("tan("), SCI_BG, SCI_FG, FM)
mkbtn(sr1, "π",    lambda: append(str(math.pi)),SCI_BG, SCI_FG, FM)

sr2 = row(sci_panel, 2)
mkbtn(sr2, "ln(",  lambda: sci_insert("ln("),SCI_BG, SCI_FG, FM)
mkbtn(sr2, "log(", lambda: sci_insert("log("),SCI_BG, SCI_FG, FM)
mkbtn(sr2, "1/x",  lambda: sci_insert("1/("), SCI_BG, SCI_FG, FM)
mkbtn(sr2, "e",    lambda: append(str(math.e)),SCI_BG, SCI_FG, FM)

sr3 = row(sci_panel, 2)
mkbtn(sr3, "exp(", lambda: sci_insert("exp("), SCI_BG, SCI_FG, FM)
mkbtn(sr3, "x²",   lambda: append("**2"),  SCI_BG, SCI_FG, FM)
mkbtn(sr3, "+/-",  do_sign, SCI_BG, SCI_FG, FM)
mkbtn(sr3, "fact(",lambda: sci_insert("fact("),SCI_BG, SCI_FG, FM)


Frame(sci_panel, bg="#3a3a3c", height=1).pack(fill=X, padx=6, pady=(4, 0))

def toggle_sci():
    global sci_visible
    if not sci_visible:
        sci_panel.pack(fill=X, pady=(5, 5), before=main_pad)
        sci_toggle_btn.config(text="▲ Scientific")
        sci_visible = True
    else:
        sci_panel.pack_forget()
        sci_toggle_btn.config(text="▼ Scientific")
        sci_visible = False

main_pad = Frame(root, bg=BG)
main_pad.pack(fill=BOTH, expand=True, padx=4, pady=2)

mr1 = row(main_pad)
mkbtn(mr1, "C",  clear,  CLR_BG, CLR_FG, FL)
mkbtn(mr1, "⌫",  backspace,OP_BG,  OP_FG,  FL)
mkbtn(mr1, "%",  do_percent, OP_BG,  OP_FG,  FL)
mkbtn(mr1, "÷",  lambda: append("/"),OP_BG,  OP_FG,  FL)

mr2 = row(main_pad)
mkbtn(mr2, "7", lambda: append("7"), NUM_BG, NUM_FG, FL)
mkbtn(mr2, "8", lambda: append("8"), NUM_BG, NUM_FG, FL)
mkbtn(mr2, "9", lambda: append("9"), NUM_BG, NUM_FG, FL)
mkbtn(mr2, "x", lambda: append("*"), OP_BG,  OP_FG,  FL)

mr3 = row(main_pad)
mkbtn(mr3, "4", lambda: append("4"), NUM_BG, NUM_FG, FL)
mkbtn(mr3, "5", lambda: append("5"), NUM_BG, NUM_FG, FL)
mkbtn(mr3, "6", lambda: append("6"), NUM_BG, NUM_FG, FL)
mkbtn(mr3, "−", lambda: append("-"), OP_BG,  OP_FG,  FL)

mr4 = row(main_pad)
mkbtn(mr4, "1", lambda: append("1"), NUM_BG, NUM_FG, FL)
mkbtn(mr4, "2", lambda: append("2"), NUM_BG, NUM_FG, FL)
mkbtn(mr4, "3", lambda: append("3"), NUM_BG, NUM_FG, FL)
mkbtn(mr4, "+", lambda: append("+"), OP_BG,  OP_FG,  FL)

mr5 = row(main_pad)
mkbtn(mr5, "(", lambda: append("("), NUM_BG, NUM_FG, FL)
mkbtn(mr5, "0",  lambda: append("0"), NUM_BG, NUM_FG, FL)
mkbtn(mr5, ")", lambda: append(")"), NUM_BG, NUM_FG, FL)
mkbtn(mr5, ".",  lambda: append("."), NUM_BG, NUM_FG, FL)
mkbtn(mr5, "=",  calculate,           EQ_BG,  EQ_FG,  FL)

toolbar = Frame(root, bg=BAR_BG)
toolbar.pack(fill=X, side=BOTTOM, pady=(4, 0))

toolbar_buttons = []

def tbtn(text, cmd, fg=BAR_FG):
    btn = Button(toolbar, text=text, command=cmd,
            bg=BAR_BG, fg=fg, activebackground="#222222", activeforeground=fg,
            font=FS, relief="flat", bd=0, cursor="hand2",
            padx=12, pady=6).pack(side=LEFT)

sci_toggle_btn = Button(toolbar, text="▼ Scientific",command=toggle_sci,
                        bg=BAR_BG, fg=BAR_FG,activebackground="#222222", activeforeground=BAR_FG,
                        font=FS, relief="flat", bd=0, cursor="hand2",
                        padx=12, pady=6)
sci_toggle_btn.pack(side=LEFT)

tbtn("Export", export_history)
tbtn("History",show_history)
tbtn("Clear History", clear_history, "#ef4444")
tbtn("About", about)
tbtn("M+", memory_add)
tbtn("M-", memory_subtract)
tbtn("MR", memory_recall)
tbtn("MC", memory_clear)

dark = True
def toggle_theme():
    global dark

    if dark:
        root.configure(bg="white")
        disp_frame.configure(bg="white")

        for btn in all_buttons:
            btn.configure(
                bg="#f0f0f0",
                fg="black",
                activebackground="#d9d9d9",
                activeforeground="black"
            )

        dark = False

    else:
        root.configure(bg="#1c1c1e")
        disp_frame.configure(bg=DBG)

        for btn in all_buttons:
            btn.configure(
                bg=NUM_BG,
                fg="white",
                activebackground=NUM_BG,
                activeforeground="white"
            )

        dark = True
tbtn("Theme", toggle_theme)

def on_key(e):
    k = e.char
    if k in "0123456789.+-*/()":
        append(k)
    elif k in ("\r", "\n"):
        calculate()
    elif e.keysym == "BackSpace":
        backspace()
    elif k.lower() == "c":
        clear()
    elif e.keysym == "Escape":
        clear()

root.bind("<Key>", on_key)

W, H = 700, 750
root.update_idletasks()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(f"{W}x{H}+{(sw-W)//2}+{(sh-H)//2}")

root.mainloop()