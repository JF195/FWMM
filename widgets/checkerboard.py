from widget import Widget as WidgetBase
from widget_config_item import WidgetConfigItem as Config
from widget_config_item import ConfigItemType as ConfigType
from const import WIDTH, HEIGHT
import numpy as np

class Widget(WidgetBase):
    name = "Checkerboard"
    desired_spf = -1
    allow_rotation = False

    def __init__(self):
        super().__init__()
        self.configuration = {
            "Board Width": Config(ConfigType.integer, 5, 1, WIDTH),
            "Board Height": Config(ConfigType.integer, 5, 1, HEIGHT),
            "Board Size": Config(ConfigType.integer, 1, 1, WIDTH),
            "X Offset": Config(ConfigType.integer, 0, 0, WIDTH),
            "Y Offset": Config(ConfigType.integer, 0, 0, HEIGHT),
            "Brightness": Config(ConfigType.integer, 255, 0, 255)
        }

    def get_current_size(self):
        return [self.configuration["Board Width"].value, self.configuration["Board Height"].value]
    
    def get_desired_spf(self):
        return -1

    def get_frame(self):
        width = self.configuration["Board Width"].value
        height = self.configuration["Board Height"].value
        size = self.configuration["Board Size"].value

        xoff = self.configuration["X Offset"].value
        yoff = self.configuration["Y Offset"].value

        base = np.matrix([[int( (((x + xoff) // size) % 2) + (((y + yoff) // size) % 2) != 1 ) * self.configuration["Brightness"].value for x in range(width)] for y in range(height)]) # type: ignore

        return base
