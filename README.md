# appium_test
Appium tests

Please validate that the Python version configured in the laptot does be 3.0

# Configure Appium server

Install the appium server according the used SO
http://appium.io/downloads.html

When starting the appium server, go to the advance option and check the "Allow Session Override" option

# Run Test:

isntall Appium-Python-Client library with the follow command:

- pip install Appium-Python-Client
 
To execute the project, please put the follow command in a terminal window:

    -  python test.py prueba_command python3 test.py {contact_name} {phone_number} 
 
 the {contact_name} argument please updapted it with the name of a new contact, in the {phone_number} put any phone number

# PD: The project is configured only to execute in an Androide real device, please update the platformVersion, deviceName and the udid with the values of yours device.
