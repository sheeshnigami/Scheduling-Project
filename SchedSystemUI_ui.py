# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Admin\Code\Scheduling-Project\SchedSystemUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(887, 713)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_sidebar = QtWidgets.QVBoxLayout()
        self.verticalLayout_sidebar.setObjectName("verticalLayout_sidebar")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayout_sidebar.addWidget(self.pushButton_back)
        self.pushButton_home = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_sidebar.addWidget(self.pushButton_home)
        self.pushButton_students = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_students.setObjectName("pushButton_students")
        self.verticalLayout_sidebar.addWidget(self.pushButton_students)
        self.pushButton_teachers = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_teachers.setObjectName("pushButton_teachers")
        self.verticalLayout_sidebar.addWidget(self.pushButton_teachers)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_sidebar.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_sidebar)
        self.stackedWidget_pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget_pages.setObjectName("stackedWidget_pages")
        self.page_view = QtWidgets.QWidget()
        self.page_view.setObjectName("page_view")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_view)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea_view = QtWidgets.QScrollArea(self.page_view)
        self.scrollArea_view.setWidgetResizable(True)
        self.scrollArea_view.setObjectName("scrollArea_view")
        self.scrollAreaWidgetContents_view = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_view.setGeometry(QtCore.QRect(0, 0, 109, 163))
        self.scrollAreaWidgetContents_view.setObjectName("scrollAreaWidgetContents_view")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_view = QtWidgets.QLabel(self.scrollAreaWidgetContents_view)
        self.label_view.setObjectName("label_view")
        self.verticalLayout.addWidget(self.label_view)
        self.horizontalLayout_view = QtWidgets.QHBoxLayout()
        self.horizontalLayout_view.setObjectName("horizontalLayout_view")
        self.comboBox_view = QtWidgets.QComboBox(self.scrollAreaWidgetContents_view)
        self.comboBox_view.setObjectName("comboBox_view")
        self.horizontalLayout_view.addWidget(self.comboBox_view)
        self.verticalLayout.addLayout(self.horizontalLayout_view)
        self.tableView_view = QtWidgets.QTableView(self.scrollAreaWidgetContents_view)
        self.tableView_view.setObjectName("tableView_view")
        self.verticalLayout.addWidget(self.tableView_view)
        self.scrollArea_view.setWidget(self.scrollAreaWidgetContents_view)
        self.horizontalLayout.addWidget(self.scrollArea_view)
        self.stackedWidget_pages.addWidget(self.page_view)
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.pushButton_add = QtWidgets.QPushButton(self.page_home)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_view = QtWidgets.QPushButton(self.page_home)
        self.pushButton_view.setObjectName("pushButton_view")
        self.verticalLayout_2.addWidget(self.pushButton_view)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.stackedWidget_pages.addWidget(self.page_home)
        self.page_add = QtWidgets.QWidget()
        self.page_add.setObjectName("page_add")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_add)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.pushButton_addStudent = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addStudent.setObjectName("pushButton_addStudent")
        self.verticalLayout_3.addWidget(self.pushButton_addStudent)
        self.pushButton_addTeacher = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addTeacher.setObjectName("pushButton_addTeacher")
        self.verticalLayout_3.addWidget(self.pushButton_addTeacher)
        self.pushButton_addDepartment = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addDepartment.setObjectName("pushButton_addDepartment")
        self.verticalLayout_3.addWidget(self.pushButton_addDepartment)
        self.pushButton_addCourse = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addCourse.setObjectName("pushButton_addCourse")
        self.verticalLayout_3.addWidget(self.pushButton_addCourse)
        self.pushButton_addSubject = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addSubject.setObjectName("pushButton_addSubject")
        self.verticalLayout_3.addWidget(self.pushButton_addSubject)
        self.pushButton_addBlock = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addBlock.setObjectName("pushButton_addBlock")
        self.verticalLayout_3.addWidget(self.pushButton_addBlock)
        self.pushButton_addRoom = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addRoom.setObjectName("pushButton_addRoom")
        self.verticalLayout_3.addWidget(self.pushButton_addRoom)
        self.pushButton_addRoomSched = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addRoomSched.setObjectName("pushButton_addRoomSched")
        self.verticalLayout_3.addWidget(self.pushButton_addRoomSched)
        self.pushButton_addSubjectSched = QtWidgets.QPushButton(self.page_add)
        self.pushButton_addSubjectSched.setObjectName("pushButton_addSubjectSched")
        self.verticalLayout_3.addWidget(self.pushButton_addSubjectSched)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.stackedWidget_pages.addWidget(self.page_add)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setObjectName("page_info")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_info)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_info = QtWidgets.QLabel(self.page_info)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_4.addWidget(self.label_info)
        self.gridLayout_info = QtWidgets.QGridLayout()
        self.gridLayout_info.setObjectName("gridLayout_info")
        self.verticalLayout_4.addLayout(self.gridLayout_info)
        self.tableView_info = QtWidgets.QTableView(self.page_info)
        self.tableView_info.setObjectName("tableView_info")
        self.verticalLayout_4.addWidget(self.tableView_info)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 10)
        self.stackedWidget_pages.addWidget(self.page_info)
        self.page_addForm = QtWidgets.QWidget()
        self.page_addForm.setObjectName("page_addForm")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_addForm)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_addForm = QtWidgets.QLabel(self.page_addForm)
        self.label_addForm.setObjectName("label_addForm")
        self.verticalLayout_5.addWidget(self.label_addForm)
        self.formLayout_addForm = QtWidgets.QFormLayout()
        self.formLayout_addForm.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_addForm.setObjectName("formLayout_addForm")
        self.verticalLayout_5.addLayout(self.formLayout_addForm)
        self.verticalLayout_5.setStretch(1, 1)
        self.stackedWidget_pages.addWidget(self.page_addForm)
        self.horizontalLayout_3.addWidget(self.stackedWidget_pages)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget_pages.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_back.setText(_translate("MainWindow", "Back"))
        self.pushButton_home.setText(_translate("MainWindow", "Home"))
        self.pushButton_students.setText(_translate("MainWindow", "Students"))
        self.pushButton_teachers.setText(_translate("MainWindow", "Teachers"))
        self.label_view.setText(_translate("MainWindow", "*LIST"))
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_view.setText(_translate("MainWindow", "View"))
        self.pushButton_addStudent.setText(_translate("MainWindow", "Add Student"))
        self.pushButton_addTeacher.setText(_translate("MainWindow", "Add Teacher"))
        self.pushButton_addDepartment.setText(_translate("MainWindow", "Add Department"))
        self.pushButton_addCourse.setText(_translate("MainWindow", "Add Course"))
        self.pushButton_addSubject.setText(_translate("MainWindow", "Add Subject"))
        self.pushButton_addBlock.setText(_translate("MainWindow", "Add Block"))
        self.pushButton_addRoom.setText(_translate("MainWindow", "Add Room"))
        self.pushButton_addRoomSched.setText(_translate("MainWindow", "Add Room Schedule"))
        self.pushButton_addSubjectSched.setText(_translate("MainWindow", "Add Subject Schedule"))
        self.label_info.setText(_translate("MainWindow", "*INFO"))
        self.label_addForm.setText(_translate("MainWindow", "*ADD"))
