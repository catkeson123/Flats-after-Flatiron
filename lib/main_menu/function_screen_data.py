import os, ipdb
from main_menu.color_class import color

'''Booking Screens'''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_booking_greeting():
    return input('''
                 
        *****************************************************************************************************************************       
        **************************************************     Welcome to Booking     ***********************************************
        *****************************************************************************************************************************
                                    
                                                                    To Exit
                                                                  [[Type 'X']]

                                        ******************************************************************
                                            When would you like your vacation to start? 
                                        ******************************************************************

        ''')

def print_user_start_date(startDate):
    print(f'''
                                        ******************************************************************
                                                        Here is your start date: {startDate}
                                        ******************************************************************
    ''')

def print_user_end_date_input():
    return input('''
                                        ******************************************************************
                                            When would you like your vacation to end? (YYYY-MM-DD)
                                        ******************************************************************
        ''')

def print_bottom_booking_screen():
    print(f'''

        *****************************************************************************************************************************
        *****************************************************************************************************************************

    ''')

def print_avaliable_properties(startDate, endDate, filtered_domiciles):
    
    print(f'''

        *****************************************************************************************************************************       
        **************************************************     Avaliable Properties     *********************************************       
        *****************************************************************************************************************************       
        
                                        ******************************************************************    
                                        
                                                Here are the available properties for those dates

                                                     Start: {startDate}        End: {endDate} 

                                        ****************************************************************** 
                     
    ''')
    
    for i, d in enumerate(filtered_domiciles):
        print(f'''
                                        ****************************************************************** 
                                            {i + 1}. {d.name} in {d.dest_location}
                                        ****************************************************************** 
        ''')
               
    return input('''

                                For More Details                                                        To Exit 
                            [[Enter Property Number]]                                                 [[Type 'X']]

        *****************************************************************************************************************************
        *****************************************************************************************************************************
                ''')

def print_book_property_details(dp):
    return input(f'''

            *****************************************************************************************************************************       
            **************************************************     Property Details     *************************************************
            *****************************************************************************************************************************

                                                                    {dp.name}
                                            
                                            
                                            ******************************************************************
                                                            Property Type: {dp.property_type}
                                            ******************************************************************

                                            ******************************************************************
                                                            Location: {dp.dest_location}
                                            ******************************************************************

                                            ******************************************************************
                                                            Sleeping Capacity: {dp.sleep_capacity}
                                            ******************************************************************

                                            ******************************************************************
                                                        Local Amenities: {dp.local_amenities}
                                            ******************************************************************                        
            
                                To Book This Property                                           To Return to Property List 
                                    [[Type 'B']]                                                       [[Type 'Z']]

            *****************************************************************************************************************************
            *****************************************************************************************************************************                
                            
                            
     ''')

def print_booking_signature(self):
    return input(f'''
                                        ************************************************************************

                                                                    *****************

                                                                    Great! Last step!

                                                                    *****************
                                            
                                                    Sign into your vacation by signing the log book!
                                   
                                                    ************************************************
                                
                                        ········································································
                                            {self.trav_obj.first_name} {self.trav_obj.last_name}
                                                Reason for visit: ''')

def print_bottom_of_signature():
    print('''                                        ········································································
                                                                                                              
    ''')

def print_booking_verification():
    print('''

                                                            **********************************
                                                            Congrats! Your vacation is booked!
                                                            **********************************

                                        ************************************************************************
                                        ************************************************************************

    ''')

'''Properties Screens'''

def print_property_page(all_dom):

    print('''
        
        ·····························································································································
        ····················································      Properties    ·····················································
        ····························································································································· 
        
        
    ''')

    for i, d in enumerate(all_dom):
        print(f'''
                    ········································································································
                        {i + 1}. {color.BOLD} Property Name: {color.END} {d.name}, {color.BOLD} Property Type: {color.END} {d.property_type}, {color.BOLD} Location: {color.END} {d.dest_location}
                    ········································································································
        ''')
                
    return input('''

                            For More Details                                                         To Exit 
                        [[Enter Property Number]]                                                 [[Type 'X']]
                                            
        ·····························································································································
        ·····························································································································                         
        ''')

