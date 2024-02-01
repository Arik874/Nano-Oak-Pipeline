import depthai as dai

# Create a pipeline
pipeline = dai.Pipeline()

# Define the camera source
cam = pipeline.createColorCamera()
cam.setBoardSocket(dai.CameraBoardSocket.RGB)
cam.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)

# Create an XLinkOut to output the video
xout = pipeline.createXLinkOut()
xout.setStreamName("video")

# Link the camera output to the XLinkOut
cam.video.link(xout.input)

# Connect to the device
with dai.Device(pipeline) as device:
    # Pipeline is created and the device is connected
    print("Successfully connected to the device!")
