"""
/***************************************************************************
Name			 	 : generowanie punktow
Description          : Generuje losowe punkty na mapie
Date                 : 10/Sep/11 
copyright            : (C) 2011 by Malgorzata Baron
email                : ggosia6@mat.umk.pl 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "generowanie punktow" 
def description():
  return "Generuje losowe punkty na mapie"
def version(): 
  return "Version 0.1" 
def qgisMinimumVersion():
  return "1.0"
def classFactory(iface): 
  # load RandomPointCreator class from file RandomPointCreator
  from RandomPointCreator import RandomPointCreator 
  return RandomPointCreator(iface)
