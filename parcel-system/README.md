# Parcel Handling System

## Overview

The Parcel Handling System is designed to manage and process parcels based on their weight and value. The system is divided into two main features:

### Feature 1
- Parcels with a weight up to 1 kg are handled by the "Mail" department.
- Parcels with a weight up to 10 kg are handled by the "Regular" department.
- Parcels with a weight over 10 kg are handled by the "Heavy" department.

### Feature 2
- Parcels with a value of over €1000 need to be signed off by the "Insurance" department before being processed by the other departments.

## Technologies Used

### Backend
- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Uvicorn**: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.

### Frontend
- **Vue.js**: A progressive JavaScript framework for building user interfaces.
- **TypeScript**: A strongly typed programming language that builds on JavaScript, giving you better tooling at any scale.
- **Vite**: A build tool that aims to provide a faster and leaner development experience for modern web projects.
- **Axios**: A promise-based HTTP client for the browser and Node.js.
- **shadcn/ui**: A library of components for building modern web applications.
- **TailwindCSS**: A utility-first CSS framework for rapidly building custom designs.
- **pnpm**: A fast, disk space efficient package manager.

## Project Main Structure

### Backend
- **api.py**: The main FastAPI application file that defines the API endpoints and business logic.
- **parcel_handler folder**: Contains the `ParcelHandler` and `DepartmentFactory` classes that handle the parsing and processing of parcels, and of course the `Department` classes.

### Frontend
- **src/constants/tableColumns.ts**: Defines the table columns for displaying parcel data.
- **src/pages/home/home.vue**: The main Vue component for displaying the parcel data in a table format.
- **src/types/table.ts**: Defines the TypeScript types for the table columns.

## Why the Factory Pattern?

The choosing of factory pattern was made for the following reasons:
1. **Encapsulation**: The factory pattern encapsulates the logic for creating department objects based on parcel weight and value. This makes the code more modular and easier to maintain.
2. **Scalability**: As business rules change or new departments are added, the factory pattern allows us to easily extend the system without modifying existing code.
3. **Separation of Concerns**: By using the factory pattern, we separate the logic for determining the appropriate department from the actual processing logic. This makes the code more readable and easier to test.

## How to Run

### Backend
1. Install the required dependencies:
   ```bash
   pip install fastapi pydantic uvicorn
   ```
2. Run the FastAPI application:
   ```bash
   uvicorn parcel_handling_system.api:app --reload
   ``` 
   or
   ```bash
   python3 api.py
   ```

### Frontend
1. Install the required dependencies:
   ```bash
   pnpm install
   ```
2. Run the development server:
   ```bash
   pnpm dev
   ```

## API Endpoints

- **GET /parcels**: Retrieves the list of parcels, processes them according to the business rules, and returns the processed parcels.

## Example

### Request
```bash
curl -X GET http://localhost:8000/parcels
```

### Response
```json
{
    "parcels": [
        {
            "name": "Parcel 1",
            "weight": 0.5,
            "value": 500,
            "department": "MailDepartment"
        },
        {
            "name": "Parcel 2",
            "weight": 5,
            "value": 1500,
            "department": "InsuranceDepartment"
        }
    ]
}
```
