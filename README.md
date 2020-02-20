# OpenCV Station Powered by Raspberry Pi and Android Phone
OpenCV powered Color tracker using Android phone Camera


## Hardware Used

- Samsung Alpha (SM-G850) Phone / Android 5.0.2

- Pavel Khlebovich's [IP WebCam App](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US)
    - Available on Google Play Store / Min Android Version : 4.0

- [Raspberry Pi 3 B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)
    - [32 GB Memory Card](https://www.amazon.com/gp/product/B06XWN9Q99/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

- [SmartPi Touch Case](https://www.amazon.com/gp/product/B01HV97F64/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

- LogiTech Wireless mouse/keyboard Combo

## Softwore Used
- OpenCV via Python
    - Instructions on how to install can be found [here](https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/) by Adrian Rosebrock

- Python 3
    - Should be pre-install in raspbian

- Rasbian
    - Instructions on how to install can be found [here](https://www.raspberrypi.org/documentation/installation/installing-images/README.md)



# How to Setup OpenCV station

 * Use your computer to install Raspbian on the Memory card of your pi.

 * Install the IP WebCam on phone of choice

 * If possible, boot the raspberry pi connected to a regular screen via it's native HDMI port as an initial check of systems. Verify that the Rasbian OS boots as expected. Test Wireless Mouse/Keyboard combo. Otherwise, use SSH to login and verify connectivity and boot to the Desktop screen. If you are booting into the terminal, try ```startx	``` after you login.

 * Follow the OpenCV instructions posted above and verify your installation has been successful via the following commands towards Python interpreter on your RPI terminal

 ``` 
    import cv2
    cv2.__version__
```

- There you should see the version installed. If not, review instructions and find potential issue.

- Use IPWebcam app to start a stream server
    - Locate the IP address assigned after you start the server on your phone. Save this address.

- As a true test for the installation, we use the following instructions to write a sample computer vision script for Python. We will make small edits to fit the Hardware we are using. Instructions for the basic setup can be found [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces). The changes that we will make will be the following:
          
    cap = cv2.VideoCapture(0) will instead refer to the ip address given to the WebCamera Stream such as 

        - cap = cv2.VideoCapture('https://xxx.xxx.x.xxx:8080/video')


- If this is successful, you should see 3 displays appear on the screen of the monitor connected to the pi. Each would be a replication of the stream/screen on your phone but with different filters. Try to use a blue item to test the Mask Image as it highlights the items of interest by color. And the verify the color you are capturing via the Res Image on the monitor.

- After you are content with tests, install the Raspberry Pi into the Smart Touch Case and verify the screen's working condition.


Author:
Chris Perez