from pyModbusTCP.client import ModbusClient

for i in range(1501,1502):

    try:
        c=ModbusClient(host="127.0.0.1", port=i, unit_id=1, auto_open=True, debug=False)
    except ValueError:
        print ("Error with host or port params")

    if c.open():

        # Modbus function WRITE_MULTIPLE_COILS (0x0F)
        # Parameters:	
        #     bits_addr (int) – bits address (0 to 65535)
        #     bits_value (list) – bits values to write
        # Returns:	True if write ok or None if fail
        # Return type:	bool or None
        #c.write_multiple_coils(0, [True,True,True])

        
        # Modbus function WRITE_MULTIPLE_REGISTERS (0x10)
        # Parameters:	
        #     regs_addr (int) – registers address (0 to 65535)
        #     regs_value (list) – registers values to write
        # Returns:	True if write ok or None if fail
        # Return type:	bool or None
        #c.write_multiple_registers(0, [100,101,102])

        
        # Modbus function WRITE_SINGLE_COIL (0x05)
        # Parameters:	
        #     bit_addr (int) – bit address (0 to 65535)
        #     bit_value (bool) – bit value to write
        # Returns:	True if write ok or None if fail
        # Return type:	bool or None
        #c.write_single_coil(1, True)

        
        # Modbus function WRITE_SINGLE_REGISTER (0x06)
        # Parameters:	
        #     reg_addr (int) – register address (0 to 65535)
        #     reg_value (int) – register value to write
        # Returns:	True if write ok or None if fail
        # Return type:	bool or None
        #c.write_single_register(4, 200)


        #Modbus function READ_COILS (0x01)
        #Parameters:	
        #   bit_addr (int) – bit address (0 to 65535)
        #   bit_nb (int) – number of bits to read (1 to 2000)
        #Returns: bits list or None if error
        #Return type:list of bool or No
        #reg_list_1 = c.read_coils(0, 3)

        #Modbus function READ_DISCRETE_INPUTS (0x02)
        #Parameters:	
        #    bit_addr (int) – bit address (0 to 65535)
        #    bit_nb (int) – number of bits to read (1 to 2000)
        #Returns:	bits list or None if error
        #Return type:	list of bool or None
        #reg_list_2 = c.read_discrete_inputs(0, 3)

        
        #Modbus function READ_HOLDING_REGISTERS (0x03)
        #Parameters:	
        #    reg_addr (int) – register address (0 to 65535)
        #    reg_nb (int) – number of registers to read (1 to 125)
        #Returns:	registers list or None if fail
        #Return type:	list of int or None
        #reg_list_3 = c.read_holding_registers(100, 105)

        
        #Modbus function READ_INPUT_REGISTERS (0x04)
        #Parameters:	
        #    reg_addr (int) – register address (0 to 65535)
        #    reg_nb (int) – number of registers to read (1 to 125)
        #Returns:	registers list or None if fail
        #Return type:	list of int or None
        #reg_list_4 = c.read_input_registers(0, 3)

        #error = c.last_error_txt()
        #execption = c.last_except_txt(verbose=True)

        c.write_multiple_coils(0, [True,True,True])
        c.write_multiple_registers(0, [100,101,102])
        c.write_single_coil(0, True)
        c.write_single_register(0, 250)

        reg_list_1 = c.read_coils(0, 11)
        reg_list_2 = c.read_discrete_inputs(0, 11)
        reg_list_3 = c.read_holding_registers(0, 11)
        reg_list_4 = c.read_input_registers(0, 11)
        
        print("coils values             :-" + str(reg_list_1))
        print("discrete_inputs values   :-" + str(reg_list_2))
        print("holding_registers values :-" + str(reg_list_3))
        print("input_registers values   :-" + str(reg_list_4))
        c.close()
        print("Test success at address  : {}".format(i))
    else:
        print("Test failed at address  : {}".format(i))

