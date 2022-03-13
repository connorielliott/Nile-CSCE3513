import time
import wx
import wx.adv

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
		
		time.sleep(3)
		
		print("ending splash screen...")
		self.Close()

if __name__ == "__main__":
	app = wx.App(False)
	frame = MyFrame()
	app.MainLoop()
