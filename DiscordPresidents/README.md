# Discord Presidents

language:

    recommend python +3.10
    no lower than python 3.9

required APIs:

    pip install openai - ai reference
    pip install pyautogui - keyboard and mouse macro
    pip install tk - window dimesioning
    pip install pynput - keyboard input for control
    
use:

    1. modify variables in program to fit computer specification. this includes the height offset and api key in the personalized variables.
        height is adjusted from the bottom of the screen up and should land on the desired typing location
    
    2. open two discord windows on one computer (divided vertically) and connect both accounts to one server
    
    ****************************
    *             |            *
    *             |            *
    *   window    |    window  *
    *             |            *
    *             |            *
    *             |            *
    ****************************
    
    3. run the program, close the program window and press esc to start conversation.
        the program should automatically type into discord if the height offset is correct
        
    4. press esc again to pause the program or close the program to stop entirely
    
note:

    trump is set to the left and obama is set to the right
    speaker and message can be manually chosen on the top level of the program
    program will remember which president spoke last and their previous message when paused.
    program will not remember current data when closed
