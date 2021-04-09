

c2cmap = {
	'stretch':'https://www.youtube.com/watch?v=ZSIp00SewO8',
	'dw':'https://www.youtube.com/watch?v=oPVte6aMprI',
	'null':'https://www.youtube.com/watch?v=V5c-eqNxeSQ&t=17s'
}

print("""

	Current c2cmap:

""")

for pair in c2cmap.items():
	print(pair)

print("""

	update? (y/n):

""")

res = input()

if res=='y':
	print('stretch:')
	new_c2cmap['stretch'] = input()

	print('dw:')
	new_c2cmap['dw'] = input()

	print('null:')
	new_c2cmap['null'] = input()

	print("""

		Updated c2cmap:

	""")

	c2cmap = new_c2cmap

	for pair in c2cmap.items():
		print(pair)

print("Complete.")