EPOCHS = 100
SAVE_EVERY = 1 # after how many epochs to save a checkpoint
LOG_EVERY = 1 # log training and validation metrics every `LOG_EVERY` epochs
BATCH_SIZE = 2
DEVICE = 'cuda'
LR = 0.0001
ROOT_PATH = 'code/data'

# the classes that we want to train
CLASSES_TO_TRAIN = ['bg', 'wet_road_region', 'road_region', 'mud', 'earthen_patch', 'mountain-stones', 'dirt', 'vegitation_misc', 'distressed_patch', 'drainage_grate', 'water_puddle', 'speed_breaker', 'misc', 'gravel_patch', 'concrete_material']

# DEBUG for visualizations
DEBUG = False
