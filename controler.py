from os import write

from model import Model
from view import View
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
import sys

""" lihat juga file view karena disana ada beberapa element yg di ganti terutama element grafik, 
dan tidak di simpan dalam file desainny ui_main_drone.ui. lihat documentasi pyqtgraf utk info
lebih jelas """

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.playing = False    # untuk memutuskan timer setelah video selesai di putar
        self.vid = None     # variabel video atau lebih dikenal cap
        # menyimpan seluruh data persentase untuk dijadikan grafik
        self.t_red = []
        self.t_yellow = []
        self.t_green = []
        self.dataTabel = None
        #
        self.setSylesheet()

    def setSylesheet(self):

        self.view.pushButton_2.clicked.connect(self.load_video)
        self.view.pushButton.clicked.connect(self.save)
        self.view.pushButton_3.clicked.connect(self.clear)

        # control playback
        self.view.pushButton_play.clicked.connect(self.play_pause)
        self.view.pushButton_forward.clicked.connect(lambda: self.skip_frame(1))
        self.view.pushButton_backward.clicked.connect(lambda: self.skip_frame(0))


    def load_video(self):
        """ alasan kenapa di sini di import modulny agar menghindari error """
        import pyqtgraph as pg
        import cv2, timeit

        self.timeStart = timeit.default_timer()     # menghitung waktu mulai

        src = QFileDialog.getOpenFileName(filter="Video (*.*)")[0]
        self.vid = cv2.VideoCapture(src)
        # src = './dataset/dataset-2s.mp4'
        # self.vid = cv2.VideoCapture(src)

        if not self.vid.isOpened()  :
            print("Video tidak bisa dibuka")
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Video is can't open")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

            # model = Model()
            # view = View()
            # Controller(model, view)
            self.clear()

        self.playing = True
        self.view.grafView.clear()

        # memastikan agar list tersebut kosong
        self.t_red = []
        self.t_yellow = []
        self.t_green = []

        # inisiasi line kosong pd grafik dan set warna line
        self.line_red = self.view.grafView.plot([], [], pen=pg.mkPen(255, 0, 0))
        self.line_yellow = self.view.grafView.plot([], pen=pg.mkPen(255, 255, 0))
        self.line_green = self.view.grafView.plot([], [], pen=pg.mkPen(0, 255, 0))


        """CREATE VIDEO"""
        f_w = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        f_h = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = int(self.vid.get(cv2.CAP_PROP_FPS))
        self.t_px = f_h * f_w
        self.t_frame = int(self.vid.get(cv2.CAP_PROP_FRAME_COUNT))

        """name file, resolusi, time processing, status"""
        name_file = src
        name_file = name_file.split('/')

        self.view.name_file.setText(name_file[len(name_file) - 1])
        self.view.label_resolusi.setText(f"{f_w} x {f_h}")
        self.view.label_drone_alti.setText("10 Meter")
        self.view.label_status.setText("Processing")

        if self.view.radioButton_record.isChecked():
            video_name = 'result.mp4'
            fourcc = cv2.VideoWriter.fourcc(*'mp4v')
            self.video_out = cv2.VideoWriter(video_name, fourcc, self.fps, (f_w, f_h))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(self.fps)

    def update_frame(self):
        import timeit

        ''' data yg akan dimasukkan kedalam tabel frame, persentase hijau, kuning, merah '''

        if self.playing:
            ret, frame_ori, hsv, hsv_vid_out, red, yellow, green = self.model.color_map(self.vid, self.view.radioButton_record.isChecked(), self.t_px)
            if ret:
                if self.view.radioButton_record.isChecked():
                    self.video_out.write(hsv_vid_out)
                self.view.update_image(frame_ori, self.view.label_ori)
                self.view.update_image(hsv, self.view.label_dp)
                self.t_red.append(float(f"{red:.2f}"))
                self.t_yellow.append(float(f"{yellow:.2f}"))
                self.t_green.append(float(f"{green:.2f}"))
                self.view.label_indi_dp.setText(f"Red = {red:.2f}%   Yellow = {yellow:.2f}%    Green = {green:.2f}%")
                self.change_icon_play(1)

                self.graph()
            else:
                self.change_icon_play(0)

                self.vid.release()
                if self.view.radioButton_record.isChecked():
                    self.video_out.release()

                self.table()

                self.vid = None
                self.view.label_status.setText("Done")
                # labels = [self.view.label_dp, self.view.label_ori, self.view.label_indi_dp]
                # [label.setText(" ") for label in labels]

                self.timer.stop()
                self.view.label_time_pro.setText(f"{(timeit.default_timer() - self.timeStart):.2f}s")   # menghitung waktu prosesing

    """ fungsi aksi yg dilakukan ketika klik tombol play or pause """
    def play_pause(self):
        if(self.playing == True):   # kondisi ketika klik tombol pause
            self.change_icon_play(0)
            self.playing = False
        else:   # kondisi ketika klik tombol play
            if(self.vid != None):   # memastikan agar tombol di klik saat memutar video
                self.change_icon_play(1)
                self.playing = True
                self.update_frame()

    def skip_frame(self, condision):
        if(self.vid != None):
            import cv2
            current_frame = int(self.vid.get(cv2.CAP_PROP_POS_FRAMES))
            frame_skip = current_frame + 20 if condision == 1 else current_frame - 20
            self.vid.set(cv2.CAP_PROP_POS_FRAMES, frame_skip)


    def save(self):
        import shutil, os

        if self.dataTabel != None:
            if self.view.radioButton_record.isChecked():
                if os.path.exists('./result/result.mp4'):
                    os.remove('./result/result.mp4')
                shutil.move('result.mp4', './result')

            self.dataTabel = self.dataTabel.replace("\t", ",")
            with open('./result/dataTable.csv', 'w') as file:
                file.write(self.dataTabel)
            self.dataTabel = None

            self.view.label_status.setText("Saved to directory result")


    def clear(self):
        self.timer.stop()
        self.vid = None
        self.change_icon_play(0)
        self.view.label_status.setText("Clear Video")
        labels = [self.view.label_dp, self.view.label_ori, self.view.label_indi_dp, self.view.name_file, self.view.label_status, self.view.label_resolusi, self.view.label_drone_alti, self.view.label_time_pro, self.view.label_status]
        [label.setText(" ") for label in labels]

        self.view.grafView.clear()

        # self.view.tableView.clear()
        # self.view.tableView.setData(self.view.dataTabel)
        self.table(1)

    def change_icon_play(self, condision):
        src = "icon/play.png" if condision == 1 else "icon/pause.png"
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(src), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.view.pushButton_play.setIcon(icon1)

    def graph(self):
        import numpy as np

        x_r = np.arange(0, len(self.t_red))
        x_y = np.arange(0, len(self.t_yellow))
        x_g = np.arange(0, len(self.t_green))

        """ set data ke line yg diinisiasi ketika loadvideo """
        """ pyqtgraf lebih ringan dan efisien dari matplotlib """
        self.line_red.setData(x_r, self.t_red)
        self.line_yellow.setData(x_y, self.t_yellow)
        self.line_green.setData(x_g, self.t_green)

    def table(self, kondisi=0):
        hd = ['Frame', 'Green', 'Yellow', 'Red']

        data = []
        if kondisi == 0:
            [data.append({hd[0]: i, hd[1]: f"{self.t_green[i]}%", hd[2]: f"{self.t_yellow[i]}%", hd[3]: f"{self.t_red[i]}%"}) for i in range(1, len(self.t_red))]
        else:
            data = self.view.dataTabel

        # for i in range(len(self.t_red)):
        #     data.append({hd[0]: i, hd[1]: f"{self.t_green[i]}%", hd[2]: f"{self.t_yellow[i]}%", hd[3]: f"{self.t_red[i]}%"})

        self.view.tableView.setData(data)
        self.dataTabel = self.view.tableView.serialize(useSelection=False)

        self.view.tableView.verticalHeader().setVisible(False)

        self.view.tableView.setColumnWidth(0, 256)
        self.view.tableView.setColumnWidth(1, 256)
        self.view.tableView.setColumnWidth(2, 256)
        self.view.tableView.setColumnWidth(3, 256)

        for row in range(self.view.tableView.rowCount()):
            for col in range(self.view.tableView.columnCount()):
                item = self.view.tableView.item(row, col)
                if item:
                    item.setTextAlignment(QtCore.Qt.AlignCenter)


def main():
    app = QApplication(sys.argv)

    model = Model()
    view = View()
    Controller(model, view)

    view.setWindowTitle('Detection of Grass')
    # view.resize(2650, 1600)
    view.resize(3500, 1600)
    view.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
