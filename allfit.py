# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 17:33:23 2023

@author: 11279
"""

line_break = '\n'#换行符，后面用于VBA代买的拼接用
a=8
class cell:
    def wcs(u,v,w):
        #移动坐标系  WCS.MoveWCS "local", "0.0", "s1+s4", "0.0"
        sCommand = 'WCS.MoveWCS "local", "%f", "%f", "%f"' % (u,v,w)
        return sCommand
        
    def inmodel (model_path):
        #导入模型
        sCommand = ['With STEP',
                    '.Reset ',
                    '.Healing "0" ',
                    '.ScaleToUnit "0" ',
                    '.FileName "%s" ' % model_path,
                    '.Id "1" ',
                    '.Version "11.0" ',
                    '.ImportToActiveCoordinateSystem "True" ',
                    '.Curves "True" ',
                    '.ImportAttributes "True" ',
                    '.ImportCurveAttributes "True" ',
                    '.Read ',
                    'End With']
        sCommand = line_break.join(sCommand)
        return sCommand
        
    def rename(cellnum):
        #重命名模型  Component.Rename "cell", "cell41"
        sCommand = 'Component.Rename "cell", "%s"' %cellnum
        return sCommand
        
    def move(model_name):    
        #移动模型
        sCommand = ['With Transform ',
                    '.Reset ',
                    '.Name "%s"' %model_name,
                    '.Vector "%f", "%f", "%f" ' % (a/2,a/2-a*4,0),
                    '.UsePickedPoints "False" ',
                    '.InvertPickedPoints "False" ',
                    '.MultipleObjects "False" ',
                    '.GroupObjects "False" ',
                    '.Repetitions "1" ',
                    '.MultipleSelection "False" ',
                    '.Transform "Shape", "Translate" ',
                    'End With']
        sCommand = line_break.join(sCommand)
        return sCommand
    
    def listname(cellname):
        #合并金属片、介质、金属片设置为pec
        #Solid.Add "cell13:circle1", "cell13:circle1_1"   
        names=[ 'Solid.Add "%s:circle1", "%s:circle1_1"'%(cellname,cellname),
                'Solid.Add "%s:circle1_10", "%s:circle1_11"'%(cellname,cellname),
                'Solid.Add "%s:circle1_12", "%s:circle1_13"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1", "%s:circle1_1_1_1"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_10", "%s:circle1_1_1_11"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_12", "%s:circle1_1_1_13"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_1", "%s:circle1_1_1_1_10"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_11", "%s:circle1_1_1_1_12"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_13", "%s:circle1_1_1_1_14"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_2", "%s:circle1_1_1_1_3"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_4", "%s:circle1_1_1_1_5"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_6", "%s:circle1_1_1_1_7"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_8", "%s:circle1_1_1_1_9"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_2", "%s:circle1_1_1_3"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_4", "%s:circle1_1_1_5"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_6", "%s:circle1_1_1_7"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_8", "%s:circle1_1_1_9"'%(cellname,cellname),
                'Solid.Add "%s:circle1_2", "%s:circle1_3"'%(cellname,cellname),
                'Solid.Add "%s:circle1_4", "%s:circle1_5"'%(cellname,cellname),
                'Solid.Add "%s:circle1_6", "%s:circle1_7"'%(cellname,cellname),
                'Solid.Add "%s:circle1_8", "%s:circle1_9"'%(cellname,cellname),
                'Solid.Add "%s:circle1", "%s:circle1_10"'%(cellname,cellname),
                'Solid.Add "%s:circle1_12", "%s:circle1_1_1"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_10", "%s:circle1_1_1_12"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_1", "%s:circle1_1_1_1_11"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_13", "%s:circle1_1_1_1_2"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_4", "%s:circle1_1_1_1_6"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_8", "%s:circle1_1_1_2"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_4", "%s:circle1_1_1_6"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_8", "%s:circle1_2"'%(cellname,cellname),
                'Solid.Add "%s:circle1_4", "%s:circle1_6"'%(cellname,cellname),
                'Solid.Add "%s:circle1_4", "%s:circle1_8"'%(cellname,cellname),
                'Solid.Add "%s:circle1", "%s:circle1_12"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_10", "%s:circle1_1_1_1_1"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_13", "%s:circle1_1_1_1_4"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_8", "%s:circle1_1_1_4"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_8", "%s:circle1_4"'%(cellname,cellname),
                'Solid.Add "%s:circle1", "%s:circle1_1_1_10"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_13", "%s:circle1_1_1_1_8"'%(cellname,cellname),
                'Solid.Add "%s:circle1_1_1_1_13", "%s:circle1_1_1_8"'%(cellname,cellname),
                'Solid.Add "%s:circle1", "%s:circle1_1_1_1_13"'%(cellname,cellname),
                
                'Solid.Add "%s:sub", "%s:sub_1_1"'%(cellname,cellname),
                'Solid.Add "%s:sub", "%s:sub_1_1_1"'%(cellname,cellname),
                
                'Solid.ChangeMaterial "%s:circle1", "PEC"'%cellname]
        return names