import os

if __name__ == "__main__":
    MODEL_FLAGS="--image_size 32 --num_channels 128 --num_res_blocks 3 --learn_sigma True --dropout 0.3"
    DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine --use_kl True"

    os.system('python image_sample.py --batch_size 128 --num_samples 128 --model_path ./Checkpoint_CIFAR/ema_0.9999_325000.pt --sample_dir Samples_CIFAR $MODEL_FLAGS $DIFFUSION_FLAGS ')

