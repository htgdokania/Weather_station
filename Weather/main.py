#import network and socket libraries to connect with wifi and receive data from the server.
import network
import socket
#For Parsing Json data and Getting response from URLs
import urequests
import utime
# Libraries to communicate with the OLED Display
import machine
import ssd1306

#Specifiy Desired Pins For CLK and DATA respectively
i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
# 128 is X direction pixels and 32 is y direction pixels
display = ssd1306.SSD1306_I2C(128, 64, i2c)


def connect_Wifi():
    # Fill the Display with 0's
    display.fill(0)
    display.text('connecting....', 0, 0)
    display.show()
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network')
        wlan.connect('SWATI', '8585865764')
        while not wlan.isconnected():
            pass
    print('network config', wlan.ifconfig())
    display.text('Connected', 0, 20)
    display.show()
    utime.sleep_ms(1000)

def get_data():
    response = urequests.get("https://www.metaweather.com/api/location/2295386/")
    data = response.json()
    return data


def print_climate_data(data):
    for i in range(6):  # 6 for next 6 days forecast. If you want only today's forecast change it to 1.
        # Fill the Display with 0's
        # This will reset the screen and avoid overwriting
        display.fill(0)

        place = data["title"]
        # Get Todays Data First
        weather = data["consolidated_weather"][i]
        date_today = weather["applicable_date"]
        weather_today = weather["weather_state_name"]
        temperature = weather["the_temp"]
        Humidity = weather["humidity"]

        # print on OLED Display
        display.text(place, 0, 0)
        display.text(date_today, 0, 15)
        display.text(weather_today, 0, 30)
        display.text(str(temperature), 0, 45)  # we need convert temperature to string in order to display.
        # Display the above on to display
        display.show()
        utime.sleep_ms(5000)  # give a 2 sec delay inbetween two days.
        
connect_Wifi()
while 1:
	data=get_data()
    print_climate_data(data)

