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
    plate1 = protocol.load_labware('corning_96_wellplate_360ul_flat', 1)
    plate2 = protocol.load_labware('corning_96_wellplate_360ul_flat', 2)
    plate3 = protocol.load_labware('corning_96_wellplate_360ul_flat', 3)
    tiprack_20 = protocol.load_labware('opentrons_96_tiprack_20ul', 6)
    p20 = protocol.load_instrument('p20_single_gen2', 'right', tip_racks=[tiprack_20])
    n = 5 #refers to the number of variations of the same sample (i.e A1.A2...)
    i = 1
    count = 0
    
#     For D1 (Assembly Master Mix)
#    p20.pick_up_tip()
#    for r in range(2*n):
#        p20.distribute(2, Falcon['D1'], plate1.columns()[r][0:n], new_tip='never') #,disposal_volume = 0)
#        p20.distribute(2, Falcon['D1'], plate2.columns()[r][0:n], new_tip='never') #,disposal_volume = 0)  
#        p20.distribute(2, Falcon['D1'], plate3.columns()[r][0:n], new_tip='never') #,disposal_volume = 0)  
#    p20.drop_tip()
    
#     For D2 (Backbone+pLac)
#    p20.pick_up_tip()
#    for r in range(2*n):
#        p20.distribute(2, Falcon['D2'], plate1.columns()[r][0:n], new_tip='never') #,disposal_volume = 0)
#        p20.distribute(2, Falcon['D2'], plate2.columns()[r][0:n], new_tip='never') #,disposal_volume = 0)  
#        p20.distribute(2, Falcon['D2'], plate3.columns()[r][0:n], new_tip='never') #,disposal_volume = 0)  
#    p20.drop_tip()
            
    #for A 
    
    while i<(n+1):
        p20.pick_up_tip()
        for r in range(n):
            if i > 4:
                p20.distribute(2, Falcon["A"+ str(i)], plate3.rows()[r][0:n], 
                             new_tip = 'never')
                
            elif i > 2:
                if i % 2 != 0:
                    p20.distribute(2, Falcon["A"+ str(i)], plate2.rows()[r][0:n], 
                            new_tip = 'never')
                else:
                    p20.distribute(2, Falcon["A"+ str(i)], plate2.rows()[r][n:n*2], 
                             new_tip = 'never')
            elif i % 2 == 0:
                p20.distribute(2, Falcon["A"+ str(i)], plate1.rows()[r][n:n*2], 
                             new_tip = 'never')
            else:
                p20.distribute(2, Falcon["A"+ str(i)], plate1.rows()[r][0:n], 
                         new_tip = 'never')
        i += 1
        p20.drop_tip()

   

    #For B Wells
#    while i<(n+1):
#        p20.distribute(2, Falcon['B' + str(i)], plate1.rows()[count][0:n], 
#                              new_tip = 'always')
#        p20.distribute(2, Falcon['B' + str(i)], plate1.rows()[count][n:n*2], 
#                              new_tip = 'always')
#        p20.distribute(2, Falcon['B' + str(i)], plate2.rows()[count][0:n], 
#                              new_tip = 'always')
#        p20.distribute(2, Falcon['B' + str(i)], plate2.rows()[count][n:n*2], 
#                              new_tip = 'always')
#        p20.distribute(2, Falcon['B' + str(i)], plate3.rows()[count][0:n], 
#                              new_tip = 'always')
#        p20.distribute(2, Falcon['B' + str(i)], plate3.rows()[count][n:n*2], 
#                              new_tip = 'always')
#        i += 1
#        count += 1

    
   #For C     
#    while i<(n+1):
#        p20.transfer(2, Falcon['C' + str(i)], plate1.columns()[count][0:n], 
#                              new_tip = 'always', blow_out = True)
#        p20.transfer(2, Falcon['C' + str(i)], plate1.columns()[count + n][0:n], 
#                              new_tip = 'always', blow_out = True)
#        p20.transfer(2, Falcon['C' + str(i)], plate2.columns()[count][0:n], 
#                              new_tip = 'always', blow_out = True)
#        p20.transfer(2, Falcon['C' + str(i)], plate2.columns()[count+n][0:n], 
#                              new_tip = 'always', blow_out = True)
#        p20.transfer(2, Falcon['C' + str(i)], plate3.columns()[count][0:n], 
#                              new_tip = 'always', blow_out = True)
#        p20.transfer(2, Falcon['C' + str(i)], plate3.columns()[count+n][0:n], 
#                              new_tip = 'always', blow_out = True)
#        i += 1
#        count +=1
        

    
   