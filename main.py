# nested_list = [
# 	['a', 'b', 'c'],
# 	['d', 'e', 'f', 'h', False],
# 	[1, 2, None],
# ]
# for item in FlatIterator(nested_list):
# 	print(item) #
# 'a'
# 'b'
# 'c'
# 'd'
# 'e'
# 'f'
# 'h'
# False
# 1
# 2
# None

from iterator import FlatIterator


if __name__ == __name__:
	nested_list = [
		['a', 'b', 'c'],
		['d', 'e', 'f', 'h', False],
		[1, 2, None],
	]
	for item in FlatIterator(nested_list):
		print(item)

	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)
