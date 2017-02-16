import ctypes
from ctypes import wintypes
import time
import serial
from statistics import mode

user32 = ctypes.WinDLL('user32', use_last_error=True)
VK_TAB  = 0x09
VK_MENU = 0x12
VK_CONTROL = 0X11
VK_UP = 0X26
VK_DOWN = 0X28
VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_Q = 0x51
VK_W = 0x57
VK_E = 0x45
VK_R = 0x52
VK_T = 0x54
VK_Y = 0x59
VK_U = 0x55
VK_I = 0x49
VK_KEY_2 = 0x32 
VK_KEY_3 = 0x33
VK_KEY_5 = 0x35
VK_KEY_6 = 0x36
VK_KEY_7 = 0x37
#dict={'a':0x32,'c':0x33,'e':0x52,'f':0x35,'h':0x36,'j':0x37,'l':0x49,'z':0x41}
ser = serial.Serial('COM3',9600)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

VK_A = 0x41
VK_B = 0x42
VK_C = 0x43
VK_D = 0x44
VK_E = 0x45
VK_F = 0x46
VK_G = 0x47
VK_H = 0x48
VK_I = 0x49
VK_J = 0x4A
VK_K = 0x4B
VK_L = 0x4C
VK_M = 0x4D
VK_N = 0x4E
VK_O = 0x4F
VK_P = 0x50
VK_Q = 0x51
VK_R = 0x52
VK_S = 0x53
VK_T = 0x54
VK_U = 0x55
VK_V = 0x56
VK_W = 0x57
VK_X = 0x58
VK_Y = 0x59
VK_Z = 0x5A
VK_0 = 0x30
VK_1 = 0x31
VK_2 = 0x32
VK_3 = 0x33
VK_4 = 0x34
VK_5 = 0x35
VK_6 = 0x36
VK_7 = 0x37
VK_8 = 0x38
VK_9 = 0x39
# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


def Upkey():
	
	PressKey(VK_UP)
	time.sleep(2)
	ReleaseKey(VK_UP)

def Downkey():
	
	PressKey(VK_DOWN)
	time.sleep(2)
	ReleaseKey(VK_UP)

def akey():
	
	PressKey(VK_A)
	#time.sleep(2)
	ReleaseKey(VK_A)

def bkey():
	
	PressKey(VK_B)
	#time.sleep(1)
	ReleaseKey(VK_B)
def ckey():
	
	PressKey(VK_C)
	#time.sleep(1)
	ReleaseKey(VK_C)
def dkey():
	
	PressKey(VK_D)
	#time.sleep(1)
	ReleaseKey(VK_D)
	
def ekey():
	
	PressKey(VK_E)
	#time.sleep(1)
	ReleaseKey(VK_E)
def fkey():
	
	PressKey(VK_F)
	#time.sleep(1)
	ReleaseKey(VK_F)
def gkey():
	
	PressKey(VK_G)
	#time.sleep(1)
	ReleaseKey(VK_G)
def hkey():
	
	PressKey(VK_G)
	#time.sleep(1)
	ReleaseKey(VK_G)
def ckey():
	
	PressKey(VK_H)
	#time.sleep(1)
	ReleaseKey(VK_H)
def ikey():
	
	PressKey(VK_I)
	#time.sleep(1)
	ReleaseKey(VK_I)
def jkey():
	
	PressKey(VK_J)
	#time.sleep(1)
	ReleaseKey(VK_J)
def kkey():
	
	PressKey(VK_K)
	#time.sleep(1)
	ReleaseKey(VK_K)
def lkey():
	
	PressKey(VK_L)
	#time.sleep(1)
	ReleaseKey(VK_L)
def mkey():
	
	PressKey(VK_M)
	#time.sleep(1)
	ReleaseKey(VK_M)
def nkey():
	
	PressKey(VK_N)
	#time.sleep(1)
	ReleaseKey(VK_N)
def okey():
	
	PressKey(VK_O)
	#time.sleep(1)
	ReleaseKey(VK_O)
def pkey():
	
	PressKey(VK_P)
	#time.sleep(1)
	ReleaseKey(VK_P)
def qkey():
	
	PressKey(VK_Q)
	#time.sleep(1)
	ReleaseKey(VK_Q)
def rkey():
	
	PressKey(VK_R)
	#time.sleep(1)
	#ReleaseKey(VK_R)
																
def skey():
	
	PressKey(VK_S)
	#time.sleep(1)
	#ReleaseKey(VK_S)
def tkey():
	
	PressKey(VK_T)
	#time.sleep(1)
	#ReleaseKey(VK_T)
def ukey():
	
	PressKey(VK_U)
	#time.sleep(1)
	#ReleaseKey(VK_U)
def vkey():
	
	PressKey(VK_V)
	#time.sleep(1)
	#ReleaseKey(VK_V)
def wkey():
	
	PressKey(VK_W)
	#time.sleep(1)
	#ReleaseKey(VK_W)
def xkey():
	
	PressKey(VK_X)
	#time.sleep(1)
	#ReleaseKey(VK_X)
def ykey():
	
	PressKey(VK_Y)
	#time.sleep(1)
	#ReleaseKey(VK_Y)
