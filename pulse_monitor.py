#!/usr/bin/env python3

import array, serial, threading, time, Queue, glob
from housepy import log

class PulseMonitor(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.queue = Queue.Queue()
        try:
            device_name = glob.glob("/dev/tty.usbmodem*")[0]            
            self.device = serial.Serial(device_name, 115200)
            self.device.open()        
        except Exception as e:
            if e.message == "list index out of range":
                log.error("Arduino not found")
                return
            if e.message != "Port is already open.":
                log.error(log.exc(e))
                return
        log.info("Receiving pulse messages on %s" % device_name)                
        self.start()

    def run(self):
        message = []
        while True:
            try:
                data = self.device.read()
                if data == "\n":
                    message = ''.join(message).strip()
                    if len(message):
                        try:
                            if message[0] == 'S':   # sensor data
                                # log.debug("Sensor: %s" % int(message[1:]))
                                pass
                            elif message[0] == 'B':   # bpm data
                                bpm = int(message[1:])
                                # log.debug("BPM: %s" % bpm)
                                if bpm > 50 and bpm < 200:
                                    while not self.queue.empty():
                                        self.queue.get_nowait()
                                    self.queue.put(bpm)
                            elif message[0] == 'Q':   # hrv data
                                # log.debug("HRV: %s" % int(message[1:]))                            
                                pass
                        except Exception as e:
                            # log.error(log.exc(e))
                            pass
                    message = []
                else:
                    message.append(data)
            except Exception as e:
                # if e.message == "device reports readiness to read but returned no data (device disconnected?)":
                #     continue
                log.error(log.exc(e))
                if e.message == "Device not configured":
                    break


if __name__ == "__main__":

    pulse_monitor = PulseMonitor()
    if pulse_monitor.is_alive():
        while True:
            bpm = pulse_monitor.queue.get()
            log.info("BPM: %s" % bpm)
            time.sleep(0.001)

