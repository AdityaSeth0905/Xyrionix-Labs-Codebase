import React, { useEffect, useState } from 'react';

const ApiTest = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api')
      .then((res) => res.text())
      .then((data) => setMessage(data))
      .catch((err) => console.error(err));
  }, []);

  return <div>Backend Message: {message}</div>;
};

export default ApiTest;
