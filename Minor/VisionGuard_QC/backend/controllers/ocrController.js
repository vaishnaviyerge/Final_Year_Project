// controllers/ocrController.js
import Tesseract from 'tesseract.js';

export const extractTextFromImage = async (req, res) => {
  const image = req.file.buffer;

  try {
    const { data: { text } } = await Tesseract.recognize(image, 'eng');
    const mrpMatch = text.match(/MRP:\s*\d+/);
    const expiryMatch = text.match(/Expiry Date:\s*\d{2}\/\d{2}\/\d{4}/);

    res.json({
      text,
      mrp: mrpMatch ? mrpMatch[0] : 'Not found',
      expiryDate: expiryMatch ? expiryMatch[0] : 'Not found'
    });
  } catch (error) {
    res.status(500).json({ error: 'OCR failed', details: error.message });
  }
};
