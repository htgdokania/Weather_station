# Necessary Libraries to be Imported
import machine
import ssd1306
import utime
#Specifiy Desired Pins For CLK and DATA respectively
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))

#Creation of Display Object using SSD1306 Library and binding it to I2C bus
# 128 is X direction pixels and 32 is y direction pixels
display = ssd1306.SSD1306_I2C(128, 64, i2c)
# Fill the Display with 0's
display.fill(0)
# Set a pixel in the origin 0,0 position.
display.text("Hello", 0, 0)
#Display the above on to display
display.show()
utime.sleep_ms(1000)