# camera.py
import time
import io
import threading
import picamera

class Camera(object):
    thread = None
    frame = None
    last_access = 0
    camera = picamera.PiCamera()

    def initialize(self):
        if Camera.thread is None:
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    def close_cam(self):
        self.camera.close()

    @classmethod
    def _thread(cls):
        cls.camera.resolution = (320, 240)
        cls.camera.hflip = True
        cls.camera.vflip = True

        cls.camera.start_preview()
        cls.camera.annotate_text_size = 50
        cls.camera.annotate_text = "Smart Farm"
        cls.camera.annotate_foreground = picamera.Color('Green')

        time.sleep(2)

        stream = io.BytesIO()
        
        for foo in cls.camera.capture_continuous(stream, 'jpeg',
                                                use_video_port=True):
            stream.seek(0)
            cls.frame = stream.read()

            stream.seek(0)
            stream.truncate()

            if time.time() - cls.last_access > 10:
                break

        cls.thread = None