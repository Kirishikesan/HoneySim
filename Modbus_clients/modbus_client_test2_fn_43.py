from pymodbus.client.sync import ModbusTcpClient
from pymodbus.mei_message import ReadDeviceInformationRequest
from pymodbus.device import *
from pyModbusTCP.client import ModbusClient

client=ModbusTcpClient('127.0.0.1','1514')
# try:
#     client=ModbusClient(host="127.0.0.1", port=1502, unit_id=1, auto_open=True, debug=False)
# except ValueError:
#     print ("Error with host or port params")
# result1 = client.read_coils(9,10)
# result2 = client.read_holding_registers(0, 11)
# result3 = client.read_input_registers(0, 11)
# result4 = client.read_discrete_inputs(3, 5)

# print(result1.bits)
# print(result2.registers)
# print(result3.registers)
# print(result4.bits)

rq = ReadDeviceInformationRequest(unit=1,read_code=3)
rr = client.execute(rq)
print(rr.information)
client.close()