import os
import subprocess
import webbrowser
import wx
import wx.adv
import time

# storing processes to kill them later
all_processes = []

# cmd is smth you'd type into a terminal
def open(cmd):
	process = subprocess.Popen(cmd)
	all_processes.append(process)

# open everything that needs to be opened
def open_all():
	# open game master python program
	#
	
	# open database python
	#
	
	# open udp python server (https://docs.python.org/3/library/subprocess.html#subprocess.Popen)
	print("opening python udp server...")
	open("python ./gui/back/server.py")
	
	# open browser-python nodejs bridge
	print("opening browser-node-python bridge...")
	open("node ./gui/middle/jsPyCommunicator.js")
	
	# open html gui (https://stackoverflow.com/a/40905794)
	print("opening web browser...")
	filestr = "file:///"
	index_pathstr = os.path.realpath("./gui/front/index.html")
	webbrowser.open_new(filestr + index_pathstr)

# make sure all the subprocesses are dead upon end of program
def kill_all():
	# (https://stackoverflow.com/a/320712)
	print("killing all processes...")
	for p in all_processes:
		p.kill()

# splashscreen stuff
class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, wx.ID_ANY, "Splash Screen", size = (0, 0))

		bitmap = wx.Bitmap('./images/logo.jpg')
		image = bitmap.ConvertToImage()
		image = image.Scale(600, 600, wx.IMAGE_QUALITY_HIGH)
		result = wx.Bitmap(image)

		splash = wx.adv.SplashScreen(
					result, 
					wx.adv.SPLASH_CENTER_ON_SCREEN | wx.adv.SPLASH_TIMEOUT, 3000, self)

		print("displaying splash screen...")
		splash.Show()

		# actually open all the stuff here
		open_all()
		
		time.sleep(3)
		
		print("ending splash screen...")
		# splash.Hide()
		self.Close()

if __name__ == "__main__":
	print("app start...")
	
	# splashscreen
	# open_all() is called inside the splashscreen init func
	app = wx.App(False)
	frame = MyFrame()
	app.MainLoop()

# have a way to get messages from ./gui/back/server.py
