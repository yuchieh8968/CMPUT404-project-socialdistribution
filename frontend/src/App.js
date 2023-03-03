import './App.css';
import {
  BrowserRouter as Router, Route, Routes, Navigate
}
  from 'react-router-dom';
import Login from './components/auth/Login';
import Signup from './components/auth/Signup';
import Inbox from './components/inbox/Inbox';
import Home from './components/home/Home';


function App() {
  return (
    <div className="App">
      <Router>
          <Routes>
            <Route exact path="/" element={<Navigate to="/login" />} />
            <Route path="/login" element={(<Login />)} />
            <Route path="/signup" element={(<Signup />)} />
            <Route path="/inbox" element={(<Inbox />)} />
            <Route path="/home" element={(<Home />)} />
          </Routes>
      </Router>
    </div>
  );
}

export default App;
