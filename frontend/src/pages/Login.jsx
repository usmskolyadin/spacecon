import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { baseUrl } from '../constats';

export default function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [test, setTest] = useState([]);
  const router = useNavigate();
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const testing = async () => {
      try {
        const response = await axios.get(`${baseUrl}/testing`);
        console.log(response.data);
        setTest(response.data);
        setLoading(false);
      } catch (e) {
        setTest([]);
        console.log(e);
      }
    };

    testing(); // Invoke the testing function
  }, []);

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(`${baseUrl}/token`, {
        username: username,
        password: password,
      });

      router('/');
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <h1>Login</h1>
      {loading ? (
          test.map((tes, index) => (
            <div key={index}>{}</div>
          ))
      ) : (
        <h1>loadin...</h1>
      )}

      <form onSubmit={handleLogin}>
        <label htmlFor="username">Username</label>
        <input
          required
          onChange={(e) => setUsername(e.target.value)}
          value={username}
          id="username"
          name="username"
          type="text"
        />

        <label htmlFor="password">Password</label>
        <input
          required
          onChange={(e) => setPassword(e.target.value)}
          value={password}
          id="password"
          name="password"
          type="password"
        />

        <button type="submit">Login</button>
      </form>
    </div>
  );
}