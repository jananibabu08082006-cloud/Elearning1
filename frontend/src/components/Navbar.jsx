import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <header className="navbar">
      <Link to="/" className="navbar-brand">
        📚 E-Learning
      </Link>
    </header>
  )
}

export default Navbar
