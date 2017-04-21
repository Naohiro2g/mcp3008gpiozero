# mcp3008gpiozero
# Simple usage of MCP3008 10-bit Analog-to-Digital Converter

This code is used to interface with 4 electrical devices namely potentiometer, LDR, and temperature sensors MCP9701 & MCP9700.
Only gpiozero libraries required for this simple test.

Components mapping:

Potentiometer = CH0<br>
LDR = CH1<br>
MCP9701 = CH2<br>
MCP9700 = CH3<br>

For MCP3008 connection to Raspberry Pi, please refer to this link.
https://www.mathworks.com/help/examples/raspberrypiio_product/win64/mcp3008_circuit.png

MCP9701/MCP9700 pinout reference. Connect V+ of both devices to 3.3V Vref of MCP3008.
http://ww1.microchip.com/downloads/en/DeviceDoc/21942e.pdf

Credit to this page for Temperature Calcution Formula.
https://phanderson.com/PIC/PICC/sourceboost/mcp9701.html
