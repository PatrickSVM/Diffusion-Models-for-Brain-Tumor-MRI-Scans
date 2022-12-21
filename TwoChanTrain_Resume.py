import os

MODEL_NAME = "TwoChan_Exp_1"

if __name__ == "__main__":
    MODEL_FLAGS="--in_channels 2 --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 4 --learn_sigma True"
    DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine"
    TRAIN_FLAGS="--lr 1e-5 --batch_size 6"
    #Smaller LR, maybe next res_blocks 3
    CALL=f"python image_train.py --log_interval 10 --save_interval 10000 --resume_checkpoint Checkpoints/Checkpoint_TwoChan_Exp_1/model030000.pt --out_dir Checkpoints/Checkpoint_{MODEL_NAME} {MODEL_FLAGS} {DIFFUSION_FLAGS} {TRAIN_FLAGS}"
    
    os.system(CALL)