import timeit
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

from . import Expense

def main():
    expenses = Expense.Expenses()
    expenses.read_expenses('data/spending_data.csv')
    expense__for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
    if expense__for_loop != divided_set_comp:
        print('Sets are not equal by == test')

    for a,b in zip(expense__for_loop, divided_set_comp):
        if not (a.issubset(b) and b.issubset(a)):
            print('Sets are not equal by == test')

    print(timeit.timeit(
                        stmt="expenses.categorize_for_loop()", 
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''', 
                        number=10000, globals=globals()))

    print(timeit.timeit(stmt="expenses.categorize_set_comprehension()", 
                        setup=
                        '''
from . import Expense
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
                        ''', 
                        number=10000, globals=globals()))
    
    fig,ax=plt.subplots()
    labels = ['Necessary', 'Food', 'Unneccessary']

    divided_expenses_sum = []
    for category_sum in divided_set_comp:
        divided_expenses_sum.append(sum(x.amount for x in category_sum))
    print(divided_set_comp)
    ax.pie(divided_expenses_sum, labels=labels, autopct = '%1.1f%%')
    plt.show()






if __name__ == "__main__":
    main()