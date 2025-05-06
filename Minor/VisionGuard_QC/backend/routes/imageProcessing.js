// backend/routes/imageProcessing.js
import { Router } from 'express';
import multer from 'multer';

import { monitorBinPlacement } from '../controllers/binMonitoringController.js';
import { validateExpirationDate } from '../controllers/expirationDateController.js';
import { detectObjects } from '../controllers/objectDetectionController.js';
import { extractTextFromImage } from '../controllers/ocrController.js';
import { inspectPackaging } from '../controllers/packagingInspectionController.js';
import { inspectProduceQuality } from '../controllers/produceInspectionController.js';

const router = Router();
const upload = multer();

router.post('/ocr', upload.single('image'), extractTextFromImage);
router.post('/object-detection', upload.single('image'), detectObjects);
router.post('/packaging-inspection', upload.single('image'), inspectPackaging);
router.post('/expiration-date', upload.single('image'), validateExpirationDate);
router.post('/produce-inspection', upload.single('image'), inspectProduceQuality);
router.post('/bin-monitoring', upload.single('image'), monitorBinPlacement);

export default router;
