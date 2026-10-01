from flask import Flask, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample course data with theory content.
# Replace/extend this list with your own courses and content.
COURSES = [
    {
        "id": 1,
        "title": "Introduction to Python",
        "category": "Programming",
        "summary": "Learn the basics of Python programming language.",
        "theory": """Python is a high-level, interpreted programming language known for its
readability and simplicity. It was created by Guido van Rossum and first
released in 1991.

Key features of Python:
1. Easy to read and write syntax
2. Dynamically typed - no need to declare variable types
3. Extensive standard library
4. Supports multiple programming paradigms (procedural, object-oriented, functional)
5. Large community and ecosystem of third-party packages

Python is widely used in web development, data science, artificial
intelligence, automation, and scientific computing. Its simplicity makes
it an excellent first language for beginners, while its power and
flexibility make it a favorite among experienced developers."""
    },
    {
        "id": 2,
        "title": "Database Management Systems",
        "category": "Databases",
        "summary": "Understand the fundamentals of DBMS and relational databases.",
        "theory": """A Database Management System (DBMS) is software that manages the
creation, retrieval, updating, and administration of databases.

Core concepts:
1. Data Model - defines how data is logically structured (relational,
   hierarchical, network, object-oriented)
2. Relational Model - organizes data into tables (relations) consisting
   of rows (tuples) and columns (attributes)
3. Normalization - the process of organizing data to reduce redundancy
   and improve data integrity, typically through normal forms (1NF, 2NF, 3NF)
4. SQL (Structured Query Language) - the standard language for
   interacting with relational databases
5. ACID Properties - Atomicity, Consistency, Isolation, and Durability
   ensure reliable transaction processing

Popular DBMS examples include MySQL, PostgreSQL, Oracle, and SQLite.
DBMSs are essential for nearly all modern applications that need to
store and retrieve structured data reliably."""
    },
    {
        "id": 3,
        "title": "Data Structures and Algorithms",
        "category": "Computer Science",
        "summary": "Master the core data structures and algorithmic techniques.",
        "theory": """Data structures are ways of organizing and storing data so that
they can be accessed and worked with efficiently. Algorithms are
step-by-step procedures for solving problems.

Common data structures:
1. Arrays - fixed-size collections of elements stored in contiguous
   memory locations
2. Linked Lists - collections of nodes where each node points to the next
3. Stacks - Last-In-First-Out (LIFO) structures
4. Queues - First-In-First-Out (FIFO) structures
5. Trees - hierarchical structures with a root and child nodes
6. Graphs - collections of nodes (vertices) connected by edges

Common algorithmic techniques:
1. Sorting (Bubble Sort, Merge Sort, Quick Sort)
2. Searching (Linear Search, Binary Search)
3. Recursion
4. Dynamic Programming
5. Greedy Algorithms

Understanding time and space complexity (Big O notation) is essential
for evaluating how efficient an algorithm or data structure is as
input size grows."""
    },
    {
        "id": 4,
        "title": "Machine Learning Basics",
        "category": "Artificial Intelligence",
        "summary": "Get introduced to core machine learning concepts.",
        "theory": """Machine Learning (ML) is a subset of artificial intelligence that
enables systems to learn patterns from data and make predictions or
decisions without being explicitly programmed for each task.

Types of Machine Learning:
1. Supervised Learning - the model learns from labeled data
   (e.g., classification, regression)
2. Unsupervised Learning - the model finds patterns in unlabeled data
   (e.g., clustering, dimensionality reduction)
3. Reinforcement Learning - an agent learns by interacting with an
   environment and receiving rewards or penalties

Typical ML workflow:
1. Data collection and preprocessing
2. Splitting data into training and testing sets
3. Choosing and training a model
4. Evaluating model performance using metrics (accuracy, precision,
   recall, F1-score)
5. Tuning hyperparameters to improve results

Popular ML libraries include scikit-learn, TensorFlow, and PyTorch.
Machine learning powers applications like recommendation systems,
image recognition, fraud detection, and natural language processing."""
    }
]


@app.route("/api/courses", methods=["GET"])
def get_courses():
    """Return the list of courses without full theory content (for the list view)."""
    course_list = [
        {
            "id": c["id"],
            "title": c["title"],
            "category": c["category"],
            "summary": c["summary"],
        }
        for c in COURSES
    ]
    return jsonify(course_list)


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    """Return full details (including theory) for a single course."""
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if course is None:
        abort(404, description="Course not found")
    return jsonify(course)


@app.errorhandler(404)
def handle_404(e):
    return jsonify({"error": str(e.description)}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
