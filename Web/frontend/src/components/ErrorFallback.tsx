import React from 'react';
import { FallbackProps } from 'react-error-boundary';

const ErrorFallback: React.FC<FallbackProps> = ({ error, resetErrorBoundary }) => {
  return (
    <div 
      className="
        flex flex-col items-center justify-center 
        min-h-screen 
        bg-gray-900 
        text-gray-100 
        p-4
      "
      role="alert"
    >
      <h1 className="text-4xl font-bold text-red-500 mb-4">
        Oops! Something went wrong
      </h1>
      <pre className="text-gray-300 bg-gray-800 p-4 rounded-md mb-4">
        {error.message}
      </pre>
      <button
        onClick={resetErrorBoundary}
        className="
          bg-blue-600 
          text-white 
          px-4 py-2 
          rounded 
          hover:bg-blue-700 
          transition-colors
        "
      >
        Try again
      </button>
    </div>
  );
};

export default ErrorFallback;