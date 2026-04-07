# Transaction Ledger CLI

## Overview

A command-line expense tracking system designed as a **practical intermediate-level Python project**.

This project is intended for developers who want to **test and strengthen their understanding of core backend concepts**, including object-oriented design, state management, file persistence, and structured logging.

Rather than focusing on UI or frameworks, it emphasizes **how real systems are structured internally**.

---

## Purpose

This project is built as a **skill checkpoint** for intermediate Python developers.
It evaluates your ability to:

* Structure a multi-file project
* Design clean abstractions using OOP
* Manage application state without global variables
* Persist data reliably using JSON
* Implement flexible search/filter logic
* Separate concerns (logic, storage, logging, interface)

---

## Features

* Add transactions (amount, category, description, timestamp)
* Persist data using JSON (data survives restarts)
* Search transactions using keyword and/or category filters
* View transactions via CLI in a structured format
* Log all actions and errors to a file

---


## Example Usage

```
Available commands: {'add', 'list', 'search', 'exit'}

> add
Enter amount: 500
Enter category: food
Enter description: burger
Transaction added successfully.

> search
Enter keyword: bur
Enter category:

1. Amount: 500 | Category: food | Description: burger

> list
[1] 500 | food | burger | 06 Apr 2026, 08:25 PM
```

---

## Project Structure

```
project/
│
├── main.py          # CLI interface (user interaction)
├── tracker.py       # Core business logic (state + operations)
├── transaction.py   # Transaction data model
├── storage.py       # JSON persistence layer
├── logger.py        # Logging system
│
├── data/
│   └── transactions.json
│
└── logs/
    └── app.log
```

---

## Key Design Concepts Tested

### 1. Separation of Concerns

Each component has a clearly defined responsibility:

* Business logic
* Data modeling
* Persistence
* Logging
* Interface

---

### 2. Object-Oriented Design

* `Transaction` represents a single data entity
* `ExpenseTracker` manages application state and behavior

This eliminates reliance on global variables and improves maintainability.

---

### 3. Scalable Search Logic

The search system uses a unified filtering approach:

> Assume a transaction matches → eliminate it if any condition fails

This pattern:

* Handles multiple optional filters cleanly
* Avoids branching complexity
* Scales easily when adding new filters

---

### 4. Logging as a First-Class Component

Logging is treated as a core system feature:

* Tracks actions (add, search)
* Captures errors
* Enables debugging beyond CLI output

---

### 5. Data Persistence

* Transactions are stored in JSON
* Automatically saved on modification
* Loaded at startup

---

## Evaluation Criteria (Self-Check)

This project is considered complete if you can confidently explain:

* Why OOP was used instead of global functions
* How state is managed across the application
* How search logic handles multiple filters
* Why logging is separated from CLI output
* Trade-offs between generators and lists in this design

---

## Limitations

* Uses JSON instead of a database
* Single-user CLI system
* No edit/delete functionality
* Minimal input validation

---

## Suggested Extensions

To push beyond intermediate level:

* Add amount range and date-based filtering
* Implement edit/delete operations
* Replace JSON with a database (SQLite/PostgreSQL)
* Add unit tests for search and storage
* Refactor CLI into command parser pattern

---

## What This Project Demonstrates

This project showcases:

* Structured problem solving
* System-level thinking in Python
* Clean separation between components
* Practical backend engineering fundamentals

---

## Notes

This is not intended to be a production application.
It is designed as a **learning-oriented system** that reflects how real-world backend components are organized and interact.
