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
"""
from PyQt4 import QtCore, QtGui 
from Ui_RandomPointCreator import Ui_RandomPointCreator
# create the dialog for RandomPointCreator
class RandomPointCreatorDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_RandomPointCreator ()
    self.ui.setupUi(self)