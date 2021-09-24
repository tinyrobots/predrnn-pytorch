import os
import pdb
import glob
import pandas as pd


data_dir = '../../data/second5k/rgb'
write_dir = '../../data/maintrain10k/categorised'
scene_file = '../../data/second5k/scene_log.csv'

start_id = 5000 # to allow starting writing at a higher number than original scene ID numbers

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
    if i%100 == 0: print('done {} matte scenes'.format(i))
    scene_id = matte_scenes.iloc[i]
    frame_list = glob.glob(os.path.join(data_dir,'rgb_{}*.png'.format(scene_id)))
    new_scene_id = 'scene'+str(int(scene_id[5:])+start_id).zfill(6)
    if not os.path.exists(os.path.join(write_dir,'matte/{}'.format(new_scene_id))):
        os.mkdir(os.path.join(write_dir,'matte/{}'.format(new_scene_id)))
    for f in frame_list:
        frame_name = f.split('/')[-1]
        os.rename(f, os.path.join(write_dir,'matte/{}/{}'.format(new_scene_id,frame_name)))

# same for all mirror scenes
for i in range(len(mirror_scenes)):
    if i %100 == 0: print('done {} mirror scenes'.format(i))
    scene_id = mirror_scenes.iloc[i]
    frame_list = glob.glob(os.path.join(data_dir,'rgb_{}*.png'.format(scene_id)))
    new_scene_id = 'scene'+str(int(scene_id[5:])+start_id).zfill(6)
    if not os.path.exists(os.path.join(write_dir,'mirror/{}'.format(new_scene_id))):
        os.mkdir(os.path.join(write_dir,'mirror/{}'.format(new_scene_id)))
    for f in frame_list:
        frame_name = f.split('/')[-1]
        os.rename(f, os.path.join(write_dir,'mirror/{}/{}'.format(new_scene_id,frame_name)))
