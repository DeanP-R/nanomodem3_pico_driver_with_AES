#########################################################################################################
# Filename      : main.py                                                                               #
# Version       : 0.0.3                                                                                 #
# Description   : Main program for handling communications for MEng Ropeless Fishing Gear Demonstrator. #
#                  With Encryption using AES-256
# Author        : Dean Rowlett                                                                          #
# Target        : Raspberry Pi Pico W with MicroPython                                                  #
# Interpreter   : MicroPython v1.22.1                                                                   #
# IDE           : Thonny 4.1.4                                                                          #
# Last Updated  : 11th February 2024                                                                    #
#########################################################################################################
"""
from nm3_pico_driver import NM3Driver
message = "Ocean Lab Test"
modem = 169

pico = NM3Driver()
pico.connect()
#addr = pico.get_address()
#print(f"Address: {addr}")

voltage = pico.get_voltage()
print(f"Voltage: {voltage}")
distance = str(pico.ping(modem))

print(f"Distance to modem 169: {distance}")
send_test = pico.send_unicast_message(modem, distance)
print(f"Sending message: {message}. To modem: {modem}. Returning: {send_test}.")
"""
pico = NM3Driver()
pico.connect()
print("Ping 169", pico.ping(169))
pico.send_unicast_message(169, "Test")
