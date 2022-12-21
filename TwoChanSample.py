import os
# Remember to set out_channels in script

MODEL_NAME = "TwoChan_Exp_1"

if __name__ == "__main__":
    MODEL_FLAGS="--in_channels 2 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 4 --learn_sigma True"
    DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine"
    OTHER=f"--batch_size 36 --num_samples 72 --model_path ./Checkpoints/Checkpoint_{MODEL_NAME}/ema_0.9999_150000.pt --sample_dir Samples/Two-Channel-160K"
    
    CALL=f"python image_sample.py  {MODEL_FLAGS} {DIFFUSION_FLAGS} {OTHER}"
    
    os.system(CALL)