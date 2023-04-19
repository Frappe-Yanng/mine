# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
sys.path.append(
    r"D:\AppInstal\pro\cst\AMD64\python_cst_libraries")
import cst
import cst.interface

import allfit
s1=48.6
s2=56.2
s4=20
a=8
Project_path = r"C:\Users\11279\Desktop\python\rcs1.cst"
cst = cst.interface.DesignEnvironment()
mws = cst.open_project(Project_path)
modeler = mws.modeler

def onestep(sCommandwcs,model_path,model_name):
   #导入模型
    sCommandinmodel=allfit.cell.inmodel(model_path)
    modeler.add_to_history('define inmodel', sCommandinmodel)
    #重命名模型
    sCommandrename=allfit.cell.rename(model_name)
    modeler.add_to_history('define Component rename', sCommandrename)
    #移动模型
    sCommandmove=allfit.cell.move(model_name)
    modeler.add_to_history('define Transform Component', sCommandmove)
    #合并金属片、介质、金属片设置为pec
    names=allfit.cell.listname(model_name)
    for name in names:
        modeler.add_to_history('define Solid', name)
    #移动坐标系
    modeler.add_to_history('define Move WCS', sCommandwcs) 
    return



model_path = r"C:\Users\11279\Desktop\meta\model\4.stp"
model_name='cell4'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\1.stp"
model_name='cell1'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\11.stp"
model_name='cell11'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\13.stp"
model_name='cell13'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\4.stp"
model_name='cell41'
sCommandwcs=allfit.cell.wcs(s2,0,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\3.stp"
model_name='cell31'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\16.stp"
model_name='cell16'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\2.stp"
model_name='cell2'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\10.stp"
model_name='cell10'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\3.stp"
model_name='cell3'
sCommandwcs=allfit.cell.wcs(s2,0,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\12.stp"
model_name='cell12'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\6.stp"
model_name='cell6'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\14.stp"
model_name='cell14'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\5.stp"
model_name='cell5'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\12.stp"
model_name='cell121'
sCommandwcs=allfit.cell.wcs(s2,0,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\7.stp"
model_name='cell71'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\8.stp"
model_name='cell8'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\9.stp"
model_name='cell9'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\15.stp"
model_name='cell15'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\7.stp"
model_name='cell7'
sCommandwcs=allfit.cell.wcs(s2,0,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\4.stp"
model_name='cell42'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\1.stp"
model_name='cell1_1'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\11.stp"
model_name='cell111'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\13.stp"
model_name='cell131'
sCommandwcs=allfit.cell.wcs(0,s1+s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\4.stp"
model_name='cell43'
sCommandwcs=allfit.cell.wcs(s2,0,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\3.stp"
model_name='cell32'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\16.stp"
model_name='cell161'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\2.stp"
model_name='cell21'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\10.stp"
model_name='cell101'
sCommandwcs=allfit.cell.wcs(0,-s1-s4,0)
onestep(sCommandwcs,model_path,model_name)

model_path = r"C:\Users\11279\Desktop\meta\model\3.stp"
model_name='cell33'
#导入模型
sCommandinmodel=allfit.cell.inmodel(model_path)
modeler.add_to_history('define inmodel', sCommandinmodel)
#重命名模型
sCommandrename=allfit.cell.rename(model_name)
modeler.add_to_history('define Component rename', sCommandrename)
#移动模型
sCommandmove=allfit.cell.move(model_name)
modeler.add_to_history('define Transform Component', sCommandmove)
#合并金属片、介质、金属片设置为pec
names=allfit.cell.listname(model_name)
for name in names:
    modeler.add_to_history('define Solid', name)
   



