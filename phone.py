from jnius import autoclass

def toggle_flashlight(state: bool):
    # Access Android hardware service
    Camera = autoclass('android.hardware.Camera')
    CameraParameters = autoclass('android.hardware.Camera$Parameters')

    # Get the camera instance
    camera = Camera.open()
    params = camera.getParameters()

    if state:
        params.setFlashMode(CameraParameters.FLASH_MODE_TORCH)
    else:
        params.setFlashMode(CameraParameters.FLASH_MODE_OFF)

    camera.setParameters(params)
    if state:
        camera.startPreview()
    else:
        camera.stopPreview()
        camera.release()

# Turn on flashlight
toggle_flashlight(True)

# Turn off flashlight
# toggle_flashlight(False)
