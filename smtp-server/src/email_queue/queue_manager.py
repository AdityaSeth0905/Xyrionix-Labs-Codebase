import os
import json
import time
import logging
import threading
from typing import Any, Dict, List, Optional
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor, as_completed

class QueueManager:
    def __init__(self, 
                 max_workers: int = 5, 
                 queue_limit: int = 1000, 
                 log_path: str = 'queue_logs'):
        """
        Initialize Queue Manager
        
        Args:
            max_workers (int): Maximum number of concurrent workers
            queue_limit (int): Maximum queue size
            log_path (str): Path for logging queue operations
        """
        # Create queues
        self.task_queue = Queue(maxsize=queue_limit)
        self.result_queue = Queue(maxsize=queue_limit)
        self.error_queue = Queue(maxsize=queue_limit)
        
        # Configuration
        self.max_workers = max_workers
        self.queue_limit = queue_limit
        
        # Logging setup
        self.log_path = log_path
        os.makedirs(log_path, exist_ok=True)
        
        # Logging configuration
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s',
            handlers=[
                logging.FileHandler(os.path.join(log_path, 'queue_manager.log')),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # Tracking
        self.processed_tasks = 0
        self.failed_tasks = 0
        
        # Flags
        self.is_running = False
        
        # Thread management
        self.executor = None
        self.monitor_thread = None
    
    def add_task(self, task: Any, priority: int = 0) -> bool:
        """
        Add a task to the queue
        
        Args:
            task (Any): Task to be processed
            priority (int): Task priority (lower number = higher priority)
        
        Returns:
            bool: Whether task was successfully added
        """
        try:
            if self.task_queue.qsize() < self.queue_limit:
                self.task_queue.put((priority, task))
                self.logger.info(f"Task added: {task}")
                return True
            else:
                self.logger.warning("Queue is full. Task not added.")
                return False
        except Exception as e:
            self.logger.error(f"Error adding task: {e}")
            return False
    
    def process_task(self, task: Any) -> Dict[str, Any]:
        """
        Process individual task
        
        Args:
            task (Any): Task to be processed
        
        Returns:
            Dict with processing result
        """
        try:
            # Placeholder for task processing logic
            # Replace with your specific task processing method
            result = {
                'status': 'success',
                'task': task,
                'processed_at': time.time()
            }
            self.processed_tasks += 1
            return result
        except Exception as e:
            self.logger.error(f"Task processing failed: {e}")
            self.failed_tasks += 1
            return {
                'status': 'failed',
                'task': task,
                'error': str(e)
            }
    
    def start_processing(self):
        """
        Start queue processing with thread pool
        """
        if self.is_running:
            self.logger.warning("Queue processing already running")
            return
        
        self.is_running = True
        self.executor = ThreadPoolExecutor(max_workers=self.max_workers)
        
        def worker():
            """Internal worker for processing tasks"""
            while self.is_running:
                try:
                    # Get task with priority
                    _, task = self.task_queue.get(timeout=1)
                    
                    # Process task
                    result = self.process_task(task)
                    
                    # Add to result queue
                    if result['status'] == 'success':
                        self.result_queue.put(result)
                    else:
                        self.error_queue.put(result)
                    
                    # Mark task as done
                    self.task_queue.task_done()
                
                except Empty:
                    # No tasks in queue
                    time.sleep(0.1)
                except Exception as e:
                    self.logger.error(f"Worker error: {e}")
        
        # Start workers
        for _ in range(self.max_workers):
            self.executor.submit(worker)
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self._queue_monitor)
        self.monitor_thread.start()
        
        self.logger.info("Queue processing started")
    
    def _queue_monitor(self):
        """
        Monitor queue status and log metrics
        """
        while self.is_running:
            try:
                self.logger.info(
                    f"Queue Status: "
                    f"Tasks={self.task_queue.qsize()}, "
                    f"Processed={self.processed_tasks}, "
                    f"Failed={self.failed_tasks}"
                )
                time.sleep(60)  # Log every minute
            except Exception as e:
                self.logger.error(f"Monitor thread error: {e}")
    
    def stop_processing(self):
        """
        Gracefully stop queue processing
        """
        self.is_running = False
        
        if self.executor:
            self.executor.shutdown(wait=True)
        
        if self.monitor_thread:
            self.monitor_thread.join()
        
        self.logger.info("Queue processing stopped")
    
    def get_results(self, timeout: int = 0) -> List[Dict]:
        """
        Retrieve processed results
        
        Args:
            timeout (int): Timeout for retrieving results
        
        Returns:
            List of processed results
        """
        results = []
        try:
            while True:
                result = self.result_queue.get(timeout=timeout)
                results.append(result)
        except Empty:
            pass
        return results
    
    def get_errors(self, timeout: int = 0) -> List[Dict]:
        """
        Retrieve error results
        
        Args:
            timeout (int): Timeout for retrieving errors
        
        Returns:
            List of error results
        """
        errors = []
        try:
            while True:
                error = self.error_queue.get(timeout=timeout)
                errors.append(error)
        except Empty:
            pass
        return errors
    
    def save_results(self, 
                     results: List[Dict], 
                     filename: str = 'results.json'):
        """
        Save results to a JSON file
        
        Args:
            results (List[Dict]): Results to save
            filename (str): Output filename
        """
        try:
            filepath = os.path.join(self.log_path, filename)
            with open(filepath, 'w') as f:
                json.dump(results, f, indent=2)
            self.logger.info(f"Results saved to {filepath}")
        except Exception as e:
            self.logger.error(f"Error saving results: {e}")

def main():
    # Example usage
    queue_manager = QueueManager(max_workers=3)
    
    # Add some sample tasks
    for i in range(10):
        queue_manager.add_task(f"Task {i}")
    
    # Start processing
    queue_manager.start_processing()
    
    # Wait a bit
    time.sleep(5)
    
    # Stop processing
    queue_manager.stop_processing()
    
    # Get and save results
    results = queue_manager.get_results()
    queue_manager.save_results(results)
    
    # Check for errors
    errors = queue_manager.get_errors()
    if errors:
        queue_manager .save_results(errors, filename='errors.json')

if __name__ == "__main__":
    main()