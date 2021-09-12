from pymodbus.client.sync import ModbusTcpClient
from pymodbus.mei_message import ReadDeviceInformationRequest
from pymodbus.device import *

client = ModbusTcpClient('192.168.8.182','5020')
result1 = client.read_coils(9,10)
result2 = client.read_holding_registers(0, 11)
result3 = client.read_input_registers(0, 11)
result4 = client.read_discrete_inputs(3, 5)

print(result1.bits)
print(result2.registers)
print(result3.registers)
print(result4.bits)


rq = ReadDeviceInformationRequest(unit=1,read_code=0x03)
rr = client.execute(rq)

print(rr.information)
print(rr.read_code)
client.close()