from StarPanel import StarPanel
from StarPanel import makeASolarSystem
from GUI import GUI

starPanel = StarPanel()
makeASolarSystem(starPanel)
gui = GUI(starPanel)
raw_input()

