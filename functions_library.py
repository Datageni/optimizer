import time
from criterions import *

def clear_screen(n):
    for _ in range(n):
        print(' ')

def menu(title,context, num_options, text_array):
        title_length = len(title)
        context_lenght = len(context)
        side_length = int((context_lenght - (title_length+2)) /2)
        if side_length % 2 == 0:
            side_char = '-' * (side_length)
            header = f'{side_char} {(title).upper()} {side_char}'
            total_char = '-' * (context_lenght-1)
        else:
            side_char = '-' * (side_length+1)
            header = f'{side_char} {(title).upper()} {side_char}'
            total_char = '-' * (context_lenght+1)
        print(header)
        print(context)
        for i in range(num_options):
            print(f'{i+1}) {text_array[i]}')
        exit_option = f'{num_options+1}) Exit'
        print(exit_option)
        print(total_char)
        menu_option = int(input('Option: '))
        return menu_option, num_options+1


def criterions_menu(type):
     criterions_while = True
     while criterions_while:
          clear_screen(100)
          criterions_option, exit_option = menu('criterons',
                      'Please select one of the following criterions:',
                      4, 
                      ['Wald Criterion', 'Optimistic Criterion','Savage Criterion','Laplace Criterion'])
          if criterions_option == exit_option:
               clear_screen(100)
               criterions_while = False
          elif criterions_option == 1:
               criterion_menu('wald',type)
          elif criterions_option == 2:
               criterion_menu('optimistic',type)
          elif criterions_option == 3:
               criterion_menu('savage', type)
          elif criterions_option == 4:
               criterion_menu('laplace', type)
          else:
               clear_screen(100)
               print('WRONG OPTION')
               time.sleep(2)
          
def criterion_menu(criterion,type):
     criterion_while = True
     while criterion_while:
          clear_screen(100)
          criterion_option, exit_option = menu(f'{criterion} criterion',
                                               'Please select one of the following options:',
                                               1,
                                               ['Enter problem']
                                               )
          if criterion_option == exit_option:
               clear_screen(100)
               criterion_while = False
          elif criterion == 'wald':
               wald(type)
          elif criterion == 'optimistic':
               optimistic(type)
          elif criterion == 'savage':
               savage(type)
          elif criterion == 'laplace':
               laplace(type)

               
    

             


