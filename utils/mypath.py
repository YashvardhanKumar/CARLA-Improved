
import os


class MyPath(object):
    @staticmethod
    def db_root_dir(database=''):
        db_names = {'msl', 'smap', 'smd', 'power', 'yahoo', 'kpi', 'swat', 'wadi'}
        assert(database in db_names)

        if database == 'msl' or database == 'smap':
            return 'CARLA/datasets/MSL_SMAP'
        elif database == 'power':
            return 'CARLA/datasets/Power'
        elif database == 'yahoo':
            return 'CARLA/datasets/yahoo'
        elif database == 'smd':
            return 'CARLA/datasets/SMD'
        elif database == 'swat':
            return 'datasets/SWAT'
        elif database == 'wadi':
            return 'datasets/WADI'
        elif database == 'kpi':
            return 'datasets/KPI'
        
        else:
            raise NotImplementedError
