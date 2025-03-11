import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-6b860-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendancerealtime-6b860.appspot.com"
})

ref = db.reference('Students')

data = {
    "VH12401":
        {
            "name": "Georgia",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "VH12402":
        {
            "name": "Modi",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "VH12403":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "VH12426":
        {
            "name": "Sukesh S T",
            "major": "Computer Science",
            "starting_year": 2022,
            "total_attendance": 10,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "VH12404":
        {
            "name": "Rounak",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 10,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-11-19 00:54:34"
        },
    "VH12437":
        {
            "name": "Thiso",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 10,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-11-19 00:54:34"
        },
    "VH12409":
        {
            "name": "SARAN MS",
            "major": "CSE",
            "starting_year": 2022,
            "total_attendance": 10,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-11-19 00:00:00"
        }

}

for key, value in data.items():
    ref.child(key).set(value)