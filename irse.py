# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:56:55 2018

@author: varol_000
"""

import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import spectrometer_gui
import pyqtgraph as pg
import numpy as np
from cv2 import *

class Spect(QMainWindow,spectrometer_gui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(Spect,self).__init__(parent)
        self.setupUi(self)


        self.cam_image = pg.ImageItem()
        self.cam_image.setScale(3)
        self.irse = np.array(np.zeros((180,60,3),dtype='uint8'))
        self.figure1.addItem(self.cam_image)
       
        self.row = pg.PlotDataItem(background='w')
        self.figure2.addItem(self.row)
        self.figure2.plotItem.setLabels(bottom='Wavelength (nm)')
        self.figure2.plotItem.setTitle('Spectrum')
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.updateImage)


        self.buttonStart.clicked.connect(self.startCapture)
        self.buttonStop.clicked.connect(self.stopCapture)
        
        self.sliderExpo.valueChanged.connect(self.changeExpo)
        self.sliderGain.valueChanged.connect(self.changeGain)
        self.sliderCont.valueChanged.connect(self.changeCont)
        self.sliderBright.valueChanged.connect(self.changeBright)
        self.sliderWB.valueChanged.connect(self.changeWB)
        self.sliderSat.valueChanged.connect(self.changeSat)
        
        self.vid_obj = None


    def startCapture(self):
        self.vid_obj = VideoCapture(0)
        
        if self.vid_obj:
            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_WIDTH,640)
            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_HEIGHT,480)
#           self.vid_obj.set(4,640)
#           self.vid_obj.set(5,480)
           
            
            self.vid_obj.set(17,5000.)
            
            self.timer1.start(50)
            self.cam_image.show()
            self.row.show()

    def stopCapture(self):
        self.timer1.stop()
        self.vid_obj.release()
        self.cam_image.hide()
        self.row.hide()
        
    def updateImage(self):
        t, frame = self.vid_obj.read()
        
        frame = frame[210:270,140:320,:]
         
        if t:
            
            self.irse[:,:,2]=frame[:,:,0].T #B
            self.irse[:,:,1]=frame[:,:,1].T #G
            self.irse[:,:,0]=frame[:,:,2].T #R
            
            gray = np.sum(frame,2)
            self.cam_image.setImage(image=self.irse, autolevels=False)
            spectrum =np.sum(gray,0).astype('float')
            spectrum_n = spectrum/255
            self.row.setData(np.linspace(313,682,180),spectrum_n)
            
            
 # VIDEO CONTROLS
    
    def changeGain(self,val):
        if self.vid_obj:
            self.vid_obj.set(14,np.uint8(val))
    def changeExpo(self,val):
        if self.vid_obj:
            self.vid_obj.set(15,-1*val)
    def changeBright(self,val):
        if self.vid_obj:
            self.vid_obj.set(10,val)
    def changeCont(self,val):
        if self.vid_obj:
            self.vid_obj.set(11,val)
    def changeWB(self,val):
        if self.vid_obj:
            self.vid_obj.set(17,val)
    def changeSat(self,val):
        if self.vid_obj:
            self.vid_obj.set(12,val)
            
            
        

app=QApplication(sys.argv)
form=Spect()
form.show()
app.exec_()
