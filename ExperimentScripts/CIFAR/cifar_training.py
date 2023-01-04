import os

if __name__ == "__main__":
    MODEL_FLAGS="--image_size 32 --num_channels 128 --num_res_blocks 3 --learn_sigma True --dropout 0.3"
    DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine --use_kl True"
    TRAIN_FLAGS="--lr 1e-4 --batch_size 32 --schedule_sampler loss-second-moment"

    CALL=f'python image_train.py --log_interval 10 --save_interval 25000 --data_dir cifar_train --out_dir Muell {MODEL_FLAGS} {DIFFUSION_FLAGS} {TRAIN_FLAGS}'

    os.system(CALL)
