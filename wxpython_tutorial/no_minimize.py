import wx

app = wx.App()
frame = wx.Frame(None, style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
		| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
frame.Show(True)

frame1 = wx.Frame(None, style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
		| wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
frame1.Show(True)

app.MainLoop()
