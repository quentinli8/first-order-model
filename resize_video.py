from argparse import ArgumentParser

import imageio
from skimage.transform import resize
from skimage import img_as_ubyte

def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("--video", required=True, help="source video filename")
    parser.add_argument("--output", default="resized_video.mp4", help="output video filename")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
    
    reader = imageio.get_reader(args.video)
    fps = reader.get_meta_data()['fps']
    input_video = []
    try:
        for im in reader:
            input_video.append(im)
    except RuntimeError:
        pass
    reader.close()

    resized_video = [resize(frame, (512, 384))[..., :3] for frame in input_video]
    imageio.mimsave(args.output, [img_as_ubyte(frame) for frame in resized_video], fps=fps)
