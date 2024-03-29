import pygame
import sys
pygame.init()
pygame.font.init()


pxl = 16
class color(object):
	red = 0
	green = 0
	blue = 0
	def __init__(self,red,green,blue):
		self.red = red
		self.green = green
		self.blue = blue

class win(object):
	scr = None
	width = 0
	height = 0
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.scr = pygame.display.set_mode((width,height))
screen = win(1000,700)
class grid(object):
	grid = {}
	fg = color(255,255,255)
	bg = color(255,255,255)
	width = 0
	height = 0
	def __init__(self,width,height,c):
		self.bg = c
		self.width = width
		self.height = height
		for x in range(width):
			for y in range(height):
				self.grid[str(x)+","+str(y)] = self.bg
	def get(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			return self.grid[str(x)+","+str(y)]
	def get_tuple(self,x,y):
		if (self.grid[str(x)+","+str(y)] != None):
			c =  self.grid[str(x)+","+str(y)]
			return (c.red,c.green,c.blue)
	def set(self,x,y,c):
		self.grid[str(x)+","+str(y)] = self.fg
g = grid(32,32,color(0,0,0))
cps = [color(255,255,255),color(0,0,0),color(255,0,0),color(0,255,0),color(0,0,255),color(255,255,0),color(0,255,255),color(255,0,255)]
cps0 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
cps1 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
cps2 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
cps3 = [color(160,160,160),color(0,72,184),color(8,48,224),color(88,24,216),color(160,8,168),color(208,0,88),color(208,16,0),color(160,32,0),color(8,88,0),color(0,104,0),color(0,104,16),color(0,96,112)]
while True:

	for event in pygame.event.get():
		if event.type == (pygame.QUIT):
			print("Exiting!")
			sys.exit()
			quit()


		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print(event.pos)
				if(event.pos[0] <= 512-8):
					if(event.pos[1] <= 512):
						print("Paint")
						print(str(int(event.pos[0]/32))+", "+str(int(event.pos[1]/32)))
						g.set(int(event.pos[0]/pxl),int(event.pos[1]/pxl),color(255,255,255))
				if(event.pos[0] >= screen.width-16):
					if(event.pos[1] <= screen.width):
						if (event.pos[1]/16 <= len(cps)):
							g.fg = cps[int(event.pos[1]/16)]
						else:
							g.fg = color(0,0,0)
			elif(event.button == 4):
				pxl = pxl*2
			elif(event.button == 5):
				if pxl > 1:
					pxl = pxl/2
			else:
				print (event.button)
	pygame.draw.rect(screen.scr,(35,39,42),pygame.Rect(0,0,screen.width,screen.height))
	for x in range(int(g.width)):
		for y in range(int(g.height)):
			c = g.get_tuple(x,y)
			pygame.draw.rect(screen.scr, c, pygame.Rect(x*pxl,y*pxl,1*pxl,1*pxl))

	c = 0
	for x in range(int(pxl/8)):
		for y in range(int(screen.width/8)):
			if c in range(len(cps)):
				pygame.draw.rect(screen.scr,(cps[c].red,cps[c].green,cps[c].blue) , pygame.Rect(screen.width-16,y*16,1*16,1*16))
			c+=1

	pygame.display.update()
	#print("update")
