def clear_screen(n):
    for _ in range(n):
        print(' ')



def wald(type):
    wald_array = []
    wald_while = True
    while wald_while:
        clear_screen(100)
        print('------------ WALD CRITERION ------------')
        n_cases = int(input('Please enter the number of cases: '))
        n_variables = int(input('Please enter the number of variables: '))
        clear_screen(100)
        for i in range(n_cases):
            wald_results = []
            print(f'\n------------------ CASE {i+1} ------------------')
            if type == 'loss':
                for j in range(n_variables):
                    n_variable = int(input(f'Please enter the value of variable number {j+1}: '))
                    wald_results.append(n_variable)
                    max_values = max(wald_results)
                wald_array.append(max_values)
                min_max = min(wald_array)
            elif type == 'gain':
                for j in range(n_variables):
                    n_variable = int(input(f'Please enter the value of variable number {j+1}: '))
                    wald_results.append(n_variable)
                    max_values = min(wald_results)
                wald_array.append(max_values)
                max_min = max(wald_array)
        clear_screen(100)
        print('--------------------- RESULT ---------------------')
        print(f'Using Wald Criterion for {type} we get: {min_max if type == 'loss' else max_min} as result.\n')
        input('PRESS ENTER TO RETURN...')
        wald_while = False



def optimistic(type):
    optimistic_array = []
    optimistic_while = True
    while optimistic_while:
        clear_screen(100)
        print('------------ OPTIMISTIC CRITERION ------------')
        n_cases = int(input('Please enter the number of cases: '))
        n_variables = int(input('Please enter the nuber of variables: '))
        for i in range(n_cases):
            optimistic_results = []
            print(f'\n------------------ CASE {i+1} ------------------')
            if type == 'loss':
                for j in range(n_variables):
                    n_value = int(input(f'Please enter the value of variable number {j+1}: '))
                    optimistic_results.append(n_value)
                    first_min = min(optimistic_results)
                optimistic_array.append(first_min)
                min_min = min(optimistic_array)
            elif type == 'gain':
                for j in range(n_variables):
                    n_value = int(input(f'Please enter the value of variable number {j+1}: '))
                    optimistic_results.append(n_value)
                    first_max = max(optimistic_results)
                optimistic_array.append(first_max)
                max_max = max(optimistic_array)
        clear_screen(100)
        print('--------------------- RESULT ---------------------')
        print(f'Using Optimistic criterion for {type} we get: {min_min if type == 'loss' else max_max} as result.\n')
        input('PRESS ENTER TO RETURN...')
        optimistic_while = False
                


def savage(type):
    original_matrix = []
    savage_while = True
    while savage_while:
        clear_screen(100)
        print('------------ SAVAGE CRITERION ------------')
        n_cases = int(input('Please enter the number of cases: '))
        n_variables = int(input('Please enter the nuber of variables: '))
        for i in range(n_cases):
            savage_results = []
            print(f'\n------------------ CASE {i+1} ------------------')
            for j in range(n_variables):
                n_value = int(input(f'Please enter the value of variable number {j+1}: '))
                savage_results.append(n_value)
            original_matrix.append(savage_results)
            transposed_matrix = list(zip(*original_matrix))
            values = []
            regret_matrix = []
            if type == "loss":
                for row in transposed_matrix:
                    values.append(min(row))
                    for val in values:
                        regret_values = []
                    for element in row:
                        regret_values.append(element - val)
                    regret_matrix.append(regret_values)
                    regret_matrix = list(zip(*regret_matrix))
            if type == 'gain':
                for row in transposed_matrix:
                    values.append(max(row))
                    for val in values:
                        regret_values = []
                    for element in row:
                        regret_values.append(val - element)
                    regret_matrix.append(regret_values)
                    regret_matrix = list(zip(*regret_matrix))
            final_max = []
            for regret_row in regret_matrix:
                final_max.append(max(regret_row))
            result = min(final_max)
        clear_screen(100)
        print('--------------------- RESULT ---------------------')
        print(f'Using Savage criterion for {type} we get: {result} as result.\n')
        input('PRESS ENTER TO RETURN...')
        savage_while = False
            
  
def laplace(type):
    original_matrix = []
    laplace_while = True
    results = []
    while laplace_while:
        clear_screen(100)
        print('------------ LAPLACE CRITERION ------------')
        n_cases = int(input('Please enter the number of cases: '))
        n_variables = int(input('Please enter the nuber of variables: '))
        clear_screen(100)
        for i in range(n_cases):
            laplace_results = []
            print(f'\n------------------ CASE {i+1} ------------------')
            for j in range(n_variables):
                n_value = int(input(f'Please enter the value of variable number {j+1}: '))
                laplace_results.append(n_value)
            original_matrix.append(laplace_results)
            for row in original_matrix:
                sum_value = sum(row)
            results.append(sum_value / len(row))
            if type == "loss":
                final_result = round(min(results), 2)
            elif type == "gain":
                final_result = round(max(results), 2)
        clear_screen(100)
        print('--------------------- RESULT ---------------------')
        print(f'Using Savage criterion for {type} we get: {final_result} as result.\n')
        input('PRESS ENTER TO RETURN...')
        laplace_while = False
