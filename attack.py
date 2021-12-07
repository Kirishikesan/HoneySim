from pyModbusTCP.client import ModbusClient
import time

for j in range(2):
    for i in range(1515,1516):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            c.write_single_register(0,30000)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Write success at address  : {}".format(i))
        else:
            c.close()
            print("Write failed at address  : {}".format(i))