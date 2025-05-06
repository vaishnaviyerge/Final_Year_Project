import cors from 'cors';
import express from 'express';
import mongoose from 'mongoose';
import multer from 'multer';
import { MONGO_URI, PORT } from './config.js';
import { detectObjects } from './controllers/objectDetectionController.js';

const app = express();

// Increase payload size limit
app.use(express.json({ limit: '50mb' }));
app.use(express.urlencoded({ limit: '50mb', extended: true }));
app.use(cors());

// MongoDB connection
mongoose.connect(MONGO_URI)
  .then(() => console.log("Connected to MongoDB"))
  .catch(err => console.error("MongoDB connection error:", err));

// Multer configuration for file uploads
const storage = multer.memoryStorage();
const upload = multer({ 
  storage,
  limits: {
    fileSize: 50 * 1024 * 1024 // 50MB limit
  }
});

// Object detection route
app.post('/api/scan-object', upload.single('image'), detectObjects);

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});