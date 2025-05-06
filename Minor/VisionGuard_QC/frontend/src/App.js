// frontend/src/App.js
import React, { useState } from 'react';
import ExtractedInfo from './components/ExtractedInfo';
import LiveScanner from './components/LiveScanner';
import UploadImage from './components/UploadImage';
import './styles.css';

function App() {
  const [extractedData, setExtractedData] = useState({});

  const handleExtractedInfo = (type, data) => {
    setExtractedData((prevData) => ({
      ...prevData,
      [type]: data
    }));
  };

  return (
    <div className="app-container">
      <h1>Product Information Extractor</h1>
      <div className="sections">
        <UploadImage onExtractedInfo={handleExtractedInfo} />
        <LiveScanner onExtractedInfo={handleExtractedInfo} />
      </div>
      <ExtractedInfo extractedData={extractedData} />
    </div>
  );
}

export default App;
