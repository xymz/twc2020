"""
Scenario 1: Constant speed, one road, vbr
"""

env_params = {'road_distances': [200],
              'acc_std': 0,
              'speed_bound': [15, 15],
              'num_seg': 15,
              'seg_TF': 10,
              'vbr_mean': 8,
              'vbr_std': 0.3,
              'vbr_max': 15,
              'bandwidth': 20,
              'cell_radius': 250,
              'Nt': 3,
              'delta_T': 1,
              'power': 46,
              'noise': -95,
              'max_rate': 160,
              'playback_start': 0,
              'stop_pos': 0,
              'stop_time_range': [0, 0]
              }

