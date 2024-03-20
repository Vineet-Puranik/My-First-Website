from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.bannerLbl.text = 'My Webpage Banner'

    # Any code you write here will run before the form opens.
  def AddABtn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bannerLbl.text += 'a'

  def DELletter_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.bannerLbl.text = self.bannerLbl.text[:-1]

