# CUDA_VISIBLE_DEVICES=MIG-GPU-e9c58922-2429-6ed4-41de-46326e9f6156/3/0 (10Gb)

from subprocess import call

call(['python', '../run_predrnn.py',\
'--is_training', '1',\
'--device', 'cuda:0',\
'--dataset_name', 'reflectionworld',\
'--train_data_paths', '../../data/stopping2k/categorised',\
'--valid_data_paths', '../../data/stopping2k/categorised',\
'--save_dir', '../../outputs_and_trained_networks/stopping2k_20210812_input05',\
'--gen_frm_dir', '../../outputs_and_trained_networks/stopping2k_20210812_input05',\
'--input_length', '5',\
'--total_length', '20',\
'--img_width', '128',\
'--img_channel', '1',\
'--model_name', 'predrnn_memory_decoupling',\
'--pretrained_model', '',\
'--num_hidden', '128,128',\
'--filter_size', '5',\
'--stride', '1',\
'--patch_size', '4',\
'--layer_norm', '1',\
'--decouple_beta', '0.01',\
'--reverse_scheduled_sampling', '1',\
'--r_sampling_step_1', '3000',\
'--r_sampling_step_2', '6000',\
'--r_exp_alpha', '600',\
'--scheduled_sampling', '0',\
'--sampling_stop_iter', '50000',\
'--sampling_start_value', '1.0',\
'--sampling_changing_rate', '0.00002',\
'--lr', '0.001',\
'--reverse_input', '1',\
'--batch_size', '8',\
'--max_iterations', '10001',\
'--display_interval', '100',\
'--test_interval', '1000',\
'--snapshot_interval', '1000',\
'--num_save_samples', '5',\
'--n_gpu', '1',\
'--visual','0',\
'--visual_path','../../outputs_and_trained_networks/'])
