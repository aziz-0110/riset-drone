import numpy as np

class Model:
    def __init__(self):
        """ mengambil nilai lower dan upper dari warna yg di tentukan """
        young_blue = [240, 255, 0]  # target kuning
        old_blue = [255, 90, 0]  # target merah
        green = [0, 255, 0]  # target hijau

        self.lower_red, self.upper_red = self.limit_color(old_blue)
        self.lower_yellow, self.upper_yellow = self.limit_color(young_blue)
        self.lower_green, self.upper_green = self.limit_color(green)

    def color_map(self, src, condision_record, total_px):
        import cv2

        ret, frame = src.read()
        ori, hsv, hsv_vid_out = None, None, None
        total_red, total_yellow, total_green = 0, 0, 0
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            hsv = cv2.applyColorMap(gray, cv2.COLORMAP_HSV)

            if condision_record:
                # prosesing for video autput
                gray_out = 170 - gray
                hsv_vid_out = cv2.applyColorMap(gray_out, cv2.COLORMAP_HSV)

            """ saya sengaja melakukan 2 kali proses hsv agar warna yg dideteksi akurat """
            hsv_mask = cv2.cvtColor(hsv, cv2.COLOR_BGR2HSV)
            mask_red = cv2.inRange(hsv_mask, self.lower_red, self.upper_red)
            mask_yellow = cv2.inRange(hsv_mask, self.lower_yellow, self.upper_yellow)
            mask_green = cv2.inRange(hsv_mask, self.lower_green, self.upper_green)

            """ menghitung jumlah px pd masing"" warna """
            t_red = np.sum(mask_red == 255)
            t_yellow = np.sum(mask_yellow == 255)
            t_green = np.sum(mask_green == 255)

            """ perhitungan persentase warna """
            total_red = (t_red/total_px)* 100
            total_yellow = (t_yellow/total_px) * 100
            total_green = (t_green/total_px) * 100


        return ret, frame, hsv, hsv_vid_out, total_red, total_yellow, total_green

    def limit_color(self, color):
        import cv2
        c = np.uint8([[color]])

        hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
        hue = hsv[0][0][0]

        if hue >= 165:
            lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
            upperLimit = np.array([180, 255, 255], dtype=np.uint8)
        if hue <= 15:
            lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
            upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
        else:
            lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
            upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

        return lowerLimit, upperLimit
