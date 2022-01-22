import sys
import os
from PyQt5.QtCore import QPropertyAnimation, QPoint, QObject
from PyQt5.QtWidgets import QWidget
from PySide2 import *
from PySide2 import QtCore
from PySide2 import QtGui
from  qt_material import *
from Calorie_health import *

class MainWindow(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    #apply_stylesheet(app, theme='dark_blue.xml')

    self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    self.shadow = QGraphicsDropShadowEffect(self)
    self.shadow.setBlurRadius(50)
    self.shadow.setXOffset(0)
    self.shadow.setYOffset(0)
    self.shadow.setColor(QColor(0, 92, 157, 550))

    self.ui.centralwidget.setGraphicsEffect(self.shadow)
    self.setWindowIcon(QtGui.QIcon(":/icons/icons8-kawaii-broccoli-64.png"))
    self.setWindowTitle("Calorie Health")
    QSizeGrip(self.ui.size_grip)

    #minimize window
    self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
    #close window
    self.ui.close_window_button.clicked.connect(lambda: self.close())

    #resotre/maximize window
    self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

    self.ui.dashboard_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.dashboard))
    self.ui.activity_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activity))
    self.ui.profile_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.profile))
    #left menu toggle button
    self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
    self.ui.time_of_day_combo_picker.addItems(['Breakfast', 'Lunch', 'Dinner'])
    self.ui.enter_button.clicked.connect(lambda: self.Entry())
    #function to move window on mouse drag event on the title bar
    def moveWindow(e):
      #detect if the window is normal size
      if self.isMaximized() == False:
        #move window only when window is normal size
        #if left mouse button is cliccked (only accept left mouse button clicks)
        if e.buttons() == Qt.LeftButton:
          self.move(self.pos() + e.globalPos() - self.clickPosition)
          self.clickPosition = e.globalPos()
          e.accept()
    # add click event, mouse move event, drag event to the top header to move the window
    self.ui.header_frame.mouseMoveEvent = moveWindow
   

    

    self.show()
  
  def restore_or_maximize_window(self):
      if self.isMaximized():
        self.showNormal()
        #self.ui.resotreWindowButton.setIcon(QtGui.QIcon)
      else:
        self.showMaximized()
        #self.ui.resotreWindowButton.setIcon(QtGui.QIcon)

# add mouse events to the window
  def mousePressEvent(self, event):
    # get the current position of the mouse
    self.clickPosition = event.globalPos()
    #we will use this value to move the window

# slide left menu function
  def slideLeftMenu(self):
    #get current left menu width
    width = self.ui.left_menu_cont_frame.width()

    #if minimized
    if width == 35:
      newWidth = 125
    #if maximized
    else:
      newWidth = 35
    
    #animate the transition
    self.animation = QtCore.QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
    self.animation.setDuration(250)
    self.animation.setStartValue(width)
    self.animation.setEndValue(newWidth)
    self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
    self.animation.start()

    
  def Entry(self):
    entry = self.ui.entry_text_box
    calories = self.ui.calories_text_box.toPlainText()
    times = self.ui.time_of_day_combo_picker.currentText()
    b = self.ui.breakfast_number
    l = self.ui.lunch_number
    d = self.ui.dinner_number
    t = self.ui.total_calories_number
    g = 0
    f = 0
    h = 0

    if times == 'Breakfast':
      b.display(int(calories))
      g = int(calories)
    elif times == 'Lunch':
      l.display(int(calories))
      f = int(calories)
    elif times == 'Dinner':
      d.display(int(calories))
      h = int(calories)
    total = g + f + h
    t.display(total)
    
    
    
    


    




#execute app

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  sys.exit(app.exec_())
 