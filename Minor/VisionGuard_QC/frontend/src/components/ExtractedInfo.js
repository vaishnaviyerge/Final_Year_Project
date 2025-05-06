// frontend/src/components/ExtractedInfo.js
import React from 'react';

function ExtractedInfo({ extractedData }) {
  return (
    <div className="extracted-info">
      <h3>Extracted Information</h3>
      <div>
        <strong>Image Text:</strong>
        <p>{extractedData.imageText || "No text extracted yet."}</p>
      </div>
      <div>
        <strong>Scanner Info:</strong>
        <p>{extractedData.scannerInfo || "No scanner information yet."}</p>
      </div>
    </div>
  );
}

export default ExtractedInfo;
