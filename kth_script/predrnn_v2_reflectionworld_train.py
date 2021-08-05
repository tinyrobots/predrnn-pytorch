CUDA_VISIBLE_DEVICES = ['MIG-GPU-dd12daeb-e2f9-bc44-a07b-f48afac87bdf/7/0']

# tse jfds jlka dlKA: 
from subprocess import call

call(['python', '../run_predrnn.py',\
'--is_training', '0',\
'--device', 'cuda:0',\
'--dataset_name', 'ref',\
'--train_data_paths', '../../data/stopping2k/mini',\
'--valid_data_paths', '../../data/stopping2k/mini',\
'--save_dir', '../../outputs_and_trained_networks/reflectionworld_test_20210805',\
'--gen_frm_dir', '../../outputs_and_trained_networks/reflectionworld_test_20210805',\
'--input_length', '5',\
'--total_length', '10',\
'--img_width', '128',\
'--img_channel', '1',\
'--model_name', 'predrnn',\
'--pretrained_model', '../../outputs_and_trained_networks/reflectionworld_test_20210805/model.ckpt-8',\
'--num_hidden', '128,128',\
'--filter_size', '5',\
'--stride', '1',\
'--patch_size', '4',\
'--layer_norm', '1',\
'--decouple_beta', '0.01',\
'--reverse_scheduled_sampling', '1',\
'--r_sampling_step_1', '1000',\
'--r_sampling_step_2', '5000',\
'--r_exp_alpha', '2000',\
'--scheduled_sampling', '0',\
'--sampling_stop_iter', '50000',\
'--sampling_start_value', '1.0',\
'--sampling_changing_rate', '0.00002',\
'--lr', '0.001',\
'--reverse_input', '1',\
'--batch_size', '4',\
'--max_iterations', '8',\
'--display_interval', '1',\
'--test_interval', '8',\
'--snapshot_interval', '8',\
'--num_save_samples', '2',\
'--n_gpu', '1',\
'--visual','0',\
'--visual_path','../../outputs_and_trained_networks/'])
