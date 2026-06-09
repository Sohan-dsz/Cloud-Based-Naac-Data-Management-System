import React, { useEffect } from 'react';
import { useKeycloak } from '@react-keycloak/web';
import { useNavigate } from 'react-router-dom';

const Analytics = () => {
  const { keycloak } = useKeycloak();
  const navigate = useNavigate();

  useEffect(() => {
    if (!keycloak.authenticated) {
      navigate('/');
      return;
    }
  }, [keycloak.authenticated, navigate]);

  return (
    <div className="max-w-6xl mx-auto mt-8 p-6 bg-white rounded shadow-md">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl">Analytics Dashboard</h2>
        <button
          onClick={() => navigate('/dashboard')}
          className="bg-gray-500 text-white px-3 py-1 rounded hover:bg-gray-600 text-sm"
        >
          Back to Dashboard
        </button>
      </div>
      <div className="w-full h-96">
        <iframe
          src="http://localhost:3001/public/dashboard/12345678-1234-1234-1234-123456789012"
          width="100%"
          height="100%"
          frameBorder="0"
          title="Metabase Analytics"
        ></iframe>
      </div>
    </div>
  );
};

export default Analytics;
