from zero import Zero

# chatbot = Zero("John")

# chatbot.start()

from TextToImage import T2Image

image_gen = T2Image(hub_api_key="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")

image = image_gen.generateImage(prompt="Iron man fighting scene", show=True, download=False)

print(image)