def print_property_details(dp):
    return input(f''' 

        ····························································································································· 
        ················································      Property Details    ···················································
        ·····························································································································     
            
        
        
                                    ··································································
                                    Property Name: {dp.name}
                                    ··································································
                                    Property Type: {dp.property_type}
                                    ··································································
                                    Location: {dp.dest_location}
                                    ··································································
                                    Sleeping Capacity: {dp.sleep_capacity}
                                    ··································································
                                    Local Amenities:  {dp.local_amenities}                    
                                    ··································································


            
                                      See Past Bookings        Return to Properties            To Exit 
                                        [[Type 'B']]               [[Type 'V']]             [[Type 'X']]

        ····························································································································· 
        ····························································································································· 

                        ''')

def print_past_residents(pastVacations, dp):
    print(f'''
        ·····························································································································
        ·····························································································································

                            ························································································
                            ·····················     Past Residents of this Property    ···························
                            ························································································ 
                                                                                                
                            ''')
                                    
    print(f'                                                            {color.BOLD}  {dp.name}  {color.END}')
    print('                            ························································································')
    print('')
    for v in pastVacations:
        print(f''' 
                                    ···········································································
                                                {v.traveler.first_name.capitalize()} {v.traveler.last_name.capitalize()}
                                                    Reason for visit: {v.rsn_for_visit}
                                    ···········································································
        ''')
                                 
    return input('''
                        
                                                  Return to Property                        To Exit 
                                                      [[Type 'V']]                        [[Type 'X']]                             
                                            
            ·····························································································································
            ·····························································································································
    ''')

'''Profile Screens'''

def print_profile_screen(trav_obj, my_vacations):
        print(f'''

        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                                        
        
                                                        <><><><><><><><><><><><><><><><><
                                                                     Profile 
                                                        ><><><><><><><><><><><><><><><><>
                                        
                                                     
                                                              First Name: {trav_obj.first_name}
                                                              Last Name: {trav_obj.last_name}
                                                              Location: {trav_obj.location}

                                                    
                                                        ><><><><><><><><><><><><><><><><><
                                                                  Your vacations:
                                                        ><><><><><><><><><><><><><><><><><

                                                                                                
        ''')

        for i, v in enumerate(my_vacations):
                print(f"                                        {i + 1}. {v.domicile.name}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}" )
        print('')

def print_no_vacations():
    print('''

                                                        ><><><><><><><><><><><><><><><><><
                                                             No vacations booked yet!
                                                        ><><><><><><><><><><><><><><><><><


        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>                                

        
    ''')

def print_edit_choice():
   return input('''

                                Type the number of the vacation you'd like to edit/delete, or 'x' to leave!:
    
    ''')

def print_vacation_editing(cv):
    print(f'''                     
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 

                                                        Currently Editing Vacation:

                                                    ><><><><><><><><><><><><><><><><><

                                                            {cv.domicile.name}
                                                            >> {cv.domicile.dest_location} 
                                                            >> {cv.start_date} - {cv.end_date}

                                                    ><><><><><><><><><><><><><><><><><                             
    ''')

    return input('''                             
                            To update this vacation, type 'U', to delete this vacation, type 'D', to leave type 'X': 
    ''')

def print_edit_options():
    return input('''
                                                    ><><><><><><><><><><><><><><><><><


                              Enter 1 to edit the start date, 2 to edit the end date, or 3 to edit the property:

    ''')

