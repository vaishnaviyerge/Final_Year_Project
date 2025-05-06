// import * as cocoSsd from '@tensorflow-models/coco-ssd';
// import * as tf from '@tensorflow/tfjs-node';
// // import sharp from 'sharp';

export const detectObjects = async (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No image file provided' });
    }

    // Convert image buffer to format suitable for TensorFlow
    const processedImage = await sharp(req.file.buffer)
      .resize(800) // Resize for better performance
      .toFormat('jpeg')
      .toBuffer();

    // Decode image using tf.node
    const imageTensor = tf.node.decodeImage(processedImage, 3);

    // Load model and detect objects
    const model = await cocoSsd.load();
    const predictions = await model.detect(imageTensor);

    // Format response
    const items = predictions.map(pred => ({
      item: pred.class,
      confidence: (pred.score * 100).toFixed(2) + '%',
      boundingBox: pred.bbox
    }));

    res.json({ 
      success: true,
      items,
      count: items.length,
      message: items.length > 0 ? 'Objects detected successfully' : 'No objects detected'
    });
  } catch (error) {
    console.error('Object detection error:', error);
    res.status(500).json({ 
      success: false,
      error: 'Object detection failed',
      details: error.message 
    });
  }
};