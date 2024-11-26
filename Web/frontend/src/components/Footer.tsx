import React from 'react';
import content from './content.json';

const Footer: React.FC = () => {
  const footerData = content.footer;

  // Function to handle Privacy Policy click
  const PrivacyPolicy = () => {
    // Implement your privacy policy logic here
    alert("Privacy Policy clicked!");
  };

  return (
    <footer className="bg-gray-800 text-white py-4 px-4">
      <div className="container mx-auto flex flex-col md:flex-row justify-between items-center">
        
        {/* Company Name and Tagline on the Left */}
        <div className="flex flex-col items-start mt-2 md:mt-0">
          <h2 className="text-2xl font-bold">{footerData.companyName}</h2>
          <p className="text-sm italic">{footerData.slogan}</p>
        </div>

        {/* Right Side Container */}
        <div className="flex flex-col items-end mt-2">
          {/* Privacy Policy at the top */}
          <button 
            id='privacyPolicy' 
            onClick={PrivacyPolicy} 
            className="text-white underline mb-2"
          >
            Privacy Policy
          </button>

          {/* Social Media Links */}
          <div className="flex space-x-4 mb-2">
            {footerData.socialMedia.map((social, index) => (
              <a 
                key={index} 
                href={social.url} 
                target="_blank" 
                rel="noopener noreferrer" 
                className="social-media-link hover:opacity-75 transition-opacity"
              >
                <img 
                  src={social.logo} 
                  alt={`${social.platform} logo`} 
                  className="social-media-logo w-8 h-8" 
                />
              </a>
            ))}
          </div>

          {/* Contact Us at the bottom */}
          <p className="text-sm">
            Contact us @ <a href={`mailto:${footerData.contactEmail}`} className="underline">{footerData.contactEmail}</a>
          </p>
        </div>
      </div>

      {/* Centered Copyright Notice */}
      <div className="text-center mt-2">
        <p className="text-sm">
          &copy; {new Date().getFullYear()} {footerData.companyName}. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;