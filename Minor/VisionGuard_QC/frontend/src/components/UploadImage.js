// frontend/src/components/UploadImage.js
import React, { useState } from 'react';
import Tesseract from 'tesseract.js';

function UploadImage({ onExtractedInfo }) {
  const [image, setImage] = useState(null);

  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
      Tesseract.recognize(file, 'eng')
        .then(({ data: { text } }) => {
          onExtractedInfo('imageText', text);
        })
        .catch((error) => {
          console.error("OCR error:", error);
          onExtractedInfo('imageText', "Failed to extract text.");
        });
    }
  };

  return (
    <div className="upload-section">
      <h2>Upload Image</h2>
      <input type="file" onChange={handleImageUpload} />
      <button onClick={handleImageUpload}>Extract Text</button>
      {image && <img src={image} alt="Uploaded" className="uploaded-image" />}
    </div>
  );
}

export default UploadImage;
