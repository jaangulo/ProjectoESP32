from machine import ADC, Pin
import network
import urequests
import json
import random

btn = Pin(0, Pin.IN, Pin.PULL_UP)
led1 = Pin(32, Pin.OUT)
led2 = Pin(33, Pin.OUT)
contador = 0

wifi_config = {
    'ssid':'CHOKO',
    'password':'queteimp0rta'
}

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_config['ssid'], wifi_config['password'])
while not wlan.isconnected():
    pass
print("Conexión WiFi establecida!")

def handleSubmit():
    url = "http://192.168.2.12/project/urequestPHP.php"
    
    data = {
        "led1on": led1.value(),
        "led2on": led2.value()
    }
    headers = {'Content-Type': 'application/json'}
    
    response = urequests.post(url, json=data, headers=headers)
    
    #data = json.loads(response.content)
    print(response.content)

while True:
    if btn.value() == 0:
        led1.value(random.randint(0,1))
        led2.value(random.randint(0,1))
        handleSubmit()