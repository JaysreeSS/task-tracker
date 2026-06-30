import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App implements OnInit {
  private apiUrl = environment.apiUrl;

  tasks: any[] = [];
  
  selectedStatus: string = '';
  selectedPriority: string = '';

  newTask = {
    title: '',
    description: '',
    priority: 'Medium',
    due_date: ''
  };


  constructor(private http: HttpClient, private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.fetchTasks();
  }

  fetchTasks(): void {
    let queryParams: string[] = [];
    
    if (this.selectedStatus) {
      queryParams.push(`status=${this.selectedStatus}`);
    }
    if (this.selectedPriority) {
      queryParams.push(`priority=${this.selectedPriority}`);
    }

    const queryString = queryParams.length > 0 ? '?' + queryParams.join('&') : '';
    const url = `${this.apiUrl}${queryString}`;

    this.http.get<any[]>(url).subscribe({
      next: (data) => {
        this.tasks = data; 
        this.cdr.detectChanges();
      },
      error: (err) => {
        console.error('Database load failed', err);
      }
    });
  }

  addTask(): void {
    if (!this.newTask.title.trim()) return;

    this.http.post(this.apiUrl, this.newTask).subscribe({
      next: () => {
        this.newTask = { title: '', description: '', priority: 'Medium', due_date: '' };
        this.fetchTasks();
        window.alert('Task created');
      }
    });
  }  

  toggleDone(task: any): void {
    this.http.put(`${this.apiUrl}/${task.id}`, { is_done: !task.is_done }).subscribe({
      next: () => this.fetchTasks()
    });
  }

  deleteTask(id: number): void {
    if (window.confirm('Delete this task?')) {
      this.http.delete(`${this.apiUrl}/${id}`).subscribe({
        next: () => this.fetchTasks()
      });
    }
  }

  get pendingCount(): number {
    return this.tasks.filter(t => !t.is_done).length;
  }

  get doneCount(): number {
    return this.tasks.filter(t => t.is_done).length;
  }
}