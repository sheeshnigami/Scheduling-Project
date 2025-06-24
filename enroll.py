from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class Enroll:
    def __init__(self, ui, stackedWidget_pages):
        self.ui = ui
        self.stackedWidget_pages = stackedWidget_pages
        self.selected_students = []  # Store selected students
        self.add_student_button = None
        self.submit_button = None
        self.schedule_combo = None

    def show_student_selection_dialog(self):
        dialog = QtWidgets.QDialog(self.ui.page_addForm)
        dialog.setWindowTitle("Select Students")
        dialog.setMinimumWidth(400)
        dialog.setMinimumHeight(500)
        dialog.setMaximumWidth(400)
        dialog.setMaximumHeight(500)

        # Create layout for the dialog
        layout = QtWidgets.QVBoxLayout(dialog)

        # Add search bar
        search_layout = QtWidgets.QHBoxLayout()
        search_label = QtWidgets.QLabel("Search:")
        search_input = QtWidgets.QLineEdit()
        search_input.setPlaceholderText("Search by ID, name, course, or year...")
        search_layout.addWidget(search_label)
        search_layout.addWidget(search_input)
        layout.addLayout(search_layout)

        # Create a scroll area for the student list
        scroll = QtWidgets.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll_content = QtWidgets.QWidget()
        scroll_layout = QtWidgets.QVBoxLayout(scroll_content)

        # Query to get all students
        query = QSqlQuery()
        query.exec_(
            "SELECT student_id, student_name, course_id, year_level FROM tbl_student"
        )

        # Store all student widgets for filtering
        student_widgets = []

        # Create checkboxes for each student
        while query.next():
            student_id = query.value(0)
            student_name = query.value(1)
            course_id = query.value(2)
            year_level = query.value(3)

            # Create a widget for each student row
            student_widget = QtWidgets.QWidget()
            student_layout = QtWidgets.QHBoxLayout(student_widget)

            # Create checkbox
            checkbox = QtWidgets.QCheckBox()
            checkbox.setText(f"{student_name} (ID: {student_id})")
            checkbox.setProperty("student_id", student_id)
            checkbox.setProperty("student_name", student_name)

            # Check if this student was previously selected
            if any(s[0] == student_id for s in self.selected_students):
                checkbox.setChecked(True)

            # Add course and year level labels
            course_label = QtWidgets.QLabel(f"Course: {course_id}")
            year_label = QtWidgets.QLabel(f"Year: {year_level}")

            # Add widgets to the student row layout
            student_layout.addWidget(checkbox)
            student_layout.addWidget(course_label)
            student_layout.addWidget(year_label)
            student_layout.addStretch()

            # Add the student row to the scroll layout
            scroll_layout.addWidget(student_widget)
            student_widgets.append(student_widget)

        # Add the scroll area to the main layout
        scroll.setWidget(scroll_content)
        layout.addWidget(scroll)

        # Add buttons
        button_layout = QtWidgets.QHBoxLayout()
        select_all_btn = QtWidgets.QPushButton("Select All")
        deselect_all_btn = QtWidgets.QPushButton("Deselect All")
        add_btn = QtWidgets.QPushButton("Add Selected")
        cancel_btn = QtWidgets.QPushButton("Cancel")

        button_layout.addWidget(select_all_btn)
        button_layout.addWidget(deselect_all_btn)
        button_layout.addWidget(add_btn)
        button_layout.addWidget(cancel_btn)
        layout.addLayout(button_layout)

        # Connect button signals
        select_all_btn.clicked.connect(
            lambda: self.toggle_all_checkboxes(scroll_content, True)
        )
        deselect_all_btn.clicked.connect(
            lambda: self.toggle_all_checkboxes(scroll_content, False)
        )
        add_btn.clicked.connect(
            lambda: self.add_selected_students(scroll_content, dialog)
        )
        cancel_btn.clicked.connect(dialog.reject)

        # Add search functionality
        def filter_students():
            search_text = search_input.text().lower()
            for widget in student_widgets:
                # Get all text from the widget's children
                widget_text = ""
                for child in widget.findChildren(QtWidgets.QWidget):
                    if isinstance(child, (QtWidgets.QLabel, QtWidgets.QCheckBox)):
                        widget_text += child.text().lower() + " "

                # Show/hide widget based on search text
                widget.setVisible(search_text in widget_text)

        search_input.textChanged.connect(filter_students)

        return dialog

    def toggle_all_checkboxes(self, container, checked):
        for i in range(container.layout().count()):
            widget = container.layout().itemAt(i).widget()
            if widget:
                checkbox = widget.findChild(QtWidgets.QCheckBox)
                if checkbox:
                    checkbox.setChecked(checked)

    def add_selected_students(self, container, dialog):
        self.selected_students = []
        for i in range(container.layout().count()):
            widget = container.layout().itemAt(i).widget()
            if widget:
                checkbox = widget.findChild(QtWidgets.QCheckBox)
                if checkbox and checkbox.isChecked():
                    student_id = checkbox.property("student_id")
                    student_name = checkbox.property("student_name")
                    self.selected_students.append((student_id, student_name))

        # Add selected students to the form
        self.update_student_labels()
        self.update_button_states()  # Update button states after adding students
        dialog.accept()

    def update_student_labels(self):
        # Clear existing student labels
        for i in range(self.ui.formLayout_addForm.count() - 1, 1, -1):
            item = self.ui.formLayout_addForm.takeAt(i)
            if item.widget():
                item.widget().deleteLater()

        # Add "add student button"
        self.add_student_button = QtWidgets.QPushButton(self.ui.page_addForm)
        self.add_student_button.setText("Add Student")
        self.add_student_button.setEnabled(False)  # Initially disabled
        self.add_student_button.clicked.connect(
            lambda: self.show_student_selection_dialog().exec_()
        )
        self.ui.formLayout_addForm.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.add_student_button
        )

        # Create table view for selected students
        table_view = QtWidgets.QTableView(self.ui.page_addForm)
        model = QSqlTableModel(self.ui.page_addForm)
        model.setTable("tbl_student")

        # Set custom headers
        model.setHeaderData(model.fieldIndex("student_id"), Qt.Horizontal, "Student ID")
        model.setHeaderData(
            model.fieldIndex("student_name"), Qt.Horizontal, "Student Name"
        )
        model.setHeaderData(model.fieldIndex("course_id"), Qt.Horizontal, "Course")
        model.setHeaderData(model.fieldIndex("year_level"), Qt.Horizontal, "Year Level")

        # Filter to show only selected students
        if self.selected_students:
            student_ids = [f"'{student[0]}'" for student in self.selected_students]
            filter_str = f"student_id IN ({','.join(student_ids)})"
            model.setFilter(filter_str)
        else:
            model.setFilter("1=0")  # Show no students if none selected

        model.select()
        table_view.setModel(model)
        table_view.resizeColumnsToContents()
        table_view.resizeRowsToContents()
        table_view.setSortingEnabled(True)
        table_view.setSelectionBehavior(table_view.SelectRows)
        table_view.setEditTriggers(table_view.NoEditTriggers)
        table_view.verticalHeader().setVisible(False)

        # Add table view to form
        self.ui.formLayout_addForm.setWidget(
            3, QtWidgets.QFormLayout.SpanningRole, table_view
        )

        # Add submit button
        self.submit_button = QtWidgets.QPushButton(self.ui.page_addForm)
        self.submit_button.setText("Submit")
        self.submit_button.setEnabled(False)  # Initially disabled
        self.submit_button.clicked.connect(self.submit_enroll)
        self.ui.formLayout_addForm.setWidget(
            4, QtWidgets.QFormLayout.SpanningRole, self.submit_button
        )

        # Update button states
        self.update_button_states()

    def enroll_student(self):
        self.stackedWidget_pages.setCurrentIndex(4)
        self.ui.label_addForm.setText("Enroll")

        # Clear existing form layout
        while self.ui.formLayout_addForm.count():
            item = self.ui.formLayout_addForm.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        label = QtWidgets.QLabel(self.ui.page_addForm)
        label.setText("Schedule: ")
        self.ui.formLayout_addForm.setWidget(0, QtWidgets.QFormLayout.LabelRole, label)

        query = QSqlQuery()
        # Query the database to get sched names
        query.exec_("SELECT sched_id, sched_name FROM tbl_subject_sched")
        sched_items = []  # Collect sched names from the query results
        while query.next():
            display_name = f"{query.value(1)}"  # sched_name
            user_data = query.value(0)  # sched_id
            sched_items.append((display_name, user_data))

        self.schedule_combo = QtWidgets.QComboBox(self.ui.page_addForm)
        self.schedule_combo.addItem("Choose Schedule", None)
        self.schedule_combo.model().item(0).setEnabled(False)
        for display_name, user_data in sched_items:
            self.schedule_combo.addItem(display_name, user_data)
        self.schedule_combo.setCurrentIndex(0)

        self.ui.formLayout_addForm.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.schedule_combo
        )

        # Add "add student button"
        self.add_student_button = QtWidgets.QPushButton(self.ui.page_addForm)
        self.add_student_button.setText("Add Student")
        self.add_student_button.setEnabled(False)  # Initially disabled
        self.add_student_button.clicked.connect(
            lambda: self.show_student_selection_dialog().exec_()
        )
        self.ui.formLayout_addForm.setWidget(
            1, QtWidgets.QFormLayout.SpanningRole, self.add_student_button
        )

        # Add submit button
        self.submit_button = QtWidgets.QPushButton(self.ui.page_addForm)
        self.submit_button.setText("Submit")
        self.submit_button.setEnabled(False)  # Initially disabled
        self.submit_button.clicked.connect(self.submit_enroll)
        self.ui.formLayout_addForm.setWidget(
            2, QtWidgets.QFormLayout.SpanningRole, self.submit_button
        )

        # Connect schedule combo box change event
        self.schedule_combo.currentIndexChanged.connect(self.update_button_states)

    def update_button_states(self):
        """Update button states based on current selections."""
        if not all([self.schedule_combo, self.add_student_button, self.submit_button]):
            return

        selected_schedule = self.schedule_combo.currentData()
        has_schedule = selected_schedule is not None
        has_students = len(self.selected_students) > 0

        self.add_student_button.setEnabled(has_schedule)
        self.submit_button.setEnabled(has_schedule and has_students)

    def submit_enroll(self):
        """Handle the enrollment submission."""
        if not self.selected_students:
            QtWidgets.QMessageBox.warning(
                None, "Input Error", "Please select at least one student."
            )
            return

        # Get the selected schedule
        selected_schedule = self.schedule_combo.currentData()

        if not selected_schedule:
            QtWidgets.QMessageBox.warning(
                None, "Input Error", "Please select a schedule."
            )
            return

        # Prepare the query
        query = QSqlQuery()
        query.prepare("INSERT INTO tbl_enrollment (student_id, sched_id) VALUES (?, ?)")

        success_count = 0
        error_count = 0

        # Insert each selected student
        for student_id, _ in self.selected_students:
            query.addBindValue(student_id)
            query.addBindValue(selected_schedule)

            if query.exec_():
                success_count += 1
            else:
                error_count += 1

        # Show result message
        if error_count == 0:
            QtWidgets.QMessageBox.information(
                None,
                "Success",
                f"Successfully enrolled {success_count} student(s) to the schedule.",
            )
            # Reset the form
            self.selected_students = []
            self.enroll_student()
        else:
            QtWidgets.QMessageBox.warning(
                None,
                "Partial Success",
                f"Enrolled {success_count} student(s) successfully.\nFailed to enroll {error_count} student(s).",
            )
