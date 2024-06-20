# How to run

- Create virtual envirement

    ```bash
    python -m venv .venv
    ```

- Activate virtual envirement

    ```bash
    source .venv/bin/activate
    ```

- Install requirements

    ```bash
    pip install -r requirements.txt
    ```

- Update env variables in `run.sh` file

- Add `execute` permission for run.sh file

    ```bash
    chmod +x ./run.sh
    ```

- Run `make_call.py` file

    ```bash
    ./run.sh make_call.py
    ```


# Tips for production

- Use [.env](https://github.com/theskumar/python-dotenv) file for env variables