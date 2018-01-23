import time
import sys
import ibmiotf.application

try:
  options = {
    "org": "sua org",
    "id": "seu app id",
    "auth-method": "apikey",
    "auth-key": "seu auth key",
    "auth-token": "seu auth token",
    "clean-session": "true"
  }
  client = ibmiotf.application.Client(options)
except ibmiotf.ConnectionException as e:
  print(str(e))
  sys.exit()

try:
   orgDetail = client.api.getOrganizationDetails()
except IoTFCReSTException as e:
  print("ERROR [" + e.httpcode + "] " + e.message)
