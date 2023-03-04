@echo off
set inPath=input
set outPath=output

for /f %%f in ('dir /b "%inPath%\"') do (
	echo wheel2rpm.py %inPath%\%%f %outPath%\%%~nf.csv
	python wheel2rpm.py %inPath%\%%f %outPath%\%%~nf.csv
)

@pause