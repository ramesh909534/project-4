[app]
title = Blood Donation App
package.name = blooddonation
package.domain = org.blooddonation
source.dir = .
source.include_exts = py,kv,png,jpg,sqlite3,db,csv
version = 1.0
requirements = python3,kivy==2.2.1,kivymd==1.1.1,plyer,sqlite3
orientation = portrait
fullscreen = 0
android.api = 31
android.minapi = 21
android.ndk = 23b
android.gradle_dependencies = com.android.support:appcompat-v7:28.0.0
android.arch = armeabi-v7a, arm64-v8a
android.permissions = INTERNET,ACCESS_FINE_LOCATION,CALL_PHONE

[buildozer]
log_level = 2
warn_on_root = 1
