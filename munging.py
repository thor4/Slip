# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:15:09 2018

@author: bryan
"""

import scipy.io
import h5py
import numpy as np
import pandas as pd

#%reset clears variable workspace
%reset
#import no_touch data
no_touch = scipy.io.loadmat('No_Touch_2.mat')
no_slip_imped = np.vstack((no_touch['Electrodes_FF'],no_touch['Electrodes_LF']))
p_t_FF = np.hstack((no_touch['Pac0_FF'],no_touch['Pac1_FF'],no_touch['Pdc_FF'],\
                    no_touch['Tac_FF'],no_touch['Tdc_FF']))
p_t_LF = np.hstack((no_touch['Pac0_LF'],no_touch['Pac1_LF'],no_touch['Pdc_LF'],\
                    no_touch['Tac_LF'],no_touch['Tdc_LF']))
p_t = np.vstack((p_t_FF,p_t_LF))
no_slip = np.hstack((no_slip_imped,p_t))
 