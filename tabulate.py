debug = False

class Column:
	def __init__(self, *data, header = "", prefix = "", suffix = "", justification = "left"):
		"""Generates column object;
  		header: str,
		justification direction: str ('left' or 'right'),
  		and data: list[str].
		"""
		self.header = str(header)
		self.justification = justification.lower()
		if not self.justification in ["left", "right"]:
			raise ValueError("Justification must be either 'left' or 'right'")
		if debug: print(f"header:\n{self.header}\n")
		if debug: print(f"justification:\n{self.justification}\n")
		
		self.data = []
		for cell in data:
			self.data.append(str(prefix) + str(cell) + str(suffix))
		if debug: print(f"data:\n{self.data}\n")
		
		self.cell_len = len(header)
		for cell in self.data:
			cell_len = len(cell)
			if cell_len > self.cell_len: self.cell_len = cell_len
		if debug: print(f"cell length:\n{self.cell_len}\n")
	
		for index, cell in enumerate(self.data):
			filler = " " * (self.cell_len - len(cell))
			cell = filler + cell if justification == "right" else cell + filler
			self.data[index] = cell
		if debug: print(f"adjusted data:\n{self.data}\n")

class Table:
	def __init__(self, *columns: Column, headers = True):
		for column in columns:
			if not isinstance(column, Column):
				raise TypeError("Collumns must be object 'Column'")
		rows = len(columns[0].data)
		for column in columns[1:]:
			if len(column.data) != rows:
				raise ValueError("All columns must be the same length")

		self.rows = rows
		self.columns = columns
		self.headers = str(headers)

	def render(self):
		output = ""
		if self.headers:

			# Add header to output
			for cell in range(len(self.columns)):
				filler = " " * (self.columns[cell].cell_len - len(self.columns[cell].header))
				output = output + self.columns[cell].header + filler
				output += " " if cell != len(self.columns) - 1 else "\n"
					
			# Add divider to output
			for cell in range(len(self.columns)):
				output = output + self.columns[cell].cell_len * "-"
				output += " " if cell != len(self.columns) - 1 else "\n"
	
		# Add data to putput
		for row in range(self.rows):
			for cell in range(len(self.columns)):
				output = output + self.columns[cell].data[row]
				output += " " if cell != len(self.columns) - 1 else "\n"

		if debug: input()
		return output
