import time   
    
#Figure out whether or not to use the data
def display_temp():
    thermometer_file = open('/sys/bus/w1/devices/28-01191a3eea60/w1_slave')
    aline = thermometer_file.readlines() 
    if 'YES' in aline[0]:
        values = aline[1].split()
        temp_str = values[9]
        temp_int = int(temp_str[2:])
        temp_reading = temp_int/1000
        thermometer_file.close()
    return temp_reading

while True:
    print(display_temp())
    time.sleep(1)
        
    