from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime

class Form1(Form1Template):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.count_click = 0
    self.map_1.center = GoogleMap.LatLng(30.286736, -97.737654)
    self.map_1.zoom = 15
    self.map_1.clickable_icons = False
    self.map_1.fullscreen_control = False
    pins = tables.app_tables.locations_2.search()
    self.markerList = []
    ind = 0
    for pin in pins:
      self.markerList.append(GoogleMap.Marker(animation=GoogleMap.Animation.DROP, position=GoogleMap.LatLng(pin['Lat'], pin['Lon'])))
      self.markerList[ind].tag = pin
      self.markerList[ind].add_event_handler('click', self.marker_click)
      self.map_1.add_component(self.markerList[ind])
      ind += 1

  def marker_click(self, sender, **properties):
    self.infoAbtPin.visible = True
    self.desc.visible = True
    self.count_click += 1
    self.infoAbtPin.text = 'You have clicked a pin ' + str(self.count_click) + ' time'
    if self.count_click > 1:
      self.infoAbtPin.text += 's'
    self.infoAbtPin.text += '\nThis pin\'s location is ' + str(sender.tag['Lat']) + ' North, ' + str(sender.tag['Lon']) + ' West'
    self.infoAbtPin.text += '\nIt is called ' + sender.tag['Name']
    self.image_1.visible = True
    self.right_btn.visible = True
    self.left_btn.visible = True
    self.pictures = tables.app_tables.images.search(Location=sender.tag)
    self.location = sender.tag
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']
    self.desc.text = self.pictures[self.count_click % len(self.pictures)]['Description']
    self.load_wall() 

  def text_box_1_pressed_enter(self, **event_args):
    pass

  def text_box_2_pressed_enter(self, **event_args):
    self.signBtn_click()
  
  def signBtn_click(self, **event_args):
    name = self.text_box_1.text.strip()
    comment = self.text_box_2.text.strip()

    if len(name) and len(comment) > 0:
      self.wallLbl.visible = False
      self.repeating_panel_1.visible = False
        #now = datetime.datetime.now()
      tables.app_tables.wall.add_row(Signer=self.text_box_1.text.strip(), When=datetime.now(), Location = self.location, Comment=self.text_box_2.text)
      self.text_box_1.text = ''
      self.text_box_2.text = ''
      self.load_wall()
    else:
      alert('You cannot comment without a name!')

  def load_wall(self):
    wall = tables.app_tables.wall.search(Location=self.location)
    if len(wall) == 0:
      self.wallLbl.visible = True
      self.repeating_panel_1.visible = True
    else:
      self.wallLbl.visible = True
      self.repeating_panel_1.visible = True
      self.repeating_panel_1.items = wall

  def left_btn_click(self, **event_args):
    self.count_click -= 1
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']
    self.desc.text = self.pictures[self.count_click % len(self.pictures)]['Description']

  def right_btn_click(self, **event_args):
    self.count_click += 1
    self.image_1.source = self.pictures[self.count_click % len(self.pictures)]['Image']
    self.desc.text = self.pictures[self.count_click % len(self.pictures)]['Description']




 
  
 



