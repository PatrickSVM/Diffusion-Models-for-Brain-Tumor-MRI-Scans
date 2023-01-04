import os

if __name__ == "__main__":
    MODEL_FLAGS="--in_channels 2 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16"
    DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False"
    TRAIN_FLAGS="--lr 1e-4 --batch_size 6"
    # Changed lr to smaller lr 
    CALL=f"python image_train.py --log_interval 10 --save_interval 10000 --out_dir Checkpoints/Checkpoint_T1CE_SEG_BigBatch {MODEL_FLAGS} {DIFFUSION_FLAGS} {TRAIN_FLAGS}"
    
    os.system(CALL)