import React, { 
    createContext, 
    useState, 
    useContext, 
    ReactNode, 
    useEffect 
  } from 'react';
  
  type ThemeContextType = {
    isDarkMode: boolean;
    toggleTheme: () => void;
  };
  
  const ThemeContext = createContext<ThemeContextType | undefined>(undefined);
  
  export const ThemeProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
    const [isDarkMode, setIsDarkMode] = useState<boolean>(true);
  
    useEffect(() => {
      if (isDarkMode) {
        document.body.classList.add('dark');
        document.body.classList.add('bg-gray-900');
        document.body.classList.add('text-gray-100');
      } else {
        document.body.classList.remove('dark');
        document.body.classList.remove('bg-gray-900');
        document.body.classList.remove('text-gray-100');
      }
    }, [isDarkMode]);
  
    const toggleTheme = () => {
      setIsDarkMode(!isDarkMode);
    };
  
    return (
      <ThemeContext.Provider value={{ isDarkMode, toggleTheme }}>
        {children}
      </ThemeContext.Provider>
    );
  };
  
  export const useTheme = () => {
    const context = useContext(ThemeContext);
    if (context === undefined) {
      throw new Error('useTheme must be used within a ThemeProvider');
    }
    return context;
  };