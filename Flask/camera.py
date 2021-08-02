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

            # 프레임 생성될 때까지 대기
            while self.frame is None:
                pass

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
        
        # Capture images continuously from the camera 
        # as an infinite iterator.
        for foo in cls.camera.capture_continuous(stream, 'jpeg',
                                                use_video_port=True):
            stream.seek(0)
            cls.frame = stream.read()

            stream.seek(0)
            stream.truncate()

            # 반응 없을 경우 탈출
            if time.time() - cls.last_access > 10:
                break

            # 100ms 딜레이(10fps)
            time.sleep(0.1)

        cls.thread = None