#Code to find the runner up of any event using List Comprehension

n = int(input()) #Taking Input of Marks
marksheet = [[input(), float(input())] for _ in range(n)]
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1] # Finding the runnerup
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
