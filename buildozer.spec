[app]

# (str) Title of your application
title = Blood Donation App

# (str) Package name
package.name = blooddonation

# (str) Package domain (must be unique)
package.domain = org.example

# (str) Source code where main.py is located
source.dir = .

# (str) Main .py file
source.main = main.py

# (str) Version
version = 0.1

# (list) Application requirements
# kivy 2.2.1 → stable
# kivymd → for UI
# requests → API calls (future)
# plyer → GPS/Call
requirements = python3,kivy==2.2.1,kivymd,requests,plyer

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CALL_PHONE

# (int) Target API
android.api = 31

# (int) Minimum API
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 31

# (int) Android NDK version to use
android.ndk = 21b

# (str) Android NDK directory (optional, usually auto)
# android.ndk_path =

# (str) Application icon
icon.filename = %(source.dir)s/icon.png

# (str) Presplash of the application
presplash.filename = %(source.dir)s/presplash.png

# (str) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (bool) Enable Android logcat
log_level = 2

# (str) Custom source folders for requirements
# (default: empty)
# requirements.source =

[buildozer]

# (str) Log level (0 = quiet, 2 = normal, 1 = debug)
log_level = 2

# (bool) Build the application in debug mode
debug = 1

# (str) Path to the Android SDK
# (auto detected by GitHub Actions)

# (str) Path to the Android NDK
# (auto detected by GitHub Actions)

# (str) Path to Android command line tools
# (auto detected by GitHub Actions)

# (bool) Use the latest build tools
android.accept_sdk_license = True
