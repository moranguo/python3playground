### Pycharm unresolved reference user define module
    1.点击菜单栏上的File -> Setting ->Build,Executing,Development ->Console -> Python Console
    2.将Add source roots to PYTHONPATH勾选上
    3.点击Apply, then restart Pycharm
    
### Pycharm unresolved reference third party module
    1.the pip install package is under os level python installed path
    2.File->Settings->Project:xxx->Project Interpreter
    3.Select the OS level python.exe
    
### change project setting under .idea
    1.Disable remember "Add file to Git" in workspace.xml
    <component name="ProjectLevelVcsManager" settingsEditedManually="true">
    <ConfirmationsSetting value="1" id="Add" />
    </component>