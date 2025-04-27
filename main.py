import sys
from interface import Ui_MainWindow
from view import ViewManager
from add import Add
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()
        self.setWindowTitle("Scheduling System")

        self.db = self.connect_to_db()
        self.ui.comboBox_view.addItems(
            ["Student", "Teacher", "Department", "Subject", "Subject Schedule"]
        )
        self.view_manager = ViewManager(self.ui, self.db)
        self.add_data = Add(self.ui, self.ui.stackedWidget_pages)

        # Navigation Buttons
        self.ui.pushButton_back.clicked.connect(self.clear_formLayout_addForm)
        self.ui.pushButton_home.clicked.connect(
            lambda: self.ui.stackedWidget_pages.setCurrentIndex(1)
        )
        self.ui.pushButton_students.clicked.connect(lambda: self.nav_view("Student"))
        self.ui.pushButton_teachers.clicked.connect(lambda: self.nav_view("Teacher"))

        # Main Content Buttons
        self.ui.pushButton_view.clicked.connect(lambda: self.page_view())
        self.ui.pushButton_add.clicked.connect(
            lambda: self.ui.stackedWidget_pages.setCurrentIndex(2)
        )

        # Add Button
        self.ui.pushButton_addStudent.clicked.connect(lambda: self.add_data.add_student())
        self.ui.pushButton_addTeacher.clicked.connect(lambda: self.add_data.add_teacher())
        self.ui.pushButton_addDepartment.clicked.connect(lambda: self.add_data.add_department())
        self.ui.pushButton_addCourse.clicked.connect(lambda: self.add_data.add_course())
        self.ui.pushButton_addSubject.clicked.connect(lambda: self.add_data.add_subject())
        self.ui.pushButton_addBlock.clicked.connect(lambda: self.add_data.add_block())
        self.ui.pushButton_addRoom.clicked.connect(lambda: self.add_data.add("room"))

    def nav_view(self, button):
        if button == "Student":
            self.ui.comboBox_view.setCurrentText("Student")
            self.ui.stackedWidget_pages.setCurrentIndex(0)
            self.page_view()
        elif button == "Teacher":
            self.ui.comboBox_view.setCurrentText("Teacher")
            self.ui.stackedWidget_pages.setCurrentIndex(0)
            self.page_view()

    # View Page
    def page_view(self):
        self.ui.stackedWidget_pages.setCurrentIndex(0)
        self.update_view()
        self.ui.comboBox_view.currentTextChanged.connect(self.update_view)

    def update_view(self):
        combo_value = self.ui.comboBox_view.currentText()
        self.model = self.view_manager.update_view(
            tableView_view=self.ui.tableView_view,
            combo_value=combo_value,
            page_info_callback=self.page_info if combo_value == "Student" else None,
        )

    # Info Page
    def page_info(self, index):
        self.ui.stackedWidget_pages.setCurrentIndex(3)

        row = index.row()
        student_id = self.model.index(row, 0)
        student_name = self.model.index(row, 1)
        student_course = self.model.index(row, 2)
        student_block = self.model.index(row, 3)

        self.ui.label_studentNo.setText(str(self.model.data(student_id)))
        self.ui.label_name.setText(self.model.data(student_name))
        self.ui.label_course.setText(self.model.data(student_course))
        self.ui.label_block.setText(self.model.data(student_block))

    # Database Connection
    def connect_to_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("sched.db")
        if not db.open():
            print("Database Error:", db.lastError().text())
            raise Exception("Could not open database.")
        return db

    def clear_formLayout_addForm(self):
        if self.ui.stackedWidget_pages.currentIndex() == 4:
            layout = self.ui.formLayout_addForm
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
            self.ui.stackedWidget_pages.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
