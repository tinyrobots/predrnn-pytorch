# CUDA_VISIBLE_DEVICES=MIG-GPU-e9c58922-2429-6ed4-41de-46326e9f6156/3/0 (10Gb)

from subprocess import call

call(['python', '../run_predrnn.py',\
'--is_training', '0',\
'--device', 'cuda:0',\
'--dataset_name', 'reflectionworld',\
'--train_data_paths', '../../data/closer_sticky',\
'--valid_data_paths', '../../data/closer_sticky',\
'--save_dir', '../../outputs_and_trained_networks/generator6v4_9.5k_20211029',\
'--gen_frm_dir', '../../outputs_and_trained_networks/generator6v4_9.5k_20211029',\
'--input_length', '10',\
'--total_length', '21',\
'--img_width', '128',\
'--img_channel', '1',\
'--model_name', 'predrnn_memory_decoupling',\
'--pretrained_model', '../../outputs_and_trained_networks/generator6v4_9.5k_20211029/model.ckpt-120000',\
'--num_hidden', '128,128,128,128',\
'--filter_size', '3',\
'--stride', '1',\
'--patch_size', '4',\
'--layer_norm', '0',\
'--decouple_beta', '0.1',\
'--reverse_scheduled_sampling', '0',\
'--r_sampling_step_1', '20000',\
'--r_sampling_step_2', '30000',\
'--r_exp_alpha', '600',\
'--scheduled_sampling', '1',\
'--sampling_stop_iter', '30000',\
'--sampling_start_value', '1.0',\
'--sampling_changing_rate', '0.00002',\
'--lr', '0.0005',\
'--reverse_input', '1',\
'--batch_size', '1',\
'--max_iterations', '40001',\
'--display_interval', '10',\
'--test_interval', '5000',\
'--snapshot_interval', '5000',\
'--num_save_samples', '3',\
'--n_gpu', '1',\
'--visual','0',\
'--visual_path','../../outputs_and_trained_networks/',\
'--saving_latents', '0',\
'--latents_dir','/raid/kate/reflectionworld/saved_latents/generator6v4_9.5k_20211029/expt1_all_latents',\
'--layers_to_save', '1','2','3',\
'--types_to_save', 'H','C','M',])
