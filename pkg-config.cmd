@echo off

REM Simple pkg-config implementation for Windows
REM This script provides pkg-config functionality for FFmpeg libraries

if "%1"=="--version" (
    echo 0.29.2
    exit /b 0
)

if "%1"=="--libs" (
    echo -L./target/native-deps/lib -lavutil -lavcodec -lavformat -lavdevice -lavfilter -lswscale -lswresample -lm -lpthread -lole32 -luuid
    exit /b 0
)

if "%1"=="--cflags" (
    echo -I./target/native-deps/include
    exit /b 0
)

echo Package libavutil libavcodec libavformat libavdevice libavfilter libswscale libswresample was not found in the pkg-config search path.
exit /b 1