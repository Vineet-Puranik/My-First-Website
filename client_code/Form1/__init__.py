from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.bannerLbl.text = 'My Webpage Banner'
    self.repeating_panel_1.items = ['a','b','c','d']
    # Any code you write here will run before the form opens.
  def AddABtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bannerLbl.text += 'a'

  def DELletter_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bannerLbl.text = self.bannerLbl.text[:-1]

  def map_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass
  self.map_1.center = GoogleMap.LatLng(30.286736,-97.737654)
  self.map_1.zoom = 15
  self.map_1.clickable_icons = False
  self.map_1.fullscreen_control = False

  pins = tables.app_tables.locations.search()
  self.markerList = []
  ind = 0
  for pin in pins:
    self.markerList.append(GoogleMap.Marker(animation=GoogleMap.Animation.DROOP,position = GoogleMap.LatLng(pin['Lat',pin['Lon']])))
    self.markerList[ind].tag = pin
    self.markerList[ind].add_event_handler('click', self.marker_click)
    self.map_1.add_component(self.markerList[ind])
    ind +=1

  def marker_click(self,sender,**properties):
    self.infoAbtPin.visible = True
    self.count_click +=1
    self.infoAbtPin.text = 'You have clicked a pin ' + str(self.count_click) + ' time'
    if self.count_click >1:
      self.infoAbtPin.text = 'a'




