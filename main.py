import collections
import itertools

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

star_list = [
	['a', 'b', 'c', ['e', 'q', 'r']],
	['d', 'e', 'f', 'h', 'F'],
	[1, 2, None],
]

class FlatIterator:
	def __init__(self, list):
		self.i, self.j = 0, 0
		self.list = list

	def __iter__(self):
		return self

	def __next__(self):

		if len(self.list) <= self.i:
			raise StopIteration

		res = self.list[self.i][self.j]
		if len(self.list[self.i]) == self.j + 1:
			self.j = 0
			self.i += 1
		else:
			self.j += 1
		return res


# class StarIterator:
# 	def __init__(self, list):
# 		self.list = list
# 		self.index = []
# 		for i in (0, 10):
# 			self.index.append(0)
#
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
#
# 		if len(self.list) <= self.i:
# 			raise StopIteration
#
# 		res = get_by_index(self.list, self.index)
#
# 		if len(self.list[self.i]) == self.j + 1:
# 			self.j = 0
# 			self.i += 1
# 		else:
# 			self.j += 1
# 		return res


def FlatGenerator(list):
	i = 0
	j = 0
	while(len(list) > i):
		l = mylen(list[i])
		if l == 0:
			yield list[i]
		else:
			while (l > j):
				yield list[i][j]
				j += 1
		i += 1
		j = 0

def mylen(obj):
	try:
		l = len(obj)
	except Exception as e:
		l = 0
	return l

# def get_by_index(mylist,index):
# 	el = mylist
# 	for i in range(0, len(index)):
# 		el = el[index[i]]

def task_1():
	print("Задача 1")
	for item in FlatIterator(nested_list):
		print(item)
	flat_list = [item for item in FlatIterator(nested_list)]
	print(flat_list)
def task_2():
	print("Задача 2")
	for item in FlatGenerator(nested_list):
		print(item)

def	flat_list(myList):
	if isinstance(myList, list):
		f_list = []
		for item in FlatGenerator(myList):
			print(item)
			f_list.append(item)
	else:
		f_list = myList
	return f_list

def task_4():
	print("Задача 4")
	f_list = star_list
	while flat_list(f_list) != f_list:
		f_list = flat_list(f_list)
	print(f_list)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
	task_1()
	task_2()
	task_4()

