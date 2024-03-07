@echo off
setlocal enabledelayedexpansion

set IN_DATA_DIR=./video_crop
set OUT_DATA_DIR=./frames

if not exist "%OUT_DATA_DIR%" (
  echo %OUT_DATA_DIR% doesn't exist. Creating it.
  mkdir "%OUT_DATA_DIR%"
)

for /r "%IN_DATA_DIR%" %%v in (*.mp4) do (
  set "video=%%v"
  set "video_name=%%~nv"

  echo !video_name!
  set "out_video_dir=%OUT_DATA_DIR%/!video_name!"

  if not exist "!out_video_dir!" (
    mkdir "!out_video_dir!"
  )

  set "out_name=!out_video_dir!/!video_name!_%%06d.jpg"

  ffmpeg -i "!video!" -r 30 -q:v 1 "!out_name!"
)

echo Done!
