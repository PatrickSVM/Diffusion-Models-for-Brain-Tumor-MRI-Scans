import os

if __name__ == "__main__":
    MODEL_FLAGS="--image_size 32 --num_channels 128 --num_res_blocks 3 --learn_sigma True --dropout 0.3"
    DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine --use_kl True"
    TRAIN_FLAGS="--lr 1e-4 --batch_size 128 --schedule_sampler loss-second-moment"

    os.system('python image_train.py --data_dir cifar_train $MODEL_FLAGS $DIFFUSION_FLAGS $TRAIN_FLAGS')

