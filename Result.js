import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

export default function Result() {
  const navigate = useNavigate();
  const location = useLocation();
  
  const state = location.state?.result || {
    index: 0,
    name: 'Unknown Pest',
    info: {
      impact: 'Unable to determine impact',
      eggs: 'No egg information available',
      control: 'No control recommendations available'
    }
  };
  
  const imageData = location.state?.imageData;

  return (
    <div className="result">
      <h2 style={{ marginBottom: '2rem', fontSize: '2rem' }}>🎯 Detection Results</h2>
      
      <div className="result-container">
        {/* Left: Image and Status */}
        <div className="result-image-section">
          <div className="result-image" style={{ background: 'linear-gradient(135deg, rgba(16,185,129,0.1), rgba(124,58,237,0.1))' }}>
            {imageData ? (
              <img 
                src={imageData} 
                alt="Captured pest" 
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  borderRadius: '12px'
                }}
              />
            ) : (
              <div style={{ 
                width: '100%', 
                height: '100%', 
                display: 'flex', 
                alignItems: 'center', 
                justifyContent: 'center',
                fontSize: '4rem'
              }}>
                🌾
              </div>
            )}
          </div>
          
          <div className="result-status">
            <div className="pest-name">{state.name}</div>
          </div>
        </div>

        {/* Right: Details */}
        <div className="result-details">
          <div className="detail-section">
            <h3>💥 Impact Assessment</h3>
            <p>{state.info?.impact || 'No impact information available'}</p>
          </div>

          <div className="detail-section">
            <h3>🥚 Egg Information</h3>
            <p>{state.info?.eggs || 'No egg information available'}</p>
          </div>

          <div className="detail-section">
            <h3>🛡️ Control Recommendations</h3>
            <p>{state.info?.control || 'No control recommendations available'}</p>
          </div>

          <div className="detail-section">
            <h3>💊 Recommended Pesticide</h3>
            <p>{state.info?.pesticide || 'No pesticide information available'}</p>
          </div>

          <div className="action-buttons">
            <button className="btn btn-primary" onClick={() => navigate('/capture')}>
              🔄 Scan Again
            </button>
            <button className="btn btn-secondary" onClick={() => navigate('/')}>
              🏠 Go Home
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
