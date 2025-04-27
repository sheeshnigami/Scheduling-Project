from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class ViewManager:
    def __init__(self, ui, db):
        self.ui = ui
        self.db = db

        # Define configurations in one place
        self.view_config = {
            "Student": {
                "table": "tbl_student",
                "label": "Student List",
                "headers": ["Student ID", "Full Name", "Course", "Block"],
            },
            "Teacher": {
                "table": "tbl_teacher",
                "label": "Teacher List",
                "headers": ["Teacher ID", "Full Name", "Department"],
            },
            "Department": {
                "table": "tbl_department",
                "label": "Department List",
                "headers": ["Department ID", "Department Name"],
            },
            "Subject": {
                "table": "tbl_subject",
                "label": "Subject List",
                "headers": ["Subject ID", "Subject Name", "Course", "Units"],
            },
            "Subject Schedule": {
                "table": "tbl_subject_sched",
                "label": "Subject Schedule List",
                "headers": [
                    "Subject Sched Code",
                    "Subject Sched Name",
                    "Course",
                    "Teacher",
                    "Block",
                    "Room",
                    "Time",
                ],
            },
        }

    def setup_table_view(self, view, model):
        view.setModel(model)
        view.resizeColumnsToContents()
        view.resizeRowsToContents()
        view.setSortingEnabled(True)
        model.setSort(-1, Qt.AscendingOrder)
        model.select()
        view.setSelectionBehavior(view.SelectRows)
        view.setEditTriggers(view.NoEditTriggers)
        view.verticalHeader().setVisible(False)

    def update_view(self, tableView_view, combo_value, page_info_callback=None):
        config = self.view_config.get(combo_value)

        if not config:
            print(f"Warning: No view config found for {combo_value}")
            return None

        self.ui.label_view.setText(config["label"])

        model = QSqlTableModel(None, self.db)
        model.setTable(config["table"])
        model.select()

        for index, header in enumerate(config["headers"]):
            model.setHeaderData(index, Qt.Horizontal, header)

        self.setup_table_view(tableView_view, model)

        if page_info_callback and combo_value == "Student":
            tableView_view.doubleClicked.connect(page_info_callback)

        return model
