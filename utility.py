import os
import datetime
from PIL import Image
from fpdf import FPDF

PATH_FOR_TEMP_IMAGES = f"{os.getcwd()}/Assets/Temp Images"
PATH_TO_SAVE_PDFS = f"{os.getcwd()}/Assets/Documents"

# Making sure all the required folders are there
if "Assets" not in os.listdir(os.getcwd()):
    print("Created Assets folder")
    os.mkdir(f"{os.getcwd()}/Assets")

if "Temp Images" not in os.listdir(f"{os.getcwd()}/Assets"):
    print("Created Assets/Temp Images folder")
    os.mkdir(f"{os.getcwd()}/Assets/Temp Images")

if "Documents" not in os.listdir(f"{os.getcwd()}/Assets"):
    print("Created Assets/Documents folder")
    os.mkdir(f"{os.getcwd()}/Assets/Documents")


class ImageManager:

    @staticmethod
    def clear_temp_folder():
        for img in os.listdir(PATH_FOR_TEMP_IMAGES):
            os.remove(f"{PATH_FOR_TEMP_IMAGES}/{img}")

    @staticmethod
    def _convert_to_png(image_path, output_path=PATH_FOR_TEMP_IMAGES):
        """
        Converts the given image in png format and resize the image to fit the page if required

        :param image_path: Path of the image to be converted
        :param output_path: Path where the output image is to be saved
        """
        try:
            image = Image.open(image_path)
        except FileNotFoundError:
            print("File not found")
        else:
            image_width, image_height = image.size
            max_width, max_height = (540, 785)

            # Resizing the images that are bigger than the maximum width or the maximum height,
            # maintaining the original aspect ratio of the images
            if image_width > max_width or image_height > max_height:
                image.thumbnail((max_width, max_height), Image.ANTIALIAS)

            image_name = image_path.split("/")[-1].split(".")[0]
            image.save(fp=f"{output_path}/{image_name}.png")

    def to_pdf(self, images: list, output_path=PATH_TO_SAVE_PDFS, filename=""):
        """
        Creates a PDF out of the given images.

        :param images: List of paths of all the images.
        :param output_path: Path where the output PDF is to be saved.
        :param filename: Filename of the output PDF
        """
        # Remove all the previous images in the image folder
        self.clear_temp_folder()

        for img in images:
            self._convert_to_png(img)

        final_images = [f"{os.getcwd()}/Assets/Temp Images/{image}" for image in os.listdir(PATH_FOR_TEMP_IMAGES)]

        # Create PDF of all the images
        pdf = FPDF()
        for image in final_images:
            pdf.add_page()
            pdf.image(image, x=10, y=10)

        if filename == "":
            today = datetime.datetime.now()
            filename = f"ProConverter_{today.strftime('%d_%b %H-%M-%S')}"
        pdf.output(f"{output_path}/{filename}.pdf", "F")
        print("PDF Created successfully")

        self.clear_temp_folder()


im_manager = ImageManager()
image_list = [f"Images/{image_name}" for image_name in os.listdir("Images")]
im_manager.to_pdf(image_list)
