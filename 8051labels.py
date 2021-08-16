# 8051 Labels
# SFRs
sfrs = {
'E0':('ACC'),   # Accumulator
'F0':('B'),     # B Register
'82':('DPL'),   # Data Pointer Low (External Memory)
'83':('DPH'),   # Data Pointer High (External Memory)
'A8':('IE'),    # Interrupt Enable
'B8':('IP'),    # Interrupt Priority
'80':('P0'),    # Port 0 Latch
'90':('P1'),    # Port 1 Latch
'A0':('P2'),    # Port 2 Latch
'B0':('P3'),    # Port 3 Latch
'87':('PCON'),  # Power Control
'D0':('PSW'),   # Program Status Word
'98':('SCON'),  # Serial Port Control
'99':('SBUF'),  # Serial Data Buffer
'81':('SP'),    # Stack Pointer
'89':('TMOD'),  # Timer / Counter Mode Control
'88':('TCON'),  # Timer / Counter Control
'8A':('TL0'),   # Timer 0 low byte
'8C':('TH0'),   # Timer 0 high byte
'8B':('TL1'),   # Timer 1 low byte
'8D':('TH1'),   # Timer 1 high byte
}

bit_addressable = {
'E0':('ACC.0'),  #Accumulator Bits
'E1':('ACC.1'),
'E2':('ACC.2'),
'E3':('ACC.3'),
'E4':('ACC.4'),
'E5':('ACC.5'),
'E6':('ACC.6'),
'E7':('ACC.7'),
'F0':('B.0'),    #B Register Bits
'F1':('B.1'),
'F2':('B.2'),
'F3':('B.3'),
'F4':('B.4'),
'F5':('B.5'),
'F6':('B.6'),
'F7':('B.7'),
'A8':('EX0'),    # Interrupt Enable
'A9':('ET0'),
'AA':('EX1'),
'AB':('ET1'),
'AC':('ES'),
'AD':('ET2'),
'AE':('-'),
'AF':('EA'),
'B8':('PX0'),    # Interrupt Priority
'B9':('PT0'),
'BA':('PX1'),
'BB':('PT1'),
'BC':('PS'),
'BD':('PT2'),
'BE':('-'),
'BF':('-'),
'80':('P0.0'),  #Port 0 Alt
'81':('P0.1'),
'82':('P0.2'),
'83':('P0.3'),
'84':('P0.4'),
'85':('P0.5'),
'86':('P0.6'),
'87':('P0.7'),
}
