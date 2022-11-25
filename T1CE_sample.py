import os
# Remember to set out_channels in script
if __name__ == "__main__":
    MODEL_FLAGS="--in_channels 2 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16"
    DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False"
    OTHER="--batch_size 8 --num_samples 64 --model_path ./Checkpoint_T1CE_SEG/ema_0.9999_250000.pt --sample_dir Samples_T1CE_SEG_250K"
    
    CALL=f"python image_sample.py  {MODEL_FLAGS} {DIFFUSION_FLAGS} {OTHER}"
    
    os.system(CALL)