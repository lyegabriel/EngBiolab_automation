# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:06:25 2020

@author: jingwui
"""

from opentrons import protocol_api

# metadata
metadata = {
    'protocolName': 'Transfer recombinant DNA from 24 Well plates to 96 Well-plates in different combinations',
    'apiLevel': '2.0'
}

# protocol run function. the part after the colon lets your editor know
# where to look for autocomplete suggestions
def run(protocol: protocol_api.ProtocolContext):
    
    Falcon = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap',4)
    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    tiprack_1 = protocol.load_labware('opentrons_96_tiprack_20ul', 5)
    tiprack_2 = protocol.load_labware('opentrons_96_tiprack_20ul', 6)
    p10 = protocol.load_instrument('p10_single', 'right', tip_racks=[tiprack_1, tiprack_2])
    n = 3 #refers to the number of variations of the same sample (i.e A1.A2...)
    i = 1
    count = 0
    
#     For D1 (Assembly Master Mix)
    p10.pick_up_tip()
    for r in range(2*n):
        p10.distribute(2, Falcon['D1'], plate1.columns()[r][0:n], new_tip='never') ,disposal_volume = 0)
        p10.distribute(2, Falcon['D1'], plate2.columns()[r][0:n], new_tip='never') ,disposal_volume = 0)  
        p10.distribute(2, Falcon['D1'], plate3.columns()[r][0:n], new_tip='never') ,disposal_volume = 0)  
    p10.drop_tip()
    
#     For D2 (Backbone+pLac)
    p10.pick_up_tip()
    for r in range(2*n):
        p10.distribute(2, Falcon['D2'], plate1.columns()[r][0:n], new_tip='never') ,disposal_volume = 0)
        p10.distribute(2, Falcon['D2'], plate2.columns()[r][0:n], new_tip='never') ,disposal_volume = 0)  
        p10.distribute(2, Falcon['D2'], plate3.columns()[r][0:n], new_tip='never') ,disposal_volume = 0)  
    p10.drop_tip()
            
    #for A 
    
    while i<(n+1):
        p10.pick_up_tip()
        for r in range(n):
            if i > 2:
                p10.distribute(2, Falcon["A"+ str(i)], plate.rows()[r][2*n:3*n], 
                         new_tip = 'never')
            elif 1< i <= 2:
                p10.distribute(2, Falcon["A"+ str(i)], plate.rows()[r][n:2*n], 
                         new_tip = 'never')
            else:
                p10.distribute(2, Falcon["A"+ str(i)], plate.rows()[r][0:n], 
                         new_tip = 'never')
                
        i += 1
        p10.drop_tip()

   

    #For B Wells
    while i<(n+1):
        p10.distribute(2, Falcon['B' + str(i)], plate.rows()[count][0:n], 
                              new_tip = 'always')
        p10.distribute(2, Falcon['B' + str(i)], plate.rows()[count][n:n*2], 
                              new_tip = 'always')
        p10.distribute(2, Falcon['B' + str(i)], plate.rows()[count][2*n:n*3], 
                              new_tip = 'always')
        i += 1
        count += 1

    
   #For C wells     
    while i<(n+1):
        p10.transfer(2, Falcon['C' + str(i)], plate.columns()[count][0:n], 
                              new_tip = 'always', blow_out = True)
        p10.transfer(2, Falcon['C' + str(i)], plate.columns()[count + n][0:n], 
                              new_tip = 'always', blow_out = True)
        p10.transfer(2, Falcon['C' + str(i)], plate.columns()[count + n+ n][0:n], 
                              new_tip = 'always', blow_out = True)

        i += 1
        count +=1
        

    
   