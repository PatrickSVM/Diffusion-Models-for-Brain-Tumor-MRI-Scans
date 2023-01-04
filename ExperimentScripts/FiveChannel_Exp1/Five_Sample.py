import os
import numpy as np
# Remember to set out_channels in script

MODEL_NAME = "FiveChan_Exp_1"
SAMPLE_STEPS = [f"0{i}000" for i in np.arange(10, 35, 5)]
MODEL_TYPES = ["ema_0.9999_", "model"]

MODEL_FLAGS="--in_channels 5 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 1  --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False"

if __name__ == "__main__":
    # Sample for each specified step and model 
    for step in SAMPLE_STEPS:
        for model in MODEL_TYPES:
            path = f"./Checkpoints/Checkpoint_{MODEL_NAME}/{model}{step}.pt"
            OTHER=f"--batch_size 42 --num_samples 84 --timestep_respacing 250 --model_path {path} --sample_dir Samples/{MODEL_NAME}/{model}{step}"

            CALL=f"python image_sample.py  {MODEL_FLAGS} {DIFFUSION_FLAGS} {OTHER}"
    
            os.system(CALL)