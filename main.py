<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>OBA Interactive Demo</title>
  <style>
    body { font-family: sans-serif; background: #f0f0f0; padding: 2rem; }
    h1 { color: #333; }
    .section { background: white; padding: 1rem; margin-bottom: 2rem; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    label { display: block; margin-top: 10px; font-weight: bold; }
    input, button { width: 100%; padding: 8px; margin-top: 5px; }
    button { background: #007bff; color: white; border: none; border-radius: 4px; margin-top: 15px; cursor: pointer; }
  </style>
</head>
<body>

  <h1>📘 Outcome-Based Assessment</h1>

  <div class="section">
    <h2>📌 Add Program</h2>
    <label for="programName">Program Name</label>
    <input type="text" id="programName" placeholder="e.g. Computer Science" />

    <label for="programDesc">Description</label>
    <input type="text" id="programDesc" placeholder="e.g. Bachelor program" />

    <button onclick="addProgram()">Add Program</button>
  </div>

  <div class="section">
    <h2>📚 Add Course</h2>
    <label for="courseName">Course Name</label>
    <input type="text" id="courseName" placeholder="e.g. Data Structures" />

    <label for="courseCode">Course Code</label>
    <input type="text" id="courseCode" placeholder="e.g. CS202" />

    <label for="courseProgramId">Program ID</label>
    <input type="number" id="courseProgramId" placeholder="e.g. 1" />

    <button onclick="addCourse()">Add Course</button>
  </div>

  <div class="section">
    <h2>📝 Add Assessment</h2>
    <label for="assessmentTitle">Title</label>
    <input type="text" id="assessmentTitle" placeholder="e.g. Quiz 1" />

    <label for="assessmentType">Type</label>
    <input type="text" id="assessmentType" placeholder="e.g. Quiz" />

    <label for="assessmentMarks">Total Marks</label>
    <input type="number" id="assessmentMarks" placeholder="e.g. 20" />

    <label for="assessmentWeight">Weightage</label>
    <input type="number" id="assessmentWeight" placeholder="e.g. 10" />

    <label for="assessmentSession">Session</label>
    <input type="text" id="assessmentSession" placeholder="e.g. Fall 2025" />

    <label for="assessmentDate">Date</label>
    <input type="date" id="assessmentDate" />

    <label for="assessmentCourseId">Course ID</label>
    <input type="number" id="assessmentCourseId" placeholder="e.g. 1" />

    <button onclick="addAssessment()">Add Assessment</button>
  </div>

  <script>
    const api = window.location.origin + '/api';

    async function addProgram() {
      const name = document.getElementById('programName').value;
      const description = document.getElementById('programDesc').value;
      await fetch(api + '/programs', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, description })
      });
      alert('✅ Program added');
    }

    async function addCourse() {
      const name = document.getElementById('courseName').value;
      const code = document.getElementById('courseCode').value;
      const program_id = parseInt(document.getElementById('courseProgramId').value);
      await fetch(api + '/courses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, code, program_id })
      });
      alert('✅ Course added');
    }

    async function addAssessment() {
      const title = document.getElementById('assessmentTitle').value;
      const type = document.getElementById('assessmentType').value;
      const total_marks = parseInt(document.getElementById('assessmentMarks').value);
      const weightage = parseInt(document.getElementById('assessmentWeight').value);
      const session = document.getElementById('assessmentSession').value;
      const date = document.getElementById('assessmentDate').value;
      const course_id = parseInt(document.getElementById('assessmentCourseId').value);
      await fetch(api + '/assessments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, type, total_marks, weightage, session, date, course_id })
      });
      alert('✅ Assessment added');
    }
  </script>

</body>
</html>
