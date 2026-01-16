# Contributing Guidelines

## 📁 Folder Structure

When working on a weekly task, create your folder structure like this:

```
tasks/
└── week-01/
    ├── john-doe/
    │   ├── daily-goals.md
    │   ├── README.md
    │   └── [your code files]
    ├── jane-smith/
    │   ├── daily-goals.md
    │   ├── README.md
    │   └── [your code files]
    └── ...
```

## 📝 Daily Workflow

1. **Each Morning**: Review your daily goal for the day
2. **During Work**: Code and make progress
3. **End of Day**: 
   - Update your `daily-goals.md` file
   - Commit and push your code (even if incomplete)
   - Mark tasks as completed

## 🔄 Git Workflow

### Initial Setup (First Time)
```bash
# Clone the repository
git clone [repository-url]
cd 2025-2026-Tasks

# Create your week folder
mkdir -p tasks/week-01/your-name
cd tasks/week-01/your-name

# Copy the daily goals template
cp ../../templates/daily-goals.md daily-goals.md
```

### Daily Commits
```bash
# Make your changes
# ...

# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Week 01 - Monday: Setup project and implement basic structure"

# Push to GitHub
git push origin main
```

### Commit Message Format
```
Week XX - [Day]: [Brief description of what you did]
```

Examples:
- `Week 01 - Monday: Setup project and implement add task functionality`
- `Week 01 - Tuesday: Add mark complete and delete features`
- `Week 01 - Wednesday: Implement file persistence`

## ✅ Code Review Checklist

Before submitting on Friday, ensure:

- [ ] All daily goals are documented
- [ ] Code follows your language's best practices
- [ ] Error handling is implemented
- [ ] README.md explains how to run the project
- [ ] Code is commented where necessary
- [ ] No hardcoded secrets or API keys
- [ ] Project runs without errors

## 📚 README Template

Your project README should include:

```markdown
# [Project Name]

## Description
Brief description of what the project does.

## Language & Technologies
- Language: [e.g., Python 3.9]
- Libraries: [e.g., requests, json]

## Setup Instructions
1. Step 1
2. Step 2
3. Step 3

## How to Run
```bash
[commands to run the project]
```

## Features Implemented
- Feature 1
- Feature 2
- Feature 3

## Challenges Faced
[Describe any challenges and how you overcame them]

## Future Improvements
[What you would add if you had more time]
```

## 🎯 Best Practices

1. **Daily Pushes**: Always push your code at the end of each day
2. **Meaningful Commits**: Write clear commit messages
3. **Clean Code**: Write readable, maintainable code
4. **Documentation**: Comment complex logic
5. **Error Handling**: Always handle edge cases
6. **Testing**: Test your code before pushing

## ❓ Questions?

If you have questions about a task:
1. Check the task description in `TASKS.md`
2. Review the daily goals template
3. Ask in team chat or during standup

---

**Remember**: The goal is to learn and improve. Don't worry about making it perfect - focus on making progress every day!
