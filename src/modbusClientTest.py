from pyModbusTCP.client import ModbusClient
import time

def writeSingleRegister(reg,value,address):
    for j in range(2):
        i=address
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")
        if c.open():
            c.write_single_register(reg,value)
            c.close()
            print("Write success at address  : {}".format(i))
        else:
            c.close()
            print("Write failed at address  : {}".format(i))

def writeSingleCoil(reg,value,address):
    for j in range(2):
        i=address
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")
        if c.open():
            c.write_single_coil(reg,value)
            c.close()
            print("Write success at address  : {}".format(i))
        else:
            c.close()
            print("Write failed at address  : {}".format(i))

def readInputRegisters(reg,num,address):
    for j in range(2):
        i=address
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")
        if c.open():
            reg_list = c.read_input_registers(reg, num)
            print(reg_list)
            c.close()
            print("Read success at address  : {}".format(i))
        else:
            c.close()
            print("Read failed at address  : {}".format(i))

def readHoldingRegisters(reg,num,address):
    for j in range(2):
        i=address
        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")
        if c.open():
            reg_list = c.read_holding_registers(reg, num)
            print(reg_list)
            c.close()
            print("Read success at address  : {}".format(i))
        else:
            c.close()
            print("Read failed at address  : {}".format(i))
############################################################################

writeSingleRegister(0,65000,1502)

while(True):
    readInputRegisters(49,10,1502)
    time.sleep(2)

