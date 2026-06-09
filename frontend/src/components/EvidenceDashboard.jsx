import React, { useState, useEffect } from 'react';
import { useKeycloak } from '@react-keycloak/web';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const EvidenceDashboard = () => {
  const { keycloak } = useKeycloak();
  const navigate = useNavigate();
  const [documents, setDocuments] = useState([]);
  const [searchQuery, setSearchQuery] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (!keycloak.authenticated) {
      navigate('/');
      return;
    }
    fetchDocuments();
  }, [keycloak.authenticated, navigate]);

  const fetchDocuments = async () => {
    setIsLoading(true);
    try {
      const response = await axios.get('/api/documents/documents/');
      setDocuments(response.data);
    } catch (error) {
      console.error('Error fetching documents:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSearch = async () => {
    if (!searchQuery.trim()) {
      fetchDocuments();
      return;
    }

    setIsLoading(true);
    try {
      const response = await axios.get(`/api/documents/search/?q=${encodeURIComponent(searchQuery)}`);
      setDocuments(response.data);
    } catch (error) {
      console.error('Error searching documents:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleApprove = async (docId) => {
    try {
      await axios.post(`/api/documents/documents/${docId}/approve/`);
      alert('Document approved successfully!');
      fetchDocuments(); // Refresh list
    } catch (error) {
      console.error('Error approving document:', error);
      alert('Approval failed!');
    }
  };

  return (
    <div className="max-w-6xl mx-auto mt-8 p-6 bg-white rounded shadow-md">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-2xl">Evidence Dashboard</h2>
        <div className="space-x-2">
          <button
            onClick={() => navigate('/upload')}
            className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
          >
            Upload Document
          </button>
          <button
            onClick={() => navigate('/analytics')}
            className="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600"
          >
            View Analytics
          </button>
          <button
            onClick={() => navigate('/reports')}
            className="bg-orange-500 text-white px-4 py-2 rounded hover:bg-orange-600"
          >
            Generate Reports
          </button>
        </div>
      </div>

      <div className="mb-6 flex">
        <input
          type="text"
          placeholder="Search documents..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
          className="flex-1 px-3 py-2 border rounded-l"
        />
        <button
          onClick={handleSearch}
          disabled={isLoading}
          className="bg-blue-500 text-white px-4 py-2 rounded-r hover:bg-blue-600 disabled:opacity-50"
        >
          {isLoading ? 'Searching...' : 'Search'}
        </button>
      </div>

      {isLoading ? (
        <p className="text-center">Loading...</p>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {documents.map(doc => (
            <div key={doc.id} className="border p-4 rounded shadow-sm">
              <h3 className="font-bold text-lg mb-2">{doc.title}</h3>
              <p className="text-sm text-gray-600 mb-2">{doc.description}</p>
              <div className="text-xs text-gray-500 space-y-1">
                <p>Evidence: {doc.evidence?.title}</p>
                <p>Criteria: {doc.evidence?.criteria?.name}</p>
                <p>Uploaded by: {doc.uploaded_by}</p>
                <p>Status: {doc.is_approved ? 'Approved' : 'Pending'}</p>
                <p>Uploaded: {new Date(doc.uploaded_at).toLocaleDateString()}</p>
              </div>
              {!doc.is_approved && (
                <button
                  onClick={() => handleApprove(doc.id)}
                  className="mt-2 bg-blue-500 text-white px-3 py-1 rounded text-xs hover:bg-blue-600"
                >
                  Approve
                </button>
              )}
            </div>
          ))}
          {documents.length === 0 && (
            <p className="col-span-full text-center text-gray-500">No documents found.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default EvidenceDashboard;
