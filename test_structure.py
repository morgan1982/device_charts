import sys
from PyQt4 import QtGui, QtCore
from test import Ui_MainWindow  # the saved ui file

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

import sqlite3
import datetime
from matplotlib.dates import datestr2num
# import time
# import datetime
# import bs4 as bs
# import urllib.request
# from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg
# from matplotlib.figure import Figure
print("initializing..")


class Main(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()  # the ui file here
        self.ui.setupUi(self)
        self.statusBar().showMessage('ready')
        self.setWindowTitle('ipad database')

        # q_widget for plot

        # self.toolbar1 = NavigationToolbar(self.canvas1, self)

        grid = QtGui.QGridLayout()
        self.ui.plt_widget.setLayout(grid)

        self.figure1 = plt.figure(figsize=(15,5))
        self.canvas1 = FigureCanvas(self.figure1)

        grid.addWidget(self.canvas1, 1,0,1,2)

        # layout1 = QtGui.QVBoxLayout()
        # layout1.addWidget(self.toolbar1)
        # layout1.addWidget(self.canvas1)

        # self.ui.plt_widget.setLayout(layout1)
        self.num_rep_init()  


    def device_selector(self, dev):

        conn = sqlite3.connect('ipad.db')
        c = conn.cursor()
        device_list = dev
        devices = []
        for i in device_list:
            c.execute("SELECT COUNT(ticket) FROM repairs WHERE device=?", (i, ))
            item = c.fetchone()
            print("item", item)
            devices.append(item)

        devices = [i[0] for i in devices]

        c.close()
        conn.close()  

        return devices






    def num_rep_init(self):


        device_list = ["ipad 2", "ipad 3", "ipad 4", "ipad air", "ipad mini"]


        devices_count = self.device_selector(device_list)
        # print(devices_count)

        dev_list = [
            ["ipad 2", devices_count[0], 'coral'],
            ["ipad 3", devices_count[1], 'blue'],
            ["ipad 4", devices_count[2], 'lightblue'],
            ["ipad air", devices_count[3], 'orange'],
            ["ipad mini", devices_count[4], 'tomato']
            
        ]

        new_list = sorted(dev_list, key=lambda k: k[1], reverse=True)
        print("new list: ", new_list)
        # dev_list.sort(key=lambda k: (k[1]), reverse=True)
        # print("shorted values ", dev_list)

        # new_val = [[i[0], i[1], i[2]] for i in dev_list.sort(key=lambda k: (k[1]), reverse=True)]
        # print("new val", new_val)        
        devices = [i[0] for i in new_list]
        print("devices", devices)
        col_pal = [i[2] for i in new_list]
        dev_counter = [i[1] for i in new_list]
        print("dev_counter", dev_counter)

        # dev_list = {
        #     "ipad 2": [device_count[0], 'coral'],
        #     "ipad 3": [device_count[1], 'blue'],
        #     "ipad 4": [device_count[2], 'lightblue'],
        #     "ipad air": [device_count[3], 'orange'],
        #     "ipad mini": [device_count[4], 'tomato']
        # }



        # setup graph 
        self.ax1 = self.figure1.add_subplot(111)
        self.ax1 = plt.subplot2grid((1, 1), (0, 0))
        self.ax1.grid(True, color='k', linestyle='dotted', linewidth=0.5 )

        width = 0.35


        self.ax1.bar(devices, dev_counter, width,  color=col_pal, alpha= 0.5, align ='center' ) # the plot data
        # self.ax1.bar(dates + 0.2, count_dev, width,  color='grey', alpha= 0.5 ) # the plot data

        self.ax1.set_axisbelow(True)

        # plt.xticks( dates)
        # plt.xticks(rotation=45)
        # self.ax1.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


        plt.xlabel('devices')
        plt.ylabel('num of repairs')
        plt.title('dev destr')

        self.canvas1.draw()


        # c.execute(
        #     "SELECT COUNT(datestamp) AS entries, DATE(datestamp) AS date FROM repairs WHERE DATE(datestamp) BETWEEN datetime('now', '-10 days') AND datetime('now', 'localtime') GROUP BY DATE(datestamp)")
        # value = c.fetchone()
        # print(value[0])
        # dev = "ipad 4"
        # print("values", values)
        # c.execute("select ticket from repairs where device=?", (dev,))
        # devices = c.fetchall()
        # x = [i[0] for i in devices]
        # print(len(x))

        # count_dev = [x[0] for x in values]
        # sum_count_dev = sum(count_dev)
        # length__dev = len(count_dev)
        # average_repairs = sum_count_dev / length__dev
        # print(sum_count_dev)
        # print(length__dev)
        # print(average_repairs)  # average of repairs total

        # dates = [x[1] for x in values]
        # print(dates)
        # dates = datestr2num(dates)
        # print(dates)


        # counter = 0
        # dates = [] # the x axis ?
        # print(dates)
        # dates = [k[1] for k  in val  for val in dates]
        # z = []
        # for i in dates:
            # for k in i:
                # z.append (k[1])
        # print(z)
        # dates_x = date2num(dates)
        # print(dates_x)
        # counter_list = [] # the y axis?
        # for x in values:
        #     dates.append(x[1])
        #     counter_list.append(counter)
        #     counter += 1
        # dates_new = dates.datestr2num(dates)
        # print(count_dev)
        # print(dates)
        # print(counter_list) # counts the days




        # c.close()
        # conn.close()




        # fig = plt.figure()
        # ax1 = plt.subplot2grid((1, 1), (0, 0))
        # plt.xticks(counter_list, dates)  #  to replace numbers in x with custom string we can use also yticks
        # plt.xticks(rotation=45)
        # # ax1.bar(counter_list, count_dev, label="devices", width=1/1.8, color="orange" )  # bars enablerL
        # plt.plot(counter_list, count_dev, color="k")  # graph enabler
        # ax1.grid(True, color='k', linestyle='dotted', linewidth=0.5)  # change the properties of the grid
        # ax1.xaxis.label.set_color('k')
        # ax1.yaxis.label.set_color('magenta')
        # ax1.set_yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        # ax1.fill_between(counter_list, 0, count_dev, color='orange', alpha=0.6)
        # ax1.spines['left'].set_color('c')
        # ax1.spines['right'].set_visible(False)
        # ax1.spines['top'].set_visible(False)
        # ax1.spines['bottom'].set_color('c')

        # ax1.set_axisbelow('True')
        # plt.xlabel('dates')
        # '''

        # to change the rotation of the dates on x axis or just plt.xticks(rotation=45)
        # '''
        # # for label in ax1.xaxis.get_ticklabels():
        # #     label.set_rotation(45)
        # plt.ylabel('repairs')
        # plt.title('Number of repairs per day\naverage numbers')
        # plt.legend()
        # '''
        # customize the view of the plot
        # '''
        # plt.subplots_adjust(left=0.09, bottom=0.21, right=0.94, top=0.85,
        #                     wspace=0.2, hspace=0)
        # plt.show()
        # c.close()
        # conn.close()












if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    # app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    window.show()
    sys.exit(app.exec_())