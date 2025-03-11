🎓 Face Recognition Attendance System

A powerful and scalable Face Recognition-based Attendance System built with Python, OpenCV, and the Face Recognition library. This system automatically marks attendance by recognizing faces from a live camera feed, storing the data securely for future records and audits.

🚀 Key Features

✅ Real-time Face Detection & Recognition
✅ Automatic Attendance Logging with timestamp & date
✅ CSV-based Attendance Report (extendable to Firebase or other databases)
✅ Modular & Scalable Design — Easy to add new faces
✅ Error Handling for unknown faces
✅ Optimized for speed and accuracy using face_recognition and OpenCV

🏗 Tech Stack

Python 3.8+

OpenCV — For computer vision and video processing

face_recognition — High accuracy face detection and recognition

NumPy — For array operations

Pandas — To manage and store attendance data

Firebase (Optional) — For real-time attendance storage and dashboard (extendable)

Tkinter (Optional) — For GUI interface (future improvements)

📂 Project Structure

Face_recognition_attendance_system/  
│  
├── images/                # Folder containing known face images  
│    ├── Rounak.png        # Sample registered user image  
│  
├── main.py               # Main program to run the system  
├── attendance.csv        # Generated attendance record (Name, Time, Date)  
├── README.md             # Project documentation  
└── .gitignore            # Files/folders to ignore in git  

⚙ Installation & Setup

1. Clone the Repository
    
git clone https://github.com/Rounakdeepsingh/face_recognition_attendance_system.git  

cd face_recognition_attendance_system  

3. Install Dependencies
   
Ensure Python 3.8+ is installed. Then, install required packages:

pip install opencv-python face-recognition numpy pandas  

5. Add Images for Recognition
   
Place clear images of faces you want to recognize in the images/ folder.
Important: Name each image with the person's full name (e.g., John_Doe.png).

6. Run the Application
   
python main.py  

📊 Attendance Output Example

Name	Time	Date
Rounak	10:15:23	2025-03-11
John Doe	10:16:45	2025-03-11

Note: Attendance is automatically saved in attendance.csv.

☁️ Firebase Integration (Optional & Extendable)

Firebase can be used to store attendance data in real-time and display it on a web dashboard.

🔑 Setup Firebase:

Go to Firebase Console, create a project.

Enable Cloud Firestore in test mode.

Navigate to Project Settings > Service Accounts.

Generate a new private key and download the JSON file.

Rename the file to firebase_key.json and place it in the project root.


✅ Example Data in Firestore:

Collection: Attendance  
Document ID: Auto-generated  
Fields:  
- Name: "John Doe"  
- ID: "001"  
- Date: "2025-03-11"  
- Time: "09:30:00"  
- Status: "Present"
  

📦 Install Firebase Admin SDK (Optional):

pip install firebase-admin  


📲 Firebase Benefits:

Real-time attendance updates.

Access data from anywhere via web or mobile.

Secured and backed up storage.

Note: Contact for ready-to-use Firebase-integrated code!


💡 Future Improvements

✅ GUI Interface using Tkinter or PyQt

✅ Cloud-based Dashboard with Firebase/SQL backend

✅ Admin Panel to manage and analyze attendance

✅ Mobile App support for teachers and students

✅ Email & SMS alerts for absent students

✅ Performance optimization for large student datasets


📸 Screenshots (Optional)


⚙ Quick Setup Recap
# Clone repo  
git clone https://github.com/Rounakdeepsingh/face_recognition_attendance_system.git  

# Go to project  
cd face_recognition_attendance_system  

# Install dependencies  
pip install opencv-python face-recognition numpy pandas  

# Run the app  

python main.py  

👨‍💻 Contributing

Contributions are always welcome!
If you have suggestions, improvements, or bug reports, feel free to open an issue or submit a pull request.

📜 License

This project is licensed under the MIT License. See LICENSE for details.

🙏 Acknowledgments

Thanks to OpenAI, dlib, OpenCV, face_recognition library developers.
Inspired by open-source face recognition and attendance projects.


✅ Steps to Add This README to Your Repo

Create README.md in your project folder
Add and Commit the README:
git add README.md  
git commit -m "Added professional README with Firebase integration"  
git push origin main 
