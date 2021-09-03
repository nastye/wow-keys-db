SET SCRIPT_PATH=%~dp0
schtasks /Create /TN nastye-post-savedinstances /TR "%SCRIPT_PATH%post-savedinstances-noconsole.exe" /SC ONLOGON /F
schtasks /Run /TN nastye-post-savedinstances
pause