def print_other_reservations(vac_by_cvd, cv, edit_prop):
    print('''

        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 

                                        This location currently has other reservations during: 
                                        
                                                    ><><><><><><><><><><><><><><><><><
                                        ''')

    for v in vac_by_cvd:
        if v.id == cv.id:
            print(f'''
                                                    ><><><><><><><><><><><><><><><><><

                                                        {v.start_date} to {v.end_date}   ⟸ Current Vacation''')
        else:
            print(f'''
                                                    ><><><><><><><><><><><><><><><><><

                                                        {v.start_date} to {v.end_date}''')
        print('''
                                                    ><><><><><><><><><><><><><><><><><
        ''')
    return input(f'''
                                            Please enter your new {'start date' if edit_prop == 1 else 'end date'} or x to exit: 
    ''')

def print_new_date(newDate, edit_prop):
    print(f'''
                                              ><><><><><><><><><><><><><><><><><><><><><><

                                                  Here is your new {'start date' if edit_prop == 1 else 'end date'}: {newDate}

                                              ><><><><><><><><><><><><><><><><><><><><><><
        
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 
                                                    ''')

def print_update_avaliable_properties(available_domiciles):

    print('''                   

        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 

                                                             Available Properties:

    ''')

    for i, d in enumerate(available_domiciles):
        print(f'''                                
                                    --------------------------------------------------------------------------
                                    {i + 1}. Property Name: {d.name}, Property Type: {d.property_type}, Location: {d.dest_location}
                                    --------------------------------------------------------------------------
        ''')

    return input('''
                                                        ><><><><><><><><><><><><><><><><><

                                        Please enter the number of the property you would like to switch to: 

                                                        ><><><><><><><><><><><><><><><><><
    ''')

def print_property_change_confirm(dom_pre_change, new_property):

    print(f'''             
                        Congrats! Property changed from {dom_pre_change[0].name} in {dom_pre_change[0].dest_location} to {new_property.name} in {new_property.dest_location}
        
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    ''')

def print_deletion_confirmation():

    print('''
                                                    ><><><><><><><><><><><><><><><><><

                                                      Vacation deleted successfully!
                                                    
                                                    ><><><><><><><><><><><><><><><><><

        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    ''')

def print_other_bookings(new_vacations):
    print('''             
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
        ><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> 

                                                                Your Booked vacations:
                                                    ><><><><><><><><><><><><><><><><><><><><><><
    ''')
                        
    if len(new_vacations) > 0:
        for i, v in enumerate(new_vacations):
            print(f'''
                                      --------------------------------------------------------------------------
                                            {i + 1}. {v.domicile.name}, in {v.domicile.dest_location} from {v.start_date} - {v.end_date}
                                      --------------------------------------------------------------------------
             ''')
    else:
        print_no_vacations()

'''Error Messages'''

def print_user_date_error():
    print('''
                                        ******************************************************************
                                        ╰༼=ಠਊಠ=༽╯    Please enter a valid date! (YYYY-MM-DD)    ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
    ''')

def print_valid_selection_error():
    print('''
                                                        **********************************
                                                          Please make a valid selection!
                                                        **********************************
    ''')

def print_lenny_selection_error():
    print('''
                                        ******************************************************************
                                            ╰༼=ಠਊಠ=༽╯    Please enter a valid selection!    ╰༼=ಠਊಠ=༽╯
                                        ******************************************************************
    ''')

def print_properties_selection_error():
    print('''
                                ··································································
                                                Please make a valid selection!
                                ··································································
    ''')

def print_properties_number_error():
    print('''
                        Please make sure to enter a number associated with a property!
    ''')

def print_profile_selection_error():
    print('''
                                        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                                                        Please make a valid selection!
                                        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    ''')

def print_profile_date_error():
    print('''
    
                                        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
                                                        Please enter a valid date!
                                        <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>
    ''')
                                                       
def print_property_change_error():

     print('''                                          ><><><><><><><><><><><><><><><><><
                                            
                                        Please make sure to enter one of the numbers associated with a property!
                                                        
                                                        ><><><><><><><><><><><><><><><><><
    ''')