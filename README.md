# FixSteelseriesSonar

This python script connects using steel series local API to move to streamer mode and back. This fixes a situation where you might unplug your USB headset and replug it but Steelseries Sonar no longer detects it no matter what.

This flips it to "streamer mode" which forces it to rediscover the USB devices and then it works again.

There is additional code that looks for a USB device (that you specify in the script) and will do the behavior everytime the device goes away and comes back. In my case it was a hyper x microphone. Really weird workaround.

## references packages
- https://github.com/Mark7888/steelseries-sonar-py
- https://github.com/rene-aguirre/pywinusb