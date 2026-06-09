import { useState, useEffect } from 'react';
import { useKeycloak } from '@react-keycloak/web';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const UploadForm = () => {
  const { keycloak } = useKeycloak();
  const navigate = useNavigate();
  const [criteria, setCriteria] = useState([]);
  const [evidences, setEvidences] = useState([]);
  const [selectedCriteria, setSelectedCriteria] = useState('');
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    evidence_id: '',
    file: null
  });
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    if (!keycloak.authenticated) {
      navigate('/');
      return;
    }

    fetchCriteria();
    fetchEvidences();
  }, [keycloak.authenticated, navigate]);

  const fetchCriteria = async () => {
    try {
      const response = await axios.get('/api/documents/criteria/');
      setCriteria(response.data);
    } catch (error) {
      console.error('Error fetching criteria:', error);
    }
  };

  const fetchEvidences = async () => {
    try {
      const response = await axios.get('/api/documents/evidence/');
      setEvidences(response.data);
    } catch (error) {
      console.error('Error fetching evidences:', error);
    }
  };

  const handleInputChange = (e) => {
    const { name, value, files } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: files ? files[0] : value
    }));
  };

  const handleCriteriaChange = async (e) => {
    const criteriaId = e.target.value;
    setSelectedCriteria(criteriaId);

    if (criteriaId) {
      try {
        // Create new evidence for selected criteria
        const criteriaObj = criteria.find(c => c.id == criteriaId);
        const response = await axios.post('/api/documents/evidence/', {
          title: `Evidence for ${criteriaObj.name}`,
          description: `Evidence documents for ${criteriaObj.name}`,
          criteria_id: criteriaId
        });
        setEvidences(prev => [...prev, response.data]);
        setFormData(prev => ({ ...prev, evidence_id: response.data.id }));
      } catch (error) {
        console.error('Error creating evidence:', error);
      }
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.title || !formData.evidence_id || !formData.file) {
      alert('Please fill all required fields');
      return;
    }

    setIsLoading(true);
    const uploadData = new FormData();
    uploadData.append('title', formData.title);
    uploadData.append('description', formData.description);
    uploadData.append('evidence_id', formData.evidence_id);
    uploadData.append('file', formData.file);

    try {
      await axios.post('/api/documents/upload/', uploadData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      alert('Document uploaded successfully!');
      setFormData({ title: '', description: '', evidence_id: '', file: null });
      setSelectedCriteria('');
      navigate('/dashboard');
    } catch (error) {
      console.error('Error uploading document:', error);
      alert('Upload failed! Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-md mx-auto mt-8 p-6 bg-white rounded shadow-md">
      <h2 className="text-2xl mb-4">Upload Document</h2>
      <form onSubmit={handleSubmit}>
        <div className="mb-4">
          <label className="block text-gray-700">Select Criteria</label>
          <select
            value={selectedCriteria}
            onChange={handleCriteriaChange}
            className="w-full px-3 py-2 border rounded"
            required
          >
            <option value="">Choose Criteria</option>
            {criteria.map(c => (
              <option key={c.id} value={c.id}>{c.name}</option>
            ))}
          </select>
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Title</label>
          <input
            name="title"
            value={formData.title}
            onChange={handleInputChange}
            className="w-full px-3 py-2 border rounded"
            type="text"
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">Description</label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleInputChange}
            className="w-full px-3 py-2 border rounded"
            rows="3"
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-700">File</label>
          <input
            name="file"
            onChange={handleInputChange}
            className="w-full px-3 py-2 border rounded"
            type="file"
            accept=".pdf,.doc,.docx,.jpg,.jpeg,.png"
            required
          />
        </div>
        <button
          type="submit"
          disabled={isLoading}
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 disabled:opacity-50"
        >
          {isLoading ? 'Uploading...' : 'Upload'}
        </button>
      </form>
    </div>
  );
};

export default UploadForm;
