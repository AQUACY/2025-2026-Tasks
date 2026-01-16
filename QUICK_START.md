# Quick Start Guide

## For Team Members

### Starting a New Week

1. **Check the Task**
   ```bash
   # Read TASKS.md to see this week's task
   cat TASKS.md
   ```

2. **Create Your Folder**
   ```bash
   # Replace XX with week number and your-name with your actual name
   mkdir -p tasks/week-XX/your-name
   cd tasks/week-XX/your-name
   ```

3. **Copy the Daily Goals Template**
   ```bash
   # From your week folder
   cp ../../templates/daily-goals.md daily-goals.md
   ```

4. **Edit Your Daily Goals**
   - Open `daily-goals.md`
   - Fill in your name and the task name
   - Plan your daily goals for the week

5. **Start Coding!**
   - Create your project files
   - Work on Monday's goals
   - Push your code at the end of the day

### Daily Routine

**Morning:**
- Review today's goal in your `daily-goals.md`
- Plan what you'll work on

**During Work:**
- Code and make progress
- Test as you go

**End of Day:**
- Update `daily-goals.md` with your progress
- Commit and push:
  ```bash
  git add .
  git commit -m "Week XX - [Day]: [What you did]"
  git push
  ```

## For Reviewers (Managers)

### Daily Review Process

1. **Check GitHub Activity**
   - Go to the repository
   - Check recent commits
   - See who pushed code today

2. **Review Individual Progress**
   - Navigate to `tasks/week-XX/person-name/`
   - Open their `daily-goals.md`
   - Review what they accomplished

3. **Quick Code Review**
   - Look at their latest commit
   - Check if code runs
   - Note any issues

4. **Update WEEKLY_REVIEW.md**
   - Mark their progress (✅, 🟡, ⬜, ❌)
   - Add notes if needed

### Friday Review Process

1. **Final Code Review**
   - Review the complete project
   - Check all requirements are met
   - Test the application

2. **Review Documentation**
   - Check README.md
   - Review daily-goals.md completeness
   - Ensure code is documented

3. **Provide Feedback**
   - Use the feedback template in WEEKLY_REVIEW.md
   - Be constructive and encouraging
   - Highlight both strengths and areas for improvement

## 📁 Example Folder Structure

After a few weeks, your repository will look like:

```
2025-2026-Tasks/
├── tasks/
│   ├── week-01/
│   │   ├── alice/
│   │   │   ├── daily-goals.md
│   │   │   ├── README.md
│   │   │   └── todo.py
│   │   ├── bob/
│   │   │   ├── daily-goals.md
│   │   │   ├── README.md
│   │   │   └── TodoApp.java
│   │   └── charlie/
│   │       ├── daily-goals.md
│   │       ├── README.md
│   │       └── todo.js
│   ├── week-02/
│   │   └── ...
│   └── week-03/
│       └── ...
├── templates/
│   ├── daily-goals.md
│   └── task-template.md
├── README.md
├── TASKS.md
├── WEEKLY_REVIEW.md
└── CONTRIBUTING.md
```

## 🚨 Common Issues & Solutions

### Issue: "I don't know where to start"
**Solution**: 
- Read the task description carefully
- Break it into smaller pieces
- Start with the simplest feature first
- Ask for help if stuck

### Issue: "I'm behind on my daily goals"
**Solution**:
- Don't panic - adjust your goals
- Focus on core requirements first
- Push what you have, even if incomplete
- Communicate any blockers

### Issue: "My code doesn't work"
**Solution**:
- Push it anyway with a note about the issue
- Ask for help in your daily notes
- Try to isolate the problem
- Document what you tried

### Issue: "I finished early"
**Solution**:
- Great! Add bonus features
- Improve code quality
- Add more error handling
- Enhance the UI/UX
- Help teammates if they're stuck

## 💡 Pro Tips

1. **Start Early**: Don't wait until Thursday to start
2. **Small Commits**: Make frequent, small commits rather than one big one
3. **Test Often**: Test your code as you build, not just at the end
4. **Read Others' Code**: Learn from your teammates' approaches
5. **Ask Questions**: It's better to ask than to be stuck
6. **Have Fun**: These are learning exercises - enjoy the process!

---

**Need Help?** Check CONTRIBUTING.md for more detailed guidelines.
