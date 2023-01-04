import os
import time

# Remember to set out_channels in script

MODEL_NAME = "TwoChan_Exp_3"
SAMPLE_STEPS = [f"0{i}0000" if i<10 else f"{i}0000" for i in range(6,7)]
MODEL_TYPES = ["ema_0.9999_", "model"]

MODEL_FLAGS="--in_channels 2 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False"

if __name__ == "__main__":
    # Sample for each specified step and model 
    for step in SAMPLE_STEPS:
        for model in MODEL_TYPES:
            path = f"./Checkpoints/Checkpoint_{MODEL_NAME}/{model}{step}.pt"
            OTHER=f"--batch_size 42 --num_samples 420 --timestep_respacing 250 --model_path {path} --sample_dir Samples/{MODEL_NAME}/{model}{step}"

            CALL=f"python image_sample.py  {MODEL_FLAGS} {DIFFUSION_FLAGS} {OTHER}"

            now = time.time()
            os.system(CALL)
            print(f"Sampling time: {time.time()-now:.2f} s for 420")
