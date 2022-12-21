import os

# Remember to set out_channels in script

MODEL_NAME = "TwoChan_Exp_1"
SAMPLE_STEPS = ["010000", "020000", "030000"]
MODEL_TYPES = ["ema_0.9999_", "model"]

MODEL_FLAGS="--in_channels 2 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 4 --learn_sigma True"
DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine"

if __name__ == "__main__":
    # Sample for each specified step and model 
    for step in SAMPLE_STEPS:
        for model in MODEL_TYPES:
            path = f"./Checkpoints/Checkpoint_{MODEL_NAME}/{model}{step}.pt"
            OTHER=f"--batch_size 36 --num_samples 36  --timestep_respacing 250 --model_path {path} --sample_dir Samples/{MODEL_NAME}/{model}{step}"

            CALL=f"python image_sample.py  {MODEL_FLAGS} {DIFFUSION_FLAGS} {OTHER}"
    
            os.system(CALL)



# Check results with les timesteps with
# --timestep_respacing 250 or something 
# Also --use_ddim True