import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="bg-xyronix-primary text-white p-4">
      <nav className="container mx-auto flex justify-between items-center">
        <div className="text-2xl font-bold">Xyronix Labs</div>
        <ul className="flex space-x-4">
          <li><Link to="/" className="hover:text-xyronix-secondary">Home</Link></li>
          <li><Link to="/about" className="hover:text-xyronix-secondary">About</Link></li>
          <li><Link to="/services" className="hover:text-xyronix-secondary">Services</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;