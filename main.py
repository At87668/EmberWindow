import win32gui
import pygetwindow as gw
class EmbedWindow(object):
    def __init__(self,parent_title,child_title):
        self.pt=parent_title
        self.ct=child_title
        self.SetWindow(self.pt,self.ct)
    def SetWindow(self,parent_title,child_title):
        self.pt=parent_title
        self.ct=child_title
        self.ph=win32gui.FindWindow(None,self.pt)
        self.ch=win32gui.FindWindow(None,self.ct)
        self.hlist=["ParentHwnd:{}".format(self.ph),"ChildHwnd:{}".format(self.ch)]
        win32gui.SetParent(self.ch,self.ph)
        return self.hlist
    def GetAllTitle(self):
        self.titles=gw.getAllTitles()
        return self.titles
    def AuthorValidate(self):
        return "AuthorId:<Github:At87668> <BiliBili:Author87668>"
'''
### EmberWindow
### A new building. ,
### Version is now beta 1.0.2.
### It is nested window provides a simple way.
### It is the author of At87668.
### We will continue to update it !
'''
