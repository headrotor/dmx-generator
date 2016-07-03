# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

m_mniOpenId = 1000
m_mniSaveId = 1001
m_mniExitId = 1002
m_mniAboutId = 1003

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"RGBY Control", pos = wx.DefaultPosition, size = wx.Size( 345,693 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btLedOn = wx.Button( self.m_panel, wx.ID_ANY, u"ALL ON", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btLedOn, 0, wx.ALL, 5 )
		
		self.m_btLedOff = wx.Button( self.m_panel, wx.ID_ANY, u"ALL OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_btLedOff, 0, wx.ALL, 5 )
		
		self.m_Rslider = wx.Slider( self.m_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,200 ), wx.SL_BOTH|wx.SL_INVERSE|wx.SL_VERTICAL )
		self.m_Rslider.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer5.Add( self.m_Rslider, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Red", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer5.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_btSVROn = wx.Button( self.m_panel, wx.ID_ANY, u"DMX ON", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_btSVROn, 0, wx.ALL, 5 )
		
		self.m_btSVROff = wx.Button( self.m_panel, wx.ID_ANY, u"DMX OFF", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_btSVROff, 0, wx.ALL, 5 )
		
		self.m_Gslider = wx.Slider( self.m_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,200 ), wx.SL_BOTH|wx.SL_INVERSE|wx.SL_VERTICAL )
		self.m_Gslider.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )
		
		bSizer51.Add( self.m_Gslider, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Green", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		bSizer51.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer4.Add( bSizer51, 1, wx.EXPAND, 5 )
		
		bSizer52 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_SWtoggle = wx.ToggleButton( self.m_panel, wx.ID_ANY, u"SW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SWtoggle.SetValue( True ) 
		bSizer52.Add( self.m_SWtoggle, 0, wx.ALL, 5 )
		
		self.m_SEtoggle = wx.ToggleButton( self.m_panel, wx.ID_ANY, u"SE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_SEtoggle.SetValue( True ) 
		bSizer52.Add( self.m_SEtoggle, 0, wx.ALL, 5 )
		
		self.m_Bslider = wx.Slider( self.m_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,200 ), wx.SL_BOTH|wx.SL_INVERSE|wx.SL_VERTICAL )
		self.m_Bslider.SetBackgroundColour( wx.Colour( 0, 0, 255 ) )
		
		bSizer52.Add( self.m_Bslider, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Blue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer52.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer4.Add( bSizer52, 1, wx.EXPAND, 5 )
		
		bSizer53 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_NWtoggle = wx.ToggleButton( self.m_panel, wx.ID_ANY, u"NW", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_NWtoggle.SetValue( True ) 
		bSizer53.Add( self.m_NWtoggle, 0, wx.ALL, 5 )
		
		self.m_NEtoggle = wx.ToggleButton( self.m_panel, wx.ID_ANY, u"NE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_NEtoggle.SetValue( True ) 
		bSizer53.Add( self.m_NEtoggle, 0, wx.ALL, 5 )
		
		self.m_Yslider = wx.Slider( self.m_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,200 ), wx.SL_BOTH|wx.SL_INVERSE|wx.SL_VERTICAL )
		self.m_Yslider.SetBackgroundColour( wx.Colour( 255, 128, 0 ) )
		
		bSizer53.Add( self.m_Yslider, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Amber", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		bSizer53.Add( self.m_staticText13, 0, wx.ALIGN_CENTER, 5 )
		
		
		bSizer4.Add( bSizer53, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer54 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_Hslider = wx.Slider( self.m_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,200 ), wx.SL_INVERSE|wx.SL_LABELS|wx.SL_SELRANGE|wx.SL_VERTICAL )
		bSizer54.Add( self.m_Hslider, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Hue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		bSizer54.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		
		bSizer41.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		bSizer511 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_Sslider = wx.Slider( self.m_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,200 ), wx.SL_INVERSE|wx.SL_LABELS|wx.SL_SELRANGE|wx.SL_VERTICAL )
		bSizer511.Add( self.m_Sslider, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Saturation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		bSizer511.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		
		bSizer41.Add( bSizer511, 1, wx.EXPAND, 5 )
		
		bSizer521 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_Vslider = wx.Slider( self.m_panel, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( -1,200 ), wx.SL_INVERSE|wx.SL_LABELS|wx.SL_SELRANGE|wx.SL_VERTICAL )
		bSizer521.Add( self.m_Vslider, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer521.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 5 )
		
		
		bSizer41.Add( bSizer521, 1, wx.EXPAND, 5 )
		
		bSizer531 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer24.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		m_RGBY_selectChoices = [ u"RGB", u"RGBY", u"sRGBY" ]
		self.m_RGBY_select = wx.RadioBox( self.m_panel, wx.ID_ANY, u"RGBY mode", wx.DefaultPosition, wx.DefaultSize, m_RGBY_selectChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_RGBY_select.SetSelection( 2 )
		bSizer24.Add( self.m_RGBY_select, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer24.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer531.Add( bSizer24, 1, wx.EXPAND, 5 )
		
		
		bSizer41.Add( bSizer531, 1, wx.EXPAND, 5 )
		
		
		bSizer31.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer31, 0, wx.EXPAND, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel, wx.ID_ANY, u"spread", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer15.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.m_spread = wx.Slider( self.m_panel, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer15.Add( self.m_spread, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer15, 0, wx.EXPAND, 5 )
		
		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText9 = wx.StaticText( self.m_panel, wx.ID_ANY, u"rotate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer16.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.m_rotate = wx.Slider( self.m_panel, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer16.Add( self.m_rotate, 1, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer16, 0, wx.EXPAND, 5 )
		
		
		self.m_panel.SetSizer( bSizer3 )
		self.m_panel.Layout()
		bSizer3.Fit( self.m_panel )
		bSizer2.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_mnFile = wx.Menu()
		self.m_mniOpen = wx.MenuItem( self.m_mnFile, m_mniOpenId, u"&Open...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniOpen )
		
		self.m_mniSave = wx.MenuItem( self.m_mnFile, m_mniSaveId, u"&Save...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniSave )
		
		self.m_mnFile.AppendSeparator()
		
		self.m_mniExit = wx.MenuItem( self.m_mnFile, m_mniExitId, u"&Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniExit )
		
		self.m_menubar.Append( self.m_mnFile, u"&File" ) 
		
		self.m_mnHelp = wx.Menu()
		self.m_mniAbout = wx.MenuItem( self.m_mnHelp, m_mniAboutId, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnHelp.AppendItem( self.m_mniAbout )
		
		self.m_menubar.Append( self.m_mnHelp, u"&?" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		
		# Connect Events
		self.m_btLedOn.Bind( wx.EVT_BUTTON, self.m_btLedOnOnButtonClick )
		self.m_btLedOff.Bind( wx.EVT_BUTTON, self.m_btLedOffOnButtonClick )
		self.m_Rslider.Bind( wx.EVT_SCROLL, self.m_RGBOnScroll )
		self.m_btSVROn.Bind( wx.EVT_BUTTON, self.m_btSVROnOnButtonClick )
		self.m_btSVROff.Bind( wx.EVT_BUTTON, self.m_btSVROffOnButtonClick )
		self.m_Gslider.Bind( wx.EVT_SCROLL, self.m_RGBOnScroll )
		self.m_Bslider.Bind( wx.EVT_SCROLL, self.m_RGBOnScroll )
		self.m_Yslider.Bind( wx.EVT_SCROLL, self.m_RGBOnScroll )
		self.m_Hslider.Bind( wx.EVT_SCROLL, self.m_HSVOnScroll )
		self.m_Sslider.Bind( wx.EVT_SCROLL, self.m_HSVOnScroll )
		self.m_Vslider.Bind( wx.EVT_SCROLL, self.m_HSVOnScroll )
		self.Bind( wx.EVT_MENU, self.m_mniOpenClick, id = self.m_mniOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniSaveClick, id = self.m_mniSave.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = self.m_mniExit.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniAboutClick, id = self.m_mniAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_btLedOnOnButtonClick( self, event ):
		event.Skip()
	
	def m_btLedOffOnButtonClick( self, event ):
		event.Skip()
	
	def m_RGBOnScroll( self, event ):
		event.Skip()
	
	def m_btSVROnOnButtonClick( self, event ):
		event.Skip()
	
	def m_btSVROffOnButtonClick( self, event ):
		event.Skip()
	
	
	
	
	def m_HSVOnScroll( self, event ):
		event.Skip()
	
	
	
	def m_mniOpenClick( self, event ):
		event.Skip()
	
	def m_mniSaveClick( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
	
	def m_mniAboutClick( self, event ):
		event.Skip()
	

