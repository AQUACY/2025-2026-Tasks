<template>
  <div class="container">
    <h1>Todo List Application</h1>

    <div class="add-task">
      <input v-model="newTask" placeholder="Enter task description" />
      <button @click="addTask">Add Task</button>
    </div>

    <div class="filters">
      <button @click="filter = 'all'">All</button>
      <button @click="filter = 'completed'">Completed</button>
      <button @click="filter = 'pending'">Pending</button>
    </div>

    <ul class="task-list">
      <li v-for="(task, index) in filteredTasks" :key="index">
        <span>
          {{ task.status === 'completed' ? '✅' : '⬜' }} {{ task.description }}
        </span>
        <div class="actions">
          <button @click="markComplete(index)" :disabled="task.status === 'completed'">
            Complete
          </button>
          <button @click="deleteTask(index)">Delete</button>
        </div>
      </li>
    </ul>

    <p v-if="filteredTasks.length === 0">No tasks found.</p>
  </div>
</template>

<script>
export default {
  name: "TodoApp",
  data() {
    return {
      newTask: "",
      filter: "all",
      tasks: []
    }
  },
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
  },
  methods: {
    addTask() {
      if (!this.newTask.trim()) return

      this.tasks.push({
        description: this.newTask,
        status: 'pending',
        created_at: new Date().toISOString()
      })
      this.newTask = ""
      this.saveTasks()
    },
    markComplete(index) {
      this.tasks[index].status = 'completed'
      this.saveTasks()
    },
    deleteTask(index) {
      this.tasks.splice(index, 1)
      this.saveTasks()
    },
    saveTasks() {
      localStorage.setItem('tasks', JSON.stringify(this.tasks))
    },
    loadTasks() {
      const saved = localStorage.getItem('tasks')
      if (saved) {
        this.tasks = JSON.parse(saved)
      }
    }
  },
  mounted() {
    this.loadTasks()
  }
}
</script>

<style scoped>
.container {
  max-width: 500px;
  margin: auto;
  font-family: Arial, sans-serif;
}
.add-task {
  display: flex;
  gap: 10px;
}
.filters button {
  margin: 5px;
}
.task-list {
  list-style: none;
  padding: 0;
}
.task-list li {
  display: flex;
  justify-content: space-between;
  margin: 8px 0;
}
.actions button {
  margin-left: 5px;
}
</style>
