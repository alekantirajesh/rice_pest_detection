import React, { useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { predictImage } from '../api';

export default function Capture() {
  const navigate = useNavigate();
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const fileInputRef = useRef(null);
  
  const [isCameraActive, setIsCameraActive] = useState(false);
  const [uploadedImage, setUploadedImage] = useState(null);
  const [loading, setLoading] = useState(false);

  // Start camera
  const startCamera = async () => {
    try {
      setIsCameraActive(true);
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'environment' }
      });
      // Wait for video ref to be available
      setTimeout(() => {
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      }, 100);
    } catch (err) {
      setIsCameraActive(false);
      alert('Cannot access camera: ' + err.message);
    }
  };

  // Stop camera
  const stopCamera = () => {
    if (videoRef.current && videoRef.current.srcObject) {
      videoRef.current.srcObject.getTracks().forEach(track => track.stop());
      setIsCameraActive(false);
    }
  };

  // Capture photo from camera
  const capturePhoto = () => {
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    context.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
    
    canvas.toBlob(blob => {
      const file = new File([blob], 'captured.jpg', { type: 'image/jpeg' });
      stopCamera(); // Disable camera after capture
      handleImageSubmit(file);
    });
  };

  // Handle file upload
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        setUploadedImage(event.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  // Upload image
  const uploadImage = () => {
    const file = fileInputRef.current.files[0];
    if (file) {
      handleImageSubmit(file);
    }
  };

  // Submit image to backend
  const handleImageSubmit = async (imageFile) => {
    setLoading(true);
    try {
      // Convert image to base64 for display
      const reader = new FileReader();
      reader.onload = async (event) => {
        const imageBase64 = event.target.result;
        
        // Get prediction from backend
        const result = await predictImage(imageFile);
        
        // Navigate to result with both prediction and image
        navigate('/result', { 
          state: { 
            result, 
            imageName: imageFile.name,
            imageData: imageBase64
          } 
        });
      };
      reader.readAsDataURL(imageFile);
    } catch (error) {
      alert('Error: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="capture">
      <h2 style={{ marginBottom: '2rem', fontSize: '2rem' }}>📸 Capture or Upload</h2>
      
      <div className="capture-container">
        {/* Camera Section */}
        <div className="camera-section">
          <h3 className="section-title">Camera Capture</h3>
          
          <div className="camera-preview">
            {isCameraActive ? (
              <>
                <video
                  ref={videoRef}
                  autoPlay
                  playsInline
                  style={{ width: '100%', height: '100%', objectFit: 'cover' }}
                />
                <canvas
                  ref={canvasRef}
                  width={640}
                  height={480}
                  style={{ display: 'none' }}
                />
              </>
            ) : (
              <p className="camera-placeholder">Camera preview will appear here</p>
            )}
          </div>

          <div className="button-group">
            {!isCameraActive ? (
              <button className="btn btn-primary" onClick={startCamera} disabled={loading}>
                📹 Start Camera
              </button>
            ) : (
              <>
                <button className="btn btn-primary" onClick={capturePhoto} disabled={loading}>
                  {loading ? '⏳ Scanning...' : '📸 Capture Photo'}
                </button>
                <button className="btn btn-secondary" onClick={stopCamera}>
                  ❌ Stop Camera
                </button>
              </>
            )}
          </div>
        </div>

        {/* Upload Section */}
        <div className="upload-section">
          <h3 className="section-title">Upload Image</h3>
          
          <div 
            className="upload-box"
            onClick={() => fileInputRef.current.click()}
          >
            <p style={{ fontSize: '3rem', margin: '1rem 0' }}>📤</p>
            <p style={{ fontWeight: '600' }}>Click to upload or drag & drop</p>
            <p style={{ fontSize: '0.9rem', color: 'var(--text-light)' }}>
              JPG, PNG up to 10MB
            </p>
            <input
              ref={fileInputRef}
              type="file"
              accept="image/*"
              onChange={handleFileChange}
            />
          </div>

          {uploadedImage && (
            <div className="upload-preview">
              <img src={uploadedImage} alt="Preview" />
              <button 
                className="btn btn-primary" 
                onClick={uploadImage} 
                disabled={loading}
                style={{ width: '100%', marginTop: '1rem' }}
              >
                {loading ? '⏳ Scanning...' : '🔍 Analyze Image'}
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
