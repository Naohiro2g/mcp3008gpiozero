#!/usr/bin/env python

from gpiozero import MCP3008,PWMLED
from time import sleep
pot = MCP3008(0)
ldr = MCP3008(1)
temp1 = MCP3008(2)
temp2 = MCP3008(3)

led = PWMLED(21)
while True:
	T = 15 * temp1.raw_value - 2048
	T2 = 15 * temp2.raw_value - 2048

	whole = T / 100
	fract = T % 100
	whole2 = ( T2 / 100 ) + 5
	fract2 = T2 % 100

	if (fract < 10):
		print("Temp1: {}.{}".format(whole,0))
	else:
		print("Temp1: {}.{}".format(whole,fract))

	if (fract2 < 10):
		print("Temp2: {}.{}".format(whole2,0))
	else:
		print("Temp2: {}.{}".format(whole2,fract2))


	print("pot:{:.2f} ldr:{:.2f} temp1:{:.2f}".format(pot.raw_value,ldr.value,T))
	sleep(0.5)
	led.source = pot.values
