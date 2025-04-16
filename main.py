import sys
from interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase, QSqlQuery

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()
        self.setWindowTitle("Scheduling System")

        self.db = self.connect_to_db()
        self.ui.comboBox_view.addItems(["Student", "Teacher"])

        # Navigation Buttons
        self.ui.pushButton_home.clicked.connect(lambda: self.ui.stackedWidget_pages.setCurrentIndex(1))

        # Main Content Buttons
        self.ui.pushButton_view.clicked.connect(lambda: self.page_view())
        self.ui.pushButton_add.clicked.connect(lambda: self.ui.stackedWidget_pages.setCurrentIndex(2))

    # Main Content Page
    def page_view(self):
        self.ui.stackedWidget_pages.setCurrentIndex(0)
        self.update_view()
        self.ui.comboBox_view.currentTextChanged.connect(self.update_view)

    # Update View Page
    def update_view(self):
        if self.ui.comboBox_view.currentText() == "Student":
            self.ui.label_view.setText("Student List")

            # Set up the model for the student table
            self.model = QSqlTableModel(self, self.db)
            self.model.setTable("student")
            self.model.select()

            self.model.setHeaderData(0, Qt.Horizontal, "ID")
            self.model.setHeaderData(1, Qt.Horizontal, "Full Name")
            self.model.setHeaderData(2, Qt.Horizontal, "Course")
            self.model.setHeaderData(3, Qt.Horizontal, "Block")

            self.ui.tableView_view.setModel(self.model)
            
            # Configure the table view
            self.ui.tableView_view.resizeColumnsToContents()  # Adjust column widths
            self.ui.tableView_view.resizeRowsToContents()     # Adjust row heights
            self.ui.tableView_view.setSortingEnabled(True)    # Enable sorting by column
            self.model.setSort(-1, Qt.AscendingOrder)  # -1 means no sort column
            self.model.select()
            self.ui.tableView_view.setSelectionBehavior(self.ui.tableView_view.SelectRows)  # Select entire rows
            self.ui.tableView_view.setEditTriggers(self.ui.tableView_view.NoEditTriggers)   # Make table read-only
            self.ui.tableView_view.verticalHeader().setVisible(False)  # Hide row numbers
            
            self.ui.tableView_view.doubleClicked.connect(self.page_info)  # Connect row click to info page
 

        elif self.ui.comboBox_view.currentText() == "Teacher":
            self.ui.label_view.setText("Teacher List")

            # Set up the model for the teacher table
            self.model = QSqlTableModel(self, self.db)
            self.model.setTable("teacher")
            self.model.select()

            self.model.setHeaderData(0, Qt.Horizontal, "ID")
            self.model.setHeaderData(1, Qt.Horizontal, "Full Name")
            self.model.setHeaderData(2, Qt.Horizontal, "Department")

            self.ui.tableView_view.setModel(self.model)

            # Configure the table view
            self.ui.tableView_view.resizeColumnsToContents()  # Adjust column widths
            self.ui.tableView_view.resizeRowsToContents()     # Adjust row heights
            self.ui.tableView_view.setSortingEnabled(True)    # Enable sorting by column
            self.model.setSort(-1, Qt.AscendingOrder)  # -1 means no sort column
            self.model.select()
            self.ui.tableView_view.setSelectionBehavior(self.ui.tableView_view.SelectRows)  # Select entire rows
            self.ui.tableView_view.setEditTriggers(self.ui.tableView_view.NoEditTriggers)   # Make table read-only

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())