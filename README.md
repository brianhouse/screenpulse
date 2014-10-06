Screenpulse
===========

Everyday cybernetics


Requires Python 3.3+

    sudo pip-3.3 install -r requirements.txt

See the massive todo for PyObjC fun    


#### Arduino setup    
    ls /dev/tty.*
to see devices. then plug in the Arduino and do it again to find the port, likely in the form /dev/tty.usbserial*  (OS X 10.9)

Set Arduino.app to the proper board, processor (my Nano is ATmega328), and port.

Load the PulseSensorAmped_Arduino_1dot2.ino sketch -- from the Pulse Sensor developers

Attach to 5v, Ground, and A0.


### Copyright/License

Copyright (c) 2014 Brian House

This program is free software licensed under the GNU General Public License, and you are welcome to redistribute it under certain conditions. It comes without any warranty whatsoever. See the LICENSE file for details, or see <http://www.gnu.org/licenses/> if it is missing.

Projects that use this software must credit Brian House and link to http://brianhouse.net

