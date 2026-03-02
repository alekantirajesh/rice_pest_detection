import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header className="header">
      <div className="header-content">
        <Link to="/" className="logo">
          🌾 Rice Pest Detector
        </Link>
        <nav className="nav-links">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="/capture" className="nav-link">Scan</Link>
        </nav>
      </div>
    </header>
  );
}
