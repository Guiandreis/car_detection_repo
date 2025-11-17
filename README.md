# 🚗 Object Detection from scratch to production

> **📝 Blog Post Series**: This project is part of a comprehensive blog series on building production-ready Python applications.  
> 🔗 **Read the blog posts**: https://guiandreis.github.io/

---

A comprehensive car detection project demonstrating how to build and deploy a project from scratch to production 


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
- **Make** (for automation commands)
- **YOLOv8 model file** (`yolov8n.pt`)

### Installation & Setup

1. **Clone and navigate to the repository:**
   ```bash
   git clone https://github.com/Guiandreis/object_detection_repo.git
   cd object_detection_repo
   ```

2. **One-command setup (installs uv, dependencies, and git hooks):**
   ```bash
   make install
   ```

3. **Run the car detection:**
   ```bash
   python src/main.py
   ```

### Available Make Commands

```bash
make install      # Install uv, dependencies, and git hooks
make test         # Run tests with coverage
make lint         # Run code linter (ruff)
make format       # Format code with ruff
make format-check # Check code formatting
make typecheck    # Run type checker (mypy)
make ci           # Run all CI checks (format-check, lint, typecheck, test)
make clean        # Clean up cache and temporary files
```

## 🛠️ Technology Stack

- **🐍 Python 3.11+**: Modern Python with type hints
- **🎯 YOLOv8**: State-of-the-art object detection
- **📦 UV**: Fast Python package management
- **🏗️ Hatchling**: Modern Python packaging
- **🧪 Pytest**: Testing framework with coverage
- **🔍 Ruff**: Fast Python linter and formatter
- **📝 MyPy**: Static type checker
- **🪝 Pre-commit**: Git hooks for code quality

## 📊 Project Progress

### ✅ Completed Features

- [x] **Hexagonal Architecture Implementation**
  - Ports and adapters pattern
  - Clear separation of concerns
  - Dependency inversion principle
- [x] **Core Object Detection**
  - YOLOv8 integration
  - Car detection and filtering
  - Image processing pipeline
- [x] **Testing Infrastructure**
  - Unit tests with 85%+ coverage
  - Pytest configuration
  - Mock-based testing
- [x] **CI/CD Pipeline**
  - GitHub Actions workflow
  - Automated testing on push/PR
  - Pre-commit and pre-push hooks
- [x] **Code Quality Tools**
  - Ruff for linting and formatting
  - MyPy for type checking
  - Pre-commit hooks integration
- [x] **Developer Experience**
  - Makefile for common tasks
  - One-command setup (`make install`)
  - Comprehensive README
- [x] **[PLACEHOLDER - Add your completed topics here]**

### 🔮 Upcoming Features (TODO)

- [ ] **[Dataset Version Control (DVC)]**
- [ ] **[MLFlow]**
- [ ] **[Classification model training]**
