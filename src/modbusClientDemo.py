from pyModbusTCP.client import ModbusClient

for i in range(1502,1503):

    try:
        c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    except ValueError:
        print ("Error with host or port params")


    if c.open():
        c.write_single_register(0,65000)
        # c.write_multiple_coils(0, [True,True,True])
        # c.write_multiple_registers(0, [65000]*30)
        # c.write_single_coil(0, True)
        # c.write_single_register(0, 250)

        c.close()
        print("Test success at address  : {}".format(i))
    else:
        print("Test failed at address  : {}".format(i))

for i in range(1505,1506):

    try:
        c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    except ValueError:
        print ("Error with host or port params")


    if c.open():
        reg_list = c.read_input_registers(49, 10)
        print(reg_list)
        # c.write_multiple_coils(0, [True,True,True])
        # c.write_multiple_registers(0, [65000]*30)
        # c.write_single_coil(0, True)
        # c.write_single_register(0, 250)

        c.close()
        print("Test success at address  : {}".format(i))
    else:
        print("Test failed at address  : {}".format(i))

