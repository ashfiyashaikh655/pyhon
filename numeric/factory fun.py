def maker(n):
    def action(x):
        return x*n
    return action
f=maker(2)
value=f(4)
print('value:',value)
