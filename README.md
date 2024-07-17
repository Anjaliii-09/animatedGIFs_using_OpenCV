
### Usage Instructions

1. **Clone the Repository**:
   - Clone your repository locally using `git clone`.

2. **Set Up Environment**:
   - Optionally, set up a virtual environment using `python -m venv venv` and activate it.

3. **Install Dependencies**:
   - Install required dependencies using `pip install -r requirements.txt`.

4. **Run Your Script**:
   - Execute your main script or application using `python src/create_gifs.py`.

### Managing `.venv` with `.gitignore`

To ensure your virtual environment (`venv`) is not pushed to your Git repository:

1. **Update `.gitignore`**:
   - Add `venv/` to your `.gitignore` file in the root of your project.

   ```plaintext
   # .gitignore
   venv/
