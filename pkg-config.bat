@echo off

setlocal

if "%1"=="--version" (
    echo 0.29.2
    exit /b 0
)

if "%1"=="--libs" (
    echo -L.	arget\native-deps\lib -lavutil -lavcodec -lavformat -lavdevice -lavfilter -lswscale -lswresample -lm -lpthread -lole32 -luuid
    exit /b 0
)

if "%1"=="--cflags" (
    echo -I.	arget\native-deps\include
    exit /b 0
)

echo Package not found
setlocal disabledelayedexpansion
exit /b 1