import argparse, os, errno
from pathlib import Path
from PIL import Image, ImageDraw

# ---------------------------------------------------------
# Handle command line arguments
# ---------------------------------------------------------

description = 'Draws a black box over the legal print at the bottom of a set of Magic card images.'

parser = argparse.ArgumentParser(description=description)

# Arguments
parser.add_argument('inputPath', type=str, help='The path to the input directory containing Magic card images.')
parser.add_argument('-o', '--output', type=str, default=None, help='The output directory. Defaults to <inputPath>/removed_legal')
parser.add_argument('-r', '--recursive', action='store_true', help='Include all image files in subdirectories of <inputPath>')

args = parser.parse_args()
input_dir = getattr(args, 'inputPath').replace('\'', '').replace('"', '')
output_dir = getattr(args, 'output') if getattr(args, 'output') is not None else Path(input_dir, 'removed_legal').resolve()
recursive = getattr(args, 'recursive')

# ---------------------------------------------------------
# Get files and paths
# ---------------------------------------------------------

glob_match = '**/*' if recursive else '*'

image_types = {".jpg", ".JPG", ".png", ".PNG"}
flag = not Path(output_dir).is_relative_to(Path(input_dir))

# Restrict file matches to the desired image formats and exclude the output directory
files = (p.resolve() for p in Path(input_dir).glob(glob_match) if (flag or not p.resolve().is_relative_to(Path(output_dir))) and p.suffix in image_types)

try:
    os.mkdir(output_dir)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# ---------------------------------------------------------
# Process all images
# ---------------------------------------------------------

files_count = 0

for file in files:
    with Image.open(file) as im:

        out_file = Path(output_dir, Path(file).name)

        print(f'Editing "{out_file.name}"', end='\r')

        draw = ImageDraw.Draw(im)

        # Points start top left going clockwise
        draw.polygon([
            (961, 2033),
            (1470, 2033),
            (1470, 2094),
            (1220, 2094),
            (1220, 2057),
            (961, 2057)],
            fill=(0, 0, 0),
            # outline=(255,0,0)
        )
        
        im.save(out_file)

        files_count += 1

if files_count == 0:
    print(f'There are no .jpg or .png files in directory: "{input_dir}"')
    exit(1)
else:
    print(f'Process complete. Edited {files_count} images.')
    exit(0)
