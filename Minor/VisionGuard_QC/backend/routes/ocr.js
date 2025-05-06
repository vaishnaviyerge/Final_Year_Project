// backend/routes/ocr.js
import { Router } from 'express';
import multer from 'multer';
import Tesseract from 'tesseract.js';
const { recognize } = Tesseract;

const router = Router();

const upload = multer({ dest: 'uploads/' });

router.post('/extract-text', upload.single('image'), async (req, res) => {
  try {
    const { path } = req.file;
    recognize(path, 'eng')
      .then(({ data: { text } }) => {
        res.json({ text });
      })
      .catch((error) => {
        res.status(500).json({ error: 'OCR failed' });
      });
  } catch (error) {
    res.status(500).json({ error: 'File upload failed' });
  }
});

export default router;
