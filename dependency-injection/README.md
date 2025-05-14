
# FastAPI Dependency Injection Demo

This is a simple FastAPI project demonstrating how to use **dependencies**, **query parameters**, and **custom 404 logic** using `Depends`, `Annotated`, and `HTTPException`.

---

##  Project Structure

```
main.py
```

---

##  Features

- Use of `Depends` with query parameters  
- Secure login simulation  
- Custom dependency injection with `Annotated`  
- Reusable 404 handling logic  
- Simple calculator with multiple dependencies

---

##  How to Run

1. **Install dependencies**

```bash
pip install fastapi uvicorn
```

2. **Run the app**

```bash
uvicorn main:app --reload
```

3. **Open in your browser**

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

##  Examples

- Login (Success):  
  `http://localhost:8000/signin?username=admin&password=admin`

- Blog Lookup:  
  `http://localhost:8000/blog/1`

- Add Numbers:  
  `http://localhost:8000/main/1`

---

##  Concepts Used

- `FastAPI`
- `Depends`, `Annotated`
- `Query`
- `HTTPException`
- `status codes`

---

##  Author
**Umm e Habiba**  
