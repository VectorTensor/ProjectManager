from database import *
from tabulate import tabulate

data=show_table()
print(tabulate(data,headers=["S.N", "Work","Remarks"]))


