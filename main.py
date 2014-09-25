#!/usr/bin/env python3

import time
from Cocoa import NSApplication, NSApp
# from Foundation import *
# from PyObjCTools import AppHelper


from Quartz import *
"""
in Quartz:
CGAcquireDisplayFadeReservation
kCGErrorSuccess
kCGMaxDisplayReservationInterval
kCGDisplayBlendNormal
kCGDisplayBlendSolidColor
CGDisplayCapture
CGDisplayFade
CGReleaseDisplayFadeReservation
"""
"""
not in Quartz:
# kCGDirectMainDisplay ==> CGMainDisplayID()
# CGDisplayFadeReservationToken
# CGError
"""


# app = NSApplication.sharedApplication()

# # Bring app to top (True)
# NSApp.activateIgnoringOtherApps_(True)

# get the display token
# print("Max display reservation is %s" % kCGMaxDisplayReservationInterval)

# https://developer.apple.com/library/mac/documentation/GraphicsImaging/Reference/Quartz_Services_Ref/Reference/reference.html#//apple_ref/c/func/CGDisplayFade

fade_level = 0.1 #kCGDisplayBlendSolidColor

def beat():
    result, token = CGAcquireDisplayFadeReservation(0.4, None)
    if result != kCGErrorSuccess:
        print("Could not reserve display!")
        exit()
    CGDisplayFade(token, 0.075, kCGDisplayBlendNormal, fade_level, 0.5, 0.0, 0.0, True)    
    CGDisplayFade(token, 0.075, fade_level, kCGDisplayBlendNormal, 0.0, 0.0, 0.0, True)        
    CGDisplayFade(token, 0.075, kCGDisplayBlendNormal, fade_level, 0.5, 0.0, 0.0, True)    
    CGDisplayFade(token, 0.075, fade_level, kCGDisplayBlendNormal, 0.0, 0.0, 0.0, True)        
    CGReleaseDisplayFadeReservation(token)

# do a fade
print("Starting...")
while True:
    try:
        beat()
        time.sleep(0.75)
    except KeyboardInterrupt as e:
        print("Goodbye")
        break


