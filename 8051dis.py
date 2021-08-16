import sys
import string
import opcodes

hex_file = open('8051.hex','r')
hex_data = hex_file.read().replace("\n","");

hex_array = [hex_data[i:i+2] for i in range(0, len(hex_data), 2)];
#Wprint(hex_array)
PC = 0;
# jumps
# AJMP  0x01,0x21,0x41,0x61,0x81,0xA1,0xC1,0xE1
# ACALL 0x11,0x31,0x51,0x71,0x91,0xB1,0xD1,0xF1


while PC < len(hex_array):
    label = "          "
    op_tuple = opcodes.opcodes8051.get(hex_array[PC].upper());
    num_operands = op_tuple[1]
    op0 = hex_array[PC].upper()
    op1 = hex_array[PC+1].upper()
    op2 = hex_array[PC+2].upper()

    if op0 != 'FF':
        print label,
        print '0x{:04x}'.format(PC),

    if num_operands == 3:
        if hex_array[PC].upper() == '02' or '12' :  #Long Jump and Long Call Special Case
            print " 0x" + op0 +" 0x"+ op1 +" 0x"+ op2,
            print op_tuple[0],
            print "0x%0.4X" % ((int(op1,16)<<8) + int(op2,16))
        else :
            print " 0x" + op0 +" 0x"+ op1 +" 0x"+ op2,
            print op_tuple[0] + " 0x" + op1+ " 0x" + op2
        PC=PC+3

    elif num_operands == 2:
        if hex_array[PC].upper() == '80':
            print " 0x" + op0 +" 0x"+ op1 +"     ",
            print op_tuple[0] + " " + op_tuple[2],
            print "0x%0.4X" % (int(hex_array[PC+1],16)+PC+2)
        else:
            print " 0x" + hex_array[PC].upper() +" 0x"+ hex_array[PC+1].upper() +"     ",
            print op_tuple[0] + " " + op_tuple[2] + " " + op1
        PC=PC+2
    else:
        if hex_array[PC].upper() == 'FF':
            PC=PC
        else :
            print " 0x" + hex_array[PC].upper() +"          ",
            print(opcodes.opcodes8051.get(hex_array[PC].upper())[0] + " " +
            opcodes.opcodes8051.get(hex_array[PC].upper())[2])
        PC=PC+1
