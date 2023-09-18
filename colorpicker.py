# debut: 16h42
# fin: 17h52

import tkinter as tk 
import pyperclip

class App:
	def __init__(self):
		self.root = tk.Tk()

		self.r_var = tk.IntVar()
		self.g_var = tk.IntVar()
		self.b_var = tk.IntVar()

		self.color = tk.StringVar(value="#000000")
		self.color.trace("w", self.set_background)

		self.valid=True


		self.create_window()
		self.add_widgets()
		self.set_color()
		self.display()

	def create_window(self):
		self.root.geometry("350x210")
		self.root.resizable(False, False)
		self.root.title("RGB Color generator")

		try:
			self.root.iconbitmap("multicolor.ico")
		except:
			print("[IconNotFounException] GUI Icon not found. Make sure the path is respected")
	def add_widgets(self):
		r = tk.Frame(self.root, width=250)
		r.pack(pady=(5, 0))
		r_head = tk.Frame(r)
		r_head.pack(fill="x")
		r_head_text = tk.Label(r_head, text="Red\tR", fg="red", font=("Arial", 12))
		r_head_text.pack(side="left")
		r_head_value = tk.Entry(r_head, width=4, justify="right", textvariable=self.r_var)
		r_head_value.pack(side="right")
		r_scale = tk.Scale(r, from_=0, to=255, length=200, orient="horizontal", showvalue=False, relief="flat", sliderlength=15, width=10, variable=self.r_var)
		r_scale.config(command=lambda x:self.set_color())
		r_scale.pack(fill="x")

		g = tk.Frame(self.root, width=250)
		g.pack(pady=(5, 0))
		g_head = tk.Frame(g)
		g_head.pack(fill="x")
		g_head_text = tk.Label(g_head, text="Green\tG", fg="green", font=("Arial", 12))
		g_head_text.pack(side="left")
		g_head_value = tk.Entry(g_head, width=4, justify="right", textvariable=self.g_var)
		g_head_value.pack(side="right")
		g_scale = tk.Scale(g, from_=0, to=255, length=200, orient="horizontal", showvalue=False, relief="flat", sliderlength=15, width=10, variable=self.g_var)
		g_scale.config(command=lambda x:self.set_color())
		g_scale.pack(fill="x")

		b = tk.Frame(self.root, width=250)
		b.pack(pady=(5, 0))
		b_head = tk.Frame(b)
		b_head.pack(fill="x")
		b_head_text = tk.Label(b_head, text="Blue\tB", fg="blue", font=("Arial", 12))
		b_head_text.pack(side="left")
		b_head_value = tk.Entry(b_head, width=4, justify="right", textvariable=self.b_var)
		b_head_value.pack(side="right", padx=(50, 0))
		b_scale = tk.Scale(b, from_=0, to=255, length=200, orient="horizontal", showvalue=False, relief="flat", sliderlength=15, width=10, variable=self.b_var)
		b_scale.config(command=lambda x:self.set_color())
		b_scale.pack(fill="x")

		result = tk.Frame(self.root, width=250)
		result.pack(pady=(30, 0))
		self.result_output = tk.Entry(result, fg="#fff", textvariable=self.color, width=10, font=("Helvetica", 14), justify="right")
		self.result_output.pack(side="left", ipady=4)
		self.copy_output = tk.Button(result, text="Copy", bg="blue", activebackground="blue", font=("Helvetica", 11, "bold"), width=8, command=lambda x=self.color:self.copy(x.get()))
		self.copy_output.pack(side="left", padx=(5, 0))

	def rgb_to_hex(self, r, g, b):
		red = hex(r)[2:].zfill(2)
		green = hex(g)[2:].zfill(2)
		blue = hex(b)[2:].zfill(2)

		return "#" + red + green + blue

	def get_saturation(self, rgb):
		return sum([i for i in self.hex_to_rgb(rgb)])

	def hex_to_rgb(self, rgb):
		r=0
		g=0
		b=0
		if len(rgb)==7:
			r = int(rgb[1:3], 16)
			g = int(rgb[3:5], 16)
			b = int(rgb[5:7], 16)
		else:
			r = int(rgb[1]*2, 16)
			g = int(rgb[2]*2, 16)
			b = int(rgb[3]*2, 16)


		return r, g, b

	def set_color(self):
		color = self.rgb_to_hex(self.r_var.get(), self.g_var.get(), self.b_var.get())

		self.color.set(color)
		self.saturation = self.get_saturation(color)

	def set_background(self, *args):
		if not self.color.get().startswith("#"):
			self.result_output.icursor(2)

		self.color.set("#" + self.color.get().replace("#", ""))
			
			
		try:
			self.result_output.config(bg=self.color.get())
			self.saturation = self.get_saturation(self.color.get())
			self.result_output.config(fg="#000" if self.saturation>380 else "#fff")

			self.r_var.set(self.hex_to_rgb(self.color.get())[0])
			self.g_var.set(self.hex_to_rgb(self.color.get())[1])
			self.b_var.set(self.hex_to_rgb(self.color.get())[2])
			self.valid=True
		except:
			self.result_output.config(bg="#000")
			self.result_output.config(fg="#fff")

			self.r_var.set(0)
			self.g_var.set(0)
			self.b_var.set(0)
			self.valid = False


	def copy(self, color):
		if self.valid:
			pyperclip.copy(color)
			self.copy_output.config(text="Copied")
		else:
			self.copy_output.config(text="Invalid", fg="red")

		self.root.after(500, lambda:self.copy_output.config(text="Copy", fg="#000"))



	def display(self):
		self.root.mainloop()


App()