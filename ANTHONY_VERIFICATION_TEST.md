# Verification Test: Anthony - Week 01, Day 01

**Purpose**: Verify understanding of the code submitted  
**Duration**: 30-45 minutes  
**Format**: Live coding and explanation session

---

## Part 1: Code Explanation (15 minutes)

Ask Anthony to explain the following code sections. Take notes on his responses.

### Question 1: Vue.js Basics
**Show him this code:**
```javascript
data() {
  return {
    newTask: "",
    filter: "all",
    tasks: []
  }
}
```

**Questions:**
1. What is the `data()` function in Vue.js?
2. Why does it return an object?
3. What happens when you change `this.newTask` in a method?
4. Why are these called "reactive" properties?

**Expected Understanding:**
- `data()` returns the component's reactive state
- Changes to these properties automatically update the UI
- Each component instance has its own data

---

### Question 2: Computed Properties
**Show him this code:**
```javascript
computed: {
  filteredTasks() {
    if (this.filter === 'completed') {
      return this.tasks.filter(t => t.status === 'completed')
    }
    if (this.filter === 'pending') {
      return this.tasks.filter(t => t.status === 'pending')
    }
    return this.tasks
  }
}
```

**Questions:**
1. What is a computed property?
2. When does `filteredTasks` get recalculated?
3. Why use a computed property instead of a method here?
4. What does `.filter()` do?

**Expected Understanding:**
- Computed properties cache results and only recalculate when dependencies change
- More efficient than methods for derived data
- `.filter()` creates a new array with items matching the condition

---

### Question 3: Methods
**Show him this code:**
```javascript
addTask() {
  if (!this.newTask.trim()) return

  this.tasks.push({
    description: this.newTask,
    status: 'pending',
    created_at: new Date().toISOString()
  })
  this.newTask = ""
  this.saveTasks()
}
```

**Questions:**
1. Walk through this function step by step
2. What does `.trim()` do and why is it important?
3. What happens if the user enters only spaces?
4. Why do we set `this.newTask = ""` after adding?
5. What does `saveTasks()` do?

**Expected Understanding:**
- `.trim()` removes whitespace from both ends
- Prevents adding empty tasks
- Clearing input provides better UX
- `saveTasks()` persists data to localStorage

---

### Question 4: localStorage
**Show him this code:**
```javascript
saveTasks() {
  localStorage.setItem('tasks', JSON.stringify(this.tasks))
},
loadTasks() {
  const saved = localStorage.getItem('tasks')
  if (saved) {
    this.tasks = JSON.parse(saved)
  }
}
```

**Questions:**
1. What is localStorage?
2. Why do we use `JSON.stringify()` and `JSON.parse()`?
3. What happens if localStorage is disabled in the browser?
4. What's the difference between localStorage and a file?
5. Why did you choose localStorage instead of a file? (Task mentioned file persistence)

**Expected Understanding:**
- localStorage stores data in the browser
- JSON methods convert objects to/from strings
- Need error handling for disabled localStorage
- Should understand the trade-off vs. file storage

---

## Part 2: Bug Identification (10 minutes)

Show Anthony these code snippets and ask him to identify the problems.

### Bug 1: Delete with Filtering
**Show him this code:**
```javascript
// In template:
<button @click="deleteTask(index)">Delete</button>

// In methods:
deleteTask(index) {
  this.tasks.splice(index, 1)
  this.saveTasks()
}
```

**Question**: What's wrong with this code when filtering is active?

**Expected Answer:**
- When filtered, `index` refers to the filtered array position, not the actual tasks array
- Deleting the wrong task or causing an error
- Should use the actual task object or unique ID

**Follow-up**: How would you fix it?

---

### Bug 2: No Error Handling
**Show him this code:**
```javascript
loadTasks() {
  const saved = localStorage.getItem('tasks')
  if (saved) {
    this.tasks = JSON.parse(saved)
  }
}
```

**Question**: What could go wrong here?

**Expected Answer:**
- `JSON.parse()` could throw an error if data is corrupted
- localStorage could be disabled
- Should use try-catch

**Follow-up**: How would you add error handling?

---

## Part 3: Live Coding Exercise (15-20 minutes)

Ask Anthony to make these changes live while you watch.

### Exercise 1: Add Edit Functionality (10 minutes)
**Task**: Add ability to edit a task's description

**Hints if needed:**
- Add an "Edit" button next to each task
- When clicked, show an input field
- Allow saving the edited description

**What to observe:**
- Does he understand the code structure?
- Can he modify it confidently?
- Does he ask clarifying questions?
- How long does it take?

**Expected Implementation:**
```javascript
// Add to data:
editingIndex: null,
editText: "",

// Add method:
startEdit(index) {
  this.editingIndex = index
  this.editText = this.tasks[index].description
},
saveEdit() {
  if (this.editingIndex !== null && this.editText.trim()) {
    this.tasks[this.editingIndex].description = this.editText.trim()
    this.editingIndex = null
    this.editText = ""
    this.saveTasks()
  }
},
cancelEdit() {
  this.editingIndex = null
  this.editText = ""
}
```

