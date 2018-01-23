import time
import sys
import ibmiotf.application
import ibmiotf.device
deviceOptions = {
  "org": "sua org",
  "type": "seu device",
  "id": "seu id",
  "auth-method": "token",
  "auth-token": "seu password"
}
try:
  deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
  print("Caught exception connecting device: %s" % str(e))
  sys.exit()
deviceCli.connect()
for x in range (0,10):
  data = { 'hello' : 'world', 'x' : x}
  deviceCli.publishEvent("greeting", "json", data)
  time.sleep(1)

deviceCli.disconnect()