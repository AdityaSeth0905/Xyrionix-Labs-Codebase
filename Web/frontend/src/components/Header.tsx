import React, { useState } from 'react';
import content from './content.json';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  const companyName = content.footer.companyName;
  const navBar = content.navBar[0];
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  // Generate route from button name
  const generateRoute = (value: string) => {
    // Home page is special case
    if (value === 'Home') return '/';
    
    // Convert to lowercase, replace spaces with hyphens
    return `/${value.toLowerCase().replace(/\s+/g, '-')}`;
  };

  // Toggle mobile menu
  const toggleMobileMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header 
      className="
        sticky top-0 z-50 
        bg-gray-900 
        text-gray-100 
        shadow-2xl 
        border-b border-gray-800
        transition-all 
        duration-300 
        ease-in-out
      "
    >
      <nav className="container mx-auto flex items-center justify-between p-4 relative">
        {/* Logo/Company Name */}
        <div className="flex items-center space-x-4">
          <Link 
            to="/" 
            className="
              text-2xl font-bold 
              tracking-wider 
              hover:text-gray-300 
              transition-colors 
              flex items-center
              group
            "
          >
            <span className="mr-3 text-gray-400 group-hover:text-gray-200 transition-colors">
              <i className="fas fa-flask text-3xl"></i>
            </span>
            {companyName}
          </Link>
        </div>

        {/* Mobile Menu Toggle */}
        <div className="md:hidden">
          <button 
            onClick={toggleMobileMenu}
            className="
              text-gray-300 
              focus:outline-none 
              focus:ring-2 
              focus:ring-gray-700 
              rounded-md 
              p-2
              hover:bg-gray-800
              transition-colors
            "
            aria-label="Toggle mobile menu"
          >
            {isMenuOpen ? (
              <i className="fas fa-times text-2xl"></i>
            ) : (
              <i className="fas fa-bars text-2xl"></i>
            )}
          </button>
        </div>

        {/* Navigation Links */}
        <ul 
          className={`
            ${isMenuOpen ? 'block' : 'hidden'} 
            md:flex 
            absolute md:static 
            top-full left-0 
            w-full md:w-auto 
            bg-gray-900 md:bg-transparent 
            md:space-x-4 
            space-y-2 md:space-y-0 
            py-4 md:py-0 
            shadow-lg md:shadow-none
            border-t border-gray-800 md:border-none
          `}
        >
          {navBar && 
            Object.entries(navBar).map(([key, value]) => (
              <li 
                key={key} 
                className="
                  text-center 
                  md:text-left 
                  px-4 md:px-0
                "
              >
                <Link 
                  to={generateRoute(value)} 
                  onClick={() => setIsMenuOpen(false)}
                  className="
                    block 
                    py-2 md:py-0 
                    text-gray-300 
                    hover:text-white 
                    hover:bg-gray-800 md:hover:bg-transparent 
                    transition-colors 
                    rounded-md md:rounded-none
                    font-medium
                  "
                >
                  {value}
                </Link>
              </li>
            ))
          }
        </ul>
      </nav>
    </header>
  );
};

export default Header;