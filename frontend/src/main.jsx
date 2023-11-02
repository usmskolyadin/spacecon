import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { Provider } from 'react-redux'
import { store } from './store/index.js'
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from 'react-router-dom';
import Login from './pages/Login.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Provider store={store}>
      <Router>
          <Routes>
            <Route path='/' element={<App/>} />
            <Route path='/auth/login' element={<Login/>} />
          </Routes>
      </Router>
    </Provider> 
 </React.StrictMode>
)
