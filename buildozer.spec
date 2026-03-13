[app]
# (str) Title of your application
title = Myanmar YT Subtitler

# (str) Package name
package.name = myanmarytsub

# (str) Package domain (needed for android packaging)
package.domain = org.knowverse

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let's include fonts and images)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# yt-dlp နဲ့ youtube-transcript-api က APK ထုတ်ရင် error တက်တတ်လို့ အသေချာဆုံး version တွေ ထည့်ထားပါတယ်
requirements = python3,kivy==2.2.1,kivymd,yt-dlp,youtube-transcript_api,requests,certifi,urllib3

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK directory (leave empty to use default)
# android.sdk = 

# (list) Architecture to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