---

### Exercise 2: Fix the Delete Bug (5 minutes)
**Task**: Fix the delete function to work correctly with filtering

**Expected Solution:**
```javascript
// Option 1: Use the actual task object
deleteTask(task) {
  const index = this.tasks.findIndex(t => t === task)
  if (index !== -1) {
    this.tasks.splice(index, 1)
    this.saveTasks()
  }
}

// Option 2: Use unique IDs (better approach)
// First, add IDs to tasks when creating them
```

---

### Exercise 3: Add Error Handling (5 minutes)
**Task**: Add try-catch to localStorage operations

**Expected Solution:**
```javascript
loadTasks() {
  try {
    const saved = localStorage.getItem('tasks')
    if (saved) {
      this.tasks = JSON.parse(saved)
    }
  } catch (error) {
    console.error('Error loading tasks:', error)
    this.tasks = []
  }
}
```

---

## Part 4: Conceptual Questions (5 minutes)

### Question 1: Why Vue.js?
**Q**: Why did you choose Vue.js for this project?  
**Follow-up**: Have you used Vue.js before? If not, how did you learn it?

### Question 2: Development Process
**Q**: Walk me through how you built this:
- What did you do first?
- What challenges did you face?
- What resources did you use?
- How long did it take?

### Question 3: Understanding vs. Copying
**Q**: Did you write this code yourself, or did you use:
- AI assistance (ChatGPT, Copilot, etc.)?
- Tutorials or templates?
- Stack Overflow examples?

**Important**: Be honest - using resources is fine, but we need to verify you understand it.

---

## Scoring Rubric

### Code Explanation (Part 1)
- **Excellent (4)**: Explains clearly, shows deep understanding
- **Good (3)**: Explains correctly but needs some prompting
- **Fair (2)**: Partial understanding, some confusion
- **Poor (1)**: Can't explain or gives incorrect answers

### Bug Identification (Part 2)
- **Excellent (4)**: Identifies all bugs and explains fixes
- **Good (3)**: Identifies bugs with hints
- **Fair (2)**: Identifies some bugs
- **Poor (1)**: Can't identify bugs

### Live Coding (Part 3)
- **Excellent (4)**: Completes exercises confidently and correctly
- **Good (3)**: Completes with minor help
- **Fair (2)**: Needs significant guidance
- **Poor (1)**: Can't complete without major assistance

### Conceptual Understanding (Part 4)
- **Excellent (4)**: Clear understanding of development process
- **Good (3)**: Understands but used resources (and learned from them)
- **Fair (2)**: Used resources but limited understanding
- **Poor (1)**: Copied without understanding

---

## Decision Matrix

### If Score is 14-16 (Excellent):
✅ **Understanding Confirmed**
- Great work! Continue to Day 2
- Encourage adding more features
- Provide positive feedback

### If Score is 10-13 (Good):
⚠️ **Understanding Mostly Confirmed**
- Continue but provide additional guidance
- Review areas of weakness
- Set up regular check-ins

### If Score is 6-9 (Fair):
⚠️ **Limited Understanding**
- Needs more support
- Consider simpler approach
- May need to rebuild with guidance
- Focus on fundamentals

### If Score is 0-5 (Poor):
❌ **Understanding Not Confirmed**
- Likely used AI/template without learning
- Restart with simpler version
- Use basic JavaScript (no framework)
- More hands-on guidance needed
- Consider pair programming

---

## Notes Section

**Use this space during the review:**

### Part 1: Code Explanation
- Q1 Response: _______________________
- Q2 Response: _______________________
- Q3 Response: _______________________
- Q4 Response: _______________________

### Part 2: Bug Identification
- Bug 1: _______________________
- Bug 2: _______________________

### Part 3: Live Coding
- Exercise 1: Time taken: _______, Help needed: _______
- Exercise 2: Time taken: _______, Help needed: _______
- Exercise 3: Time taken: _______, Help needed: _______

### Part 4: Conceptual
- Development process: _______________________
- Resources used: _______________________
- Honesty level: _______________________

### Overall Assessment:
- Total Score: _____ / 16
- Understanding Level: _______________________
- Recommendation: _______________________

---

## Follow-up Actions

Based on the score, document next steps:

1. **If Understanding Confirmed:**
   - [ ] Provide positive feedback
   - [ ] Address code issues (folder structure, documentation)
   - [ ] Move to Day 2 tasks
   - [ ] Set expectations for better documentation

2. **If Understanding Needs Work:**
   - [ ] Schedule additional review sessions
   - [ ] Provide learning resources
   - [ ] Consider simpler project approach
   - [ ] Set up regular check-ins

3. **If Understanding Not Confirmed:**
   - [ ] Have honest conversation about using AI
   - [ ] Restart with simpler project
   - [ ] Focus on fundamentals
   - [ ] Provide more structured guidance

---

**Reviewer Signature**: _______________________  
**Date**: _______________________  
**Anthony's Signature**: _______________________
