import React, { lazy, Suspense, useEffect } from 'react';
import { 
  BrowserRouter as Router, 
  Routes, 
  Route, 
  Navigate 
} from 'react-router-dom';
import { ErrorBoundary } from 'react-error-boundary';
import Layout from './components/Layout';
import content from './components/content.json';
import Loading from './components/Loading';
import ErrorFallback from './components/ErrorFallback';
import '@fortawesome/fontawesome-free/css/all.min.css';

// Dark theme context for global theme management
import { ThemeProvider } from './context/ThemeContext';

// Enhanced dynamic page import with error handling
const dynamicPageImport = (pageName: string) => {
  return lazy(() => {
    // Convert page name to kebab-case for file naming
    const formattedPageName = pageName
      .toLowerCase()
      .replace(/\s+/g, '-');
    
    return import(`./pages/${formattedPageName}.tsx`)
      .catch(error => {
        console.error(`Failed to load page: ${formattedPageName}`, error);
        return import('./pages/404'); // Fallback to 404 page
      });
  });
};

// Route configuration type
interface RouteConfig {
  path: string;
  element: React.ReactNode;
  index?: boolean;
}

const App: React.FC = () => {
  // Extract navigation items from content
  const navBar = content.navBar[0];

  // Apply dark mode class to body
  useEffect(() => {
    document.body.classList.add('dark');
    document.body.classList.add('bg-gray-900');
    document.body.classList.add('text-gray-100');
  }, []);

  // Generate routes dynamically with improved type safety
  const generateRoutes = (): RouteConfig[] => {
    const routes: RouteConfig[] = Object.entries(navBar).map(([key, value]) => {
      // Handle home page separately
      if (key === 'b1') {
        const HomePage = dynamicPageImport(value);
        return {
          path: '/',
          index: true,
          element: (
            <ErrorBoundary FallbackComponent={ErrorFallback}>
              <Suspense fallback={<Loading />}>
                <div className="min-h-screen bg-gray-900 text-gray-100">
                  <HomePage />
                </div>
              </Suspense>
            </ErrorBoundary>
          )
        };
      }

      // Create routes for other pages
      const PageComponent = dynamicPageImport(value);
      const path = value.toLowerCase().replace(/\s+/g, '-');

      return {
        path,
        element: (
          <ErrorBoundary FallbackComponent={ErrorFallback}>
            <Suspense fallback={<Loading />}>
              <div className="min-h-screen bg-gray-900 text-gray-100">
                <PageComponent />
              </div>
            </Suspense>
          </ErrorBoundary>
        )
      };
    });

    // Add a catch-all route to redirect to 404 or home
    routes.push({
      path: '*',
      element: <Navigate to="/" replace />
    });

    return routes;
  };

  return (
    <ThemeProvider>
      <div className="dark bg-gray-900 text-gray-100 min-h-screen">
        <Router>
          <ErrorBoundary FallbackComponent={ErrorFallback}>
            <Routes>
              <Route 
                path="/" 
                element={
                  <div className="bg-gray-900 text-gray-100 min-h-screen">
                    <Layout />
                  </div>
                }
              >
                {generateRoutes().map((route, index) => (
                  <Route 
                    key={index} 
                    path={route.path}
                    index={route.index}
                    element={route.element as React.ReactElement}
                  />
                ))}
              </Route>
            </Routes>
          </ErrorBoundary>
        </Router>
      </div>
    </ThemeProvider>
  );
};

export default App;