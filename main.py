import sys
from interface import Ui_MainWindow
from view import ViewManager
from add import Add
from info import Info
from enroll import Enroll
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import Qt
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()
        self.setWindowTitle("Scheduling System")

        # Initialize database and managers
        self.db = self.connect_to_db()
        self.view_manager = ViewManager(self.ui, self.db)
        self.add_data = Add(self.ui, self.ui.stackedWidget_pages)
        self.info = Info(
            self.ui, self.ui.stackedWidget_pages, self.db, self.view_manager
        )
        self.enroll = Enroll(self.ui, self.ui.stackedWidget_pages)

        # Setup UI components
        self.setup_combo_box()
        self.setup_navigation_buttons()
        self.setup_main_content_buttons()
        self.setup_add_buttons()

    # Setup ComboBox
    def setup_combo_box(self):
        self.ui.comboBox_view.addItems(
            [
                "Student List",
                "Teacher List",
                "Department List",
                "Subject List",
                "Course List",
                "Block List",
                "Room List",
                "Room Schedule List",
                "Subject Schedule List",
            ]
        )
        self.ui.comboBox_view.currentTextChanged.connect(self.update_view)

    # Setup Navigation Buttons
    def setup_navigation_buttons(self):
        navigation_buttons = {
            self.ui.pushButton_back: 2,
            self.ui.pushButton_home: 1,
            self.ui.pushButton_nav_add: 2,
        }
        for button, page_index in navigation_buttons.items():
            button.clicked.connect(
                lambda _, index=page_index: self.ui.stackedWidget_pages.setCurrentIndex(
                    index
                )
            )

        self.ui.pushButton_nav_view.clicked.connect(self.page_view)

    # Setup Main Content Buttons
    def setup_main_content_buttons(self):
        self.ui.pushButton_view.clicked.connect(self.page_view)
        self.ui.pushButton_add.clicked.connect(
            lambda: self.ui.stackedWidget_pages.setCurrentIndex(2)
        )

    # Setup Add Buttons
    def setup_add_buttons(self):
        add_buttons = {
            self.ui.pushButton_addStudent: self.add_data.add_student,
            self.ui.pushButton_addTeacher: self.add_data.add_teacher,
            self.ui.pushButton_addDepartment: self.add_data.add_department,
            self.ui.pushButton_addCourse: self.add_data.add_course,
            self.ui.pushButton_addSubject: self.add_data.add_subject,
            self.ui.pushButton_addBlock: self.add_data.add_block,
            self.ui.pushButton_addRoom: self.add_data.add_room,
            self.ui.pushButton_addRoomSched: self.add_data.add_room_sched,
            self.ui.pushButton_addSubjectSched: self.add_data.add_subject_sched,
            self.ui.pushButton_enroll: self.enroll.enroll_student,
        }
        for button, handler in add_buttons.items():
            button.clicked.connect(handler)

    # View Page
    def page_view(self):
        self.ui.stackedWidget_pages.setCurrentIndex(0)
        self.update_view()

    def update_view(self):
        combo_value = self.ui.comboBox_view.currentText()
        if combo_value == "Student List":
            update_value = "student"
        elif combo_value == "Teacher List":
            update_value = "teacher"
        elif combo_value == "Department List":
            update_value = "department"
        elif combo_value == "Subject List":
            update_value = "subject"
        elif combo_value == "Course List":
            update_value = "course"
        elif combo_value == "Block List":
            update_value = "block"
        elif combo_value == "Room List":
            update_value = "room"
        elif combo_value == "Room Schedule List":
            update_value = "room schedule"
        elif combo_value == "Subject Schedule List":
            update_value = "subject schedule"

        self.update_value = update_value

        self.model = self.view_manager.update_view(
            tableView_view=self.ui.tableView_view,
            combo_value=update_value,
            page_info_callback=self.page_info,
        )

    def page_info(self, index):
        row = index.row()
        combo_value = self.update_value

        data_extractors = {
            "student": (self.info.show_student_info, [0, 1, 2, 3]),
            "teacher": (self.info.show_teacher_info, [0, 1, 2]),
            "department": (self.info.show_department_info, [0, 1]),
            "subject": (self.info.show_subject_info, [0, 1, 2, 3]),
            "course": (self.info.show_course_info, [0, 1, 2]),
            "block": (self.info.show_block_info, [0, 1, 2]),
            "room": (self.info.show_room_info, [0, 1, 2]),
            "room schedule": (
                self.info.show_room_schedule_info,
                [0, 1, 2, 3, 4, 5, 6, 7],
            ),
            "subject schedule": (
                self.info.show_subject_schedule_info,
                [0, 1, 2, 3, 4, 5],
            ),
        }

        if combo_value in data_extractors:
            show_function, columns = data_extractors[combo_value]
            selected_data = tuple(self.model.index(row, col).data() for col in columns)
            show_function(selected_data)

    # Database Connection
    def connect_to_db(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("sched.db")
        if not db.open():
            print("Database Error:", db.lastError().text())
            raise ConnectionError("Could not open database.")

        # Initialize database schema
        self.initialize_database(db)
        return db

    def initialize_database(self, db):
        # Read and execute the schema.sql file
        schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
        try:
            with open(schema_path, "r") as file:
                schema_sql = file.read()

            # Split the SQL file into individual statements
            statements = schema_sql.split(";")

            # Execute each statement
            query = QSqlQuery(db)
            for statement in statements:
                if statement.strip() and not query.exec_(statement):
                    QMessageBox.critical(
                        self,
                        "Database Error",
                        f"Error executing SQL: {query.lastError().text()}\nStatement: {statement}",
                    )
        except Exception as e:
            QMessageBox.critical(
                self, "Database Error", f"Error initializing database: {str(e)}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
