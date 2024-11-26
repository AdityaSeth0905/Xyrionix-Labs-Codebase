import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Layout from './components/Layout';
import content from './components/content.json';
import Loading from './components/Loading'; // Create a simple loading component

// Dynamic page import function
const dynamicPageImport = (pageName: string) => {
  return lazy(() => {
    // Convert page name to kebab-case for file naming
    const formattedPageName = pageName
      .toLowerCase()
      .replace(/\s+/g, '-');
    
    return import(`./pages/${formattedPageName}.tsx`);
  });
};

const App: React.FC = () => {
  // Extract navigation items from content
  const navBar = content.navBar[0];

  // Generate routes dynamically
  const generateRoutes = () => {
    return Object.entries(navBar).map(([key, value]) => {
      // Handle home page separately
      if (key === 'b1') {
        const HomePage = dynamicPageImport(value);
        return (
          <Route 
            key={key} 
            index 
            element={
              <Suspense fallback={<Loading />}>
                <HomePage />
              </Suspense>
            } 
          />
        );
      }

      // Create routes for other pages
      const PageComponent = dynamicPageImport(value);
      const path = value.toLowerCase().replace(/\s+/g, '-');

      return (
        <Route 
          key={key} 
          path={path} 
          element={
            <Suspense fallback={<Loading />}>
              <PageComponent />
            </Suspense>
          } 
        />
      );
    });
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Layout />}>
          {generateRoutes()}
        </Route>
      </Routes>
    </Router>
  );
};

export default App;