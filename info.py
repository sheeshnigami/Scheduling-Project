from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlQuery


class Info:
    def __init__(self, ui, stackedWidget_pages, db, view_manager):
        self.ui = ui
        self.stackedWidget_pages = stackedWidget_pages
        self.db = db
        self.view_manager = view_manager
        self.current_data = None
        self.current_type = None

    def setup_info(self, title, fields, data_type, data):
        """General method to set up an info page with dynamic labels."""
        self.stackedWidget_pages.setCurrentIndex(3)
        self.ui.label_info.setText(title)
        self.current_data = data
        self.current_type = data_type

        # Clear existing grid layout
        while self.ui.gridLayout_info.count():
            item = self.ui.gridLayout_info.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                while item.layout().count():
                    nested_item = item.layout().takeAt(0)
                    if nested_item.widget():
                        nested_item.widget().deleteLater()
                item.layout().deleteLater()

        # Add fields dynamically
        for row, (label_text, field_value) in enumerate(fields.items()):
            # Field name label
            label = QtWidgets.QLabel(self.ui.page_info)
            label.setText(label_text)
            label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.ui.gridLayout_info.addWidget(label, row, 0)

            # Field value label
            value_label = QtWidgets.QLabel(self.ui.page_info)
            value_label.setText(str(field_value))
            value_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            self.ui.gridLayout_info.addWidget(value_label, row, 1)

        # Add delete button at the bottom
        delete_btn = QtWidgets.QPushButton("Delete", self.ui.page_info)
        delete_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """
        )
        delete_btn.clicked.connect(self.confirm_delete)
        self.ui.gridLayout_info.addWidget(
            delete_btn, len(fields), 0, 1, 2, Qt.AlignCenter
        )

    def confirm_delete(self):
        """Show confirmation dialog before deletion."""
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setText("Are you sure you want to delete this record?")
        msg.setInformativeText("This action cannot be undone.")
        msg.setWindowTitle("Confirm Deletion")
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if msg.exec_() == QtWidgets.QMessageBox.Yes:
            self.delete_record()

    def delete_record(self):
        """Delete the record from the database."""
        if not self.current_data or not self.current_type:
            return

        table_map = {
            "student": ("tbl_student", "student_id"),
            "teacher": ("tbl_teacher", "teacher_id"),
            "department": ("tbl_department", "department_id"),
            "course": ("tbl_course", "course_id"),
            "subject": ("tbl_subject", "subject_code"),
            "block": ("tbl_block", "block_id"),
            "room": ("tbl_room", "room_id"),
        }

        table_info = table_map.get(self.current_type)
        if not table_info:
            return

        table_name, id_field = table_info
        query = QSqlQuery(self.db)
        query.prepare(f"DELETE FROM {table_name} WHERE {id_field} = :id")
        query.bindValue(":id", self.current_data[0])

        if query.exec_():
            # Return to the previous page after successful deletion
            self.stackedWidget_pages.setCurrentIndex(0)
            # Set the combo box value to refresh the correct view
            self.ui.comboBox_view.setCurrentText(self.current_type)
            # Refresh the table view
            self.view_manager.update_view(
                tableView_view=self.ui.tableView_view, combo_value=self.current_type
            )
        else:
            print(f"Error deleting record: {query.lastError().text()}")

    def show_student_info(self, student_data):
        fields = {
            "Student ID:": student_data[0],
            "Full Name:": student_data[1],
            "Course:": student_data[2],
            "Block:": student_data[3],
        }
        self.setup_info("Student Information", fields, "student", student_data)

    def show_teacher_info(self, teacher_data):
        fields = {
            "Teacher ID:": teacher_data[0],
            "Full Name:": teacher_data[1],
            "Department:": teacher_data[2],
        }
        self.setup_info("Teacher Information", fields, "teacher", teacher_data)

    def show_department_info(self, department_data):
        fields = {
            "Department ID:": department_data[0],
            "Department Name:": department_data[1],
        }
        self.setup_info("Department Information", fields, "department", department_data)

    def show_subject_info(self, subject_data):
        fields = {
            "Subject Code:": subject_data[0],
            "Subject Name:": subject_data[1],
            "Course:": subject_data[2],
            "Units:": subject_data[3],
        }
        self.setup_info("Subject Information", fields, "subject", subject_data)

    def show_course_info(self, course_data):
        fields = {
            "Course ID:": course_data[0],
            "Course Name:": course_data[1],
            "Department:": course_data[2],
        }
        self.setup_info("Course Information", fields, "course", course_data)

    def show_block_info(self, block_data):
        fields = {
            "Block ID:": block_data[0],
            "Block Name:": block_data[1],
            "Course:": block_data[2],
        }
        self.setup_info("Block Information", fields, "block", block_data)

    def show_room_info(self, room_data):
        fields = {
            "Room ID:": room_data[0],
            "Room Name:": room_data[1],
            "Building:": room_data[2],
        }
        self.setup_info("Room Information", fields, "room", room_data)
