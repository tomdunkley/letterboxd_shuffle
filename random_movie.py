import win32api, win32con, time, win32gui, win32process, win32com.client, winsound
from pywinauto.application import Application

def click(x,y):
    win32api.SetCursorPos((x,y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def scroll(n):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 300, 300, -n, 0)

click(100,50)
time.sleep(3)
click(330,550)
time.sleep(4)
scroll(520)
time.sleep(1)
click(330,860)
time.sleep(2)


window = win32gui.GetForegroundWindow()
tid, pid = win32process.GetWindowThreadProcessId(window)
app = Application(backend="uia").connect(process=pid, time_out=10)
dlg = app.top_window()
title = "Address and search bar"
url = dlg.child_window(title=title, control_type="Edit").get_value()
start_url = url.split('/')[0]


if start_url == "netflix.com":
    click(570,630)
    time.sleep(0.3)
    wsh = win32com.client.Dispatch("WScript.Shell")
    wsh.SendKeys("{F11}")
elif start_url == "itv.com":
    time.sleep(3)
    click(945,620)
    time.sleep(1)
    click(1350,680)
elif start_url == "bbc.co.uk":
    click(220,1000)
    time.sleep(1)
    click(970,700)
    time.sleep(1)
    click(1500,970)
    time.sleep(0.1)
    click(1500,870)
elif start_url == "disneyplus.com":
    time.sleep(6)
    click(180,630)
    time.sleep(0.3)
    wsh = win32com.client.Dispatch("WScript.Shell")
    wsh.SendKeys("{F11}")
elif start_url == "channel4.com":
    click(320,860)
    time.sleep(0.3)
    wsh = win32com.client.Dispatch("WScript.Shell")
    wsh.SendKeys("{F11}")


winsound.PlaySound("SystemExit", winsound.SND_ALIAS)