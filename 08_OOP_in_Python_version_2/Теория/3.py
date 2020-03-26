x = eval('sum([3, 2])')
print(x)

im = 'im'
port = 'port'
exec(f"""
{im}{port} os
y = 1
y += 2
print(y)
""")