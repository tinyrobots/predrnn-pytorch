import os
import pdb
import glob
import pandas as pd


data_dir = '../../data/stopping2k/rgb'
write_dir = '../../data/stopping2k/mini'
scene_file = '../../data/stopping2k/scene_log.csv'

scene_df = pd.read_csv(scene_file)

matte_scenes = scene_df[scene_df['mat_condition']==0]['scene_num']
mirror_scenes = scene_df[scene_df['mat_condition']==1]['scene_num']

# set up main category directories
if not os.path.exists(os.path.join(write_dir,'matte')):
    os.mkdir(os.path.join(write_dir,'matte'))
if not os.path.exists(os.path.join(write_dir,'mirror')):
    os.mkdir(os.path.join(write_dir,'mirror'))

# move all matte scenes into their own folders
for i in range(len(matte_scenes)):
    scene_id = matte_scenes.iloc[i]
    frame_list = glob.glob(os.path.join(data_dir,'rgb_{}*.png'.format(scene_id)))
    if not os.path.exists(os.path.join(write_dir,'matte/{}'.format(scene_id))):
        os.mkdir(os.path.join(write_dir,'matte/{}'.format(scene_id)))
    # pdb.set_trace()
    for f in frame_list:
        frame_name = f.split('/')[-1]
        os.rename(f, os.path.join(write_dir,'matte/{}/{}'.format(scene_id,frame_name)))

# same for all mirror scenes
for i in range(len(mirror_scenes)):
    scene_id = mirror_scenes.iloc[i]
    frame_list = glob.glob(os.path.join(data_dir,'rgb_{}*.png'.format(scene_id)))
    if not os.path.exists(os.path.join(write_dir,'mirror/{}'.format(scene_id))):
        os.mkdir(os.path.join(write_dir,'mirror/{}'.format(scene_id)))
    # pdb.set_trace()
    for f in frame_list:
        frame_name = f.split('/')[-1]
        os.rename(f, os.path.join(write_dir,'mirror/{}/{}'.format(scene_id,frame_name)))
