CREATE TABLE IF NOT EXISTS tbl_block (
    block_id TEXT PRIMARY KEY UNIQUE,
    block_name TEXT NOT NULL,
    course_id TEXT NOT NULL,
    department_id TEXT NOT NULL,
    year_level TEXT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES tbl_course(course_id),
    FOREIGN KEY (department_id) REFERENCES tbl_department(department_id)
);

CREATE TABLE IF NOT EXISTS tbl_course (
    course_id TEXT PRIMARY KEY UNIQUE,
    course_name TEXT NOT NULL,
    department_id TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES tbl_department(department_id)
);

CREATE TABLE IF NOT EXISTS tbl_department (
    department_id TEXT PRIMARY KEY UNIQUE,
    department_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tbl_enrollment (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT NOT NULL,
    sched_id INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES tbl_student(student_id),
    FOREIGN KEY (sched_id) REFERENCES tbl_subject_sched(sched_id)
);

CREATE TABLE IF NOT EXISTS tbl_room (
    room_id TEXT PRIMARY KEY UNIQUE,
    room_name TEXT NOT NULL,
    building TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tbl_room_sched (
    room_avail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_avail_name TEXT NOT NULL UNIQUE,
    room_id TEXT NOT NULL,
    day_available TEXT NOT NULL,
    time_start TEXT NOT NULL,
    time_end TEXT NOT NULL,
    is_available INTEGER NOT NULL,
    FOREIGN KEY (room_id) REFERENCES tbl_room(room_id)
);

CREATE TABLE IF NOT EXISTS tbl_student (
    student_id INTEGER PRIMARY KEY UNIQUE,
    student_name TEXT NOT NULL,
    course_id INTEGER NOT NULL,
    year_level TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES tbl_course(course_id)
);

CREATE TABLE IF NOT EXISTS tbl_subject (
    subject_code TEXT PRIMARY KEY UNIQUE,
    subject_name TEXT NOT NULL,
    course_id INT NOT NULL,
    units INTEGER NOT NULL,
    year_level TEXT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES tbl_course(course_id)
);

CREATE TABLE IF NOT EXISTS tbl_subject_sched (
    sched_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sched_name TEXT NOT NULL UNIQUE,
    subject_code TEXT NOT NULL,
    teacher_id TEXT NOT NULL,
    block_id TEXT NOT NULL,
    room_avail_id INTEGER NOT NULL,
    year_level TEXT NOT NULL,
    FOREIGN KEY (subject_code) REFERENCES tbl_subject(subject_code),
    FOREIGN KEY (teacher_id) REFERENCES tbl_teacher(teacher_id),
    FOREIGN KEY (block_id) REFERENCES tbl_block(block_id),
    FOREIGN KEY (room_avail_id) REFERENCES tbl_room_sched(room_avail_id)
);

CREATE TABLE IF NOT EXISTS tbl_teacher (
    teacher_id INTEGER PRIMARY KEY UNIQUE,
    teacher_name TEXT NOT NULL,
    department_id TEXT NOT NULL,
    FOREIGN KEY (department_id) REFERENCES tbl_department(department_id)
);
