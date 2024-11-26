import React from 'react';
import content from './content.json';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  const companyName = content.footer.companyName;
  const navBar = content.navBar[0];

  // Generate route from button name
  const generateRoute = (value: string) => {
    // Home page is special case
    if (value === 'Home') return '/';
    
    // Convert to lowercase, replace spaces with hyphens
    return `/${value.toLowerCase().replace(/\s+/g, '-')}`;
  };

  return (
    <header className="bg-xyronix-primary text-white p-4">
      <nav className="container mx-auto flex flex-col md:flex-row justify-between items-center">
        <div className="text-2xl font-bold text-center md:text-left mb-4 md:mb-0">
          {companyName}
        </div>
        <ul className="flex flex-col md:flex-row space-x-0 md:space-x-4">
          {navBar && 
            Object.entries(navBar).map(([key, value]) => (
              <li key={key} className="mb-2 md:mb-0">
                <Link 
                  to={generateRoute(value)} 
                  className="hover:text-xyronix-secondary block"
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