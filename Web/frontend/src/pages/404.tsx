import React from 'react';
import { Link } from 'react-router-dom';

const NotFound: React.FC = () => {
  return (
    <div 
      className="
        flex flex-col items-center justify-center 
        min-h-screen 
        bg-gray-900 
        text-gray-100 
        text-center 
        p-4
      "
    >
      <h1 className="text-6xl font-bold text-red-500 mb-4">
        404
      </h1>
      <p className="text-2xl mb-6">
        Page Not Found
      </p>
      <Link 
        to="/" 
        className="
          bg-blue-600 
          text-white 
          px-6 py-3 
          rounded-lg 
          hover:bg-blue-700 
          transition-colors
        "
      >
        Return to Home
      </Link>
    </div>
  );
};

export default NotFound;