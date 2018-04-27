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
import cv2
import time

class Spect(QMainWindow,spectrometer_gui.Ui_MainWindow):
    def __init__(self,parent=None):
        super(Spect,self).__init__(parent)
        self.setupUi(self)


        self.cam_image = pg.ImageItem()
#        self.cam_image.setScale(3)
        self.irse = np.array(np.zeros((1141,196,3),dtype='uint8'))
       
        self.grabbed = np.array(np.zeros((1141,196,3),dtype='uint8'))
        self.wavelengths = np.linspace(392,800,1141)
        self.globalSpectrum = np.zeros((1141), dtype='float')
        self.rawSpectrum = np.zeros((1141), dtype='float')  
        self.calibVect = np.ones((1141), dtype='float')
        self.figure1.addItem(self.cam_image)
       
        self.row = pg.PlotDataItem(background='w')
        self.figure2.addItem(self.row)
        #self.figure2.plotItem.setLabels(bottom='Wavelength (nm)')
        self.figure2.plotItem.setLabels(bottom='Index')
        self.figure2.plotItem.setTitle('Spectrum')
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.updateImage)


        self.buttonStart.clicked.connect(self.startCapture)
        self.buttonStop.clicked.connect(self.stopCapture)
        self.buttonGrab.clicked.connect(self.grabImage)
        self.buttonCalibrate.clicked.connect(self.calibrate)
        
       
        
        self.vid_obj =''


    def startCapture(self):
        self.vid_obj = cv2.VideoCapture(0)
        while not self.vid_obj:
            continue
        if self.vid_obj:
            
            self.getCamParameters()
#            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_WIDTH,640)
#            self.vid_obj.set(cv.CV_CAP_PROP_FRAME_HEIGHT,480)
            self.vid_obj.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1280)
            self.vid_obj.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,960)
#           self.vid_obj.set(4,640)
#           self.vid_obj.set(5,480)
           
            
            #self.vid_obj.set(17,5000.)
            
            self.timer1.start(50)
           
            

    def stopCapture(self):
        self.timer1.stop()
        self.vid_obj.release()
        self.cam_image.hide()
        self.row.hide()
       
    def grabImage(self):
        self.timer1.stop()
        veri=time.localtime()
#        ad = '{}-{}-{}-{}-{}-{}'.format(veri[0],veri[1],veri[2],veri[3],veri[4],veri[5])
        
        ad = self.lineFilename.text()
        if ad == '': 
            ad = '{}-{}-{}-{}-{}-{}'.format(veri[0],veri[1],veri[2],veri[3],veri[4],veri[5])
            
        if cv2.imwrite(ad+'.jpeg', self.grabbed):
            np.savetxt(ad+'.txt', np.vstack((self.wavelengths,self.globalSpectrum)).T, fmt='%.3f',delimiter=',')
            self.timer1.start(50)
        else:
            print 'Failed'
            
    
    def calibrate(self):
        self.timer1.stop()
        while self.timer1.isActive():
            continue
        print 'Calibration okey'
        self.calibVect = 1/self.rawSpectrum
        self.timer1.start(50)
       
       
    def updateImage(self):
        t, frame = self.vid_obj.read()
      
        if t:
            frame = frame[540:736,100:1241,:]
            
            self.grabbed = frame
            
            
            self.irse[:,:,2]=frame[:,:,0].T #B
            self.irse[:,:,1]=frame[:,:,1].T #G
            self.irse[:,:,0]=frame[:,:,2].T #R
            
            
            raw = np.sum(frame,2)
            self.cam_image.setImage(image=self.irse, autolevels=False)
            raw = raw[45:125,:] # 26.04.2018
            spectrum =np.sum(raw,0).astype('float')
            spectrum_n = spectrum/(raw.shape[0]*3*255.)
            self.rawSpectrum = spectrum_n
            self.globalSpectrum = self.rawSpectrum * self.calibVect
            
        
            self.row.setData(self.wavelengths,self.globalSpectrum)
        else:
            print "No image"
            
            
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
            
    def getCamParameters(self):
        
        self.sliderExpo.setValue(-1*self.vid_obj.get(15))
        self.sliderGain.setValue(self.vid_obj.get(14))
        self.sliderCont.setValue(self.vid_obj.get(11))
        self.sliderBright.setValue(self.vid_obj.get(10))
        self.sliderWB.setValue(self.vid_obj.get(17))
        self.sliderSat.setValue(self.vid_obj.get(12))
        
        self.sliderExpo.valueChanged.connect(self.changeExpo)
        self.sliderGain.valueChanged.connect(self.changeGain)
        self.sliderCont.valueChanged.connect(self.changeCont)
        self.sliderBright.valueChanged.connect(self.changeBright)
        self.sliderWB.valueChanged.connect(self.changeWB)
        self.sliderSat.valueChanged.connect(self.changeSat)
        
            
            
        

app=QApplication(sys.argv)
form=Spect()
form.show()
app.exec_()
