[app]
title = Blood Donation App
package.name = blooddonation
package.domain = org.bloodapp
source.dir = .
source.include_exts = py, kv, csv, db
version = 1.0

# Main file
main.py = main.py

# Requirements
requirements = python3, kivy==2.2.1, kivymd==1.1.1, plyer, sqlite3

# Orientation
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET, ACCESS_FINE_LOCATION, CALL_PHONE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Icon (optional - uncomment if you have one)
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]
# Android SDK/NDK settings
android.minapi = 21
android.sdk = 33
android.ndk = 25b
