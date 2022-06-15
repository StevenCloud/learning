from BramblPy import brambl
from BramblPy.brambl.credentials import credential_manager

keyMan = credential_manager(password = "PASSWORD", networkPrefix = "valhalla")

dirPath = "./keyfiles"
keyMan.exportToFile(dirPath)
