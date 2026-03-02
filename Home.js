import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-content">
          <h1>Rice Pest Detection</h1>
          <p>Advanced AI-powered system for accurate identification of rice pests. Get instant recommendations for safe and effective pest control. Protect your harvest with cutting-edge technology.</p>
          <div className="hero-actions">
            <button className="btn btn-primary" onClick={() => navigate('/capture')}>
              🔍 Get Started
            </button>
          </div>
        </div>
        <div className="hero-visual">
          <div className="hero-icon">🌾</div>
        </div>
      </section>

      <section className="details">
        <div className="detail-card">
          <h3>⚡ Lightning Fast</h3>
          <p>Real-time pest identification powered by advanced machine learning algorithms optimized for speed.</p>
        </div>
        <div className="detail-card">
          <h3>🎯 Highly Accurate</h3>
          <p>Trained on thousands of rice field images to identify 15 different pest species with precision.</p>
        </div>
        <div className="detail-card">
          <h3>📱 Field Ready</h3>
          <p>Works on your mobile device with camera or image upload. No internet required for predictions.</p>
        </div>
        <div className="detail-card">
          <h3>🛡️ Safe Guidance</h3>
          <p>Detailed control recommendations that are plant-safe and environmentally responsible.</p>
        </div>
        <div className="detail-card">
          <h3>🔬 AI-Powered</h3>
          <p>Built with state-of-the-art deep learning models for reliable and consistent results.</p>
        </div>
        <div className="detail-card">
          <h3>📊 Detailed Info</h3>
          <p>Get comprehensive information about pest impact, lifecycle, and control strategies.</p>
        </div>
      </section>
    </div>
  );
}
