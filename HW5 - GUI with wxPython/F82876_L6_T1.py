import wx
class windowClass(wx.Frame):
 
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
 
        self.basicGUI()
 
    def basicGUI(self):
       
        panel = wx.Panel(self)
       
        menuBar = wx.MenuBar()
       
        fileButton = wx.Menu()
       
        exitItem = fileButton.Append(wx.ID_EXIT,'Exit','status msg..')
 
        menuBar.Append(fileButton,"&File")
 
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit,exitItem)
       
 
 
 
 
 
 
       
       
        aweText = wx.StaticText(panel,-1,"Body Mass Index", (15,19))
        #aweText.SetForegroundColour('#67cddc')
        weightText = wx.StaticText(panel,-1,"weight:",(15,75))
        heightText = wx.StaticText(panel,-1,"height:",(15,140))
        self.over_result_text = wx.StaticText(panel,-1,"Result:",(260,85))
        self.result_text = wx.StaticText(panel,-1,"",(248,105))
 
        self.weight = wx.SpinCtrl(panel,value='0',pos=(150,70),size=(60,-1),min = 0,
        max = 300)
        self.height = wx.SpinCtrl(panel,value='0',pos=(150,135),size=(60,-1),min = 0,
        max = 300)
 
        self.btn = wx.Button(panel,label='Compute',pos=(60,230),size=(80,-1))
        self.btn.Bind(wx.EVT_BUTTON,self.onCompute)
       
        self.close_btn = wx.Button(panel,label='Close',pos=(240,230),size=(80,-1))
        self.close_btn.Bind(wx.EVT_BUTTON,self.Quit)
 
 
        self.SetTitle('wx.SpinCtrl')
 
        self.Centre()
        self.Show(True)
    def Quit(self,e):
        self.Close()
    def onCompute(self,e):
        if(self.height.GetValue() == 0 or self.weight.GetValue() == 0):
            self.result_text.SetLabel("Error ! Can't devide by zero.")
        else:
            self.result_text.SetLabel(str(self.compute_BMI(self.height.GetValue(),
            self.weight.GetValue())))
        self.btn.SetBackgroundColour((0,0,255))
        #time.sleep(0.1)
        self.btn.SetBackgroundColour((0,255,0))
 
    def compute_BMI(self,height,weight):
        height_m = float(height) / 100
        BMI = weight/(height_m*height_m)
        return BMI
def main():
    app = wx.App()
 
    windowClass(None,title="classic",size=(380,320))
 
 
    app.MainLoop()
 
main()
