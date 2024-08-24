import React from 'react';
import {
  Panel,
  useReactFlow,
  getNodesBounds,
  getViewportForBounds,
} from '@xyflow/react';
import { toPng } from 'html-to-image';

function downloadImage(dataUrl) {
  const a = document.createElement('a');

  a.setAttribute('download', 'reactflow.png');
  a.setAttribute('href', dataUrl);
  a.click();
}

const imageWidth = 1200;
const imageHeight = 900;

function sendImageData(imageDataUrl) {
  const message = JSON.stringify({
    'action': 'store image',
    'img': imageDataUrl, // Adjust this if you need to include more data
  });

  window.parent.postMessage(message, 'http://127.0.0.1:8000/whiteboard/');
}

function DownloadButton() {
  const { getNodes } = useReactFlow();
  const onClick = () => {
    
    const nodesBounds = getNodesBounds(getNodes());
    const viewport = getViewportForBounds(
      nodesBounds,
      imageWidth,
      imageHeight,
      0.5,
      2,
    );

    toPng(document.querySelector('.react-flow__renderer'), {
      backgroundColor: '#F3F5F6',
      width: imageWidth,
      height: imageHeight,
      style: {
        width: imageWidth,
        height: imageHeight,
        transform: `translate(${viewport.x}px, ${viewport.y}px) scale(${viewport.zoom})`,
      },
    }).then(sendImageData);
  };

  return (
    <Panel position="top-left">
      <button id="download-img-btn" className="download-btn d-none" onClick={onClick}>
        Download Image
      </button>
    </Panel>
  );
}

export default DownloadButton;
