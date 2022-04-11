import os
import time
import webbrowser
import _thread

# distinguishes between .js and .py and runs node or python accordingly
def open(x):
	if x.strip()[-2:] == "py":
		os.system("python {}".format(x))
	elif x.strip()[-2:] == "js":
		os.system("node {}".format(x))
	else:
		os.system(x)

# run in new thread
def run(x):
	try:
		print("starting \"{}\"...".format(x))
		threads.append(_thread.start_new_thread(open, (x,)))
	except:
		print("! failed to start \"{}\"".format(x))

if __name__ == "__main__":
	print("app start...")
	
	# open splashscreen
	run("./front/splashscreen.py")
	time.sleep(3)
	# open game master python program
	# this already includes udp python server and database python file
	run("./back/main.py")
	
	# open browser-python nodejs bridge
	run("./middle/jsPyCommunicator.js")
	
	# open html gui (https://stackoverflow.com/a/40905794)
	print("opening web browser...")
	filestr = "file:///"
	index_pathstr = os.path.realpath("./front/index.html")
	webbrowser.open_new(filestr + index_pathstr)
	
	# don't weird out terminal
	while True:
		time.sleep(1)
