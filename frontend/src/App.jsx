import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ReactKeycloakProvider } from '@react-keycloak/web';
import Keycloak from 'keycloak-js';
import axios from 'axios';
import Login from './components/Login';
import UploadForm from './components/UploadForm';
import EvidenceDashboard from './components/EvidenceDashboard';
import Analytics from './components/Analytics';
import ReportDownload from './components/ReportDownload';

const keycloak = new Keycloak({
  url: 'http://localhost:8080',
  realm: 'naac-realm',
  clientId: 'naac-client',
  onLoad: 'check-sso',
});

// Set up axios interceptor for auth headers
const setupAxiosInterceptors = (keycloak) => {
  axios.interceptors.request.use(
    (config) => {
      if (keycloak.authenticated) {
        config.headers.Authorization = `Bearer ${keycloak.token}`;
      }
      return config;
    },
    (error) => Promise.reject(error)
  );

  // Refresh token on 401
  axios.interceptors.response.use(
    (response) => response,
    async (error) => {
      if (error.response?.status === 401 && keycloak.authenticated) {
        try {
          await keycloak.updateToken(70);
          error.config.headers.Authorization = `Bearer ${keycloak.token}`;
          return axios(error.config);
        } catch (refreshError) {
          keycloak.logout();
        }
      }
      return Promise.reject(error);
    }
  );
};

function App() {
  return (
    <ReactKeycloakProvider
      authClient={keycloak}
      initOptions={{
        onLoad: 'check-sso',
        silentCheckSsoRedirectUri: window.location.origin + '/silent-check-sso.html',
      }}
      onEvent={(event, error) => {
        if (event === 'onReady') {
          setupAxiosInterceptors(keycloak);
        }
      }}
    >
      <Router>
        <div className="min-h-screen bg-gray-100">
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/upload" element={<UploadForm />} />
            <Route path="/dashboard" element={<EvidenceDashboard />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route path="/reports" element={<ReportDownload />} />
          </Routes>
        </div>
      </Router>
    </ReactKeycloakProvider>
  );
}

export default App;
