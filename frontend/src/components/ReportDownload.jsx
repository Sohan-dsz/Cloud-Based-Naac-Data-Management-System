import React, { useState, useEffect } from 'react';
import { useKeycloak } from '@react-keycloak/web';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const ReportDownload = () => {
  const { keycloak } = useKeycloak();
  const navigate = useNavigate();
  const [criteria, setCriteria] = useState([]);
  const [selectedCriteria, setSelectedCriteria] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (!keycloak.authenticated) {
      navigate('/');
      return;
    }
    fetchCriteria();
  }, [keycloak.authenticated, navigate]);

  const fetchCriteria = async () => {
    try {
      const response = await axios.get('/api/documents/criteria/');
      setCriteria(response.data);
    } catch (error) {
      console.error('Error fetching criteria:', error);
    }
  };

  const handleDownload = async () => {
    if (!selectedCriteria) return;

    setIsLoading(true);
    try {
      const response = await axios.get(`/api/reports/naac/${selectedCriteria}/`, {
        responseType: 'blob'
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `naac_report_${selectedCriteria}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Error downloading report:', error);
      alert('Download failed! Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8 p-6 bg-white rounded shadow-md">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl">Download NAAC Report</h2>
        <button
          onClick={() => navigate('/dashboard')}
          className="bg-gray-500 text-white px-3 py-1 rounded hover:bg-gray-600 text-sm"
        >
          Back to Dashboard
        </button>
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 mb-2">Select Criteria</label>
        <select
          value={selectedCriteria}
          onChange={(e) => setSelectedCriteria(e.target.value)}
          className="w-full px-3 py-2 border rounded"
        >
          <option value="">Choose Criteria</option>
          {criteria.map(c => (
            <option key={c.id} value={c.name}>{c.name}</option>
          ))}
        </select>
      </div>
      <button
        onClick={handleDownload}
        disabled={!selectedCriteria || isLoading}
        className="w-full bg-green-500 text-white py-2 rounded hover:bg-green-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        {isLoading ? 'Generating Report...' : 'Download PDF Report'}
      </button>
    </div>
  );
};

export default ReportDownload;
