import React from 'react';
import { useKeycloak } from '@react-keycloak/web';
import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import axios from 'axios';

const Login = () => {
  const { keycloak } = useKeycloak();
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (keycloak.authenticated) {
      // Sync with backend after Keycloak authentication
      syncWithBackend();
    }
  }, [keycloak.authenticated]);

  const syncWithBackend = async () => {
    setIsLoading(true);
    try {
      const response = await axios.post('/api/auth/keycloak-login/', {
        access_token: keycloak.token,
        refresh_token: keycloak.refreshToken,
        expires_in: keycloak.tokenParsed?.exp,
        token_type: 'Bearer'
      });

      if (response.status === 200) {
        navigate('/dashboard');
      }
    } catch (error) {
      console.error('Backend sync failed:', error);
      alert('Authentication failed. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleLogin = () => {
    keycloak.login({
      redirectUri: window.location.origin + '/dashboard'
    });
  };

  const handleLogout = () => {
    keycloak.logout({
      redirectUri: window.location.origin
    });
  };

  if (keycloak.authenticated) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="bg-white p-8 rounded shadow-md">
          <h2 className="text-2xl mb-4">Welcome, {keycloak.tokenParsed?.preferred_username}</h2>
          {isLoading ? (
            <p>Syncing with backend...</p>
          ) : (
            <div className="space-x-4">
              <button
                onClick={() => navigate('/dashboard')}
                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
              >
                Go to Dashboard
              </button>
              <button
                onClick={handleLogout}
                className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
              >
                Logout
              </button>
            </div>
          )}
        </div>
      </div>
    );
  }

  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="bg-white p-8 rounded shadow-md">
        <h2 className="text-2xl mb-4">NAAC Data Management System</h2>
        <button
          onClick={handleLogin}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Login with Keycloak
        </button>
      </div>
    </div>
  );
};

export default Login;
