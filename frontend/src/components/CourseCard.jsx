import { Link } from 'react-router-dom'

function CourseCard({ course }) {
  return (
    <Link to={`/courses/${course.id}`} className="course-card">
      <span className="course-category">{course.category}</span>
      <h3 className="course-title">{course.title}</h3>
      <p className="course-summary">{course.summary}</p>
      <span className="course-link">Read theory →</span>
    </Link>
  )
}

export default CourseCard
