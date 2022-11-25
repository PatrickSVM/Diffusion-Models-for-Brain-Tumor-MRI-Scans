import numpy as np
from torch.utils.data import DataLoader, Dataset
from skimage import io
import torch
import os

#### Specify channels to include ####

CHANNELS = ["T1CE", "Seg"]
ROOT = './brats2020_313subjects_noaugmentation_singlesegmentationchannel_min15percentcoverage'


############## Custom data loader and DataSet class for the BRATS dataset ##############

class load_channels_from_dir(Dataset):
    """Load each channel from a different directory."""

    def __init__(self, channel_paths, transform=None, return_class=False):
        super().__init__()
        self.channel_paths = channel_paths # List with lists of full paths for each image-channel
        self.num_channel = len(channel_paths[0]) # Number of channels to include
        self.transform = transform
        self.return_class = return_class

    def __len__(self):
        return len(self.channel_paths)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        
        # Fetch all channels
        all_chan = [] # Store each channel tensor in list
        for c in range(self.num_channel):
            # Load image channel
            img_path = self.channel_paths[idx][c]
            img = io.imread(img_path) # Size: (256,256)

            # Normalize in PyTorch manner img/127.5 - 1 so range -1,1
            img = img/127.5 - 1
            
            # Transform to tensor and unsqueeze in first dim
            img = torch.Tensor(img)
            
            if len(img.shape)==4:
                img = img.unsqueeze(dim=0) # Remove redundant dimension, depending on Torch version

            all_chan.append(img)

        if len(all_chan)==1:
            # If only one channel, add dummy dimension 
            final_img = all_chan[0][None,:,:]
        else:
            # Create and return tensor of size (Channels, Size, Size) 
            final_img = torch.stack(all_chan)


        #if self.transform:
        #    sample = self.transform(sample)
        return final_img, {}



def get_BRATS_paths(channels_to_include, root=ROOT):

    channels =  ['FLAIR', 'Seg', 'T1', 'T1CE', 'T2']
    channel_paths = [os.path.join(root, channel_dir) for channel_dir in channels]

    channel_list = []
    if 'FLAIR' in channels_to_include:
        FLAIR = [os.path.join(channel_paths[0], path) for path in sorted(os.listdir(channel_paths[0])) if path.endswith(".png")]
        channel_list.append(FLAIR)
    
    if 'Seg' in channels_to_include:
        SEG = [os.path.join(channel_paths[1], path) for path in sorted(os.listdir(channel_paths[1])) if path.endswith(".png")]
        channel_list.append(SEG)

    if 'T1' in channels_to_include:
        T1 = [os.path.join(channel_paths[2], path) for path in sorted(os.listdir(channel_paths[2])) if path.endswith(".png")]
        channel_list.append(T1)

    if 'T1CE' in channels_to_include:
        T1CE = [os.path.join(channel_paths[3], path) for path in sorted(os.listdir(channel_paths[3])) if path.endswith(".png")]
        channel_list.append(T1CE)

    if 'T2' in channels_to_include:
        T2 = [os.path.join(channel_paths[4], path) for path in sorted(os.listdir(channel_paths[4])) if path.endswith(".png")]
        channel_list.append(T2)

    if len(channel_list)>1:
        ALL_CHANNELS = list(zip(*channel_list))
    else: # If only one channel
        ALL_CHANNELS = channel_list[0]
        ALL_CHANNELS = np.array(ALL_CHANNELS).reshape(-1,1) # Convert to (d,1)


    return ALL_CHANNELS




def load_data(*, batch_size, image_size, class_cond=False, deterministic=False, brats_channels=CHANNELS, **kwargs):
    
    all_paths = get_BRATS_paths(brats_channels)

    dataset = load_channels_from_dir(channel_paths=all_paths)

    if deterministic:
        loader = DataLoader(
            dataset, batch_size=batch_size, shuffle=False, num_workers=1, drop_last=True
        )
    else:
        loader = DataLoader(
            dataset, batch_size=batch_size, shuffle=True, num_workers=1, drop_last=True
        )
    while True:
        yield from loader



