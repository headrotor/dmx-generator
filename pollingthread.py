# hardware interface to Alicat flow controllser
import serial #get from http://pyserial.sourceforge.net/
import sys
import time
import wx
import threading


class GetHWPoller(threading.Thread):
  """ thread to repeatedly poke hardware
  pollfunc:  method to call repeatedly
  sleeptime: time to sleep between queries"""

  def __init__(self,sleeptime,pollfunc):

    self.sleeptime = sleeptime
    self.pollfunc = pollfunc
    threading.Thread.__init__(self)
    self.runflag = threading.Event()
    self.runflag.clear()
      
  def run(self):
    self.runflag.set()
    self.worker()

  def worker(self):
    while(1):
      if self.runflag.is_set():
        self.pollfunc()
        #time.sleep(self.sleeptime)
      else:
        time.sleep(0.01)

  def pause(self):
    self.runflag.clear()

  def resume(self):
    self.runflag.set()

  def running(self):
    return(self.runflag.is_set())

  def kill(self):
    print "WORKER END"
    sys.stdout.flush()
    self._Thread__stop()
 
class HW_Interface(object):
  """Class to interface with serial hardware.
  Repeatedly polls hardware, unless we are sending a command
  "ser" is a serial port class from the serial module """

  def __init__(self,ser,sleeptime):
    self.ser = ser
    # R, G, B, A color tuple
    self.color = (0, 0, 0, 0)
    # base DMX addresses of all units
    self.all_base = (1,5,10,14)
    self.base = ()
    self.active = True
    nullstr = u"00 "*20
    # make a buffer full of zeros
    self.buf = bytearray.fromhex(nullstr)

    self.sleeptime = float(sleeptime)
    self.worker = GetHWPoller(self.sleeptime,self.poll_HW)
    self.response = None # last response retrieved by polling
    self.worker.start()
    self.callback = None

  def set_server(self, onoff):
    self.active = onoff
 
  def set_rgba(self,rgba):
    self.color = rgba
    print "got color: " + repr(self.color)

  def kill(self):
    self.worker.kill()

  def poll_HW(self):
    """Called repeatedly by thread. Check for interlock, of OK get pressure"""
    if self.active:
      
      self.ser.flush() # wait until all output is written
      # send a break to start next DMX packet
      self.ser.setBreak(True)
      time.sleep(0.01) # >1 ms break, hopefully (spec says > 88 uS)
      self.ser.setBreak(False)
      time.sleep(0.01) # Mark-After-Break for 10 uS
      # start code buf[0] should be zero

      # need to update this for different colors for different fixtures
      r, g, b, a = self.color
      self.buf[0] = 0

      
      # if no fixture base specified,
      if len(self.base) == 0:
        # step through all fixtures
        self.base = self.all_base
      #print "base " + str(self.base)
      for base in self.base:
          self.buf[base + 0] = r
          self.buf[base + 1] = g
          self.buf[base + 2] = b
          self.buf[base + 3] = a

     
    # write the DMX packet to the serial port
    self.ser.write(self.buf)
    sys.stdout.flush()
    time.sleep(0.02)


if __name__ == '__main__':
  usage = """ commands: 
  --> v              where v is int: set all r,g,b,a values to v 
  --> r g b a        where r,g,b,a integers between 0 & 255, 
                     set corresponding color channel to value 
  --> X exit """


  portname = "COM1"

#setup serial port for DMX, blocking write, two stopbits, 250Kbaud
  ser = serial.Serial(port=portname,
                  baudrate=250000,
                  writeTimeout = None,
                  stopbits=serial.STOPBITS_TWO)
  print "opened port " + portname + " for DMX"

  sys.stdout.flush()
  dmx = HW_Interface(ser,0.1)
  #dmx.run()

  print usage
  print "Interactive mode. Commands: "
 
  r, g, b, a = (0, 0, 0, 0)

  while(1):
    cmd = raw_input('--> ')
    cmd = cmd.strip()
    cmd = cmd.split()

    if cmd[0] == "X":
      # clean exit
      print "bye!"
      sys.stdout.flush()
      dmx.kill()
      sys.exit()

    print "got cmd: '%s'" % repr(cmd)
    sys.stdout.flush()
    if len(cmd) >3:
      r = int(cmd[0])
      g = int(cmd[1])
      b = int(cmd[2])
      a = int(cmd[3])
    elif len(cmd) == 1:
      r = int(cmd[0])
      g = int(cmd[0])
      b = int(cmd[0])
      a = int(cmd[0])



    print "r,g,b,a=" + str((r,g,b,a))
    dmx.set_rgba((r,g,b,a))


