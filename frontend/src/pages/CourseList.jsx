import { useEffect, useState } from 'react'
import CourseCard from '../components/CourseCard.jsx'

const API_BASE = 'http://127.0.0.1:5000'

function CourseList() {
  const [courses, setCourses] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(`${API_BASE}/api/courses`)
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch courses')
        return res.json()
      })
      .then((data) => {
        setCourses(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  if (loading) return <p className="status-text">Loading courses...</p>
  if (error) return <p className="status-text error-text">Error: {error}</p>

  return (
    <div className="course-list-page">
      <h1>Available Courses</h1>
      <p className="page-subtitle">Pick a course to read its theory content.</p>
      <div className="course-grid">
        {courses.map((course) => (
          <CourseCard key={course.id} course={course} />
        ))}
      </div>
    </div>
  )
}

export default CourseList
