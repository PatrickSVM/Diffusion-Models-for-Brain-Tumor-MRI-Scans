import os


MODEL_FLAGS="--in_channels 3 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False"

if __name__ == "__main__":
    # Sample for each specified step and model 
    path = f"./Checkpoints/LSUN_pretr/lsun_uncond_100M_1200K_bs128.pt"
    OTHER=f"--batch_size 42 --num_samples 252 --timestep_respacing 250 --model_path {path} --sample_dir Samples/LSUN"

    CALL=f"python image_sample.py  {MODEL_FLAGS} {DIFFUSION_FLAGS} {OTHER}"

    os.system(CALL)
