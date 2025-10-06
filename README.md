# 🚗 Object Detection with Hexagonal Architecture

A comprehensive object detection project demonstrating **Hexagonal Architecture** (Ports and Adapters) principles using YOLO for real-time car detection. This project serves as both a practical application and a learning resource for clean architecture patterns in Python.

## 🏗️ Architecture Overview

This project implements the **Hexagonal Architecture** pattern, also known as Ports and Adapters, which provides:

- **🔄 Separation of Concerns**: Business logic is isolated from external dependencies
- **🧪 Enhanced Testability**: Easy dependency injection and mocking for comprehensive testing
- **🔧 Implementation Flexibility**: Swap detection models or data sources without changing core logic
- **📈 Maintainability**: Clear boundaries make the codebase easier to understand and modify

### 📁 Project Structure

```
src/
├── domain/           # 🧠 Business logic (core domain)
│   └── filter_car_detections.py
├── ports/            # 🔌 Interfaces (contracts/ports)
│   └── object_detection_port.py
├── adapters/         # 🔌 External implementations (adapters)
│   └── yolo_detection.py
├── infra/            # 🏗️ Infrastructure layer
│   └── car_count_repository.py
└── main.py          # 🚀 Application entry point
```

## 🚀 Quick Start

### Prerequisites
- **Python 3.11+**
- **UV package manager** (recommended) or pip
- **YOLOv8 model file** (`yolov8n.pt`)

### Installation & Setup

1. **Clone and navigate to the repository:**
   ```bash
   git clone https://github.com/Guiandreis/object_detection_repo.git
   cd object_detection_repo
   ```

2. **Install dependencies:**
   ```bash
   # Using UV (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Run the car detection:**
   ```bash
   python src/main.py
   ```

## 🎯 Core Functionality

- **🔍 Object Detection**: Uses YOLOv8 to detect objects in images
- **🚗 Car Filtering**: Intelligently filters detections to focus on cars (class_id=2)
- **📊 Data Persistence**: Stores and retrieves car counts per image
- **🏛️ Clean Architecture**: Demonstrates SOLID principles and dependency inversion

## 📝 Blog Post Series: From Simple to Production

This project evolves through a comprehensive blog post series, with each iteration adding production-ready features:
The order of the phases of the project can change, and new phases and parts will be added. 

### **Phase 1: Foundation** 🏗️
1. **Part 1**: Hexagonal Architecture Fundamentals *(current version)*
2. **Part 2**: Unit Testing & Test-Driven Development
3. **Part 3**: GitHub Actions CI/CD Pipeline, Code Formatting & Linting

### **Phase 2: Coming Soon** 🚀
*Stay tuned for exciting new features and production-ready enhancements!*
...

## 🏛️ Why Hexagonal Architecture?

### **Key Benefits:**

- **🧪 Testability**: Mock external dependencies easily for isolated unit testing
- **🔄 Flexibility**: Swap YOLO for other detection models (TensorRT, ONNX, etc.)
- **🛠️ Maintainability**: Clear separation makes code easier to understand and modify
- **📈 Scalability**: Add new features without breaking existing functionality
- **🔒 Independence**: Core business logic is independent of external frameworks

### **Real-World Applications:**
- **Microservices**: Each service can have its own hexagonal architecture
- **API Development**: Clean separation between business logic and HTTP concerns
- **Data Processing**: Easy to swap data sources (files, databases, APIs)
- **ML Pipelines**: Flexible model swapping and testing

## 🛠️ Technology Stack

- **🐍 Python 3.11+**: Modern Python with type hints
- **🎯 YOLOv8**: State-of-the-art object detection
- **📦 UV**: Fast Python package management
- **🏗️ Hatchling**: Modern Python packaging

## 📚 Learning Resources

- [Hexagonal Architecture by Alistair Cockburn](https://alistair.cockburn.us/hexagonal-architecture/)
- [Clean Architecture by Robert Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [Dependency Inversion Principle](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

