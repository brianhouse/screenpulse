the USB device should ideally deliver the software as well, is that possible?
sounds hard.

just have a product video that implies it.

get jordan to shoot this.

is this concept deep enough? too simple?

/

need nice conductive thread to make it look good.

and of course a really small arduino.

/

look at this -- could be bluetooth? why.
http://arduino.cc/en/ArduinoAtHeart/Products


definitely the smallest:
http://arduino.cc/en/Main/ArduinoBoardProMini

and then would solder on an inverted usb connector


/

obvi prototype this all first with a big arduino

3d print a case, obvi.
or better, lasercut it.

plexi, baby!

//

http://stackoverflow.com/questions/12864650/importerror-no-module-named-pyobjc
https://pythonhosted.org/pyobjc/examples/Cocoa/AppKit/SimpleService/index.html

/
installing
https://groups.google.com/forum/#!topic/pupil-discuss/ofSmfsrt3ag

trying to get around failures
http://blog.pythonaro.com/2012/08/how-to-compile-pyobjc-for-python-3-on.html


sudo pip3.4 install pyobjc-core==2.5.1
sudo pip3.4 install pyobjc

sudo pip3.4 install pyobjc-framework-Cocoa      # fail with version incompatibility


sudo pip3.4 install pyobjc-framework-Cocoa==2.5.1

installs.
but is 2.5.1 going to work with python3?

sudo pip3.4 install pyobjc-framework-Quartz==2.5.1
sudo pip3.4 install pyobjc-framework-CoreData==2.5.1
sudo pip3.4 install pyobjc-framework-QTKit==2.5.1


sudo pip3.4 install pyobjc-framework-CFNetwork==2.5.1
sudo pip3.4 install pyobjc-framework-CoreData==2.5.1
sudo pip3.4 install pyobjc-framework-CoreLocation==2.5.1
sudo pip3.4 install pyobjc-framework-CoreText==2.5.1
sudo pip3.4 install pyobjc-framework-ExceptionHandling==2.5.1
sudo pip3.4 install pyobjc-framework-FSEvents==2.5.1
sudo pip3.4 install pyobjc-framework-InputMethodKit==2.5.1
sudo pip3.4 install pyobjc-framework-InstallerPlugins==2.5.1

sudo pip3.4 install pyobjc-framework-LatentSemanticMapping==2.5.1
sudo pip3.4 install pyobjc-framework-Message==2.5.1
sudo pip3.4 install pyobjc-framework-QTKit==2.5.1
sudo pip3.4 install pyobjc-framework-ScreenSaver==2.5.1
sudo pip3.4 install pyobjc-framework-ScriptingBridge==2.5.1
sudo pip3.4 install pyobjc-framework-WebKit==2.5.1


failed:
sudo pip3.4 install pyobjc-framework-InterfaceBuilderKit==2.5.1
sudo pip3.4 install pyobjc-framework-XgridFoundation==2.5.1




//////


concept: 
not just pure heartrate. can alter it, push it.