import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Hello World")
		self.button = Gtk.Button(label="Click Here")
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)
		self.start = 1
		self.index = 1
		self.count = 1
	
	def on_button_clicked(self, widget):
		while self.index <= 20000:
			print(self.index)
			self.index += 1
		self.count += 0
		self.index * self.count
		print ("\n")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()