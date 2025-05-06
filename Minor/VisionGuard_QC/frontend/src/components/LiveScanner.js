import React, { useRef, useState } from 'react';

function LiveScanner({ onExtractedInfo }) {
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const [scanning, setScanning] = useState(false);
  const [stream, setStream] = useState(null);

  const startVideo = async () => {
    try {
      const mediaStream = await navigator.mediaDevices.getUserMedia({ 
        video: { 
          width: 1280, 
          height: 720,
          facingMode: 'environment' 
        } 
      });
      
      videoRef.current.srcObject = mediaStream;
      videoRef.current.play();
      setStream(mediaStream);
      setScanning(true);
      onExtractedInfo('scannerInfo', 'Camera started. Point at an object to scan.');
    } catch (error) {
      console.error("Video error:", error);
      onExtractedInfo('scannerInfo', "Camera access denied or not available.");
    }
  };

  const stopVideo = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
    }
    setScanning(false);
    videoRef.current.srcObject = null;
    onExtractedInfo('scannerInfo', 'Camera stopped.');
  };

  const captureAndScan = async () => {
    if (!videoRef.current || !scanning) return;

    try {
      // Create canvas to capture frame
      const canvas = canvasRef.current;
      const video = videoRef.current;
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

      // Convert canvas to blob
      canvas.toBlob(async (blob) => {
        const formData = new FormData();
        formData.append('image', blob, 'capture.jpg');

        // Send to backend for detection
        const response = await fetch('http://localhost:5000/api/scan-object', {
          method: 'POST',
          body: formData
        });

        const data = await response.json();
        
        if (data.success) {
          const detectedItems = data.items.map(item => 
            `${item.item} (${item.confidence})`
          ).join(', ');
          
          onExtractedInfo('scannerInfo', 
            data.count > 0 
              ? `Detected: ${detectedItems}` 
              : 'No objects detected'
          );
        } else {
          onExtractedInfo('scannerInfo', 'Detection failed. Please try again.');
        }
      }, 'image/jpeg', 0.9);
    } catch (error) {
      console.error("Scanning error:", error);
      onExtractedInfo('scannerInfo', "Scanning failed. Please try again.");
    }
  };

  return (
    <div className="scanner-section">
      <h2>Live Object Scanner</h2>
      <video 
        ref={videoRef} 
        className="video" 
        playsInline 
        style={{ display: scanning ? 'block' : 'none' }}
      />
      <canvas ref={canvasRef} style={{ display: 'none' }} />
      
      <div className="scanner-buttons">
        {!scanning ? (
          <button onClick={startVideo}>Start Video</button>
        ) : (
          <>
            <button onClick={captureAndScan}>Scan Object</button>
            <button onClick={stopVideo}>Stop Video</button>
          </>
        )}
      </div>
    </div>
  );
}

export default LiveScanner;