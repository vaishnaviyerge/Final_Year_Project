// expirationDateController.js
// import Tesseract from 'tesseract.js';

export const validateExpirationDate = async (req, res) => {
    try {
        const image = req.file.path;
        const { data: { text } } = await Tesseract.recognize(image, 'eng');
        const expiryMatch = text.match(/Expiry Date:\s*\d{2}\/\d{2}\/\d{4}/);
        res.json({ expiryDate: expiryMatch ? expiryMatch[0] : 'Not found' });
    } catch (error) {
        res.status(500).json({ error: 'Expiration date validation failed', details: error.message });
    }
};