import wx


class Window(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 300))
        self.Maximize()

        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)



        panel.SetSizer(main_sizer)


app = wx.App()
wnd = Window(None, 'Alma')
wnd.Show()
app.MainLoop()
