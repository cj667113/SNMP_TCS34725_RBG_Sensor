import smbus
import time
bus = smbus.SMBus(1)
bus.write_byte(0x29,0x80|0x12)
ver = bus.read_byte(0x29)
if ver == 0x44:
 bus.write_byte(0x29, 0x80|0x00) # 0x00 = ENABLE register
 bus.write_byte(0x29, 0x01|0x02) # 0x01 = Power on, 0x02 RGB sensors enabled
 bus.write_byte(0x29, 0x80|0x14) # Reading results start register 14, LSB then MSB
 while True:
  data = bus.read_i2c_block_data(0x29, 0)
  clear = clear = data[1] << 8 | data[0]
  red = data[3] << 8 | data[2]
  green = data[5] << 8 | data[4]
  blue = data[7] << 8 | data[6]
  clear = (clear/256)
  red = (red/256)
  green = (green/256)
  blue = (blue/256)
  crgb = "C: %s, R: %s, G: %s, B: %s\n" % (clear, red, green, blue)
  #print crgb
  if red > ((green*1.2)+1) and red > ((blue*1.2)+1):
	print "On"
  else:
	print "off"
else:
 print "Device not found\n"
