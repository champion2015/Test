@echo off
echo =============Cocos2D-x新建项目==============
set /p name=输入项目的名称：
echo 项目名为： %name%
echo 正在创建新项目...
set pack=com.champion.
cocos new %name% -p %pack%%name% -l lua
echo 创建完成.
pause
