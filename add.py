from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

# Table headers configuration
TABLE_HEADERS = {
    "tbl_student": {
        "student_id": "Student ID",
        "student_name": "Student Name",
        "course_id": "Course",
        "year_level": "Year Level",
        "status": "Status",
    },
    "tbl_teacher": {
        "teacher_id": "Teacher ID",
        "teacher_name": "Teacher Name",
        "department_id": "Department",
    },
    "tbl_department": {
        "department_id": "Department ID",
        "department_name": "Department Name",
    },
    "tbl_course": {
        "course_id": "Course ID",
        "course_name": "Course Name",
        "department_id": "Department",
    },
    "tbl_subject": {
        "subject_code": "Subject Code",
        "subject_name": "Subject Name",
        "course_id": "Course",
        "units": "Units",
        "year_level": "Year Level",
    },
    "tbl_block": {
        "block_id": "Block ID",
        "block_name": "Block Name",
        "course_id": "Course",
        "department_id": "Department",
        "year_level": "Year Level",
    },
    "tbl_room": {
        "room_id": "Room ID",
        "room_name": "Room Name",
        "building": "Building",
    },
    "tbl_room_sched": {
        "room_avail_id": "Room Available ID",
        "room_avail_name": "Room Available Name",
        "room_id": "Room",
        "day_available": "Day",
        "time_start": "Time Start",
        "time_end": "Time End",
        "is_available": "Available",
    },
    "tbl_subject_sched": {
        "sched_id": "Schedule ID",
        "sched_name": "Schedule Name",
        "subject_code": "Subject Code",
        "teacher_id": "Teacher",
        "block_id": "Block",
        "room_avail_id": "Room Schedule",
        "year_level": "Year Level",
    },
}


