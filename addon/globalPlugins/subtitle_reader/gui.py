#encoding=utf-8

from __future__ import absolute_import

import addonHandler
addonHandler.initTranslation()

import wx
import gui

tray = gui.mainFrame.sysTrayIcon
toolsMenu = tray.toolsMenu

class Menu(wx.Menu):
	def __init__(self):
		super(Menu, self).__init__()
		self.menuItem = toolsMenu.AppendSubMenu(self, _(u'字幕閱讀器 (&R)'))
		self.switch = self.AppendCheckItem(wx.ID_ANY, _(u'閱讀器開關 (&S)'))
		self.switch.Check(True)
		
		self.infoCardPrompt = self.AppendCheckItem(wx.ID_ANY, _(u'資訊卡提示(&I)'))
		self.infoCardPrompt.Check(True)
		
		self.checkForUpdate = self.Append(wx.ID_ANY, _(u'立即檢查更新(&C)'))
		
		self.openChangeLog = self.Append(wx.ID_ANY, _(u'開啟更新日誌(&O)'))
		
		self.checkUpdateAutomatic = self.AppendCheckItem(wx.ID_ANY, _(u'自動檢查更新(&A)'))
		self.checkUpdateAutomatic.Check(True)
	

class UpdateDialog(wx.Dialog):
	def __init__(self, version):
		super(UpdateDialog, self).__init__(gui.mainFrame, title=_(u'字幕閱讀器 V') + str(version) + _(u' 新版資訊'))
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.changeLogLabel = wx.StaticText(self, label=_(u'更新日誌'))
		self.changelogText = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2 | wx.HSCROLL, size=(700, -1))
		self.progress = wx.Gauge(self, style=wx.GA_VERTICAL)
		self.updateNow = wx.Button(self, label=_(u'現在更新(&U)'))
		self.skipVersion = wx.Button(self, label=_(u'跳過此版本(&S)'))
		self.later = wx.Button(self, label=_(u'晚點再說(&L)'))
		self.SetSizerAndFit(self.sizer)
	