def zkey():
	
	PressKey(VK_Z)
	#time.sleep(1)
	#ReleaseKey(VK_Z)
def zerokey():
	
	PressKey(VK_0)
	#time.sleep(1)
	#ReleaseKey(VK_0)
def onekey():
	
	PressKey(VK_1)
	#time.sleep(1)
	#ReleaseKey(VK_1)
def twokey():
	
	PressKey(VK_2)
	#time.sleep(1)
	#ReleaseKey(VK_2)
def threekey():
	
	PressKey(VK_3)
	#time.sleep(1)
	#ReleaseKey(VK_3)
def fourkey():
	
	PressKey(VK_4)
	#time.sleep(1)
	#ReleaseKey(VK_4)
def fivekey():
	
	PressKey(VK_5)
	#time.sleep(1)
	#ReleaseKey(VK_5)
def sixkey():
	
	PressKey(VK_6)
	#time.sleep(1)
	#ReleaseKey(VK_6)
def sevenkey():
	
	PressKey(VK_7)
	#time.sleep(1)
	#ReleaseKey(VK_7)
def eightkey():
	
	PressKey(VK_8)
	#time.sleep(1)

def ninekey():
	
	PressKey(VK_9)
	#time.sleep(1)
	

pvalue='z'
phex=0x41
datahex=0X41
PressKey(VK_A)
if __name__ == "__main__":
	while True:
		data3=ser.read(3)
		data2=data3.split()
		try:
			data=mode(data2)
		except:
			data=pvalue
		print(data)
		#print(data)
		print('pvalue=',pvalue)
		'''pvalue=data
        if (data!=pvalue):
        	ReleaseKey(int(dict(pvalue.decode('ascii')),16))

        	PressKey(int(dict(data.decode('ascii')),16))
        	PressKey(VK_I)
        	time.sleep(1)
        	ReleaseKey(VK_I)
        	print('world')
        else:	
        	print('Hello')
        rvalue=data
        print('rvalue=',rvalue)'''
		ser.flushInput()
		
#dict={'a':0x32,'c':0x33,'e':0x52,'f':0x35,'h':0x36,'j':0x37,'l':0x49,'z':0x41}
		if data.decode('ascii') == 'a':
			PressKey(VK_I)
			datahex = VK_I
		'''if data.decode('ascii') == 'b':
			key2()'''
		if data.decode('ascii') == 'b':
			PressKey(VK_9)
			datahex = VK_9
		if data.decode('ascii') == 'c':
			PressKey(VK_O)
			datahex = VK_O
		if data.decode('ascii') == 'd':
			PressKey(VK_0)
			datahex = VK_0
		if data.decode('ascii') == 'e':
			PressKey(VK_P)
			datahex = VK_P
		if data.decode('ascii') == 'f':
			PressKey(0x52) #r
			#time.sleep(0.1)
			datahex=0x52
		''''if data.decode('ascii') == 'k':
			key7()'''
		if data.decode('ascii') == 'g':
			PressKey(0x35) #5
			#time.sleep(0.1)
			datahex=0x35
		if data.decode('ascii') == 'h':
			PressKey(0x54) #t
			#time.sleep(0.1)
			datahex=0x54	
		if data.decode('ascii') == 'i':
			PressKey(0x36) #6
			#time.sleep(0.1)
			datahex=0x36
		if data.decode('ascii') == 'j':
			PressKey(0x59) #y
			#time.sleep(0.1)
			datahex=0x59
		if data.decode('ascii') == 'k':
			PressKey(0x37) #7
			#time.sleep(0.1)
			datahex=0x37
		if data.decode('ascii') == 'l':
			PressKey(VK_M) #u
			#time.sleep(0.1)
			
			datahex=VK_M				
		if data.decode('ascii') == 'm':
		    PressKey(VK_Q)
		    datahex = VK_Q
		if data.decode('ascii') == 'n':
		    PressKey(VK_2)
		    datahex = VK_KEY_2
		if data.decode('ascii') == 'o':
		    PressKey(VK_W)
		    datahex = VK_W    	
		if data.decode('ascii') == 'p':
		    PressKey(VK_3)
		    datahex = VK_3
		if data.decode('ascii') == 'q':
		    PressKey(VK_E)
		    datahex= VK_E
		if data.decode('ascii') == 'r':
		    PressKey(VK_R)
		    datahex = VK_R
		if data.decode('ascii') == 's':
		   PressKey(VK_5)
		   datahex = VK_5
		if data.decode('ascii') == 't':
		    PressKey(VK_T)
		    datahex = VK_T
		if data.decode('ascii') == 'u':
		    PressKey(VK_6)
		    datahex = VK_6
		if data.decode('ascii') == 'v':
		    PressKey(VK_Y)
		    datahex = VK_Y
		if data.decode('ascii') == 'w':
		    PressKey(VK_7)
		    datahex = VK_7
		if data.decode('ascii') == 'x':
		    PressKey(VK_U)
		    datahex = VK_U
		if data.decode('ascii') == 'z':
		    PressKey(0x41) #a
		    datahex=0x41                
		if data!=pvalue:
			ReleaseKey(phex)
		pvalue=data
		phex=datahex

        
