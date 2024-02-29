import requests
import io
from PIL import Image
import time
class T2Image:
    def __init__(self, hub_api_key, T2ImgModel = "stabilityai/stable-diffusion-xl-base-1.0"):
        self.hub_api_key = hub_api_key
        self.T2ImgModel = T2ImgModel
    
    def generateImage(self,prompt, download : bool = True, show : bool = True):
        """This function takes show and download as a boolean to show and download the image."""
        try:
            API_URL = f"https://api-inference.huggingface.co/models/{self.T2ImgModel}"
            headers = {"Authorization": f"Bearer {self.hub_api_key}"}
            payload = {"inputs": prompt}
            response = requests.post(API_URL, headers=headers, json=payload)
            imageBytes = response.content
            # print(imageBytes)
            # print("\n")
            if show and download:
                download_status = self.downloadImage(imageBytes)
                if not download_status:
                    return "Failed to download image."
                show_status = self.showImage(imageBytes)
                if not show_status:
                    return "Failed to display Image!"
                return "Image downloaded successfully!"
            elif show:
                show_status = self.showImage(imageBytes)
                if not show_status:
                    return "Failed to display Image!"
                return "Image generated successfullly!"
            else:
                status = self.downloadImage(imageBytes)
                if status:
                    return "Image download successfully!"
                else:
                    return "Failed to download image."
        except Exception as e:
            print(e)
            return f"Failed to generate image: {str(e)}"

    @staticmethod
    def showImage(image_bytes):
        try:
            image = Image.open(io.BytesIO(image_bytes))
            image.show()
            return True
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    def downloadImage(image_bytes):
        try:
            timestamp = time.strftime("%Y%m%d%H%M%S")
            new_filename = f"image_{timestamp}.png"
            with open(new_filename, 'wb') as f:
                f.write(image_bytes)
            return True
        except Exception as e:
            print(e)
            return False





