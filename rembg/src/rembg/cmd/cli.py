import os
import sys
sys.path.append('./rembg/src/rembg')

import argparse
import glob
from tqdm import tqdm

from distutils.util import strtobool

try:
    from rembg.src.rembg.bg import remove
except:
    from bg import remove

class Removal():
    def main(input_path_, output_path_):

        model_path = os.environ.get(
            "U2NETP_PATH",
            os.path.expanduser(os.path.join("~", ".u2net")),
        )
        model_choices = [os.path.splitext(os.path.basename(x))[0] for x in set(glob.glob(model_path + "/*"))]
        if len(model_choices) == 0:
            model_choices = ["u2net", "u2netp", "u2net_human_seg"]

        ap = argparse.ArgumentParser()

        ap.add_argument(
            "-m",
            "--model",
            default="u2net",
            type=str,
            choices=model_choices,
            help="The model name.",
        )

        ap.add_argument(
            "-a",
            "--alpha-matting",
            nargs="?",
            const=True,
            default=False,
            type=lambda x: bool(strtobool(x)),
            help="When true use alpha matting cutout.",
        )

        ap.add_argument(
            "-af",
            "--alpha-matting-foreground-threshold",
            default=240,
            type=int,
            help="The trimap foreground threshold.",
        )

        ap.add_argument(
            "-ab",
            "--alpha-matting-background-threshold",
            default=10,
            type=int,
            help="The trimap background threshold.",
        )

        ap.add_argument(
            "-ae",
            "--alpha-matting-erode-size",
            default=10,
            type=int,
            help="Size of element used for the erosion.",
        )

        ap.add_argument(
            "-az",
            "--alpha-matting-base-size",
            default=1000,
            type=int,
            help="The image base size.",
        )

        ap.add_argument(
            "-input_p",
            "--input_path",
            default=input_path_,
            type=str,
            #nargs=2,
            help="An input folder and an output folder.",
        )

        ap.add_argument(
            "-output_p",
            "--output_path",
            default=output_path_,
            type=str,
            # nargs=2,
            help="An input folder and an output folder.",
        )

        args = ap.parse_args()

        included_extensions = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
        file_names = [fn for fn in os.listdir(args.input_path)
                      if any(fn.endswith(ext) for ext in included_extensions)]


        try:
            if not os.path.exists(output_path_):
                os.makedirs(output_path_)
        except OSError:
            print("Error: Failed to create the directory.")



        for paths in tqdm(file_names):
            remove(
                args.input_path,
                args.output_path,
                paths,
                model_name=args.model,
                alpha_matting=args.alpha_matting,
                alpha_matting_foreground_threshold=args.alpha_matting_foreground_threshold,
                alpha_matting_background_threshold=args.alpha_matting_background_threshold,
                alpha_matting_erode_structure_size=args.alpha_matting_erode_size,
                alpha_matting_base_size=args.alpha_matting_base_size)


if __name__ == '__main__':
    input_path_ = "C:\\Users\\ParkHyunyong\\PycharmProjects\\background_removal\\rembg\\src\\rembg\\cmd\\test\\"
    output_path_ = "./output/"
    Removal.main(input_path_, output_path_)
