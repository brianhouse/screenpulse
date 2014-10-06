#!/usr/bin/env python3

import array, serial, threading, time, queue, glob
from housepy import log

class PulseMonitor(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.queue = queue.Queue()
        try:
            device_name = glob.glob("/dev/tty.usbserial*")[0]            
            self.device = serial.Serial(device_name, 115200)
            log.info("Connecting to %s" % device_name)
        except IndexError as e:
            log.error("Arduino not found")
            return
        except serial.SerialException as e:            
            log.error("Serial error: %s" % e)
            return
        log.info("Receiving pulse messages on %s" % device_name)                
        self.start()

    def run(self):
        message = []
        bpm, hrv = None, None
        while True:
            try:
                data = self.device.read()
                if data == "\n".encode('ascii'):
                    message = ''.join(message).strip()
                    if len(message):
                        try:
                            if message[0] == 'S':   # sensor data
                                # log.debug("Sensor: %s" % int(message[1:]))
                                pass
                            elif message[0] == 'B':   # bpm data
                                bpm = int(message[1:])
                                # log.debug("BPM: %s" % bpm)
                            elif message[0] == 'Q':   # hrv data
                                hrv = int(message[1:])                                
                                # log.debug("HRV: %s" % hrv)  
                                self.queue.put((bpm, hrv))
                        except Exception as e:
                            # log.error(log.exc(e))
                            pass
                    message = []
                else:
                    message.append(data.decode('ascii'))
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
            bpm, hrv = pulse_monitor.queue.get()
            log.info("BPM: %s HRV: %s" % (bpm, hrv))
            time.sleep(0.001)

