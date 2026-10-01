import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'

const API_BASE = 'http://127.0.0.1:5000'

function CourseTheory() {
  const { id } = useParams()
  const [course, setCourse] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    setLoading(true)
    setError(null)
    fetch(`${API_BASE}/api/courses/${id}`)
      .then((res) => {
        if (!res.ok) throw new Error('Course not found')
        return res.json()
      })
      .then((data) => {
        setCourse(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [id])

  if (loading) return <p className="status-text">Loading theory...</p>
  if (error) return <p className="status-text error-text">Error: {error}</p>

  return (
    <div className="course-theory-page">
      <Link to="/" className="back-link">
        ← Back to courses
      </Link>
      <span className="course-category">{course.category}</span>
      <h1>{course.title}</h1>
      <pre className="theory-content">{course.theory}</pre>
    </div>
  )
}

export default CourseTheory
