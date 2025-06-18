from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import Qt


class Add:
    def __init__(self, ui, stackedWidget_pages):
        self.ui = ui
        self.stackedWidget_pages = stackedWidget_pages

    def add_student(self):
        self.stackedWidget_pages.setCurrentIndex(4)

        self.ui.label_addForm.setText("Add Student")
        # 0,0
        self.label_studID = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_studID.setObjectName("label_studID")
        self.ui.formLayout_addForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_studID)
        self.label_studID.setText("Student ID: ")
        self.lineEdit_studID = QtWidgets.QLineEdit(self.ui.page_addForm)
        self.lineEdit_studID.setObjectName("lineEdit_studID")
        self.ui.formLayout_addForm.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_studID
        )
        self.lineEdit_studID.setPlaceholderText("Enter Student ID...")
        self.lineEdit_studID.setText("")
        # 1,0
        self.label_studName = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_studName.setObjectName("label_studName")
        self.ui.formLayout_addForm.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_studName
        )
        self.label_studName.setText("Student Name: ")
        self.lineEdit_studName = QtWidgets.QLineEdit(self.ui.page_addForm)
        self.lineEdit_studName.setObjectName("lineEdit_studName")
        self.ui.formLayout_addForm.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_studName
        )
        self.lineEdit_studName.setPlaceholderText("Enter Student Name...")
        self.lineEdit_studName.setText("")
        # 2,0
        self.label_studCourse = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_studCourse.setObjectName("label_studCourse")
        self.ui.formLayout_addForm.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_studCourse
        )
        self.label_studCourse.setText("Course: ")
        self.comboBox_studCourse = QtWidgets.QComboBox(self.ui.page_addForm)
        self.comboBox_studCourse.setObjectName("comboBox_studCourse")
        self.ui.formLayout_addForm.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.comboBox_studCourse
        )
        self.comboBox_studCourse.addItem("Choose Student Course...")
        self.comboBox_studCourse.setCurrentIndex(0)
        self.comboBox_studCourse.setItemData(0, 0, Qt.UserRole - 1)
        self.comboBox_studCourse.addItems(["BSIT", "BSCS", "BSIS"])
        # 3,0
        self.label_studBlock = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_studBlock.setObjectName("label_studBlock")
        self.ui.formLayout_addForm.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_studBlock
        )
        self.label_studBlock.setText("Block: ")
        self.comboBox_studBlock = QtWidgets.QComboBox(self.ui.page_addForm)
        self.comboBox_studBlock.setObjectName("comboBox_studBlock")
        self.ui.formLayout_addForm.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.comboBox_studBlock
        )
        self.comboBox_studBlock.addItem("Choose Student Block...")
        self.comboBox_studBlock.setCurrentIndex(0)
        self.comboBox_studBlock.setItemData(0, 0, Qt.UserRole - 1)
        self.comboBox_studBlock.addItems(["A", "B", "C"])
        # 4,0
        self.pushButton_addSubmit = QtWidgets.QPushButton(self.ui.page_addForm)
        self.pushButton_addSubmit.setObjectName("pushButton_submit")
        self.pushButton_addSubmit.setText("Submit")
        self.ui.formLayout_addForm.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.pushButton_addSubmit
        )
        # Connect the submit button to a handler
        self.pushButton_addSubmit.clicked.connect(self.submit_student)

    def add_teacher(self):
        self.stackedWidget_pages.setCurrentIndex(4)

        self.ui.label_addForm.setText("Add Teacher")
        # 0,0
        self.label_teachID = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_teachID.setObjectName("label_teachID")
        self.ui.formLayout_addForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_teachID)
        self.label_teachID.setText("Teacher ID: ")
        self.lineEdit_teachID = QtWidgets.QLineEdit(self.ui.page_addForm)
        self.lineEdit_teachID.setObjectName("lineEdit_teachID")
        self.ui.formLayout_addForm.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_teachID
        )
        self.lineEdit_teachID.setPlaceholderText("Enter Teacher ID...")
        self.lineEdit_teachID.setText("")
        # 1,0
        self.label_teachName = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_teachName.setObjectName("label_label_teachName")
        self.ui.formLayout_addForm.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_teachName
        )
        self.label_teachName.setText("Teacher Name: ")
        self.lineEdit_teachName = QtWidgets.QLineEdit(self.ui.page_addForm)
        self.lineEdit_teachName.setObjectName("lineEdit_teachName")
        self.ui.formLayout_addForm.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_teachName
        )
        self.lineEdit_teachName.setPlaceholderText("Enter Teacher Name...")
        self.lineEdit_teachName.setText("")
        # 2,0
        self.label_teachDept = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_teachDept.setObjectName("label_teachDept")
        self.ui.formLayout_addForm.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_teachDept
        )
        self.label_teachDept.setText("Department: ")
        self.comboBox_teachDept = QtWidgets.QComboBox(self.ui.page_addForm)
        self.comboBox_teachDept.setObjectName("comboBox_teachDept")
        self.ui.formLayout_addForm.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.comboBox_teachDept
        )
        self.comboBox_teachDept.addItem("Choose Department...")
        self.comboBox_teachDept.setCurrentIndex(0)
        self.comboBox_teachDept.setItemData(0, 0, Qt.UserRole - 1)
        self.comboBox_teachDept.addItems(["CASE", "CBMA", "CEAFA", "CHS"])
        # 3,0
        self.pushButton_addSubmit = QtWidgets.QPushButton(self.ui.page_addForm)
        self.pushButton_addSubmit.setObjectName("pushButton_submit")
        self.pushButton_addSubmit.setText("Submit")
        self.ui.formLayout_addForm.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.pushButton_addSubmit
        )
        # Connect the submit button to a handler
        self.pushButton_addSubmit.clicked.connect(self.submit_teacher)

    def add_department(self):
        self.stackedWidget_pages.setCurrentIndex(4)

        self.ui.label_addForm.setText("Add Department")
        # 0,0
        self.label_deptID = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_deptID.setObjectName("label_deptID")
        self.ui.formLayout_addForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_deptID)
        self.label_deptID.setText("Department ID: ")
        self.lineEdit_deptID = QtWidgets.QLineEdit(self.ui.page_addForm)
        self.lineEdit_deptID.setObjectName("lineEdit_deptID")
        self.ui.formLayout_addForm.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_deptID
        )
        self.lineEdit_deptID.setPlaceholderText("Enter Department ID...")
        self.lineEdit_deptID.setText("")
        # 1,0
        self.label_deptName = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_deptName.setObjectName("label_deptName")
        self.ui.formLayout_addForm.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_deptName
        )
        self.label_deptName.setText("Department Name: ")
        self.lineEdit_deptName = QtWidgets.QLineEdit(self.ui.page_addForm)
        self.lineEdit_deptName.setObjectName("lineEdit_deptName")
        self.ui.formLayout_addForm.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_deptName
        )
        self.lineEdit_deptName.setPlaceholderText("Enter Department Name...")
        self.lineEdit_deptName.setText("")
        # 2,0
        self.pushButton_addSubmit = QtWidgets.QPushButton(self.ui.page_addForm)
        self.pushButton_addSubmit.setObjectName("pushButton_submit")
        self.pushButton_addSubmit.setText("Submit")
        self.ui.formLayout_addForm.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, self.pushButton_addSubmit
        )
        # Connect the submit button to a handler
        self.pushButton_addSubmit.clicked.connect(self.submit_department)

    def add_course(self):
        self.stackedWidget_pages.setCurrentIndex(4)

        self.ui.label_addForm.setText("Add Course")
        # 0,0
        self.label_courseID = QtWidgets.QLabel(self.ui.page_addForm)
        self.label_courseID.setObjectName("label_courseID")
        self.ui.formLayout_addForm.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_courseID
        )
        self.label_courseID.setText("Course ID: ")
        self.lineEdit_courseID = QtWidgets.QLineEdit(self.ui.page_addForm)
        self.lineEdit_courseID.setObjectName("lineEdit_courseID")
        self.ui.formLayout_addForm.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_courseID
        )
        self.lineEdit_courseID.setPlaceholderText("Enter Course ID...")
        self.lineEdit_courseID.setText("")

    def submit_student(self):
        student_id = self.lineEdit_studID.text().strip()
        student_name = self.lineEdit_studName.text().strip()
        student_course = self.comboBox_studCourse.currentText()
        student_block = self.comboBox_studBlock.currentText()

        if (
            not student_id
            or not student_name
            or student_course == "Choose Student Course..."
            or student_block == "Choose Student Block..."
        ):
            QtWidgets.QMessageBox.warning(
                None, "Input Error", "Please fill in all fields correctly."
            )
            return

        query = QSqlQuery()
        query.prepare(
            """
            INSERT INTO tbl_student (student_id, student_name, course_id, block_id)
            VALUES (?, ?, ?, ?)
        """
        )
        query.addBindValue(student_id)
        query.addBindValue(student_name)
        query.addBindValue(student_course)
        query.addBindValue(student_block)

        if query.exec_():
            QtWidgets.QMessageBox.information(None, "Success", "Student added successfully!")
            # Clear fields
            self.lineEdit_studID.clear()
            self.lineEdit_studName.clear()
            self.comboBox_studCourse.setCurrentIndex(0)
            self.comboBox_studBlock.setCurrentIndex(0)
        else:
            QtWidgets.QMessageBox.critical(None, "Database Error", query.lastError().text())

    def submit_teacher(self):
        teacher_id = self.lineEdit_teachID.text().strip()
        teacher_name = self.lineEdit_teachName.text().strip()
        teacher_dept = self.comboBox_teachDept.currentText()

        if not teacher_id or not teacher_name or teacher_dept == "Choose Department...":
            QtWidgets.QMessageBox.warning(
                None, "Input Error", "Please fill in all fields correctly."
            )
            return

        query = QSqlQuery()
        query.prepare(
            """
            INSERT INTO tbl_teacher (teacher_id, teacher_name, department_id)
            VALUES (?, ?, ?)
        """
        )
        query.addBindValue(teacher_id)
        query.addBindValue(teacher_name)
        query.addBindValue(teacher_dept)

        if query.exec_():
            QtWidgets.QMessageBox.information(None, "Success", "Teacher added successfully!")
            # Clear fields
            self.lineEdit_teachID.clear()
            self.lineEdit_teachName.clear()
            self.comboBox_teachDept.setCurrentIndex(0)
        else:
            QtWidgets.QMessageBox.critical(None, "Database Error", query.lastError().text())

    def submit_department(self):
        department_id = self.lineEdit_deptID.text().strip()
        department_name = self.lineEdit_deptName.text().strip()

        if not department_id or not department_name:
            QtWidgets.QMessageBox.warning(
                None, "Input Error", "Please fill in all fields correctly."
            )
            return

        query = QSqlQuery()
        query.prepare(
            """
            INSERT INTO tbl_department (department_id, department_name)
            VALUES (?, ?)
        """
        )
        query.addBindValue(department_id)
        query.addBindValue(department_name)

        if query.exec_():
            QtWidgets.QMessageBox.information(None, "Success", "Department added successfully!")
            # Clear fields
            self.lineEdit_deptID.clear()
            self.lineEdit_deptName.clear()
        else:
            QtWidgets.QMessageBox.critical(None, "Database Error", query.lastError().text())
