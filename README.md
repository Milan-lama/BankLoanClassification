# Bank Loan Prediction API

A Django REST API that predicts bank loan approval using machine learning. The API takes customer information and returns a prediction whether the loan would be approved or not.

## Features

- RESTful API endpoints for loan prediction
- Machine learning model integration
- Customer data validation and storage
- Support for multiple input parameters
- Easy-to-use JSON interface

## Tech Stack

- Python 3.x
- Django 5.0.7
- Django REST Framework
- NumPy
- scikit-learn (for ML model)
- SQLite3

## Project Structure

```
Bank_loan_prediction_API/
├── manage.py
├── api/
├── Bank_loan_prediction_API/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── model_prediction/
    ├── models.py
    ├── views.py
    ├── serializers.py
    └── my_model.py
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Bank_loan_prediction_API
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install django djangorestframework numpy scikit-learn
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## API Usage

### Prediction Endpoint

**POST** `/api/predict/`

Request Body:
```json
{
    "age": 25,
    "experience": 3,
    "income": 40000,
    "zip_code": 12345,
    "family": 4,
    "ccavg": 4.5,
    "education": 1,
    "mortgage": 0,
    "home_ownership": "Rent",
    "securities_account": 0,
    "cd_account": 0,
    "online": 1,
    "credit_card": 1,
    "gender": "male"
}
```

Response:
```json
{
    "prediction": "Approved"
}
```

## Input Parameters

- **age**: Customer's age (integer)
- **experience**: Years of work experience (integer)
- **income**: Annual income (float)
- **zip_code**: ZIP code (integer)
- **family**: Number of family members (integer)
- **ccavg**: Average monthly credit card spending (float)
- **education**: Education level (1: Bachelor's, 2: Master's, 3: Advanced/Professional)
- **mortgage**: Existing mortgage value (float)
- **home_ownership**: Home ownership status ("Rent", "Home Owner", "Other")
- **securities_account**: Has securities account (0/1)
- **cd_account**: Has certificate of deposit account (0/1)
- **online**: Uses online banking (0/1)
- **credit_card**: Has credit card (0/1)
- **gender**: Gender ("male", "female", "others")

## License

[MIT License](LICENSE)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Acknowledgments

- Thanks to all contributors who helped in building this project
- Special thanks to the Django and scikit-learn communities
