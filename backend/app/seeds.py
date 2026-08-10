users = [
    {
        "id": 1,
        "email": "john.doe@example.com",
        "fullname": "John Doe",
    },
    {
        "id": 2,
        "email": "jane.smith@example.com",
        "fullname": "Jane Smith",
    },
    {
        "id": 3,
        "email": "bob.johnson@example.com",
        "fullname": "Bob Johnson",
    },
]

subscriptions = [
    {
        "id": 1,
        "userId": 1,
        "plan": "Basic",
        "status": "active",
    },
    {
        "id": 2,
        "userId": 2,
        "plan": "Premium",
        "status": "inactive",
    },
    {
        "id": 3,
        "userId": 2,
        "plan": "Premium",
        "status": "active",
    },
    {
        "id": 4,
        "userId": 3,
        "plan": "Pro",
        "status": "active",
    },
]

payments = [
    {
        "id": 1,
        "userId": 1,
        "amount": 10.0,
        "status": "completed",
    },
    {
        "id": 2,
        "userId": 2,
        "amount": 20.0,
        "status": "pending",
    },
    {
        "id": 3,
        "userId": 3,
        "amount": 30.0,
        "status": "failed",
    },
]