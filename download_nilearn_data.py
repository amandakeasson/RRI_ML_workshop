
print('Importing nilearn')
from nilearn import datasets
import warnings
warnings.filterwarnings('ignore')

print('Downloading Haxby dataset')
datasets.fetch_haxby()

print('\nDone downloading nilearn data!\n\n')
print('See you at the workshop. :)\n\n')


