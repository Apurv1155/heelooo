[app]

# (str) Title of your application
title = FaceApp Attendance

# (str) Package name (MUST BE UNIQUE, e.g., com.yourname.yourapp)
package.name = com.yourcompany.faceapp

# (str) Package domain (needed for android/ios packaging)
package.domain = yourcompany.com

# (str) Application versioning (method 1)
version = 0.1

# (str) Kivy application main file
# IMPORTANT: This must match the name of your main Python file.
main.py = face_recognition.py

# (str) The directory where your source code is located
# '.' means the current directory (the root of your project)
source.dir = .

# (list) Source files to include (let empty to include all the files
# in the current directory)
# Ensure all your Python files, images, and audio files are listed or included by patterns.
source.include_exts = py,png,jpg,mp3,wav,kv,xml,json

# (list) Application requirements
# These packages will be installed by pip in the Android environment.
# 'cython' is crucial for Kivy and many Python extensions to compile for Android.
requirements = python3,kivy,opencv,numpy,requests,setuptools,pyjnius,android,certifi,cython

# (str) Kivy version to use
kivy.version = 2.3.0

# (str) Android API level to use (targetSdkVersion)
# Using a recent stable API level for better compatibility and security.
android.api = 33

# (str) Minimum Android API level required (minSdkVersion)
android.minapi = 21

# (str) Android target SDK version (same as android.api for consistency)
android.targetsdk = 33

# (list) Android architecture to build for
# Building for both common ARM architectures for broader device compatibility.
android.archs = arm64-v8a, armeabi-v7a

# (list) Android permissions
# INTERNET for Google Forms/email, CAMERA for webcam,
# READ/WRITE_EXTERNAL_STORAGE for broader compatibility (though user_data_dir is internal).
android.permissions = INTERNET, CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Icon file to use. This should be a .png file in your project root.
# Uncomment and specify if you have a custom icon (e.g., 'icon.png').
# icon.filename = %(source.dir)s/icon.png

# (str) A string that specifies the orientation of the screen.
orientation = portrait

# (int) The version number of your application.
# This is an integer value that is incremented with each release.
android.version_code = 1
