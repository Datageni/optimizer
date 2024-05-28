import time
from functions_library import *


def main():
    clear_screen(100)
    print('----------- OPTIMIZER -----------')
    time.sleep(2)
    clear_screen(100)
    main_while = True
    while main_while:
       clear_screen(100)
       main_menu_option, main_exit_option = menu('main menu', 
                                       'Please enter your problem type:', 
                                       2, 
                                       ['Gain problem','Loss problem'])
       if main_menu_option == main_exit_option:
           clear_screen(100)
           main_while = False
       elif main_menu_option == 1:
          criterions_menu('gain')
       elif main_menu_option == 2:
           criterions_menu('loss')
       else:
          clear_screen(100)
          print('WRONG OPTION')
          time.sleep(2)
main()





    
