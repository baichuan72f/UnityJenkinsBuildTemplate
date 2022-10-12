:: 此处执行Unity打包
"C:\Program Files\Unity\Hub\Editor\2021.3.4f1\Editor\Unity.exe" ^
-quit ^
-batchmode ^
-projectPath %1 ^
-executeMethod BuildTools.BuildApk ^
-logFile %1\output.log ^
--productName:%2 ^
--version:%3
