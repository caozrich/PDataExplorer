#PData_explorer by Richard Libreros 
#v1.0.0

# ///
from PySide6.QtCore import *  # type: ignore
import sys
import os
import numpy as np
import pandas as pd
import io
from PyQt5.QtWidgets import QDialog, QApplication,QWidget, QTableWidgetItem
from PyQt5           import QtCore,QtGui,QtWidgets, uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from PyQt5.QtGui     import QPixmap
from PyQt5.QtCore    import *
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import time
from help_functions import * 

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" 


# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
DataFrame = pd.DataFrame()
allnumeric = pd.DataFrame()


        
        

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////

        
        
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.all_features = []  
        self.categorical_features = []
        self.numerical_features = []
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True



        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        self.ui.pushButton_1.clicked.connect(self.fade)

        self.ui.pushButton_3.clicked.connect(lambda: self.close())
        # LEFT MENUS
        
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_compare.clicked.connect(self.buttonClick)
        widgets.btn_correlation.clicked.connect(self.buttonClick)      
        widgets.btn_clear.clicked.connect(self.buttonClick)             
        #preview BUTTONS
        
        widgets.pushButton.clicked.connect(self.buttonClick2)
        widgets.pushButton_7.clicked.connect(self.buttonClick2)
        widgets.pushButton_8.clicked.connect(self.buttonClick2)
        widgets.pushButton_9.clicked.connect(self.buttonClick2)            
        # widgets.btn_save.clicked.connect(self.buttonClick)

        #save
        
        # widgets.csave.clicked.connect(self.save_data_as_csv)         

         
        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        # widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        # widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()
        self.setWindowTitle("PDataExplorer")
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.page)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        
        #FIND THE FILE:
        
        widgets.pushButton_2.clicked.connect(self.browsefiles)
        
    
        #plots1
        
        self.figure = plt.figure()  
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        # widgets.verticalLayout.addWidget(self.canvas)
        # widgets.verticalLayout.addWidget(self.toolbar)
  
        #plots2
        
        # self.figure2 = plt.figure()  
        # self.canvas2 = FigureCanvas(self.figure2)
        # self.toolbar2 = NavigationToolbar(self.canvas2, self)
        # widgets.verticalLayout_3.addWidget(self.canvas2)
        # widgets.verticalLayout_3.addWidget(self.toolbar2)




    def browsefiles(self):
        
        global DataFrame
        global allnumeric
                  
        if not DataFrame.empty:
            self.categorical_features = []
            self.numerical_features = []
            self.all_features = []            
            

        fname=QFileDialog.getOpenFileName(self, 'Open file', '', 'CSV files (*.csv)')
        widgets.lineEdit_2.setText(fname[0])

        df = pd.read_csv(fname[0])
        DataFrame = df.copy()
        
        tx = df.shape
        
        widgets.labelVersion_4.setText(str(tx[0]) +  " rows x " + str(tx[1]) + " colums")     
       

        col = list(df.columns)

        for i in col:
            if len(df[i].unique()) > 6:
                self.numerical_features.append(i)
            else:
                self.categorical_features.append(i)
                

        allnumeric = DataFrame.copy()

        #PlotButtons
    
        
        #transform cat to num
        if self.categorical_features != []:
            le = LabelEncoder()
            for col in allnumeric[self.categorical_features]:
                    allnumeric[col] = le.fit_transform(allnumeric[col])
                    
                    
        col = list(allnumeric.columns)    
        for i in col:  
            self.all_features.append(i)      
                                                
                    

                
                
                
        #TITTLE

        name = self.find_between(fname[0], '/', '.csv')
        widgets.data.setText(name + ".csv")

        #        
        
  
        self.all_data = df.head(100)
        NumRows = len(self.all_data.index)
        self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
        self.ui.tableWidget.setRowCount(NumRows)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))
                
         

         
         
        #info
        

           
        
        buffer = io.StringIO()
        df.info(buf=buffer)
        lines = buffer.getvalue().splitlines()
        df2 = (pd.DataFrame([x.split() for x in lines[5:-2]], columns=lines[3].split())
            .drop('Count',axis=1)
            .rename(columns={'Non-Null':'Non-Null Count'}))

        self.all_data2 = df2.head(100)
        NumRows = len(self.all_data2.index)
        self.ui.tableWidget_4.setColumnCount(len(self.all_data2.columns))
        self.ui.tableWidget_4.setRowCount(NumRows)
        self.ui.tableWidget_4.setHorizontalHeaderLabels(self.all_data2.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data2.columns)):
                self.ui.tableWidget_4.setItem(i, j, QTableWidgetItem(str(self.all_data2.iat[i, j])))
                

        
        #DESCRIBE
        
        df3 = df.describe().T
        df3.insert(0,' ', df3.index )
        
        self.all_data3 = df3.head(100)
        NumRows = len(self.all_data3.index)
        self.ui.tableWidget_5.setColumnCount(len(self.all_data3.columns))
        self.ui.tableWidget_5.setRowCount(NumRows)
        self.ui.tableWidget_5.setHorizontalHeaderLabels(self.all_data3.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data3.columns)):
                self.ui.tableWidget_5.setItem(i, j, QTableWidgetItem(str(self.all_data3.iat[i, j])))
                

        
        
        #UNIQUE
        
        du = df.nunique()
        du = pd.DataFrame(du)
        du.insert(0,'Column', du.index )
        du = du.reset_index(drop=True)
        du = du.rename(columns={0: "count"})

        # df4.insert(0,' ', df3.index )
        
        self.all_data4 = du.head(100)
        NumRows = len(self.all_data4.index)
        self.ui.tableWidget_6.setColumnCount(len(self.all_data4.columns))
        self.ui.tableWidget_6.setRowCount(NumRows)
        self.ui.tableWidget_6.setHorizontalHeaderLabels(self.all_data4.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data4.columns)):
                self.ui.tableWidget_6.setItem(i, j, QTableWidgetItem(str(self.all_data4.iat[i, j])))
                


        QTimer.singleShot(50, lambda:self.fixshit())            
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        
    def fixshit (self):

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()            
        

        
    def find_between(self, s, first, last ):
        try:
            start = s.rfind(first)
            end = s.rfind(last)
            return s[start+1:end]
        except ValueError:
            return ""  
            


    # BUTTONS CLICK
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        global DataFrame
        
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()
        
        if not DataFrame.empty:
            # SHOW HOME PAGE
            if btnName == "btn_home":
                widgets.stackedWidget.setCurrentWidget(widgets.home)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

            # SHOW WIDGETS PAGE
            if btnName == "btn_widgets":
                widgets.stackedWidget.setCurrentWidget(widgets.widgets)
                UIFunctions.resetStyle(self, btnName)
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
                
                #combobox


                widgets.comboBox.clear() 
                widgets.comboBox_2.clear()                    
                widgets.comboBox_2.addItems(self.numerical_features)
                

                
                
                if self.numerical_features != []:
                    
                    widgets.comboBox.addItem("Numerical")
                    
                if self.numerical_features != []:
                    
                    widgets.comboBox.addItem("Categorical")                
           

                
                
                #combobox event
                widgets.comboBox.currentTextChanged.connect(self.trggered)                
                widgets.comboBox_2.currentTextChanged.connect(self.trggered)
                
                
                #PlotButtons
            
                widgets.plot_1.clicked.connect(self.plot_featurDis)    
                
                
                
                
                

            # SHOW NEW PAGE
            if btnName == "btn_compare":
                widgets.stackedWidget.setCurrentWidget(widgets.target) # SET PAGE
                UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
                

                            
                            

                widgets.comboBox_5.clear()                     
                widgets.comboBox_5.addItems(self.all_features)               
                widgets.comboBox_3.clear()                     
                widgets.comboBox_3.addItems(self.all_features)   
                widgets.comboBox_4.clear()
                widgets.comboBox_4.addItems(self.all_features)             
                
                widgets.plot_2.clicked.connect(self.plot_featurDis2)                         
                

            if btnName == "btn_correlation":
                widgets.stackedWidget.setCurrentWidget(widgets.correlations) # SET PAGE  
                UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
                
                
                
                self.canvas.figure.clear()  
                widgets.verticalLayout_8.addWidget(self.canvas)
                widgets.verticalLayout_8.addWidget(self.toolbar)
                sns.heatmap(allnumeric.corr(),annot=True)
                self.canvas.draw()  

            if btnName == "btn_clear":
                
                
                widgets.stackedWidget.setCurrentWidget(widgets.clean) # SET PAGE  
                UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
                btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU  
                
                
                
                
                
                        
                widgets.csave.clicked.connect(self.save_data_as_csv)         
                
                
                  
                

                
                       
                
                
                

    def buttonClick2(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "pushButton":
            widgets.stackedWidget_2.setCurrentWidget(widgets.preview)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.fixshit()

        # SHOW WIDGETS PAGE
        if btnName == "pushButton_7":
            widgets.stackedWidget_2.setCurrentWidget(widgets.info)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "pushButton_8":
            widgets.stackedWidget_2.setCurrentWidget(widgets.describe) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "pushButton_9":
            widgets.stackedWidget_2.setCurrentWidget(widgets.unique) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU


    def plot_featurDis(self): #PLOT1
         
        global DataFrame  
        self.canvas.figure.clear()    
        cat = str(widgets.comboBox.currentText()) 
        selected = str(widgets.comboBox_2.currentText()) 
        
        widgets.verticalLayout.addWidget(self.canvas)
        widgets.verticalLayout.addWidget(self.toolbar)

        colors = ['#328CFF','#01c975']                       


        if cat == "Numerical":                
            sns.distplot(DataFrame[selected],kde_kws = {'bw' : 1},color = colors[0])
            title = 'Distribution : ' + selected
            plt.title(title);
        elif cat == "Categorical":
            # values = DataFrame[selected].value_counts()
            # dlist = pd.unique(DataFrame[selected])
            # plt.pie(values, labels=dlist, autopct="%.2f%%", startangle=56)       
            sns.countplot(x =selected, data = DataFrame,palette=colors)

        
        self.canvas.draw()  
        
        
        
    def plot_featurDis2(self): #PLOT2 
        
        global allnumeric  
        self.canvas.figure.clear()    
        Tclass = str(widgets.comboBox_5.currentText()) 
        X = str(widgets.comboBox_3.currentText()) 
        Y = str(widgets.comboBox_4.currentText()) 
        
        widgets.verticalLayout_3.addWidget(self.canvas)
        widgets.verticalLayout_3.addWidget(self.toolbar)
        
        colors = ['#328CFF','#FFA532']                       



        sns.scatterplot(x = allnumeric[X],y = allnumeric[Y],data = allnumeric,hue = Tclass,palette = colors, edgecolor = 'black');
        plt.legend()
        title = X + ' vs ' + Y
        plt.title(title)


        self.canvas.draw()          
        
        
        
        
        
    
        
    def trggered (self):
        global DataFrame       
        btn = self.sender()
        btnName = btn.objectName()
        if btnName == "comboBox":
                if str(widgets.comboBox.currentText()) ==  "Categorical":
                    
                     widgets.comboBox_2.clear()
                     widgets.comboBox_2.addItems(self.categorical_features)                 
                    
                elif str(widgets.comboBox.currentText()) ==  "Numerical":   
                    
                     widgets.comboBox_2.clear()                     
                     widgets.comboBox_2.addItems(self.numerical_features)
                     
                    
    def save_data_as_csv(self):
        
        self.cleaned_df = DataFrame.copy()
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "csave":
            
            
            if widgets.radioButton.isChecked() == True: #delete columns with nan values
                     self.cleaned_df = self.cleaned_df.dropna()
            elif widgets.radioButton_2.isChecked() == True: #replace nan values with 0         
                     self.cleaned_df = self.cleaned_df.replace(np.nan,0)

                            
            if widgets.radioButton_7.isChecked() == True: #delete columns with inf values
                     
                     self.cleaned_df.replace([np.inf, -np.inf], np.nan,inplace=True)
                     self.cleaned_df = self.cleaned_df.dropna()
            elif widgets.radioButton_8.isChecked() == True: #replace inf values with 0         
                     self.cleaned_df = self.cleaned_df.replace([np.inf, -np.inf], 0,inplace=True)              
                    
                    
                               
            name = QFileDialog.getSaveFileName(self, 'Save File', filter='*.csv')
            if(name[0] == ''):
                pass
            else:
                self.cleaned_df.to_csv(name[0], index = False)           
                
                
                
                
    def fade(self):
        
        x_o =self.x()
        y_o =self.y()
        for i in range(10):
            i = i / 10
            self.setWindowOpacity(1 - i)
            self.move(x_o+int(i*40),y_o+int(i*50))
            time.sleep(0.01)
        self.showMinimized()
        
        self.move(x_o,y_o)
        self.setWindowOpacity(1)          
                    
    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    path = resource_path('icon.ico')  
    app.setWindowIcon(QIcon(path))
    window = MainWindow()
    sys.exit(app.exec_())
