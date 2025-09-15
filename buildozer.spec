[app]
title = BloodDonationApp
package.name = blooddonation
package.domain = org.blooddonation
source.dir = .
source.include_exts = py,kv,db,csv
version = 1.0
requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer,sqlite3
orientation = portrait
fullscreen = 0

# Icon + Presplash (optional)
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

[app:source.exclude_patterns]
*.spec
*.git*
*.pyc
__pycache__

[android]
# Permissions (Location + Call + Internet)
android.permissions = INTERNET, ACCESS_FINE_LOCATION, CALL_PHONE, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Minimum & Target SDK
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
