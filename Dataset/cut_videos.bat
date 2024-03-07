@echo off
set IN_DATA_DIR=./videos
set OUT_DATA_DIR=./video_crop
ffmpeg -ss 0 -t 36 -y -i "%IN_DATA_DIR%/1.mp4" "%OUT_DATA_DIR%/1.mp4"
ffmpeg -ss 1240 -t 36 -y -i "%IN_DATA_DIR%/1.mp4" "%OUT_DATA_DIR%/2.mp4"

