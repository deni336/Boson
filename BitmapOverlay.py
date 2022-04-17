from tkinter import BitmapImage
import CameraEngine as CE

thermalTempOverlay = BitmapImage(CE.callThermalData())
print(thermalTempOverlay)
