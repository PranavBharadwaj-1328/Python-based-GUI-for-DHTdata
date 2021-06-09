import paho.mqtt as mqtt
import paho.mqtt.subscribe as subscribe
import time
import json
from tkinter import *
# The ThingSpeak Channel ID.
# Replace <YOUR-CHANNEL-ID> with your channel ID.
channelID = "1379680"
# The write API key for the channel.
# Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
readAPIKey = "4509YU9SIR82AAQE"
# The hostname of the ThingSpeak MQTT broker.
mqttHost = "mqtt.thingspeak.com"
# You can use any username.
mqttUsername = "mwa0000022383501"
# Your MQTT API key from Account > My Profile.
mqttAPIKey = "43GRWC90R8UAF2LE"
# Create the topic string.
topic = "channels/" + channelID + "/subscribe/json/" + readAPIKey
window = Tk()
window.title("DHT Data")
window.geometry("200x100")
label_a = Label(text="Temperature:")
label_a.grid(padx= 10,pady=10)
label_b = Label(text="Humidity:")
label_b.grid(padx=10,pady=10)
while(True):
	degree_sign = u"\N{DEGREE SIGN}"
	try:
		msg = subscribe.simple(topic, hostname=mqttHost, auth={'username':mqttUsername,'password':mqttAPIKey})
		entry = json.loads(msg.payload)
		temp = "Temperature: "+str(entry["field1"])+degree_sign+"C"
		label_a.config(text=temp)
		print ("Temperature:"+str(entry["field1"]))
		humid = "Humidity: "+str(entry["field2"])+"%"
		label_b.config(text=humid)
		print ("Humidity: "+str(entry["field2"]))
	except KeyboardInterrupt:
		print("Bye")
	except:
		print("Inherent Error")
	window.update()
	time.sleep(10)

