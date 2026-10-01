import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar.jsx'
import CourseList from './pages/CourseList.jsx'
import CourseTheory from './pages/CourseTheory.jsx'
import './App.css'

function App() {
  return (
    <div className="app">
      <Navbar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<CourseList />} />
          <Route path="/courses/:id" element={<CourseTheory />} />
        </Routes>
      </main>
    </div>
  )
}

export default App
