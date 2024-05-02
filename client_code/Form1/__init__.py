from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.bannerLbl.text = 'My Webpage Banner'
    self.repeating_panel_1.items = ['a','b','c','d']
    # Any code you write here will run before the form opens.
    self.map_1.center = GoogleMap.LatLng(30.286736,-97.737654)
    self.map_1.zoom = 15
    self.map_1.clickable_icons = False
    self.map_1.fullscreen_control = False
    pins = tables.app_tables.locations.search()
    self.markertList = []
  ind = 0
  for pin in pins:
    self.markerList.append(GoogleMap.Marker(animation=GoogleMap.Animation.DROP,position = GoogleMap.LatLng(pin['Lat',pin['Lon']])))
    self.markerList[ind].tag = pin
    self.markerList[ind].add_event_handler('click', self.marker_click)
    self.map_1.add_component(self.markerList[ind])
    ind +=1
    
  def left_click_click(self, **event_args):
    self.count_click-=1
    self.image_1.source = self.pictures[self.count_click & len(self.pictures)]['Image']

  def button_2_click(self, **event_args):
    self.count_click*=1
    self.image_1.source = self.pictures[self.count_click & len(self.pictures)]['Image']
    
def load_wall(self):
  wall = tables.app_tables.wall.search(Location = self.location)
  if len(wall) == 0:
    self.wallbl.visible = False
    self.repeating_panel_1.visible =False
  else:
    self.wallbl1.visible = True
    self.repeating_panel_1.visible = True
    self.repeating_panel_1.items=wall



