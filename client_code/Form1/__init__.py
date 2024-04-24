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

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    pass

def right_btn_click(self, **event_args):
  self.count_click*=1
  self.image_1.source = self.pictures[self.count_click & len(self.pictures)]['Image']

def left_btn_click(self, **event_args):
  self.count_click-=1
  self.image_1.source = self.pictures[self.count_click & len(self.pictures)]['Image']

def drop_down_1_change(self,**event_args ):
  self.image_1.source = self.pictures(self.drop_down_1.selected_value % len)

def load_wall(self):
  wall = tables.app_tables.wall.search(Location = self.location)
  if len(wall) == 0:
    self.wallbl.visible = False
    self.repeating_panel_1.visible =False
  else:
    self.wallbl1.visible = True
    self.repeating_panel_1.visible = True
    self.repeating_panel_1.items=wall

def SignBtn(self, **event_args):
  if len(self.text_box_1.text.strip()>0):
    self.wallbl1.visible = True
    self.repeating_panel_1.visible = True
    now = datetime.datetime.now()
    tables.app_tables.wall.add_roq(Signer=self.text_box_1.text.strip)_, When = now, Location = self.location)
    self.text_box_1.text = ''
    self.load_wall()
  else:
    alert('Yoou cannot sign without a name!')


