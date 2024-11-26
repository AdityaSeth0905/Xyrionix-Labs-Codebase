import React from 'react';
import { Link } from 'react-router-dom';
import content from './content.json';

const Footer: React.FC = () => {
  const footerData = content.footer;
  const currentYear = new Date().getFullYear();

  // Function to handle Privacy Policy navigation
  const navigateToPrivacyPolicy = () => {
    // Use React Router navigation instead of alert
    // Assuming you have a route set up for privacy policy
    // history.push('/privacy-policy');
  };

  return (
    <footer 
      className="bg-gray-900 text-gray-200 py-12 px-6 transition-all duration-300 ease-in-out"
    >
      <div className="container mx-auto max-w-6xl grid md:grid-cols-3 gap-8">
        {/* Company Information Column */}
        <div className="flex flex-col space-y-4">
          <div>
            <h2 className="text-3xl font-bold text-white mb-2">
              {footerData.companyName}
            </h2>
            <p className="text-sm italic text-gray-400">
              {footerData.slogan}
            </p>
          </div>
          
          {/* Contact Information */}
          <div>
            <h3 className="text-xl font-semibold mb-2">Contact</h3>
            <a 
              href={`mailto:${footerData.contactEmail}`} 
              className="text-gray-300 hover:text-white transition-colors 
                         flex items-center space-x-2"
            >
              <i className="fas fa-envelope mr-2"></i>
              {footerData.contactEmail}
            </a>
          </div>
        </div>

        {/* Quick Links Column */}
        <div>
          <h3 className="text-xl font-semibold mb-4">Quick Links</h3>
          <ul className="space-y-2">
            <li>
              <Link 
                to="/about-us" 
                className="text-gray-300 hover:text-white transition-colors"
              >
                About Us
              </Link>
            </li>
            <li>
              <Link 
                to="/products" 
                className="text-gray-300 hover:text-white transition-colors"
              >
                Products
              </Link>
            </li>
            <li>
              <button 
                onClick={navigateToPrivacyPolicy} 
                className="text-gray-300 hover:text-white transition-colors 
                           text-left focus:outline-none"
              >
                Privacy Policy
              </button>
            </li>
          </ul>
        </div>

        {/* Social Media Column */}
        <div>
          <h3 className="text-xl font-semibold mb-4">Connect With Us</h3>
          <div className="flex space-x-4">
            {footerData.socialMedia.map((social, index) => (
              <a 
                key={index} 
                href={social.url} 
                target="_blank" 
                rel="noopener noreferrer" 
                className="
                  text-gray-200 text-2xl 
                  hover:text-blue-400 
                  transition-colors 
                  transform hover:scale-110
                "
                aria-label={`${social.platform} profile`}
              >
                <i className={`fab fa-${social.platform.toLowerCase()}`}></i>
              </a>
            ))}
          </div>
        </div>
      </div>

      {/* Copyright Section */}
      <div 
        className="
          mt-8 pt-6 border-t border-gray-700 
          text-center text-gray-400 text-sm
        "
      >
        <p>
          &copy; {currentYear} {footerData.companyName}. 
          All rights reserved. Crafted with ❤️ by Xyronix Labs.
        </p>
      </div>
    </footer>
  );
};

export default Footer;