class Add:
    def __init__(self, ui, stackedWidget_pages):
        self.ui = ui
        self.stackedWidget_pages = stackedWidget_pages

    def setup_form(self, title, fields, submit_handler, table_name=None):
        """General method to set up a form dynamically."""
        self.stackedWidget_pages.setCurrentIndex(4)
        self.ui.label_addForm.setText(title)

        # Clear existing form layout
        while self.ui.formLayout_addForm.count():
            item = self.ui.formLayout_addForm.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Add fields dynamically
        self.form_inputs = {}
        self.field_map = {}
        for row, (label_text, db_field, field_type, options) in enumerate(fields):
            label = QtWidgets.QLabel(self.ui.page_addForm)
            label.setText(label_text)
            self.ui.formLayout_addForm.setWidget(
                row, QtWidgets.QFormLayout.LabelRole, label
            )

            if field_type == "line_edit":
                field = QtWidgets.QLineEdit(self.ui.page_addForm)
                field.setPlaceholderText(options.get("placeholder", ""))
            elif field_type == "combo_box":
                field = QtWidgets.QComboBox(self.ui.page_addForm)
                field.addItem(
                    options.get("default", "Choose..."), None
                )  # Default item with no user data
                field.model().item(0).setEnabled(False)
                # Add items with display text and user data
                items = options.get("items", [])
                for item in items:
                    if isinstance(item, tuple):
                        display_text, user_data = item
                        field.addItem(
                            display_text, user_data
                        )  # Add display text with user data
                    else:
                        field.addItem(item)  # Add item as display text only

                field.setCurrentIndex(0)
            else:
                raise ValueError("Unsupported field type")

            self.ui.formLayout_addForm.setWidget(
                row, QtWidgets.QFormLayout.FieldRole, field
            )
            self.form_inputs[label_text] = field
            self.field_map[label_text] = db_field

        # Add submit button
        submit_button = QtWidgets.QPushButton(self.ui.page_addForm)
        submit_button.setText("Submit")
        submit_button.clicked.connect(submit_handler)
        self.ui.formLayout_addForm.setWidget(
            len(fields), QtWidgets.QFormLayout.SpanningRole, submit_button
        )

        table_view = QtWidgets.QTableView(self.ui.page_addForm)
        self.ui.formLayout_addForm.setWidget(
            len(fields) + 1, QtWidgets.QFormLayout.SpanningRole, table_view
        )
        self.table_view = table_view

        # Show current table data if table_name is provided
        if table_name:
            model = QSqlTableModel(self.ui.page_addForm)
            model.setTable(table_name)

            # Set custom headers if available
            if table_name in TABLE_HEADERS:
                for col, header in TABLE_HEADERS[table_name].items():
                    model.setHeaderData(model.fieldIndex(col), Qt.Horizontal, header)

            model.select()
            self.table_view.setModel(model)
            self.table_view.resizeColumnsToContents()
            self.table_view.resizeRowsToContents()
            self.table_view.setSortingEnabled(True)
            model.setSort(-1, Qt.AscendingOrder)
            model.select()
            self.table_view.setSelectionBehavior(self.table_view.SelectRows)
            self.table_view.setEditTriggers(self.table_view.NoEditTriggers)
            self.table_view.verticalHeader().setVisible(False)

    def add_student(self):
        query = QSqlQuery()
        # Query the database to get course names
        query.exec_("SELECT course_name, course_id FROM tbl_course")
        course_items = []  # Collect course names from the query results
        while query.next():
            display_name = f"{query.value(0)}, {query.value(1)}"  # course_name
            user_data = query.value(1)  # course_id
            course_items.append((display_name, user_data))
        fields = [
            (
                "Student ID:",
                "student_id",
                "line_edit",
                {"placeholder": "Enter Student ID..."},
            ),
            (
                "Student Name:",
                "student_name",
                "line_edit",
                {"placeholder": "Enter Student Name..."},
            ),
            (
                "Course:",
                "course_id",
                "combo_box",
                {"default": "Choose Student Course...", "items": course_items},
            ),
            (
                "Year Level:",
                "year_level",
                "combo_box",
                {
                    "default": "Choose Year Level...",
                    "items": [
                        "Grade 11",
                        "Grade 12",
                        "1st Year",
                        "2nd Year",
                        "3rd Year",
                        "4th Year",
                    ],
                },
            ),
            (
                "Status",
                "status",
                "combo_box",
                {
                    "default": "Choose Student Status...",
                    "items": ["Regular", "Irregular"],
                },
            ),
        ]
        self.setup_form(
            "Add Student", fields, self.submit_student, table_name="tbl_student"
        )

    def add_teacher(self):
        query = QSqlQuery()
        # Query the database to get department names
        query.exec_("SELECT department_name, department_id FROM tbl_department")
        department_items = []  # Collect department names from the query results
        while query.next():
            display_name = f"{query.value(0)}, {query.value(1)}"  # department_name
            user_data = query.value(1)  # department_id
            department_items.append((display_name, user_data))
        fields = [
            (
                "Teacher ID:",
                "teacher_id",
                "line_edit",
                {"placeholder": "Enter Teacher ID..."},
            ),
            (
                "Teacher Name:",
                "teacher_name",
                "line_edit",
                {"placeholder": "Enter Teacher Name..."},
            ),
            (
                "Department:",
                "department_id",
                "combo_box",
                {"default": "Choose Department...", "items": department_items},
            ),
        ]
        self.setup_form(
            "Add Teacher", fields, self.submit_teacher, table_name="tbl_teacher"
        )

    def add_department(self):
        fields = [
            (
                "Department ID:",
                "department_id",
                "line_edit",
                {"placeholder": "Enter Department ID..."},
            ),
            (
                "Department Name:",
                "department_name",
                "line_edit",
                {"placeholder": "Enter Department Name..."},
            ),
        ]
        self.setup_form(
            "Add Department",
            fields,
            self.submit_department,
            table_name="tbl_department",
        )

    def add_course(self):
        query = QSqlQuery()
        # Query the database to get department names
        query.exec_("SELECT department_name, department_id FROM tbl_department")
        department_items = []  # Collect department names from the query results
        while query.next():
            display_name = f"{query.value(0)}, {query.value(1)}"  # department_name
            user_data = query.value(1)  # department_id
            department_items.append((display_name, user_data))
        fields = [
            (
                "Course ID:",
                "course_id",
                "line_edit",
                {"placeholder": "Enter Course ID..."},
            ),
            (
                "Course Name:",
                "course_name",
                "line_edit",
                {"placeholder": "Enter Course Name..."},
            ),
            (
                "Department:",
                "department_id",
                "combo_box",
                {"default": "Choose Department...", "items": department_items},
            ),
        ]
        self.setup_form(
            "Add Course", fields, self.submit_course, table_name="tbl_course"
        )

    def add_subject(self):
        query = QSqlQuery()
        # Query the database to get course names
        query.exec_("SELECT course_name, course_id FROM tbl_course")
        course_items = []  # Collect course names from the query results
        while query.next():
            display_name = f"{query.value(0)}, {query.value(1)}"  # course_name
            user_data = query.value(1)  # course_id
            course_items.append((display_name, user_data))
        fields = [
            (
                "Subject Code:",
                "subject_code",
                "line_edit",
                {"placeholder": "Enter Subject Code..."},
            ),
            (
                "Subject Name:",
                "subject_name",
                "line_edit",
                {"placeholder": "Enter Subject Name..."},
            ),
            (
                "Course:",
                "course_id",
                "combo_box",
                {"default": "Choose Course...", "items": course_items},
            ),
            (
                "Units:",
                "units",
                "combo_box",
                {"default": "Choose Subject Units...", "items": ["1", "2", "3"]},
            ),
            (
                "Year Level:",
                "year_level",
                "combo_box",
                {
                    "default": "Choose Year Level...",
                    "items": [
                        "Grade 11",
                        "Grade 12",
                        "1st Year",
                        "2nd Year",
                        "3rd Year",
                        "4th Year",
                    ],
                },
            ),
        ]
        self.setup_form(
            "Add Subject", fields, self.submit_subject, table_name="tbl_subject"
        )

    def add_block(self):
        query = QSqlQuery()
        # Query the database to get course names
        query.exec_("SELECT course_name, course_id FROM tbl_course")
        course_items = []  # Collect course names from the query results
        while query.next():
            display_name = f"{query.value(0)}, {query.value(1)}"  # course_name
            user_data = query.value(1)  # course_id
            course_items.append((display_name, user_data))
        query.exec_("SELECT department_name, department_id FROM tbl_department")
        department_items = []  # Collect department names from the query results
        while query.next():
            display_name = f"{query.value(0)}, {query.value(1)}"  # department_name
            user_data = query.value(1)  # department_id
            department_items.append((display_name, user_data))
        fields = [
            (
                "Block ID:",
                "block_id",
                "line_edit",
                {"placeholder": "Enter Block ID..."},
            ),
            (
                "Block Name:",
                "block_name",
                "line_edit",
                {"placeholder": "Enter Block Name..."},
            ),
            (
                "Course:",
                "course_id",
                "combo_box",
                {"default": "Choose Course...", "items": course_items},
            ),
            (
                "Department:",
                "department_id",
                "combo_box",
                {"default": "Choose Department...", "items": department_items},
            ),
            (
                "Year Level:",
                "year_level",
                "combo_box",
                {
                    "default": "Choose Year Level...",
                    "items": [
                        "Grade 11",
                        "Grade 12",
                        "1st Year",
                        "2nd Year",
                        "3rd Year",
                        "4th Year",
                    ],
                },
            ),
        ]
        self.setup_form("Add Block", fields, self.submit_block, table_name="tbl_block")

    def add_room(self):
        fields = [
            (
                "Room ID:",
                "room_id",
                "line_edit",
                {"placeholder": "Enter Room ID..."},
            ),
            (
                "Room Name:",
                "room_name",
                "line_edit",
                {"placeholder": "Enter Room Name..."},
            ),
            (
                "Building:",
                "building",
                "line_edit",
                {"placeholder": "Enter Building Name..."},
            ),
        ]
        self.setup_form("Add Room", fields, self.submit_room, table_name="tbl_room")

    def add_room_sched(self):
        query = QSqlQuery()
        # Query the database to get room names
        query.exec_("SELECT room_name, room_id, building FROM tbl_room")
        room_items = []  # Collect department names from the query results
        while query.next():
            display_name = f"{query.value(0)}, {query.value(2)}"  # room_name
            user_data = query.value(1)  # room_id
            room_items.append((display_name, user_data))
        fields = [
            (
                "Room:",
                "room_id",
                "combo_box",
                {"default": "Choose Room...", "items": room_items},
            ),
            (
                "Day:",
                "day_available",
                "combo_box",
                {
                    "default": "Choose Day...",
                    "items": [
                        "Monday",
                        "Tuesday",
                        "Wednesday",
                        "Thursday",
                        "Friday",
                        "Saturday",
                    ],
                },
            ),
            (
                "Time Start:",
                "time_start",
                "combo_box",
                {
                    "default": "Choose Time Start...",
                    "items": [
                        "7:00 AM",
                        "9:00 AM",
                        "11:00 AM",
                        "1:00 PM",
                        "3:00 PM",
                        "5:00 PM",
                    ],
                },
            ),
            (
                "Time End:",
                "time_end",
                "combo_box",
                {
                    "default": "Choose Time End...",
                    "items": [
                        "9:00 AM",
                        "11:00 AM",
                        "1:00 PM",
                        "3:00 PM",
                        "5:00 PM",
                        "7:00 PM",
                    ],
                },
            ),
        ]
        self.setup_form(
            "Add Room", fields, self.submit_room_sched, table_name="tbl_room_sched"
        )

    def add_subject_sched(self):
        query = QSqlQuery()
        # Initial empty lists for subject and block
        subject_items = []
        block_items = []
        # Query the database to get teacher names
        query.exec_("SELECT teacher_name, teacher_id, department_id FROM tbl_teacher")
        teacher_items = []  # Collect teacher names from the query results
        while query.next():
            display_name = f"{query.value(0)}, ({query.value(2)})"  # teacher_name
            user_data = query.value(1)  # teacher_id
            teacher_items.append((display_name, user_data))
        # Query the database to get room names
        query.exec_(
            "SELECT room_avail_id, room_id, day_available, time_start, time_end, is_available FROM tbl_room_sched WHERE is_available = 1"
        )
        room_avail_items = []  # Collect room names from the query results
        while query.next():
            display_name = f"{query.value(1)} - {query.value(2)}, {query.value(3)} - {query.value(4)}"  # room_name
            user_data = query.value(0)  # room_id
            room_avail_items.append((display_name, user_data))
        fields = [
            (
                "Year Level:",
                "year_level",
                "combo_box",
                {
                    "default": "Choose Year Level...",
                    "items": [
                        "Grade 11",
                        "Grade 12",
                        "1st Year",
                        "2nd Year",
                        "3rd Year",
                        "4th Year",
                    ],
                },
            ),
            (
                "Subject Code:",
                "subject_code",
                "combo_box",
                {"default": "Enter Subject Code...", "items": subject_items},
            ),
            (
                "Teacher:",
                "teacher_id",
                "combo_box",
                {"default": "Choose Teacher...", "items": teacher_items},
            ),
            (
                "Block:",
                "block_id",
                "combo_box",
                {"default": "Choose Block...", "items": block_items},
            ),
            (
                "Room:",
                "room_avail_id",
                "combo_box",
                {"default": "Choose Room...", "items": room_avail_items},
            ),
        ]
        self.setup_form(
            "Add Subject Sched",
            fields,
            self.submit_subject_sched,
            table_name="tbl_subject_sched",
        )

        # --- Dynamic filtering logic ---
        year_level_cb = self.form_inputs["Year Level:"]
        subject_cb = self.form_inputs["Subject Code:"]
        block_cb = self.form_inputs["Block:"]

        def update_subjects_blocks():
            year_level = year_level_cb.currentText()
            # Only update if a valid year level is selected
            if year_level.startswith("Choose"):
                # Clear subject and block combo boxes
                subject_cb.clear()
                subject_cb.addItem("Enter Subject Code...", None)
                subject_cb.model().item(0).setEnabled(False)
                block_cb.clear()
                block_cb.addItem("Choose Block...", None)
                block_cb.model().item(0).setEnabled(False)
                return
            # Update subject combo box
            query = QSqlQuery()
            query.prepare(
                "SELECT subject_code, subject_name FROM tbl_subject WHERE year_level = ?"
            )
            query.addBindValue(year_level)
            query.exec_()
            subject_cb.clear()
            subject_cb.addItem("Enter Subject Code...", None)
            subject_cb.model().item(0).setEnabled(False)
            while query.next():
                display_name = f"{query.value(0)}, ({query.value(1)})"
                user_data = query.value(0)
                subject_cb.addItem(display_name, user_data)
            # Update block combo box
            query = QSqlQuery()
            query.prepare(
                "SELECT block_id, block_name, course_id, department_id FROM tbl_block WHERE year_level = ?"
            )
            query.addBindValue(year_level)
            query.exec_()
            block_cb.clear()
            block_cb.addItem("Choose Block...", None)
            block_cb.model().item(0).setEnabled(False)
            while query.next():
                display_name = (
                    f"{query.value(1)} - ({query.value(2)} - {query.value(3)})"
                )
                user_data = query.value(0)
                block_cb.addItem(display_name, user_data)

        year_level_cb.currentIndexChanged.connect(update_subjects_blocks)
        # Optionally, call once to initialize if a year is preselected
        update_subjects_blocks()

    def submit_form(self, table_name, fields, message):
        """General method to handle form submission."""
        values = {}
        for label, field in self.form_inputs.items():
            if isinstance(field, QtWidgets.QLineEdit):
                values[self.field_map[label]] = field.text().strip()
            elif isinstance(field, QtWidgets.QComboBox):
                values[self.field_map[label]] = (
                    field.currentData()
                    if field.currentData() is not None
                    else field.currentText()
                )

        # Add is_available if needed
        if table_name == "tbl_room_sched":
            values["is_available"] = 1
            # Create room_avail_name by combining room_id, day, and time information
            room_id = values["room_id"]
            day = values["day_available"]
            time_start = values["time_start"]
            time_end = values["time_end"]
            values["room_avail_name"] = f"{room_id} - {day}, {time_start}-{time_end})"

        if table_name == "tbl_subject_sched":
            # Query to get teacher name
            query = QSqlQuery()
            query.prepare("SELECT teacher_name FROM tbl_teacher WHERE teacher_id = ?")
            query.addBindValue(values["teacher_id"])
            query.exec_()
            teacher_name = query.value(0) if query.next() else values["teacher_id"]

            # Query to get block name
            query.prepare("SELECT block_name FROM tbl_block WHERE block_id = ?")
            query.addBindValue(values["block_id"])
            query.exec_()
            block_name = query.value(0) if query.next() else values["block_id"]

            # Query to get room availability name
            query.prepare(
                "SELECT room_avail_name FROM tbl_room_sched WHERE room_avail_id = ?"
            )
            query.addBindValue(values["room_avail_id"])
            query.exec_()
            room_avail_name = (
                query.value(0) if query.next() else values["room_avail_id"]
            )

            # Create sched_name using descriptive names
            values["sched_name"] = (
                f"{values['subject_code']} - ({room_avail_name}) ({teacher_name}-({block_name}))"
            )

            update_query = QSqlQuery()
            update_query.prepare(
                "UPDATE tbl_room_sched SET is_available = 0 WHERE room_avail_id = ?"
            )
            update_query.addBindValue(values["room_avail_id"])
            update_query.exec_()

        # Validate inputs
        for key, value in values.items():
            if not value or (isinstance(value, str) and "Choose" in value):
                QtWidgets.QMessageBox.warning(
                    None, "Input Error", "Please fill in all fields correctly."
                )
                return

        # Map labels to database fields
        mapped_values = [values[field] for field in fields]

        print(fields)
        print(mapped_values)

        # Prepare and execute query
        query = QSqlQuery()
        placeholders = ", ".join(["?"] * len(fields))
        query.prepare(
            f"INSERT INTO {table_name} ({', '.join(fields)}) VALUES ({placeholders})"
        )
        for value in mapped_values:
            query.addBindValue(value)

        if query.exec_():
            # Construct success message with all inputted data
            success_message = f"{message} added successfully!\n\n"
            for key, value in values.items():
                success_message += f"{key.replace('_', ' ').upper()}: {value}\n"

            QtWidgets.QMessageBox.information(None, "Success", success_message)

            # Call the appropriate setup_form method based on table_name
            if table_name == "tbl_student":
                self.add_student()
            elif table_name == "tbl_teacher":
                self.add_teacher()
            elif table_name == "tbl_department":
                self.add_department()
            elif table_name == "tbl_course":
                self.add_course()
            elif table_name == "tbl_subject":
                self.add_subject()
            elif table_name == "tbl_block":
                self.add_block()
            elif table_name == "tbl_room":
                self.add_room()
            elif table_name == "tbl_room_sched":
                self.add_room_sched()
            elif table_name == "tbl_subject_sched":
                self.add_subject_sched()

        else:
            QtWidgets.QMessageBox.critical(
                None, "Database Error", query.lastError().text()
            )

    def submit_student(self):
        self.submit_form(
            "tbl_student",
            ["student_id", "student_name", "course_id", "year_level", "status"],
            "Student",
        )

    def submit_teacher(self):
        self.submit_form(
            "tbl_teacher", ["teacher_id", "teacher_name", "department_id"], "Teacher"
        )

    def submit_department(self):
        self.submit_form(
            "tbl_department", ["department_id", "department_name"], "Department"
        )

    def submit_course(self):
        self.submit_form(
            "tbl_course",
            ["course_id", "course_name", "department_id"],
            "Course",
        )

    def submit_subject(self):
        self.submit_form(
            "tbl_subject",
            ["subject_code", "subject_name", "course_id", "units", "year_level"],
            "Subject",
        )

    def submit_block(self):
        self.submit_form(
            "tbl_block",
            ["block_id", "block_name", "course_id", "department_id", "year_level"],
            "Block",
        )

    def submit_room(self):
        self.submit_form("tbl_room", ["room_id", "room_name", "building"], "Room")

    def submit_room_sched(self):
        self.submit_form(
            "tbl_room_sched",
            [
                "room_avail_name",
                "room_id",
                "day_available",
                "time_start",
                "time_end",
                "is_available",
            ],
            "Room Schedule",
        )

    def submit_subject_sched(self):
        self.submit_form(
            "tbl_subject_sched",
            ["sched_name", "subject_code", "teacher_id", "block_id", "room_avail_id"],
            "Subject Schedule",
        )

    def refresh_table_view(self):
        self.table_view.model().select()
        self.table_view.resizeColumnsToContents()
        self.table_view.resizeRowsToContents()
