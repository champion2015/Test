@echo off
echo =============Cocos2D-x�½���Ŀ==============
set /p name=������Ŀ�����ƣ�
echo ��Ŀ��Ϊ�� %name%
echo ���ڴ�������Ŀ...
set pack=com.champion.
cocos new %name% -p %pack%%name% -l lua
echo �������.
pause
