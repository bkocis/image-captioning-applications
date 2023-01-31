import os
import uvicorn
import logging

from fastapi import FastAPI, File, UploadFile

from inference import InferenceOnSingleImage

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

app = FastAPI(docs_url="/")


@app.post("/upload_image/")
async def image_file(image_file: UploadFile = File(...)):
    logging.info(image_file.file)
    try:
        os.mkdir("resources/image_file")

        logging.info(os.getcwd())
    except Exception as e:
        logging.info(e)

    file_path = os.path.join(os.getcwd(), "resources/image_file", image_file.filename.replace(" ", "-"))
    with open(file_path, 'wb+') as f:
        f.write(image_file.file.read())

    # result = ...

    output = {
        "filename": image_file.filename,
        # "predicted_caption": result
    }

    logging.info(f"Prediction for {image_file} ...done!")
    return output

if __name__ == "__main__":
    get_caption = InferenceOnSingleImage().caption_sentence()
    logging.info("The service is starting...")
    uvicorn.run(app, host="0.0.0.0", port=8080)
