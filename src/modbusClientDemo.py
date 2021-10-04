from pyModbusTCP.client import ModbusClient
import time

for j in range(2):
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
            c.close()
            print("Test failed at address  : {}".format(i))
for j in range(2):
    for i in range(1515,1518):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            c.write_single_register(0,20000)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Test success at address  : {}".format(i))
        else:
            c.close()
            print("Test failed at address  : {}".format(i))

for j in range(2):
    for i in range(1513,1514):

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
            c.close()
            print("Test failed at address  : {}".format(i))
for j in range(2):
    for i in range(1508,1509):

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
            c.close()
            print("Test failed at address  : {}".format(i))

    # for i in range(1513,1514):

    #     try:
    #         c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    #     except ValueError:
    #         print ("Error with host or port params")


    #     if c.open():
    #         c.write_single_register(0,65000)
    #         # c.write_multiple_coils(0, [True,True,True])
    #         # c.write_multiple_registers(0, [65000]*30)
    #         # c.write_single_coil(0, True)
    #         # c.write_single_register(0, 250)

    #         c.close()
    #         print("Test success at address  : {}".format(i))
    #     else:
    #         c.close()
    #         print("Test failed at address  : {}".format(i))

while(True):
    # for i in range(1501,1502):

    #     try:
    #         c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    #     except ValueError:
    #         print ("Error with host or port params")


    #     if c.open():
    #         reg_list = c.read_coils(0, 5)
    #         print(reg_list)
    #         # c.write_multiple_coils(0, [True,True,True])
    #         # c.write_multiple_registers(0, [65000]*30)
    #         # c.write_single_coil(0, True)
    #         # c.write_single_register(0, 250)

    #         c.close()
    #         print("Test success at address  : {}".format(i))
    #     else:
    #         c.close()
    #         print("Test failed at address  : {}".format(i))
        
    for i in range(1505,1512,6):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            reg_list = c.read_input_registers(50, 5)
            print(reg_list)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Test success at address  : {}".format(i))
        else:
            c.close()
            print("Test failed at address  : {}".format(i))


    for i in range(1514,1515):

        try:
            c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
        except ValueError:
            print ("Error with host or port params")


        if c.open():
            reg_list = c.read_input_registers(50, 5)
            print(reg_list)
            # c.write_multiple_coils(0, [True,True,True])
            # c.write_multiple_registers(0, [65000]*30)
            # c.write_single_coil(0, True)
            # c.write_single_register(0, 250)

            c.close()
            print("Test success at address  : {}".format(i))
        else:
            c.close()
            print("Test failed at address  : {}".format(i))

    # for j in range(2):
    #     for i in range(1515,1518):
    #         try:
    #             c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    #         except ValueError:
    #             print ("Error with host or port params")


    #         if c.open():
    #             reg_list = c.read_input_registers(49, 10)
    #             print(reg_list)
    #             # c.write_multiple_coils(0, [True,True,True])
    #             # c.write_multiple_registers(0, [65000]*30)
    #             # c.write_single_coil(0, True)
    #             # c.write_single_register(0, 250)

    #             c.close()
    #             print("Test success at address  : {}".format(i))
    #         else:
    #             c.close()
    #             print("Test failed at address  : {}".format(i))
    time.sleep(2)

    # for i in range(1511,1512):

    #     try:
    #         c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    #     except ValueError:
    #         print ("Error with host or port params")


    #     if c.open():
    #         reg_list = c.read_input_registers(50, 10)
    #         print(reg_list)
    #         # c.write_multiple_coils(0, [True,True,True])
    #         # c.write_multiple_registers(0, [65000]*30)
    #         # c.write_single_coil(0, True)
    #         # c.write_single_register(0, 250)

    #         c.close()
    #         print("Test success at address  : {}".format(i))
    #     else:
    #         c.close()
    #         print("Test failed at address  : {}".format(i))
    # time.sleep(2)   

